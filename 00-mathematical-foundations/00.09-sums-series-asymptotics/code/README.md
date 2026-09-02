# Code for §0.09 Sums, Series, and Asymptotics

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Worked solutions](../solutions/README.md)

## Purpose

[`series_tools.py`](series_tools.py) implements a small set of standard-library tools that map directly to the module's derivations:

- exact arithmetic and geometric finite sums using `fractions.Fraction`;
- finite partial sums and harmonic numbers using `math.fsum`;
- integral bounds for harmonic numbers;
- alternating harmonic partial sums;
- the leading log-Stirling approximation, exact rational correction bounds, and outward-rounded floating endpoints.

The Stirling helpers stay in the logarithmic domain. This avoids factorial overflow and makes the correction term visible. For large inputs, the analytic interval can be narrower than one binary64 unit, so the exact rational correction interval is the authoritative result. The float endpoints are padded by several representable steps for diagnostics, not offered as formal interval arithmetic.

## Run

From this directory, run:

```bash
python -m unittest -v
```

No third-party packages, network access, randomness, or data files are required.

## Evidence boundary

The tests compare finite-sum formulas with direct exact sums and check harmonic, alternating-series, and Stirling inequalities over declared finite ranges. Those checks can catch implementation and transcription errors. They do not prove convergence or an asymptotic statement.

The symbolic proofs and source-supported hypotheses live in the module lesson. Python's `math.fsum` and `math.lgamma` behavior is tied to the official documentation cited there.

[Back to module](../README.md) | [Exercises](../exercises/README.md)