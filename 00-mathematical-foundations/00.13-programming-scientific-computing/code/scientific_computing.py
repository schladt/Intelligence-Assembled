"""Contract-first scientific-computing helpers for module 0.13."""

from __future__ import annotations

from collections.abc import Callable, Iterable, Sequence
from dataclasses import asdict, dataclass
from importlib.metadata import version
import json
import operator
import os
from pathlib import Path
import platform
import subprocess
import sys
import timeit
from typing import Any

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np
from numpy.exceptions import AxisError
from numpy.typing import ArrayLike, NDArray


class ContractError(ValueError):
    """Report that an input violates a documented computational contract."""


@dataclass(frozen=True)
class ArrayContract:
    """Describe the required shape and dtype family of a NumPy array."""

    shape: tuple[int | None, ...]
    dtype_kind: str = "f"
    finite: bool = True

    def validate(self, value: ArrayLike, *, name: str = "array") -> NDArray[Any]:
        """Return an ndarray after validating rank, axes, dtype, and finiteness."""
        array = np.asarray(value)
        if array.ndim != len(self.shape):
            raise ContractError(
                f"{name} must have ndim={len(self.shape)}, got ndim={array.ndim}"
            )
        for axis, (actual, expected) in enumerate(zip(array.shape, self.shape)):
            if expected is not None and actual != expected:
                raise ContractError(
                    f"{name} axis {axis} must have length {expected}, got {actual}"
                )
        if array.dtype.kind not in self.dtype_kind:
            raise ContractError(
                f"{name} dtype kind must be one of {self.dtype_kind!r}, "
                f"got {array.dtype}"
            )
        if self.finite and not np.all(np.isfinite(array)):
            raise ContractError(f"{name} must contain only finite values")
        return array


@dataclass(frozen=True)
class BenchmarkResult:
    """Store observations and setup metadata without claiming universal speed."""

    label: str
    number: int
    repeat: int
    warmup: int
    seconds: tuple[float, ...]
    python: str
    numpy: str
    platform: str
    machine: str

    @property
    def best_seconds_per_call(self) -> float:
        """Return the smallest observed repeat divided by calls per repeat."""
        return min(self.seconds) / self.number

    def to_json(self) -> str:
        """Serialize the complete result as deterministic JSON."""
        return json.dumps(asdict(self), indent=2, sort_keys=True)


@dataclass
class RunningMean:
    """Consume numeric iterables once while maintaining a testable invariant."""

    count: int = 0
    total: float = 0.0

    def update(self, values: Iterable[float]) -> None:
        """Consume values once and update count and total together."""
        for value in values:
            numeric = float(value)
            if not np.isfinite(numeric):
                raise ContractError("running mean values must be finite")
            self.count += 1
            self.total += numeric

    @property
    def mean(self) -> float:
        """Return the current mean, refusing an empty state."""
        if self.count == 0:
            raise ContractError("mean is undefined before any values are consumed")
        return self.total / self.count


def affine_batch(
    features: ArrayLike,
    weights: ArrayLike,
    bias: ArrayLike,
) -> NDArray[np.float64]:
    """Compute features @ weights.T + bias under explicit 2-D contracts."""
    feature_array = ArrayContract((None, None), "f").validate(
        features, name="features"
    ).astype(np.float64, copy=False)
    weight_array = ArrayContract((None, feature_array.shape[1]), "f").validate(
        weights, name="weights"
    ).astype(np.float64, copy=False)
    bias_array = ArrayContract((weight_array.shape[0],), "f").validate(
        bias, name="bias"
    ).astype(np.float64, copy=False)
    return feature_array @ weight_array.T + bias_array


def stable_logsumexp(values: ArrayLike, axis: int = -1) -> NDArray[np.float64]:
    """Compute log(sum(exp(values))) after a maximum shift."""
    array = np.asarray(values, dtype=np.float64)
    if array.ndim == 0 or array.size == 0:
        raise ContractError("values must be a nonempty array with at least one axis")
    if not np.all(np.isfinite(array)):
        raise ContractError("values must contain only finite values")
    try:
        maximum = np.max(array, axis=axis, keepdims=True)
    except AxisError as error:
        raise ContractError(f"axis {axis} is invalid for shape {array.shape}") from error
    shifted_sum = np.sum(np.exp(array - maximum), axis=axis, keepdims=True)
    result = maximum + np.log(shifted_sum)
    return np.squeeze(result, axis=axis)


def _shape_length(value: int) -> int:
    if isinstance(value, bool):
        raise TypeError
    return operator.index(value)


def broadcast_result_shape(*shapes: Sequence[int]) -> tuple[int, ...]:
    """Return the NumPy broadcast shape or raise a contract-focused error."""
    try:
        normalized = tuple(
            tuple(_shape_length(length) for length in shape)
            for shape in shapes
        )
    except TypeError as error:
        raise ContractError("shape lengths must be integers") from error
    if any(length < 0 for shape in normalized for length in shape):
        raise ContractError("shape lengths must be nonnegative")
    try:
        return np.broadcast_shapes(*normalized)
    except ValueError as error:
        raise ContractError(f"shapes are not broadcast-compatible: {normalized}") from error


def memory_relation(source: ArrayLike, result: ArrayLike) -> dict[str, bool]:
    """Report exact sharing, conservative possible sharing, and base presence."""
    source_array = np.asarray(source)
    result_array = np.asarray(result)
    return {
        "shares_memory": bool(np.shares_memory(source_array, result_array)),
        "may_share_memory": bool(np.may_share_memory(source_array, result_array)),
        "result_has_base": result_array.base is not None,
    }


def spawn_generators(root_entropy: int, count: int) -> tuple[np.random.Generator, ...]:
    """Create reproducible child generators through SeedSequence.spawn."""
    if isinstance(root_entropy, bool) or not isinstance(root_entropy, int):
        raise TypeError("root_entropy must be an integer")
    if root_entropy < 0:
        raise ContractError("root_entropy must be nonnegative")
    if isinstance(count, bool) or not isinstance(count, int):
        raise TypeError("count must be an integer")
    if count < 1:
        raise ContractError("count must be at least one")
    children = np.random.SeedSequence(root_entropy).spawn(count)
    return tuple(np.random.default_rng(child) for child in children)


def benchmark(
    function: Callable[[], object],
    *,
    label: str,
    number: int = 10,
    repeat: int = 5,
    warmup: int = 1,
) -> BenchmarkResult:
    """Measure a no-argument callable with explicit warmup and repeat metadata."""
    if not callable(function):
        raise TypeError("function must be callable")
    for name, value, minimum in (
        ("number", number, 1), ("repeat", repeat, 2), ("warmup", warmup, 0)
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
            raise ContractError(f"{name} must be an integer at least {minimum}")
    for _ in range(warmup):
        function()
    timer = timeit.Timer(function)
    observations = tuple(timer.repeat(repeat=repeat, number=number))
    return BenchmarkResult(
        label=label,
        number=number,
        repeat=repeat,
        warmup=warmup,
        seconds=observations,
        python=platform.python_version(),
        numpy=np.__version__,
        platform=platform.platform(),
        machine=platform.machine(),
    )


def environment_snapshot(repository: Path | None = None) -> dict[str, Any]:
    """Capture process, package, and optional Git state as JSON-compatible data."""
    snapshot: dict[str, Any] = {
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "python_executable": sys.executable,
        "numpy_version": np.__version__,
        "matplotlib_version": version("matplotlib"),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "process_id": os.getpid(),
    }
    if repository is not None:
        root = Path(repository).resolve()
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "status", "--porcelain=v1"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        snapshot["git_commit"] = commit
        snapshot["git_dirty"] = bool(status)
    return snapshot


def save_exploration_plot(
    x_values: ArrayLike,
    y_values: ArrayLike,
    output_path: Path,
    *,
    x_unit: str,
    y_unit: str,
) -> Path:
    """Save a labeled PNG with the noninteractive Agg canvas."""
    x_array = ArrayContract((None,), "fiu").validate(x_values, name="x_values")
    y_array = ArrayContract((x_array.size,), "fiu").validate(
        y_values, name="y_values"
    )
    path = Path(output_path)
    if path.suffix.lower() != ".png":
        raise ContractError("output_path must end in .png")
    path.parent.mkdir(parents=True, exist_ok=True)

    figure = Figure(figsize=(6.4, 4.0), layout="constrained")
    FigureCanvasAgg(figure)
    axes = figure.subplots()
    axes.plot(x_array, y_array, color="#16697a", marker="o", label="observed")
    axes.set_xlabel(f"input ({x_unit})")
    axes.set_ylabel(f"output ({y_unit})")
    axes.set_title("Exploratory computation")
    axes.grid(True, alpha=0.25)
    axes.legend()
    figure.savefig(path, dpi=120, metadata={"Software": "module 0.13"})
    return path