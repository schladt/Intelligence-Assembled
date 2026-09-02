# Code for §0.15 Computability and Complexity

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Resources](../resources/README.md)

## Purpose

`complexity.py` contains small reference implementations for finite-state
recognition, context-free membership, bounded machine simulation, certificate
verification, pseudopolynomial search, reductions, parameterized search, and
approximation. `test_complexity.py` checks the observable contracts and compares
small exact results with exhaustive references.

The package uses only the Python 3.14 standard library. It illustrates models and
proof obligations. It does not decide nonhalting, prove asymptotic lower bounds,
or replace optimized parsers and solvers.

## Contents

| Symbol | Teaching purpose | Main bound |
|---|---|---|
| `DFA` | total deterministic finite-state recognition | $O(n)$ transitions, constant model memory |
| `CNFGrammar.accepts` | CYK context-free membership without epsilon rules | $O(n^3|G|)$ in direct analysis |
| `TuringMachine` | explicit tape-machine contract | model definition |
| `run_bounded` | separate accept, reject, and timeout | at most the requested steps |
| `verify_subset_sum` | check an indexed subset certificate | $O(n+|c|)$ validation and summation |
| `subset_sum_dp` | recover a nonnegative subset-sum witness | $O(nT)$ time, $O(T)$ sum states |
| `verify_vertex_cover` | check an undirected cover certificate | $O(|V|+|E|)$ |
| `independent_set_to_vertex_cover` | preserve YES answers through complement | $O(|V|+|E|)$ materialization |
| `vertex_cover_fpt` | branch on an uncovered edge | $O(2^k poly(|V|+|E|))$ |
| `vertex_cover_2approx` | maximal-matching endpoint cover | $O(|V|+|E|)$ after validation |

Bounds describe the algorithms under the lesson's model. They are not measured
Python timing guarantees.

## Run the tests

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 ../../../.venv/bin/python -m unittest -v
```

Expected result: 14 tests pass and no bytecode cache is created.

## Import the helpers

Run examples from this directory or place the directory on `PYTHONPATH`:

```python
from complexity import subset_sum_dp, verify_subset_sum

values = [3, 5, 9, 12]
witness = subset_sum_dp(values, 17)
assert witness is not None
assert verify_subset_sum(values, 17, witness)
```

For vertex cover:

```python
from complexity import verify_vertex_cover, vertex_cover_2approx

graph = {
    "a": ("b",),
    "b": ("a", "c"),
    "c": ("b",),
}
cover = vertex_cover_2approx(graph)
assert verify_vertex_cover(graph, cover)
```

## Contract boundaries

- `DFA` requires a nonempty state set and exactly one transition for every
  state-symbol pair.
- `CNFGrammar` accepts only nonempty token sequences and productions of the
  forms $A\to a$ and $A\to BC$. Epsilon and unit productions are outside its
  interface.
- `TuringMachine` permits partial transition tables, but `run_bounded` raises an
  error if execution reaches an undefined transition. Formal rejection requires
  the explicit reject state.
- `run_bounded` reports `TIMEOUT` when the step budget expires. It never converts
  that status to rejection.
- Subset-sum values and target are nonnegative integers. Certificates contain
  distinct in-range indices.
- Graph inputs explicitly contain every vertex and use symmetric adjacency.
  Self-loops are permitted and force their endpoint into a cover.
- `vertex_cover_fpt` returns one cover within the budget or `None` after the
  branch search proves none exists.
- `vertex_cover_2approx` guarantees feasibility and factor 2 under the minimum
  vertex-cover contract. It does not return an optimum certificate.

## Evidence boundary

The tests establish selected behavior, refusal cases, and small-domain reference
agreement. They do not prove regular-language separations, undecidability,
NP-completeness, running-time classes, or approximation bounds. The lesson's
formal arguments own those claims.

---

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Resources](../resources/README.md)
