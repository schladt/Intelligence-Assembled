# Code for §0.11 Graph Theory

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

## Purpose

[`graph_tools.py`](graph_tools.py) contains one compact implementation for each
algorithm family emphasized by the lesson:

- validated, multiplicity-aware undirected adjacency;
- BFS and iterative DFS;
- Kahn topological ordering with cycle refusal;
- Kruskal MST with union-find;
- proposer-side deferred acceptance;
- Edmonds-Karp maximum flow with a residual minimum-cut certificate.

## Run

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v
```

No third-party packages, randomness, network access, or data files are needed.

## Contracts and limits

- Vertices must be unique and hashable.
- Traversal and topological tie order follow input order.
- Undirected validation rejects loops and parallel edges unless enabled. A loop
  is stored twice so adjacency length equals degree.
- Kruskal requires a connected underlying graph, permits finite negative and
  tied weights, ignores loops, and permits parallel edges. Ties preserve input
  order and produce one valid MST.
- Stable matching requires equal sides and complete strict rankings. It computes
  the proposer-optimal stable matching, not maximum bipartite matching.
- Edmonds-Karp requires finite nonnegative capacities and distinct source and
  sink. This teaching implementation refuses loops and antiparallel original
  arcs so residual reverse arcs remain unambiguous.

The theorem families can support broader representations. The narrower code
contract keeps each mechanism inspectable.

## Evidence boundary

The 14 tests cover hand-computed results, graph-model refusals, loop degree,
parallel edges, disconnected inputs, tied weights, cyclic DAG input, invalid
preferences, zero flow, capacity errors, and a flow-cut certificate. Passing
tests establish the implementation behavior on those cases. The theorem proofs
in the lesson establish the universal finite claims.

[Back to module](../README.md) | [Exercises](../exercises/README.md)