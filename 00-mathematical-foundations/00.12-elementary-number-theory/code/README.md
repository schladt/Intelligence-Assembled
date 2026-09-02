# Code for §0.12 Elementary Number Theory

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

## Purpose

[`number_theory.py`](number_theory.py) implements the lesson's central
mechanisms with exact integer arithmetic:

- normalized gcd, lcm, and a Euclidean trace;
- extended Euclid and modular inverses;
- pairwise-coprime and general compatible CRT merging;
- trial factorization and $\varphi$ from prime factors;
- repeated-squaring modular exponentiation;
- small prime-field addition, multiplication, inversion, and division;
- explicitly toy-only RSA key construction, encryption, and decryption.

## Run

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v
```

No third-party packages, randomness, network access, or data files are needed.

## Contracts and limits

- Integer APIs reject Boolean values even though `bool` subclasses `int` in
  Python.
- `gcd(a, b)` is nonnegative and returns zero only for `(0, 0)`.
- `lcm(a, b)` is nonnegative and returns zero when either input is zero.
- Euclidean traces use absolute operands, positive divisors, and nonnegative
  remainders.
- Modular APIs require a modulus of at least two.
- `modular_inverse` succeeds exactly when the gcd is one.
- `chinese_remainder` requires at least one congruence, accepts noncoprime
  moduli when compatible, and returns the normalized class modulo their lcm.
- Trial factorization requires $n\ge2$ and is intended only for small inputs.
- `phi_from_factors` requires a complete list of distinct primes with positive
  exponents.
- Prime-field helpers validate a small prime modulus and refuse zero division.
- Toy RSA requires distinct small primes, a valid public exponent, and integer
  representatives in $[0,n)$. It performs raw deterministic exponentiation.

## Security warning

The RSA functions are deliberately named `toy_rsa_*`. They do not generate
secure primes, choose production key sizes, encode byte strings, apply OAEP or
PSS, protect private material, run in constant time, blind exponents, resist
faults, or provide protocol-level security. They must not be used to protect
data. A maintained cryptographic library and current protocol profile own those
responsibilities.

## Trusted comparisons

The tests compare from-scratch results with `math.gcd`, built-in three-argument
`pow`, and `pow(value, -1, modulus)` after the lesson mechanisms have been
implemented. These comparisons detect implementation disagreement. They do not
replace theorem proofs.

## Evidence boundary

The tests cover sign and zero normalization, every Euclidean step, Bézout
identities, nonunits, pairwise and noncoprime CRT cases, invalid factors,
Carmichael behavior, composite field refusal, invalid RSA keys, out-of-range
representatives, and RSA messages sharing factors with $n$. Passing them
establishes behavior on those finite cases. The lesson's proofs establish the
general claims.

[Back to module](../README.md) | [Exercises](../exercises/README.md)