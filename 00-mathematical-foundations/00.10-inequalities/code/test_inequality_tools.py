"""Tests for the finite inequality audit helpers."""

import itertools
import math
import unittest

from inequality_tools import (
    bernoulli_sides,
    cauchy_schwarz_sides,
    holder_sides,
    jensen_gap,
    lp_norm,
    minkowski_sides,
    rearrangement_extremes,
    union_bound,
    weighted_am_gm_sides,
)


class InequalityToolsTests(unittest.TestCase):
    def test_lp_norms_and_triangle(self) -> None:
        self.assertEqual(lp_norm((3, 4), 2), 5)
        self.assertEqual(lp_norm((-3, 4), math.inf), 4)
        for exponent in (1, 1.5, 2, 4, math.inf):
            left, right = minkowski_sides((1, -2, 3), (-4, 5, 1), exponent)
            self.assertLessEqual(left, right + 1e-12)

    def test_weighted_am_gm_and_equality(self) -> None:
        geometric, arithmetic = weighted_am_gm_sides((1, 4), (0.5, 0.5))
        self.assertEqual(geometric, 2)
        self.assertEqual(arithmetic, 2.5)
        equal_geometric, equal_arithmetic = weighted_am_gm_sides(
            (7, 7, 7), (0.2, 0.3, 0.5)
        )
        self.assertAlmostEqual(equal_geometric, 7)
        self.assertAlmostEqual(equal_arithmetic, 7)
        self.assertEqual(weighted_am_gm_sides((0, 9), (0.5, 0.5))[0], 0)

    def test_cauchy_schwarz_and_equality(self) -> None:
        left, right = cauchy_schwarz_sides((1, 2, 3), (4, -5, 6))
        self.assertLessEqual(left, right)
        equality_left, equality_right = cauchy_schwarz_sides((1, 2), (-3, -6))
        self.assertAlmostEqual(equality_left, 15)
        self.assertAlmostEqual(equality_right, 15)
        self.assertEqual(cauchy_schwarz_sides((0, 0), (2, 3)), (0, 0))

    def test_holder_and_minkowski_equality(self) -> None:
        for exponent in (1.25, 1.5, 2, 3, 5):
            left, right = holder_sides((1, -2, 4), (-3, 5, 2), exponent)
            self.assertLessEqual(left, right + 1e-12)
        self.assertEqual(minkowski_sides((1, 2), (2, 4), 3), (lp_norm((3, 6), 3), 3 * lp_norm((1, 2), 3)))

    def test_jensen_gap_direction_and_equality(self) -> None:
        self.assertGreater(jensen_gap((1, 3), (0.25, 0.75), lambda value: value**2), 0)
        self.assertAlmostEqual(
            jensen_gap((2, 2, 2), (0.2, 0.3, 0.5), lambda value: value**2), 0
        )
        self.assertLess(jensen_gap((1, 4), (0.5, 0.5), math.log), 0)

    def test_union_bound(self) -> None:
        self.assertEqual(union_bound((0.1, 0.2, 0.3)), 0.6)
        self.assertEqual(union_bound((0.8, 0.7)), 1)
        self.assertEqual(union_bound(()), 0)

    def test_bernoulli_and_equality_cases(self) -> None:
        for exponent in range(11):
            for increment in (-1, -0.5, 0, 0.25, 2):
                left, right = bernoulli_sides(increment, exponent)
                self.assertGreaterEqual(left + 1e-12, right)
        self.assertEqual(bernoulli_sides(3, 0), (1, 1))
        self.assertEqual(bernoulli_sides(3, 1), (4, 4))
        self.assertEqual(bernoulli_sides(0, 8), (1, 1))

    def test_rearrangement_against_all_permutations(self) -> None:
        left = (3, -1, 2, 2)
        right = (4, 0, -2, 5)
        minimum, maximum = rearrangement_extremes(left, right)
        products = [
            math.fsum(a * b for a, b in zip(left, permutation))
            for permutation in itertools.permutations(right)
        ]
        self.assertEqual(minimum, min(products))
        self.assertEqual(maximum, max(products))

    def test_invalid_contracts(self) -> None:
        with self.assertRaises(ValueError):
            lp_norm((), 2)
        with self.assertRaises(ValueError):
            lp_norm((1, 2), 0.5)
        with self.assertRaises(ValueError):
            weighted_am_gm_sides((-1, 2), (0.5, 0.5))
        with self.assertRaises(ValueError):
            weighted_am_gm_sides((1, 2), (0.4, 0.4))
        with self.assertRaises(ValueError):
            cauchy_schwarz_sides((1,), (1, 2))
        with self.assertRaises(ValueError):
            holder_sides((1,), (1,), 1)
        with self.assertRaises(ValueError):
            union_bound((0.2, 1.1))
        with self.assertRaises(ValueError):
            bernoulli_sides(-1.1, 2)
        with self.assertRaises(ValueError):
            bernoulli_sides(0.1, True)


if __name__ == "__main__":
    unittest.main()