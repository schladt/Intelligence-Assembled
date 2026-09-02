"""Finite numerical audits for module 0.10.

The helpers expose both sides of inequalities. Passing finite checks can catch
implementation mistakes, but it does not prove the corresponding theorem.
"""

from collections.abc import Callable, Iterable, Sequence
from math import exp, fsum, inf, isfinite, log


def _finite_values(values: Iterable[float], name: str) -> tuple[float, ...]:
    result = tuple(float(value) for value in values)
    if not result:
        raise ValueError(f"{name} must be nonempty")
    if not all(isfinite(value) for value in result):
        raise ValueError(f"{name} must contain only finite real values")
    return result


def _paired_values(
    left: Iterable[float], right: Iterable[float]
) -> tuple[tuple[float, ...], tuple[float, ...]]:
    left_values = _finite_values(left, "left")
    right_values = _finite_values(right, "right")
    if len(left_values) != len(right_values):
        raise ValueError("left and right must have the same length")
    return left_values, right_values


def _weights(weights: Iterable[float], count: int) -> tuple[float, ...]:
    result = _finite_values(weights, "weights")
    if len(result) != count:
        raise ValueError("weights and values must have the same length")
    if any(weight < 0 for weight in result):
        raise ValueError("weights must be nonnegative")
    if not abs(fsum(result) - 1.0) <= 1e-12:
        raise ValueError("weights must sum to one")
    return result


def lp_norm(values: Iterable[float], exponent: float) -> float:
    """Return the finite-dimensional l^p norm for 1 <= p <= infinity."""
    vector = _finite_values(values, "values")
    if exponent == inf:
        return max(abs(value) for value in vector)
    if not isfinite(exponent) or exponent < 1:
        raise ValueError("exponent must satisfy 1 <= p <= infinity")
    return fsum(abs(value) ** exponent for value in vector) ** (1 / exponent)


def weighted_am_gm_sides(
    values: Iterable[float], weights: Iterable[float]
) -> tuple[float, float]:
    """Return weighted geometric and arithmetic means for nonnegative values."""
    data = _finite_values(values, "values")
    normalized_weights = _weights(weights, len(data))
    if any(value < 0 for value in data):
        raise ValueError("AM-GM values must be nonnegative")
    arithmetic = fsum(weight * value for weight, value in zip(normalized_weights, data))
    if any(value == 0 and weight > 0 for value, weight in zip(data, normalized_weights)):
        geometric = 0.0
    else:
        geometric = exp(
            fsum(
                weight * log(value)
                for value, weight in zip(data, normalized_weights)
                if weight > 0
            )
        )
    return geometric, arithmetic


def cauchy_schwarz_sides(
    left: Iterable[float], right: Iterable[float]
) -> tuple[float, float]:
    """Return |<x,y>| and ||x||_2 ||y||_2."""
    left_values, right_values = _paired_values(left, right)
    dot_magnitude = abs(fsum(a * b for a, b in zip(left_values, right_values)))
    norm_product = lp_norm(left_values, 2) * lp_norm(right_values, 2)
    return dot_magnitude, norm_product


def holder_sides(
    left: Iterable[float], right: Iterable[float], exponent: float
) -> tuple[float, float]:
    """Return Holder sides for finite conjugate exponents p and q."""
    if not isfinite(exponent) or exponent <= 1:
        raise ValueError("exponent must be finite and greater than one")
    conjugate = exponent / (exponent - 1)
    left_values, right_values = _paired_values(left, right)
    product_sum = fsum(abs(a * b) for a, b in zip(left_values, right_values))
    norm_product = lp_norm(left_values, exponent) * lp_norm(right_values, conjugate)
    return product_sum, norm_product


def minkowski_sides(
    left: Iterable[float], right: Iterable[float], exponent: float
) -> tuple[float, float]:
    """Return ||x+y||_p and ||x||_p + ||y||_p for p >= 1."""
    left_values, right_values = _paired_values(left, right)
    summed = (a + b for a, b in zip(left_values, right_values))
    return (
        lp_norm(summed, exponent),
        lp_norm(left_values, exponent) + lp_norm(right_values, exponent),
    )


def jensen_gap(
    values: Iterable[float],
    weights: Iterable[float],
    function: Callable[[float], float],
) -> float:
    """Return sum_i w_i f(x_i) - f(sum_i w_i x_i)."""
    data = _finite_values(values, "values")
    normalized_weights = _weights(weights, len(data))
    mean = fsum(weight * value for weight, value in zip(normalized_weights, data))
    mean_of_outputs = fsum(
        weight * function(value) for weight, value in zip(normalized_weights, data)
    )
    gap = mean_of_outputs - function(mean)
    if not isfinite(gap):
        raise ValueError("function must return finite real values on the inputs and mean")
    return gap


def union_bound(probabilities: Iterable[float]) -> float:
    """Return min(1, sum of valid marginal event probabilities)."""
    values = tuple(float(value) for value in probabilities)
    if not all(isfinite(value) and 0 <= value <= 1 for value in values):
        raise ValueError("probabilities must lie in [0, 1]")
    return min(1.0, fsum(values))


def bernoulli_sides(base_increment: float, exponent: int) -> tuple[float, float]:
    """Return (1 + x)^n and 1 + nx for x >= -1 and integer n >= 0."""
    if not isfinite(base_increment) or base_increment < -1:
        raise ValueError("base_increment must be finite and at least -1")
    if not isinstance(exponent, int) or isinstance(exponent, bool) or exponent < 0:
        raise ValueError("exponent must be a nonnegative integer")
    return (1 + base_increment) ** exponent, 1 + exponent * base_increment


def rearrangement_extremes(
    left: Sequence[float], right: Sequence[float]
) -> tuple[float, float]:
    """Return minimum and maximum dot products over all pairings."""
    left_values, right_values = _paired_values(left, right)
    ascending_left = sorted(left_values)
    ascending_right = sorted(right_values)
    minimum = fsum(a * b for a, b in zip(ascending_left, reversed(ascending_right)))
    maximum = fsum(a * b for a, b in zip(ascending_left, ascending_right))
    return minimum, maximum