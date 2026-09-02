"""Boundary-focused tests for the module 0.12 teaching algorithms."""

import math
import unittest

from number_theory import (
    chinese_remainder,
    extended_gcd,
    fp_add,
    fp_divide,
    fp_inverse,
    fp_multiply,
    gcd,
    gcd_trace,
    lcm,
    make_toy_rsa_key,
    modular_inverse,
    modular_power,
    phi,
    phi_from_factors,
    toy_rsa_decrypt,
    toy_rsa_encrypt,
    trial_factorization,
)


class NumberTheoryTests(unittest.TestCase):
    def test_gcd_normalizes_signs_and_zero(self) -> None:
        for left, right, expected in (
            (0, 0, 0), (0, -18, 18), (-24, 0, 24), (-54, 24, 6), (54, -24, 6)
        ):
            self.assertEqual(gcd(left, right), expected)
            self.assertEqual(gcd(left, right), math.gcd(left, right))
        self.assertEqual(lcm(-6, 15), 30)
        self.assertEqual(lcm(0, 15), 0)

    def test_euclid_trace_preserves_division_contract(self) -> None:
        common, steps = gcd_trace(-252, 105)
        self.assertEqual(common, 21)
        self.assertTrue(steps)
        for dividend, divisor, quotient, remainder in steps:
            self.assertEqual(dividend, quotient * divisor + remainder)
            self.assertLess(remainder, divisor)
            self.assertGreaterEqual(remainder, 0)

    def test_extended_gcd_returns_bezout_coefficients_for_all_signs(self) -> None:
        for left, right in ((240, 46), (-240, 46), (240, -46), (-240, -46), (0, 0)):
            result = extended_gcd(left, right)
            self.assertEqual(result.gcd, math.gcd(left, right))
            self.assertEqual(left * result.x + right * result.y, result.gcd)

    def test_modular_inverse_exists_exactly_for_coprime_inputs(self) -> None:
        self.assertEqual(modular_inverse(-3, 11), 7)
        self.assertEqual(modular_inverse(38, 97), pow(38, -1, 97))
        with self.assertRaisesRegex(ValueError, "exactly"):
            modular_inverse(6, 15)
        with self.assertRaises(ValueError):
            modular_inverse(1, 1)

    def test_crt_pairwise_coprime_system(self) -> None:
        result = chinese_remainder(((2, 3), (3, 5), (2, 7)))
        self.assertEqual(result, (23, 105))

    def test_crt_noncoprime_compatible_and_incompatible_systems(self) -> None:
        compatible = chinese_remainder(((2, 6), (8, 9)))
        self.assertEqual(compatible, (8, 18))
        self.assertEqual(compatible.residue % 6, 2)
        self.assertEqual(compatible.residue % 9, 8)
        with self.assertRaisesRegex(ValueError, "incompatible"):
            chinese_remainder(((1, 4), (2, 6)))

    def test_factorization_and_phi_contracts(self) -> None:
        self.assertEqual(trial_factorization(2), ((2, 1),))
        self.assertEqual(trial_factorization(360), ((2, 3), (3, 2), (5, 1)))
        self.assertEqual(phi_from_factors(((2, 3), (3, 2), (5, 1))), 96)
        self.assertEqual(phi(36), 12)
        with self.assertRaises(ValueError):
            trial_factorization(1)
        with self.assertRaises(ValueError):
            phi_from_factors(((4, 1),))

    def test_modular_power_matches_builtin_and_exposes_fermat_caveat(self) -> None:
        for base, exponent, modulus in ((7, 128, 13), (-4, 37, 19), (5, 0, 11)):
            self.assertEqual(modular_power(base, exponent, modulus), pow(base, exponent, modulus))
        self.assertEqual(modular_power(2, 560, 561), 1)
        self.assertNotEqual(modular_power(3, 560, 561), 1)

    def test_finite_field_operations_and_composite_refusal(self) -> None:
        self.assertEqual(fp_add(6, 5, 7), 4)
        self.assertEqual(fp_multiply(6, 5, 7), 2)
        self.assertEqual(fp_inverse(3, 7), 5)
        self.assertEqual(fp_divide(4, 3, 7), 6)
        with self.assertRaisesRegex(ValueError, "zero"):
            fp_inverse(7, 7)
        with self.assertRaisesRegex(ValueError, "prime"):
            fp_inverse(3, 8)

    def test_toy_rsa_round_trip_includes_nonunits(self) -> None:
        key = make_toy_rsa_key(11, 17, 7)
        self.assertEqual((key.n, key.phi, key.d), (187, 160, 23))
        for message in (0, 1, 11, 17, 22, 42, 186):
            self.assertEqual(toy_rsa_decrypt(toy_rsa_encrypt(message, key), key), message)

    def test_toy_rsa_refuses_invalid_keys_and_representatives(self) -> None:
        with self.assertRaisesRegex(ValueError, "distinct"):
            make_toy_rsa_key(11, 11, 7)
        with self.assertRaisesRegex(ValueError, "prime"):
            make_toy_rsa_key(9, 17, 7)
        with self.assertRaisesRegex(ValueError, "gcd"):
            make_toy_rsa_key(11, 17, 10)
        key = make_toy_rsa_key(11, 17, 7)
        with self.assertRaises(ValueError):
            toy_rsa_encrypt(key.n, key)
        with self.assertRaises(ValueError):
            toy_rsa_decrypt(-1, key)


if __name__ == "__main__":
    unittest.main()