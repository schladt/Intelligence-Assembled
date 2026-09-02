# Code for §0.13 Programming and Scientific Computing

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

## Purpose

[`scientific_computing.py`](scientific_computing.py) implements the lesson's
contract-first mechanisms:

- shape, dtype-family, and finite-value validation;
- batch affine computation using `@` and trailing-axis broadcasting;
- stable log-sum-exp;
- broadcasting validation and memory-sharing diagnostics;
- a stateful running mean that consumes iterables once;
- independent reproducible generators through `SeedSequence.spawn`;
- a benchmark harness that records setup and all repeat observations;
- a JSON-compatible process and environment snapshot;
- labeled PNG output through Matplotlib's noninteractive Agg canvas.

## Dependencies

The module requires Python, NumPy, and Matplotlib. This repository has no
project-level dependency-file convention, so no requirements file or packaging
metadata was invented for this module.

Validated on 2026-09-01 with:

- CPython `3.14.4`;
- NumPy `2.5.2`;
- Matplotlib `3.11.1`.

These are the exact validation versions, not permanent support bounds.

## Run

From this directory, use the repository interpreter exactly:

```bash
PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg \
  /home/mschladt/projects/Intelligence-Assembled/.venv/bin/python \
  -m unittest -v test_scientific_computing.py
```

Tests create plots only in `TemporaryDirectory`. No data, network access,
interactive backend, committed output, or persistent random state is used.

## Contract map

| API | Inputs | Output or state | Main refusals |
|---|---|---|---|
| `ArrayContract.validate` | array-like, shape pattern, dtype kinds | validated ndarray | rank, axis, dtype, or finiteness mismatch |
| `affine_batch` | `(batch, features)`, `(outputs, features)`, `(outputs,)` | float64 `(batch, outputs)` | nonfloating, nonfinite, or mismatched axes |
| `stable_logsumexp` | nonempty finite array and valid axis | float64 reduction | scalar, empty, nonfinite, or invalid axis |
| `broadcast_result_shape` | nonnegative integer shape tuples | common shape | noninteger lengths or incompatible trailing axes |
| `memory_relation` | two array-like objects | exact sharing, conservative possible sharing, and base presence | none beyond conversion failure |
| `RunningMean.update` | one-pass finite iterable | updated count and total | nonfinite value; empty mean access |
| `spawn_generators` | nonnegative root entropy, positive count | child `Generator` tuple | invalid entropy or count |
| `benchmark` | no-argument callable and repeat policy | observations plus metadata | invalid callable or counts |
| `environment_snapshot` | optional Git repository path | JSON-compatible dictionary | invalid Git repository or unavailable Git |
| `save_exploration_plot` | equal-length 1-D numeric arrays, units, PNG path | written path | shape, finiteness, or suffix mismatch |

## Evidence boundary

The tests check hand-computed array operations, contract failures, a
long-double log-sum-exp reference, trailing-axis broadcasting, actual memory
sharing, one-shot iterator consumption, independent stream reconstruction,
benchmark metadata, environment versions, and temporary PNG output. They avoid
timing thresholds and random-distribution claims.

Passing the suite establishes behavior for those cases in the recorded
environment. It does not prove universal numerical accuracy, performance,
cross-version random bitstreams, total process-memory accounting, or scientific
validity of a future dataset or model.

[Back to module](../README.md) | [Exercises](../exercises/README.md)