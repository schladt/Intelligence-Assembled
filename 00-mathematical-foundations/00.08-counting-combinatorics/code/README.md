# Code for §0.08 Counting and Combinatorics

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Worked solutions](../solutions/README.md)

## Purpose

[`counting.py`](counting.py) implements the module's finite counting mechanisms with Python's standard library and exact integer arithmetic:

- falling factorials and multinomial coefficients;
- weak and positive composition counts;
- all four ordered/unordered and with/without-replacement sampling counts;
- full finite inclusion-exclusion;
- finite generating-polynomial convolution;
- bounded integer-sum coefficient extraction;
- iterative Fibonacci values and exact Catalan numbers.

The implementation is intentionally small. It exposes the formulas and coefficient operations instead of hiding them behind a symbolic algebra system.

## Run

From this directory, run:

```bash
python -m unittest -v
```

No third-party packages, network access, randomness, or data files are required. On the configured project environment, the suite should complete in under one second on ordinary hardware.

## Evidence boundary

The tests compare formulas with exhaustive enumeration on small finite domains and verify identities over declared ranges. That is strong evidence for the implementation on those inputs. The general theorems still require the bijective, algebraic, or inclusion-exclusion arguments in the lesson.

Python's `math.comb`, `math.perm`, and `itertools` behavior is sourced from the official documentation cited by the module. The surrounding helpers, tests, examples, and assertions are original.

[Back to module](../README.md) | [Exercises](../exercises/README.md)