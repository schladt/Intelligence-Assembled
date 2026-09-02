# Code for §0.14 Algorithms and Data Structures

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Resources](../resources/README.md)

## Purpose

`algorithms.py` contains compact reference implementations that expose the
module's invariants and refusal cases. `test_algorithms.py` checks observable
correctness, mutation boundaries, recovered witnesses, invalid inputs, and
small-domain reference comparisons.

The package uses only the Python 3.14 standard library. It is instructional code,
not a production container or graph library.

## Contents

| Symbol | Teaching purpose | Main bound |
|---|---|---|
| `binary_search_left` | half-open search boundary | $O(\log n)$ comparisons |
| `merge_sort` | stable divide, solve, merge | $\Theta(n\log n)$ time, $\Theta(n)$ auxiliary space |
| `MinHeap` | array-backed parent-child invariant | $O(\log n)$ push and pop |
| `bfs_shortest_paths` | FIFO frontier and parent recovery | $\Theta(|V|+|E|)$ |
| `dijkstra` | nonnegative weighted frontier | $O((|V|+|E|)\log|V|)$ |
| `DisjointSet` | union by size and path compression | $O(m\alpha(n))$ per sequence |
| `sparse_matvec` | visit stored nonzeros only | $\Theta(z)$ |
| `knapsack_01` | recurrence table and witness recovery | $\Theta(nW)$ time and space |
| `interval_schedule` | earliest-finish exchange rule | $O(n\log n)$ |
| `quickselect` | caller-owned random pivot stream | expected $\Theta(n)$, worst $\Theta(n^2)$ |

Bounds assume the representations and cost model stated in the primary lesson.
They are not measured Python timing guarantees.

## Run the tests

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 ../../../.venv/bin/python -m unittest -v
```

Expected result: 17 tests pass and no bytecode cache is created.

## Import the helpers

Run examples from this directory or place the directory on `PYTHONPATH`:

```python
import random

from algorithms import MinHeap, quickselect

heap = MinHeap([5, 2, 7, 1])
assert [heap.pop() for _ in range(len(heap))] == [1, 2, 5, 7]

values = [9, 2, 5, 1, 7]
assert quickselect(values, 2, rng=random.Random(14)) == 5
```

## Contract boundaries

- Binary search assumes the input is already sorted by the same key.
- Search, sort, heap, and selection values must provide a consistent total
  ordering for the comparisons the algorithm performs.
- Graphs must explicitly contain every neighbor as a vertex key.
- Dijkstra rejects negative, infinite, NaN, Boolean, and nonnumeric weights
  before search begins.
- Sparse multiplication treats missing entries as zero and rejects invalid
  columns or nonfinite values.
- Knapsack uses positive integer weights and nonnegative integer capacity. Values
  may be any finite real numbers.
- Intervals are finite, real, half-open boundaries with `start < finish`.
- Quickselect requires a caller-owned `random.Random` instance so stream state is
  explicit.

## Evidence boundary

The tests establish the documented behavior on selected examples, failures, and
small exhaustive references. They do not prove asymptotic bounds. The lesson's
invariants and derivations provide those arguments.

---

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Resources](../resources/README.md)
