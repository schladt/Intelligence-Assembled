"""Exact finite-counting helpers for module 0.08."""

from collections.abc import Iterable, Sequence
from math import comb, perm


def _require_nonnegative(name: str, value: int) -> None:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def falling_factorial(population: int, draws: int) -> int:
    """Return population * (population - 1) * ... for ``draws`` factors."""
    _require_nonnegative("population", population)
    _require_nonnegative("draws", draws)
    return perm(population, draws)


def multinomial(counts: Iterable[int]) -> int:
    """Count words with the requested multiplicity of each symbol."""
    result = 1
    placed = 0
    for count in counts:
        _require_nonnegative("each count", count)
        result *= comb(placed + count, count)
        placed += count
    return result


def weak_composition_count(total: int, parts: int) -> int:
    """Count nonnegative integer solutions to x_1 + ... + x_parts = total."""
    _require_nonnegative("total", total)
    _require_nonnegative("parts", parts)
    if parts == 0:
        return int(total == 0)
    return comb(total + parts - 1, parts - 1)


def positive_composition_count(total: int, parts: int) -> int:
    """Count positive integer solutions to x_1 + ... + x_parts = total."""
    _require_nonnegative("total", total)
    _require_nonnegative("parts", parts)
    if parts == 0:
        return int(total == 0)
    if total < parts:
        return 0
    return comb(total - 1, parts - 1)


def sampling_count(
    population: int,
    draws: int,
    *,
    replacement: bool,
    ordered: bool,
) -> int:
    """Return the size of one of the four finite sampling spaces."""
    _require_nonnegative("population", population)
    _require_nonnegative("draws", draws)
    if draws == 0:
        return 1
    if population == 0:
        return 0
    if replacement and ordered:
        return population**draws
    if replacement:
        return comb(population + draws - 1, draws)
    if ordered:
        return perm(population, draws)
    return comb(population, draws)


def inclusion_exclusion_union(sets: Sequence[set[object]]) -> int:
    """Count a finite union by the full inclusion-exclusion formula."""
    total = 0
    family_size = len(sets)
    for mask in range(1, 1 << family_size):
        selected = [sets[index] for index in range(family_size) if mask >> index & 1]
        intersection = set.intersection(*selected)
        sign = 1 if len(selected) % 2 else -1
        total += sign * len(intersection)
    return total


def convolve(left: Sequence[int], right: Sequence[int]) -> list[int]:
    """Multiply two finite generating polynomials in coefficient form."""
    if not left or not right:
        return []
    result = [0] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            result[left_degree + right_degree] += left_coefficient * right_coefficient
    return result


def bounded_sum_count(maxima: Sequence[int], total: int) -> int:
    """Count solutions with 0 <= x_i <= maxima[i] and a fixed sum."""
    _require_nonnegative("total", total)
    coefficients = [1]
    for maximum in maxima:
        _require_nonnegative("each maximum", maximum)
        coefficients = convolve(coefficients, [1] * (maximum + 1))
    return coefficients[total] if total < len(coefficients) else 0


def fibonacci(number: int) -> int:
    """Return F_number for F_0 = 0 and F_1 = 1."""
    _require_nonnegative("number", number)
    previous, current = 0, 1
    for _ in range(number):
        previous, current = current, previous + current
    return previous


def catalan(number: int) -> int:
    """Return the number of balanced parenthesis words with ``number`` pairs."""
    _require_nonnegative("number", number)
    return comb(2 * number, number) // (number + 1)