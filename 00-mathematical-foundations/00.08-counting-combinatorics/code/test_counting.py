"""Tests for the exact finite-counting helpers."""

import unittest
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb

from counting import (
    bounded_sum_count,
    catalan,
    convolve,
    falling_factorial,
    fibonacci,
    inclusion_exclusion_union,
    multinomial,
    positive_composition_count,
    sampling_count,
    weak_composition_count,
)


class CountingTests(unittest.TestCase):
    def test_sampling_table_matches_enumeration(self) -> None:
        population = tuple(range(5))
        draws = 3
        cases = (
            (True, True, product(population, repeat=draws)),
            (True, False, combinations_with_replacement(population, draws)),
            (False, True, permutations(population, draws)),
            (False, False, combinations(population, draws)),
        )
        for replacement, ordered, outcomes in cases:
            with self.subTest(replacement=replacement, ordered=ordered):
                self.assertEqual(
                    sampling_count(
                        len(population), draws,
                        replacement=replacement,
                        ordered=ordered,
                    ),
                    len(tuple(outcomes)),
                )

    def test_sampling_boundaries(self) -> None:
        for replacement in (False, True):
            for ordered in (False, True):
                self.assertEqual(
                    sampling_count(0, 0, replacement=replacement, ordered=ordered), 1
                )
                self.assertEqual(
                    sampling_count(0, 2, replacement=replacement, ordered=ordered), 0
                )
        self.assertEqual(
            sampling_count(2, 3, replacement=False, ordered=False), 0
        )
        self.assertEqual(sampling_count(2, 3, replacement=False, ordered=True), 0)

    def test_permutation_and_multinomial_counts(self) -> None:
        self.assertEqual(falling_factorial(8, 3), 336)
        self.assertEqual(multinomial((2, 2, 1)), 30)
        self.assertEqual(multinomial(()), 1)
        for red in range(6):
            for blue in range(6 - red):
                green = 5 - red - blue
                self.assertEqual(
                    multinomial((red, blue, green)),
                    comb(5, red) * comb(5 - red, blue),
                )

    def test_composition_counts_match_enumeration(self) -> None:
        for total in range(8):
            for parts in range(5):
                weak = sum(
                    sum(values) == total
                    for values in product(range(total + 1), repeat=parts)
                )
                positive = sum(
                    sum(values) == total
                    for values in product(range(1, total + 1), repeat=parts)
                )
                self.assertEqual(weak_composition_count(total, parts), weak)
                self.assertEqual(positive_composition_count(total, parts), positive)

    def test_inclusion_exclusion_matches_direct_union(self) -> None:
        families = (
            (),
            ({1, 2},),
            ({1, 2, 3}, {3, 4}, {2, 3, 5}),
            (set(), {1}, {1, 2}, {2, 3}),
        )
        for family in families:
            expected = len(set().union(*family)) if family else 0
            self.assertEqual(inclusion_exclusion_union(family), expected)

    def test_convolution_and_bounded_sums(self) -> None:
        self.assertEqual(convolve([1, 1], [1, 1]), [1, 2, 1])
        self.assertEqual(convolve([1, 1], [1, 1, 1]), [1, 2, 2, 1])
        self.assertEqual(convolve([], [1]), [])
        for total in range(10):
            expected = sum(
                left + middle + right == total
                for left in range(3)
                for middle in range(4)
                for right in range(2)
            )
            self.assertEqual(bounded_sum_count((2, 3, 1), total), expected)

    def test_binomial_and_vandermonde_identities(self) -> None:
        for number in range(15):
            coefficients = [1]
            for _ in range(number):
                coefficients = convolve(coefficients, [1, 1])
            self.assertEqual(coefficients, [comb(number, index) for index in range(number + 1)])
        for left_size in range(8):
            for right_size in range(8):
                for chosen in range(left_size + right_size + 1):
                    self.assertEqual(
                        sum(
                            comb(left_size, index) * comb(right_size, chosen - index)
                            for index in range(chosen + 1)
                            if index <= left_size and chosen - index <= right_size
                        ),
                        comb(left_size + right_size, chosen),
                    )

    def test_fibonacci_and_catalan_recurrences(self) -> None:
        fibonacci_values = [fibonacci(index) for index in range(16)]
        for index in range(2, len(fibonacci_values)):
            self.assertEqual(
                fibonacci_values[index],
                fibonacci_values[index - 1] + fibonacci_values[index - 2],
            )

        catalan_values = [catalan(index) for index in range(10)]
        for number in range(1, len(catalan_values)):
            self.assertEqual(
                catalan_values[number],
                sum(
                    catalan_values[left] * catalan_values[number - 1 - left]
                    for left in range(number)
                ),
            )

    def test_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            falling_factorial(-1, 0)
        with self.assertRaises(TypeError):
            fibonacci(2.0)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            catalan(True)
        with self.assertRaises(ValueError):
            bounded_sum_count((2, -1), 0)


if __name__ == "__main__":
    unittest.main()