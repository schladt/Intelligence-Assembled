# Code for §0.10 Inequalities

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Worked solutions](../solutions/README.md)

## Purpose

[`inequality_tools.py`](inequality_tools.py) implements finite, standard-library
audit helpers that map directly to the lesson:

- finite $\ell^p$ norms for $1\le p\le\infty$;
- weighted AM-GM sides with validated values and weights;
- Cauchy-Schwarz, Hölder, and Minkowski sides;
- a finite weighted Jensen gap for a caller-supplied function;
- the capped sum used to report a finite union bound;
- Bernoulli's two sides for its integer-exponent contract;
- finite rearrangement extrema.

The functions reject empty vectors, unequal lengths, invalid exponents,
unnormalized or negative weights, nonfinite values, invalid probabilities, and
Bernoulli inputs outside the stated domain.

## Run

From this directory, run:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v
```

No third-party packages, network access, randomness, or data files are required.

## Design limits

The helpers use binary floating-point arithmetic. `math.fsum` reduces summation
error but does not provide formal interval arithmetic. Equality cases involving
roots, logarithms, or noninteger powers therefore use justified tolerances in
tests.

`jensen_gap` evaluates a function but cannot prove that the function is convex,
concave, or defined on an entire interval. The caller owns that mathematical
proof. `union_bound` receives marginal probabilities, not event sets, so it
cannot measure overlap or compute the actual union probability.

## Evidence boundary

The 9 tests cover hand-computed values, equality cases, invalid contracts,
several exponents, and all $4!$ pairings of one rearrangement example. These
checks can catch implementation and transcription errors. They do not prove any
theorem for all real vectors, functions, probabilities, lengths, or exponents.

[Back to module](../README.md) | [Exercises](../exercises/README.md)