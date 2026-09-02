"""Tests for the finite-sum and asymptotic-bound helpers."""

import unittest
from decimal import Decimal, localcontext
from fractions import Fraction
from math import factorial, lgamma, log

from series_tools import (
    alternating_harmonic_partial_sum,
    arithmetic_sum,
    geometric_sum,
    harmonic_integral_bounds,
    harmonic_number,
    partial_sums,
    stirling_log_bounds,
    stirling_log_correction_bounds,
    stirling_log_leading,
)


class SeriesToolsTests(unittest.TestCase):
    def test_arithmetic_sum_matches_direct_exact_sum(self) -> None:
        for first in range(-3, 4):
            for difference in range(-3, 4):
                for count in range(20):
                    expected = sum(first + index * difference for index in range(count))
                    self.assertEqual(arithmetic_sum(first, difference, count), expected)

    def test_geometric_sum_matches_direct_exact_sum(self) -> None:
        ratios = (Fraction(-1, 2), Fraction(0), Fraction(1, 3), Fraction(1), Fraction(2))
        for ratio in ratios:
            for count in range(15):
                expected = sum((Fraction(3, 2) * ratio**index for index in range(count)), Fraction())
                self.assertEqual(geometric_sum(Fraction(3, 2), ratio, count), expected)

    def test_partial_sums_preserve_prefix_meaning(self) -> None:
        self.assertEqual(partial_sums([1.0, -0.5, 0.25]), [1.0, 0.5, 0.75])
        self.assertEqual(partial_sums([]), [])

    def test_harmonic_integral_bounds(self) -> None:
        for number in range(1, 1001):
            lower, upper = harmonic_integral_bounds(number)
            value = harmonic_number(number)
            self.assertLessEqual(lower, value)
            self.assertLessEqual(value, upper)

    def test_harmonic_euler_remainder_bound(self) -> None:
        euler_gamma = 0.5772156649015328606
        for number in (1, 2, 10, 100, 1000, 10_000):
            remainder = harmonic_number(number) - log(number) - euler_gamma
            self.assertGreater(remainder, 0)
            self.assertLessEqual(remainder, 1 / number)

    def test_sharp_harmonic_remainder_at_high_precision(self) -> None:
        euler_gamma = Decimal(
            "0.57721566490153286060651209008240243104215933593992359880576723488486"
        )
        with localcontext() as context:
            context.prec = 70
            for number in (1, 2, 10, 100, 1000):
                decimal_number = Decimal(number)
                harmonic = sum(
                    (Decimal(1) / Decimal(index) for index in range(1, number + 1)),
                    Decimal(0),
                )
                approximation = (
                    decimal_number.ln()
                    + euler_gamma
                    + Decimal(1) / (2 * decimal_number)
                    - Decimal(1) / (12 * decimal_number**2)
                )
                remainder = harmonic - approximation
                self.assertGreater(remainder, 0)
                self.assertLess(remainder, Decimal(1) / (120 * decimal_number**4))

    def test_alternating_harmonic_next_term_bound(self) -> None:
        for number in range(1, 1000):
            error = abs(alternating_harmonic_partial_sum(number) - log(2))
            self.assertLessEqual(error, 1 / (number + 1))

    def test_padded_stirling_float_interval_contains_lgamma(self) -> None:
        for number in range(1, 10_001):
            lower, upper = stirling_log_bounds(number)
            exact_log = lgamma(number + 1)
            self.assertLessEqual(lower, exact_log)
            self.assertLessEqual(exact_log, upper)

    def test_exact_stirling_correction_bounds_at_high_precision(self) -> None:
        pi_decimal = Decimal(
            "3.1415926535897932384626433832795028841971693993751058209749445923078164"
        )
        with localcontext() as context:
            context.prec = 70
            for number in (1, 2, 10, 100, 1000):
                decimal_number = Decimal(number)
                exact_log = Decimal(factorial(number)).ln()
                leading = (
                    (decimal_number + Decimal("0.5")) * decimal_number.ln()
                    - decimal_number
                    + Decimal("0.5") * (2 * pi_decimal).ln()
                )
                correction = exact_log - leading
                lower, upper = stirling_log_correction_bounds(number)
                decimal_lower = Decimal(lower.numerator) / Decimal(lower.denominator)
                decimal_upper = Decimal(upper.numerator) / Decimal(upper.denominator)
                self.assertLessEqual(decimal_lower, correction)
                self.assertLessEqual(correction, decimal_upper)

    def test_stirling_correction_has_explicit_finite_width(self) -> None:
        for number in (1, 2, 10, 100, 1000):
            lower, upper = stirling_log_correction_bounds(number)
            self.assertEqual(upper - lower, Fraction(1, 360 * number**3))
            self.assertGreater(lower, 0)

    def test_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            arithmetic_sum(1, 1, -1)
        with self.assertRaises(TypeError):
            geometric_sum(1, 2, True)
        with self.assertRaises(ValueError):
            harmonic_integral_bounds(0)
        with self.assertRaises(ValueError):
            stirling_log_bounds(0)


if __name__ == "__main__":
    unittest.main()