"""Finite sums and certified bounds for module 0.09."""

from collections.abc import Iterable
from fractions import Fraction
from math import fsum, inf, log, nextafter, pi


def _require_nonnegative_integer(name: str, value: int) -> None:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def arithmetic_sum(
    first: int | Fraction,
    difference: int | Fraction,
    count: int,
) -> Fraction:
    """Return an exact sum of ``count`` terms from an arithmetic sequence."""
    _require_nonnegative_integer("count", count)
    first_fraction = Fraction(first)
    difference_fraction = Fraction(difference)
    return Fraction(count, 2) * (
        2 * first_fraction + (count - 1) * difference_fraction
    )


def geometric_sum(
    first: int | Fraction,
    ratio: int | Fraction,
    count: int,
) -> Fraction:
    """Return an exact finite geometric sum."""
    _require_nonnegative_integer("count", count)
    first_fraction = Fraction(first)
    ratio_fraction = Fraction(ratio)
    if ratio_fraction == 1:
        return count * first_fraction
    return first_fraction * (1 - ratio_fraction**count) / (1 - ratio_fraction)


def partial_sums(terms: Iterable[float]) -> list[float]:
    """Return floating-point partial sums using accurate prefix summation."""
    prefix: list[float] = []
    result: list[float] = []
    for term in terms:
        prefix.append(term)
        result.append(fsum(prefix))
    return result


def harmonic_number(number: int) -> float:
    """Return H_number as an accurately accumulated floating-point sum."""
    _require_nonnegative_integer("number", number)
    return fsum(1 / index for index in range(1, number + 1))


def harmonic_integral_bounds(number: int) -> tuple[float, float]:
    """Return lower and upper integral bounds for a positive harmonic number."""
    _require_nonnegative_integer("number", number)
    if number == 0:
        raise ValueError("number must be positive")
    return log(number + 1), 1 + log(number)


def alternating_harmonic_partial_sum(number: int) -> float:
    """Return the first ``number`` terms of the alternating harmonic series."""
    _require_nonnegative_integer("number", number)
    return fsum((1 if index % 2 else -1) / index for index in range(1, number + 1))


def stirling_log_leading(number: int) -> float:
    """Return log(sqrt(2*pi*n) * (n/e)**n) without overflow."""
    _require_nonnegative_integer("number", number)
    if number == 0:
        raise ValueError("number must be positive")
    return (number + 0.5) * log(number) - number + 0.5 * log(2 * pi)


def stirling_log_correction_bounds(number: int) -> tuple[Fraction, Fraction]:
    """Bound the correction to the leading log-Stirling expression exactly."""
    _require_nonnegative_integer("number", number)
    if number == 0:
        raise ValueError("number must be positive")
    lower = Fraction(1, 12 * number) - Fraction(1, 360 * number**3)
    upper = Fraction(1, 12 * number)
    return lower, upper


def stirling_log_bounds(number: int) -> tuple[float, float]:
    """Return padded float endpoints derived from Stirling inequalities."""
    leading = stirling_log_leading(number)
    correction_lower, correction_upper = stirling_log_correction_bounds(number)
    lower = nextafter(leading + float(correction_lower), -inf, steps=16)
    upper = nextafter(leading + float(correction_upper), inf, steps=16)
    return lower, upper