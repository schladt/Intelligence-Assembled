# Solutions for §0.13 Programming and Scientific Computing

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

These are full worked solutions. Equivalent work is valid when it preserves the
same contracts and evidence limits. Run Python fences from `code/` with NumPy
and Matplotlib available.

## E0.13.01 Write an executable function contract

### Key idea

The function contract includes runtime facts that annotations cannot enforce.

### Reasoning

Accepted values are finite, floating, rank-two arrays with no zero-norm row.
Rows are examples, columns are features, and units must be consistent within a
row norm. The function does not mutate the input. It returns a newly allocated
`float64` array with the same shape and unitless rows of norm one.

```python
import numpy as np
from scientific_computing import ArrayContract, ContractError

def normalize_rows(matrix):
    array = ArrayContract((None, None), "f").validate(matrix, name="matrix")
    array = array.astype(np.float64, copy=False)
    norms = np.sqrt(np.sum(array * array, axis=1, keepdims=True))
    if np.any(norms == 0.0):
        raise ContractError("every row must have nonzero norm")
    return array / norms

source = np.array([[3.0, 4.0], [0.0, -2.0]], dtype=np.float32)
result = normalize_rows(source)
np.testing.assert_allclose(result, [[0.6, 0.8], [0.0, -1.0]])
assert result.dtype == np.float64
assert not np.shares_memory(source, result)
try:
    normalize_rows([[0.0, 0.0]])
except ContractError:
    pass
else:
    raise AssertionError("zero row accepted")
```

Annotations support readers and static tools. They do not automatically inspect
rank, dtype, finiteness, or norm.

### Verification

Both output row norms are one within floating tolerance, and the source remains
unchanged.

### Common wrong turn

Do not divide first and hope NumPy warnings enforce a domain contract.

## E0.13.02 Audit a one-shot iterator and state invariant

### Key idea

An iterable may produce an iterator, while an iterator itself advances and can
be exhausted.

### Reasoning

```python
from scientific_computing import RunningMean

values = [2.0, 4.0, 9.0]
stream = (value for value in values)
assert list(values) == list(values) == [2.0, 4.0, 9.0]

running = RunningMean()
running.update(stream)
assert list(stream) == []
assert (running.count, running.total, running.mean) == (3, 15.0, 5.0)
running.update(iter([5.0, 10.0]))
assert (running.count, running.total, running.mean) == (5, 30.0, 6.0)
```

The invariant is that `count` equals the number consumed, `total` equals their
sum, and `mean == total / count` when count is positive.

The broken expression consumes `values` in `sum` before `list(values)` can count
it. A one-pass repair tracks count and total together, as `RunningMean` does. A
different repair is `materialized = list(values)` followed by `sum` and `len`.
That permits repeated passes but stores every reference.

### Verification

Two updates preserve all three invariant clauses.

### Common wrong turn

`Iterable` does not promise `len` or a second traversal.

## E0.13.03 Separate shape, size, ndim, and dtype

### Key idea

Logical structure and arithmetic representation are separate contracts.

### Reasoning

The metadata is `(2, 3, 4)`, `24`, `3`, `2` bytes, `48` bytes, and strides
`(24, 8, 2)`. Reducing axis one removes its length-three axis, yielding shape
`(2, 4)`. NumPy promotes this small signed integer reduction to the platform
integer dtype in the validated environment.

```python
import numpy as np

array = np.arange(24, dtype=np.int16).reshape(2, 3, 4)
assert (array.shape, array.size, array.ndim) == ((2, 3, 4), 24, 3)
assert (array.itemsize, array.nbytes, array.strides) == (2, 48, (24, 8, 2))
reduced = array.sum(axis=1)
assert reduced.shape == (2, 4)
assert reduced.dtype == np.dtype(np.int_)

overflow = np.array([120], dtype=np.int8) + np.array([20], dtype=np.int8)
assert overflow.item() == -116
assert 120 + 20 == 140
assert np.float32(16_777_216) + np.float32(1) == np.float32(16_777_216)
```

Python integers expand. NumPy `int8` arithmetic is fixed-width. `float32`
cannot distinguish every consecutive integer at that magnitude.

### Verification

Stride products match row-major movement: 12, 4, and 1 elements per step.

### Common wrong turn

Shape correctness does not detect overflow, rounding, wrong units, or wrong
axis meaning.

## E0.13.04 Trace strides, views, and copies

### Key idea

Strides map indices to bytes; indexing policy determines sharing.

### Reasoning

The offset of `(2, 3)` is $2(40)+3(8)=104$ bytes. Transpose shape and strides
are `(5, 4)` and `(8, 40)`. The step-two slice has shape `(4, 3)` and strides
`(40, 16)`.

```python
import numpy as np
from scientific_computing import memory_relation

source = np.arange(20, dtype=np.float64).reshape(4, 5)
assert sum(index * stride for index, stride in zip((2, 3), source.strides)) == 104
assert (source.T.shape, source.T.strides) == ((5, 4), (8, 40))
assert (source[:, ::2].shape, source[:, ::2].strides) == ((4, 3), (40, 16))

view = source[1:3, 1:4]
copy = source[[1, 2], 1:4]
assert memory_relation(source, view)["shares_memory"]
assert not memory_relation(source, copy)["shares_memory"]
view[0, 0] = 99
copy[0, 1] = -1
assert source[1, 1] == 99
assert source[1, 2] != -1
```

A reshaped array can already be a view of the original one-dimensional buffer,
so another view's `.base` may refer to an earlier owner rather than the name
`source`. `np.shares_memory` answers the sharing question directly. Copy a small
slice when retaining it would otherwise retain a much larger buffer whose other
data is no longer needed.

### Verification

Mutation changes only the basic-slice source region.

### Common wrong turn

Do not describe strides as element counts without dividing by `itemsize`.

## E0.13.05 Derive broadcasting and multiplication contracts

### Key idea

Broadcast from the trailing side, and distinguish elementwise from contracted
axes.

### Reasoning

The outcomes are `(7, 3, 5)`, `(4, 3, 6)`, `(2, 4)`, and incompatible. In the
second pair, trailing `1` versus `6` and `3` versus `3` are compatible, while
the missing leading axis behaves as `1` against `4`. In the final pair, trailing
`3` versus `2` fails.

```python
import numpy as np
from scientific_computing import affine_batch, broadcast_result_shape

assert broadcast_result_shape((7, 1, 5), (3, 5)) == (7, 3, 5)
assert broadcast_result_shape((4, 3, 1), (3, 6)) == (4, 3, 6)
assert broadcast_result_shape((), (2, 4)) == (2, 4)
try:
    broadcast_result_shape((2, 3), (2,))
except ValueError:
    pass
else:
    raise AssertionError("incompatible shapes accepted")

left = np.array([[1, 2], [3, 4]])
right = np.array([[5, 6], [7, 8]])
assert (left * right).tolist() == [[5, 12], [21, 32]]
assert (left @ right).tolist() == [[19, 22], [43, 50]]

output = affine_batch(np.ones((8, 3)), np.ones((5, 3)), np.zeros(5))
assert output.shape == (8, 5)
```

For the affine operation, `(8,3) @ (3,5) -> (8,5)`, then `(5,)` broadcasts
over rows. The explicit two-by-two pair shows both operators run and differ.

### Verification

Each aligned trailing axis is either equal or one.

### Common wrong turn

Do not call a shape incompatible before checking missing leading axes as ones.

## E0.13.06 Stabilize and compare two computations

### Key idea

Subtracting the maximum preserves exact algebra while bounding every exponent by
one.

### Reasoning

For $m=\max_i x_i$, factor $e^m$ from the sum and move it outside the log.

```python
import numpy as np
from scientific_computing import stable_logsumexp

values = np.array([[1000.0, 1001.0, 999.0], [-1000.0, -999.0, -1001.0]])
with np.errstate(over="ignore"):
    assert np.isinf(np.log(np.sum(np.exp(values[0]))))

def loop_logsumexp(rows):
    outputs = []
    for row in rows:
        maximum = np.max(row)
        outputs.append(maximum + np.log(np.sum(np.exp(row - maximum))))
    return np.array(outputs)

observed = stable_logsumexp(values, axis=1)
looped = loop_logsumexp(values)
extended = values.astype(np.longdouble)
maximum = extended.max(axis=1)
reference = maximum + np.log(np.exp(extended - maximum[:, None]).sum(axis=1))
np.testing.assert_allclose(observed, looped, rtol=1e-14, atol=0.0)
np.testing.assert_allclose(observed, reference, rtol=1e-14, atol=0.0)
```

The array form removes the outer Python loop, but speed still depends on input
size, memory layout, temporary allocation, NumPy build, hardware, and competing
work.

### Verification

The direct form overflows while both shifted forms agree with extended
precision for the stated cases.

### Common wrong turn

Numerical agreement and vectorized syntax do not prove a universal timing rank.

## E0.13.07 Build an evidence ladder before trust

### Key idea

Different tests target different failure modes, and their finite domain must be
recorded.

### Reasoning

Use `Generator` local to the test and record root entropy. For affine reference
output, loop over batch and output coordinates, accumulating feature products.
For log-sum-exp, include the hand case `log(exp(0)+exp(0)) = log(2)`, empty and
nonfinite refusals, then 100 translation cases. A defensible tolerance for
random `float64` values near unit scale is `rtol=1e-13, atol=1e-13`; this is an
exercise policy, not a universal default.

```python
import numpy as np
from scientific_computing import affine_batch, stable_logsumexp

rng = np.random.default_rng(713)
np.testing.assert_allclose(stable_logsumexp([0.0, 0.0]), np.log(2.0))
for _ in range(100):
    values = rng.normal(size=(4, 7))
    shift = rng.normal()
    np.testing.assert_allclose(
        stable_logsumexp(values + shift, axis=1),
        stable_logsumexp(values, axis=1) + shift,
        rtol=1e-13, atol=1e-13,
    )

features = rng.normal(size=(3, 4))
weights = rng.normal(size=(2, 4))
bias = rng.normal(size=2)
reference = np.empty((3, 2))
for row in range(3):
    for output in range(2):
        reference[row, output] = sum(
            features[row, feature] * weights[output, feature]
            for feature in range(4)
        ) + bias[output]
np.testing.assert_allclose(affine_batch(features, weights, bias), reference)
```

Add focused `assertRaises` tests for each documented refusal. These tests do not
prove all values, all dtypes, all shapes, numerical optimality, or model validity.

### Verification

Hand values, randomized properties, and an independently expressed reference
all agree.

### Common wrong turn

Using the same vectorized expression in implementation and reference can repeat
the same mistake.

## E0.13.08 Localize a failure with a minimal reproduction

### Key idea

Reduce the failure while preserving it, then test the violated axis contract.

### Reasoning

The minimal reproduction is:

```text
features = np.ones((2, 3))
weights = np.ones((4, 2))
bias = np.zeros(4)
affine_batch(features, weights, bias)
```

The traceback ends at the contract error for weights axis one. At a breakpoint
before the call, inspect `type`, `shape`, `dtype`, `np.isfinite(...).all()`, and
whether preprocessing mutated or transposed either input. The falsifiable
hypothesis is: the weight loader produced `(outputs, 2)` but the feature contract
requires three columns. A regression test expects refusal for `(4,2)`.

The repair depends on provenance. If the loader accidentally dropped one weight
column, restore it and produce `(4,3)`. Do not transpose blindly: `(2,4)` still
does not match three features. Catching and discarding the exception would erase
the exact axis evidence and permit missing output downstream.

### Verification

The test fails before repair and `affine_batch(np.ones((2,3)),
np.ones((4,3)), np.zeros(4))` returns shape `(2,4)` afterward.

### Common wrong turn

Do not repair a shape mismatch without checking what each axis means.

## E0.13.09 Make an exploratory plot reproducible

### Key idea

The plot contract includes data origin, units, output path, backend, and cleanup.

### Reasoning

```python
from pathlib import Path
import tempfile
import numpy as np
from scientific_computing import ContractError, save_exploration_plot

x_values = np.arange(11.0)
y_values = x_values ** 2
with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "squared-distance.png"
    save_exploration_plot(x_values, y_values, path, x_unit="s", y_unit="m")
    assert path.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
    assert path.stat().st_size > 1_000
assert not path.exists()

for bad_x, bad_y, bad_path in (([0, 1], [0], "plot.png"), ([0], [0], "plot.pdf")):
    try:
        save_exploration_plot(bad_x, bad_y, Path(bad_path), x_unit="s", y_unit="m")
    except ContractError:
        pass
    else:
        raise AssertionError("invalid plot contract accepted")
```

The data is original synthetic data with transformation $y=x^2$. The line
suggests the sampled output grows nonlinearly. It does not establish a physical
law, causal relation, or behavior between and beyond samples.

### Verification

The test checks file identity, content size, refusal, and cleanup. Labels and
units are set by the helper and covered by source inspection.

### Common wrong turn

A visually smooth curve is not proof of the generating mechanism.

## E0.13.10 Profile time and memory within their limits

### Key idea

Timing, call profiling, and Python allocation tracing answer different questions.

### Reasoning

```python
import tracemalloc
import numpy as np
from scientific_computing import benchmark

array = np.arange(10_000.0)
values = array.tolist()

def python_squares():
    return [value * value for value in values]

def array_squares():
    return array * array

python_result = benchmark(python_squares, label="python list", number=10, repeat=5, warmup=2)
array_result = benchmark(array_squares, label="numpy array", number=10, repeat=5, warmup=2)
assert len(python_result.seconds) == len(array_result.seconds) == 5

tracemalloc.start()
python_squares()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
assert current >= 0 and peak >= current
```

Report both JSON records, all repeats, setup, and hardware. `cProfile` can show
that `python_squares` executes Python-level calls and where cumulative time is
attributed. It adds overhead and does not provide a fair Python-versus-native
benchmark. `tracemalloc` measures traced Python allocator blocks. The native
buffer behind a NumPy result may not appear as a corresponding Python allocation.

### Verification

Only metadata and nonnegative observations are asserted. No speed ratio or time
threshold is a correctness condition.

### Common wrong turn

Do not report the fastest local observation as a universal property.

## E0.13.11 Design a reproducible run record

### Key idea

Reproduction needs a joined record of code, process, environment, data, state,
hardware, and evidence.

### Reasoning

```python
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import numpy as np
from scientific_computing import environment_snapshot

data = np.arange(12, dtype=np.float64).reshape(3, 4)
record = {
    "run": {
        "command": "python experiment.py --root-entropy 20260901",
        "working_directory": str(Path.cwd()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    },
    "environment": environment_snapshot(Path.cwd().parents[2]),
    "data": {
        "origin": "original synthetic sequence",
        "license": "project MIT license",
        "shape": data.shape,
        "dtype": str(data.dtype),
        "units": "unitless",
        "transformation": "arange(12).reshape(3, 4)",
        "sha256": sha256(data.tobytes()).hexdigest(),
    },
    "random": {"root_entropy": 20260901, "stream_role": "data"},
    "evidence": {"tests": ["test_scientific_computing.py"], "gaps": []},
}
assert len(json.dumps(record)) > 100
```

Add BitGenerator identity, output checksums, thread settings, CPU or accelerator
details, and limitations relevant to the real run. `pip freeze` omits code,
data, command, system, and hardware. A commit omits dirty changes and all
external state. A seed omits generator version, stream role, call order, and
everything outside randomness.

### Verification

The record serializes, includes an exact data checksum, and captures Git dirty
state rather than pretending the commit alone identifies source.

### Common wrong turn

Do not record sensitive environment values or credentials in a run manifest.

## E0.13.12 Construct independent random streams

### Key idea

Spawn named streams from one root and reconstruct them by the same child
position, while recording version and generator identity.

### Reasoning

```python
import numpy as np
from scientific_computing import spawn_generators

roles = ("data", "parameters", "resampling")
first = dict(zip(roles, spawn_generators(20260901, len(roles))))
second = dict(zip(roles, spawn_generators(20260901, len(roles))))

first_draws = {role: generator.integers(0, 2**31, size=12)
               for role, generator in first.items()}
second_draws = {role: generator.integers(0, 2**31, size=12)
                for role, generator in second.items()}
for role in roles:
    np.testing.assert_array_equal(first_draws[role], second_draws[role])
assert not np.array_equal(first_draws["data"], first_draws["parameters"])

shared_a = np.random.default_rng(7)
data_then_model = (shared_a.integers(10, size=3), shared_a.integers(10, size=3))
shared_b = np.random.default_rng(7)
model_only = shared_b.integers(10, size=3)
np.testing.assert_array_equal(data_then_model[0], model_only)
assert not np.array_equal(data_then_model[1], model_only)
```

The finite nonidentity check detects an accidental clone in this sample. It
does not prove statistical independence. `root_seed + worker_id` can overlap
across runs when both roots and worker IDs change by small increments, and it
does not encode a spawn tree. `SeedSequence.spawn` mixes child position into
state construction.

Record NumPy `2.5.2` for this validation, the `PCG64` BitGenerator observed in
each stream, root entropy, child index, and role. NumPy does not guarantee the
`Generator` bitstream across versions, so reproduction includes version and
algorithm identity.

Beyond `seed(0)`, record source commit and dirty state, command, interpreter,
packages, process and worker topology, environment, data checksum and
preprocessing, configuration, hardware and threads, stream roles, outputs,
tests, and limitations.

### Verification

Each role reproduces by position; the roles are not finite clones; and the
global-stream example exposes call-order coupling.

### Common wrong turn

Changing the integer seed for each worker is not the same contract as spawning
independent child streams.

[Back to module](../README.md) | [Exercise set](../exercises/README.md)