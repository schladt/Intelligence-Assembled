# Exercises for §0.14 Algorithms and Data Structures

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening its solution. State contracts and cost-model
assumptions with every algorithm. Code exercises use the module's standard-library
implementation package unless the problem says otherwise.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.14.01 | Choose representations from operation traces | critique and applied | 2 | 1, 2 | 30-45 min |
| E0.14.02 | Prove the dynamic-array append bound | derivation and proof | 3 | 3, 4 | 35-50 min |
| E0.14.03 | Audit hashing contracts and collisions | calculation and critique | 3 | 2, 3 | 35-50 min |
| E0.14.04 | Repair and test a min-heap | implementation and proof | 3 | 2, 4, 5 | 45-70 min |
| E0.14.05 | Preserve stability through merge sort | derivation and implementation | 3 | 4, 5 | 40-60 min |
| E0.14.06 | Prove a duplicate-aware binary search | proof and implementation | 3 | 4, 5 | 40-60 min |
| E0.14.07 | Match graph frontiers to path contracts | applied and implementation | 4 | 1, 2, 5 | 50-75 min |
| E0.14.08 | Maintain incremental connectivity | proof and implementation | 3 | 2, 4, 5 | 40-60 min |
| E0.14.09 | Derive and recover a knapsack solution | derivation and implementation | 4 | 4, 6 | 60-90 min |
| E0.14.10 | Prove or reject a greedy schedule | proof and critique | 4 | 4, 7 | 45-70 min |
| E0.14.11 | Measure randomized quickselect honestly | experiment and critique | 4 | 3, 8 | 60-90 min |
| E0.14.12 | Design an evidence-backed algorithm | applied synthesis | 5 | 1-8 | 90-150 min |

## E0.14.01 Choose representations from operation traces

- **Type:** critique and applied
- **Difficulty:** 2
- **Objective:** 1, 2
- **Estimated time:** 30-45 minutes

### Problem

For each workload, choose a primary representation and justify the choice from
its dominant operations. State one rejected alternative and the cost that makes
it worse under the stated trace.

1. Process tasks in arrival order, appending at one end and removing at the
   other, with no middle access.
2. Maintain one million `(token, count)` pairs with frequent exact-token lookup
   and no sorted-range query.
3. Repeatedly remove the smallest tentative distance and insert revised
   candidates.
4. Store a $10^6\times10^6$ matrix with about eight nonzeros per row and perform
   matrix-vector products.
5. Keep values ordered while frequently asking for predecessor and successor.

For each answer, write the representation invariant and expected or worst-case
qualifier that the cost claim requires.

### Hint

Start from queue, dictionary, priority-queue, sparse-row, and ordered-set
interfaces. Do not begin with Python class names.

## E0.14.02 Prove the dynamic-array append bound

- **Type:** derivation and proof
- **Difficulty:** 3
- **Objective:** 3, 4
- **Estimated time:** 35-50 minutes

### Problem

A dynamic array starts with capacity 1. Appending to a full array allocates twice
the old capacity and copies every live item. Count one unit for each ordinary
write and one unit for each copied item.

1. List the capacity and cost of each of the first 10 appends.
2. For arbitrary $m\ge1$, prove that total copy cost is less than $2m$.
3. Derive a constant upper bound on amortized append cost.
4. Explain why this result neither says every append is $O(1)$ worst case nor
   uses an average input distribution.
5. Give a grow-and-shrink policy that avoids immediate resize thrashing.

### Hint

Resize capacities form a geometric sequence. For shrinking, leave a gap between
the grow and shrink thresholds.

## E0.14.03 Audit hashing contracts and collisions

- **Type:** calculation and critique
- **Difficulty:** 3
- **Objective:** 2, 3
- **Estimated time:** 35-50 minutes

### Problem

A separate-chaining table has $m=8$ buckets and uses $h(k)=k\bmod8$. Insert keys
`0, 8, 16, 1, 9, 2, 10, 18`.

1. Draw the resulting chains and compute load factor $\alpha$.
2. Count equality checks for successful lookup of `18` and unsuccessful lookup
   of `26`, assuming insertion appends to each chain.
3. Explain why this deterministic family refutes an unconditional worst-case
   $O(1)$ lookup claim.
4. State assumptions under which expected $O(1+\alpha)$ lookup is defensible.
5. Propose two tests for collision handling and one test for resize behavior.

### Hint

`26 % 8` is not an empty bucket. Separate correctness from the distributional
assumption used for expected cost.

## E0.14.04 Repair and test a min-heap

- **Type:** implementation and proof
- **Difficulty:** 3
- **Objective:** 2, 4, 5
- **Estimated time:** 45-70 minutes

### Problem

Start with array `[2, 7, 4, 9, 8, 6]`.

1. Verify the zero-based min-heap invariant at every nonroot index.
2. Insert `1` by appending it and tracing every upward swap.
3. Remove the minimum by moving the final item to the root and tracing every
   downward swap.
4. Repeat the operations with `MinHeap` from the module code and assert the
   exact popped sequence after inserting `5`, `1`, and `5` into an empty heap.
5. Prove that upward and downward repair each inspect at most one root-to-leaf
   path and therefore take $O(\log n)$ time.
6. Give a heap array that is valid but not globally sorted.

### Hint

Children of index $i$ are $2i+1$ and $2i+2$. The smaller child is the only legal
candidate for a downward swap in a min-heap.

## E0.14.05 Preserve stability through merge sort

- **Type:** derivation and implementation
- **Difficulty:** 3
- **Objective:** 4, 5
- **Estimated time:** 40-60 minutes

### Problem

Sort records

```text
[(2, "a"), (1, "b"), (2, "c"), (1, "d"), (2, "e")]
```

by the integer key.

1. Trace the recursive split and merge performed by `merge_sort`.
2. State the merge-loop invariant.
3. Explain why choosing the left item when keys tie preserves stability.
4. Change that tie rule conceptually to choose the right item and give the first
   pair whose original order can reverse.
5. Verify with code that output keys are sorted, input is unchanged, and equal
   keys preserve label order.
6. Derive $\Theta(n\log n)$ time and $\Theta(n)$ auxiliary-space bounds for the
   array implementation.

### Hint

At each merge step, the output prefix must be the stable sorted merge of the
consumed prefixes.

## E0.14.06 Prove a duplicate-aware binary search

- **Type:** proof and implementation
- **Difficulty:** 3
- **Objective:** 4, 5
- **Estimated time:** 40-60 minutes

### Problem

For `values = [1, 3, 3, 3, 7, 9]`, use `binary_search_left`.

1. Trace `(lo, mid, hi)` while searching for `3`, `4`, `0`, and `10`.
2. State initialization, preservation, termination, and postcondition for the
   half-open interval invariant.
3. Prove the return value is the first index whose value is not less than the
   target.
4. Explain how the caller distinguishes presence from insertion position.
5. Test empty, singleton, all-equal, absent-below, absent-between, and
   absent-above cases.
6. Explain why inserting at the returned index in an array remains $O(n)$.

### Hint

The postcondition is stronger and more useful than "find any equal item."

## E0.14.07 Match graph frontiers to path contracts

- **Type:** applied and implementation
- **Difficulty:** 4
- **Objective:** 1, 2, 5
- **Estimated time:** 50-75 minutes

### Problem

Consider this directed graph:

```text
s -> a (4), s -> b (1), b -> a (2), a -> g (1), b -> g (8)
```

1. Ignore weights and use `bfs_shortest_paths` to recover a path from `s` to
   `g`. State what its distance means.
2. Use `dijkstra` with the weights and recover a minimum-weight path. State what
   its distance means.
3. Explain why the paths can differ without either algorithm being wrong.
4. Add edge `g -> a (-3)` and show that the implementation rejects the graph
   before making a shortest-path claim.
5. Derive the adjacency-list bounds for both algorithms.
6. Give a graph representation under which scanning every possible neighbor
   would change the traversal bound.

### Hint

BFS minimizes edge count. Dijkstra minimizes summed nonnegative weight.

## E0.14.08 Maintain incremental connectivity

- **Type:** proof and implementation
- **Difficulty:** 3
- **Objective:** 2, 4, 5
- **Estimated time:** 40-60 minutes

### Problem

Create `DisjointSet(8)` and apply unions

```text
(0,1), (2,3), (4,5), (6,7), (0,2), (4,6), (0,4)
```

1. Record the components after each union without relying on representative
   numbers as semantic labels.
2. State the parent-forest and size invariants.
3. Trigger `find` on every element and explain what path compression may change
   and what it cannot change.
4. Assert that all elements are connected and that repeating `union(0,7)`
   reports no merge.
5. Explain why union by size alone gives logarithmic tree height.
6. State the qualified sequence bound when path compression is added.

### Hint

Representatives are implementation artifacts. The partition is the abstract
value.

## E0.14.09 Derive and recover a knapsack solution

- **Type:** derivation and implementation
- **Difficulty:** 4
- **Objective:** 4, 6
- **Estimated time:** 60-90 minutes

### Problem

Items have weights `[2, 3, 4, 5]`, values `[3, 4, 8, 8]`, and capacity `7`.

1. Define $D[i,w]$ precisely and write base cases.
2. Fill the complete value table for $0\le i\le4$ and $0\le w\le7$.
3. State why every recurrence dependency is available in row-major order.
4. Recover one optimal item set and verify its weight and value.
5. Compare the result with exhaustive subset enumeration.
6. Explain why $\Theta(nW)$ is pseudopolynomial rather than polynomial in the
   binary input length.
7. Give one state-compression optimization and explain what reconstruction data
   it risks losing.

### Hint

At state $(i,w)$, the final decision is either to exclude item $i-1$ or include
it when legal.

## E0.14.10 Prove or reject a greedy schedule

- **Type:** proof and critique
- **Difficulty:** 4
- **Objective:** 4, 7
- **Estimated time:** 45-70 minutes

### Problem

Intervals are half-open:

```text
A=(0,3), B=(1,2), C=(2,4), D=(3,5), E=(4,7), F=(5,6)
```

1. Run `interval_schedule` and state the compatibility boundary.
2. Prove earliest-finish selection is maximum-cardinality using an exchange
   argument and induction.
3. Show that earliest-start can fail using a separate counterexample.
4. Assign weights `A=100` and every other interval weight `1`. Explain why the
   cardinality proof does not establish maximum total weight.
5. Propose a dynamic-programming state for weighted interval scheduling.
6. Identify the exact sentence in your exchange proof that fails for the
   weighted objective.

### Hint

The exchange preserves the number of scheduled intervals, not arbitrary total
weight.

## E0.14.11 Measure randomized quickselect honestly

- **Type:** experiment and critique
- **Difficulty:** 4
- **Objective:** 3, 8
- **Estimated time:** 60-90 minutes

### Problem

Use `quickselect` to select the median of shuffled ranges of sizes 101, 501, and
1001.

1. Spawn at least 30 independent `random.Random` instances from recorded seeds
   per size.
2. Instrument or wrap the implementation to record the total number of elements
   partitioned in each run.
3. Report median, 90th percentile, maximum, and normalized work divided by $n$.
4. Verify every result against `sorted(values)[k]`.
5. Construct a deterministic extreme-pivot recurrence and derive its
   $\Theta(n^2)$ cost.
6. Explain why the experiment proves neither expected linear time nor absence of
   quadratic runs.

### Hint

Correctness is checked per run. The expected-time theorem is a separate
mathematical claim about the random pivot distribution.

## E0.14.12 Design an evidence-backed algorithm

- **Type:** applied synthesis
- **Difficulty:** 5
- **Objective:** 1-8
- **Estimated time:** 90-150 minutes

### Problem

Design a route planner for a directed network with nonnegative travel times.
The planner receives repeated source-target queries, the graph is sparse, and
occasional edge-weight updates occur between queries.

Deliver:

1. a problem contract covering vertices, edge direction, weight domain,
   unreachable targets, and tie behavior;
2. a representation ledger and comparison with one rejected representation;
3. an algorithm and frontier choice;
4. correctness invariants and a proof outline;
5. time and auxiliary-space analysis using $|V|$, $|E|$, and query count $q$;
6. a cache or preprocessing proposal, including invalidation after updates;
7. at least six tests covering normal, boundary, invalid, and adversarial cases;
8. an experiment plan that records environment and graph provenance without
   claiming benchmark results are universal;
9. one plausible change in requirements that would invalidate the chosen
   algorithm.

### Hint

A good answer may use Dijkstra per source and cache results, but the update
contract determines whether cached trees remain valid.

---

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)
