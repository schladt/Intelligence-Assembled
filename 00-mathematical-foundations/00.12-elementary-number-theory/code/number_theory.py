"""Exact teaching implementations for module 0.12.

The functions use integer arithmetic and expose their mathematical contracts.
Factorization, primality checks, finite-field operations, and RSA construction
are intentionally limited to small educational inputs.
"""

from dataclasses import dataclass
from math import isqrt
from typing import NamedTuple


class EuclidStep(NamedTuple):
    dividend: int
    divisor: int
    quotient: int
    remainder: int


class BezoutResult(NamedTuple):
    gcd: int
    x: int
    y: int


class CRTResult(NamedTuple):
    residue: int
    modulus: int


@dataclass(frozen=True)
class ToyRSAKey:
    """A tiny textbook RSA key, unsuitable for security."""

    p: int
    q: int
    n: int
    phi: int
    e: int
    d: int


def _require_int(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def gcd_trace(a: int, b: int) -> tuple[int, tuple[EuclidStep, ...]]:
    """Return normalized gcd(a, b) and Euclidean division steps.

    The gcd is nonnegative, including gcd(0, 0) = 0. Trace operands are
    absolute values, so every nonterminal step has 0 <= remainder < divisor.
    """
    _require_int(a, "a")
    _require_int(b, "b")
    dividend, divisor = abs(a), abs(b)
    steps: list[EuclidStep] = []
    while divisor:
        quotient, remainder = divmod(dividend, divisor)
        steps.append(EuclidStep(dividend, divisor, quotient, remainder))
        dividend, divisor = divisor, remainder
    return dividend, tuple(steps)


def gcd(a: int, b: int) -> int:
    """Return the nonnegative greatest common divisor of two integers."""
    return gcd_trace(a, b)[0]


def lcm(a: int, b: int) -> int:
    """Return the nonnegative least common multiple, with lcm(a, 0) = 0."""
    _require_int(a, "a")
    _require_int(b, "b")
    if a == 0 or b == 0:
        return 0
    return abs((a // gcd(a, b)) * b)


def extended_gcd(a: int, b: int) -> BezoutResult:
    """Return g, x, y with g = gcd(a, b) >= 0 and ax + by = g."""
    _require_int(a, "a")
    _require_int(b, "b")
    old_remainder, remainder = abs(a), abs(b)
    old_x, x = 1, 0
    old_y, y = 0, 1

    while remainder:
        quotient = old_remainder // remainder
        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    if a < 0:
        old_x = -old_x
    if b < 0:
        old_y = -old_y
    return BezoutResult(old_remainder, old_x, old_y)


def modular_inverse(value: int, modulus: int) -> int:
    """Return value's inverse in [0, modulus), requiring modulus >= 2."""
    _require_int(value, "value")
    _require_int(modulus, "modulus")
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    result = extended_gcd(value, modulus)
    if result.gcd != 1:
        raise ValueError("an inverse exists exactly when gcd(value, modulus) is 1")
    return result.x % modulus


def chinese_remainder(congruences: tuple[tuple[int, int], ...]) -> CRTResult:
    """Solve a finite compatible congruence system.

    Moduli must be at least 2 but need not be pairwise coprime. A solution
    exists exactly when every merged residue agrees modulo the relevant gcd.
    The result is normalized modulo the least common multiple of all moduli.
    """
    if not congruences:
        raise ValueError("at least one congruence is required")
    residue, modulus = 0, 1
    for index, pair in enumerate(congruences):
        if len(pair) != 2:
            raise ValueError("each congruence must contain a residue and modulus")
        next_residue, next_modulus = pair
        _require_int(next_residue, f"residue {index}")
        _require_int(next_modulus, f"modulus {index}")
        if next_modulus < 2:
            raise ValueError("every modulus must be at least 2")
        next_residue %= next_modulus

        common = gcd(modulus, next_modulus)
        difference = next_residue - residue
        if difference % common:
            raise ValueError("congruences are incompatible modulo their gcd")

        reduced_modulus = next_modulus // common
        if reduced_modulus == 1:
            multiplier = 0
        else:
            multiplier = (
                (difference // common)
                * modular_inverse(modulus // common, reduced_modulus)
            ) % reduced_modulus
        combined_modulus = modulus * reduced_modulus
        residue = (residue + modulus * multiplier) % combined_modulus
        modulus = combined_modulus
    return CRTResult(residue, modulus)


def trial_factorization(n: int) -> tuple[tuple[int, int], ...]:
    """Factor n >= 2 by trial division for small educational inputs."""
    _require_int(n, "n")
    if n < 2:
        raise ValueError("factorization requires n >= 2")
    factors: list[tuple[int, int]] = []
    exponent = 0
    while n % 2 == 0:
        n //= 2
        exponent += 1
    if exponent:
        factors.append((2, exponent))

    candidate = 3
    while candidate <= isqrt(n):
        exponent = 0
        while n % candidate == 0:
            n //= candidate
            exponent += 1
        if exponent:
            factors.append((candidate, exponent))
        candidate += 2
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def _is_small_prime(n: int) -> bool:
    return n >= 2 and trial_factorization(n) == ((n, 1),)


def phi_from_factors(factors: tuple[tuple[int, int], ...]) -> int:
    """Compute Euler's phi from a complete distinct-prime factorization."""
    if not factors:
        raise ValueError("a nonempty factorization is required")
    seen: set[int] = set()
    result = 1
    for prime, exponent in factors:
        _require_int(prime, "prime")
        _require_int(exponent, "exponent")
        if prime in seen or not _is_small_prime(prime) or exponent < 1:
            raise ValueError("factors must be distinct primes with positive exponents")
        seen.add(prime)
        result *= (prime - 1) * prime ** (exponent - 1)
    return result


def phi(n: int) -> int:
    """Return the number of residue classes coprime to n, for n >= 2."""
    return phi_from_factors(trial_factorization(n))


def modular_power(base: int, exponent: int, modulus: int) -> int:
    """Compute base**exponent modulo modulus by repeated squaring."""
    _require_int(base, "base")
    _require_int(exponent, "exponent")
    _require_int(modulus, "modulus")
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    result = 1
    factor = base % modulus
    remaining = exponent
    while remaining:
        if remaining % 2:
            result = (result * factor) % modulus
        factor = (factor * factor) % modulus
        remaining //= 2
    return result % modulus


def fp_add(left: int, right: int, prime: int) -> int:
    """Add two representatives in F_p, validating a small prime modulus."""
    _require_small_prime(prime)
    return (left + right) % prime


def fp_multiply(left: int, right: int, prime: int) -> int:
    """Multiply two representatives in F_p, validating a small prime modulus."""
    _require_small_prime(prime)
    return (left * right) % prime


def fp_inverse(value: int, prime: int) -> int:
    """Invert a nonzero representative in F_p."""
    _require_small_prime(prime)
    if value % prime == 0:
        raise ValueError("zero has no multiplicative inverse in a field")
    return modular_inverse(value, prime)


def fp_divide(numerator: int, denominator: int, prime: int) -> int:
    """Divide in F_p by multiplying by the denominator's inverse."""
    return fp_multiply(numerator, fp_inverse(denominator, prime), prime)


def _require_small_prime(prime: int) -> None:
    _require_int(prime, "prime")
    if not _is_small_prime(prime):
        raise ValueError("the modulus must be prime for F_p field operations")


def make_toy_rsa_key(p: int, q: int, e: int) -> ToyRSAKey:
    """Construct a tiny textbook RSA key for arithmetic demonstrations only."""
    _require_small_prime(p)
    _require_small_prime(q)
    _require_int(e, "e")
    if p == q:
        raise ValueError("p and q must be distinct primes")
    modulus = p * q
    totient = (p - 1) * (q - 1)
    if not 1 < e < totient or gcd(e, totient) != 1:
        raise ValueError("e must satisfy 1 < e < phi(n) and gcd(e, phi(n)) = 1")
    return ToyRSAKey(p, q, modulus, totient, e, modular_inverse(e, totient))


def toy_rsa_encrypt(message: int, key: ToyRSAKey) -> int:
    """Apply raw textbook RSA exponentiation, which is not secure encryption."""
    _require_int(message, "message")
    if not 0 <= message < key.n:
        raise ValueError("message representative must satisfy 0 <= message < n")
    return modular_power(message, key.e, key.n)


def toy_rsa_decrypt(ciphertext: int, key: ToyRSAKey) -> int:
    """Invert raw textbook RSA exponentiation, without padding or security."""
    _require_int(ciphertext, "ciphertext")
    if not 0 <= ciphertext < key.n:
        raise ValueError("ciphertext representative must satisfy 0 <= ciphertext < n")
    return modular_power(ciphertext, key.d, key.n)