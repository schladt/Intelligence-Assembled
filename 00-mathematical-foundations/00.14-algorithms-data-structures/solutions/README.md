# Solutions for §0.14 Algorithms and Data Structures

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

These solutions show one complete route. Different representations or proofs are
valid when their contracts and cost claims are equally explicit.

## E0.14.01 Choose representations from operation traces

### Key idea

The operation trace selects the interface; the interface selects candidate
representations.

### Reasoning

1. Use a FIFO queue backed by a deque. Invariant: stored order matches arrival
   order. Append right and remove left are $O(1)$ under the deque contract. A
   dynamic array with front deletion is rejected because each deletion shifts
   the remaining references and costs $O(n)$.
2. Use a hash table from token to count. Invariant: each stored key appears once
   and maps to its current count. Lookup and update are expected $O(1)$ under a
   controlled load and hashing assumption, with $O(n)$ worst case. A sorted
   array is rejected because frequent insertions or new-token updates can need
   shifts even though lookup is logarithmic.
3. Use a min-priority queue backed by a binary heap. Invariant: every parent
   priority is no greater than either child's. Minimum removal and insertion are
   $O(\log n)$; the minimum is $O(1)$. A sorted list makes minimum access cheap
   but insertion $O(n)$.
4. Use a sparse row representation containing only nonzeros. Invariant: missing
   entries are zero and each stored column is valid. Matrix-vector work is
   $\Theta(z)$ for $z$ stored entries. A dense array is rejected because it owns
   $10^{12}$ positions and scans mostly zeros.
5. Use a balanced ordered search tree. Invariant: in-order traversal is sorted
   and height remains $O(\log n)$. Search, update, predecessor, and successor
   are $O(\log n)$. A hash table is rejected because it does not expose ordered
   neighbors as part of its contract.

### Verification

Each choice follows from a named dominant operation and includes the qualifier
needed by its cost claim.

### Common wrong turn

Do not say "dictionary is fast" or "tree is sorted" without specifying expected
versus worst case, balance, and the operation being analyzed.

## E0.14.02 Prove the dynamic-array append bound

### Key idea

Expensive resizes occur at geometrically separated capacities.

### Reasoning

For the first 10 appends, counting ordinary write plus copied items:

| Append | Capacity after append | Copies | Total append cost |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 2 |
| 3 | 4 | 2 | 3 |
| 4 | 4 | 0 | 1 |
| 5 | 8 | 4 | 5 |
| 6 | 8 | 0 | 1 |
| 7 | 8 | 0 | 1 |
| 8 | 8 | 0 | 1 |
| 9 | 16 | 8 | 9 |
| 10 | 16 | 0 | 1 |

Let $2^r$ be the largest copied capacity before or during the first $m$
appends. Then $2^r<m$ unless $m=1$, and total copies are

$$
1+2+\cdots+2^r=2^{r+1}-1<2m.
$$

Ordinary writes cost exactly $m$, so total cost is less than $3m$. The amortized
charge is therefore below 3 units per append and belongs to $O(1)$.

A valid policy grows at load 1 and shrinks when load falls to at most $1/4$,
perhaps halving capacity while retaining a minimum capacity. After growth the
load is about $1/2$; after shrink it is at most $1/2$. A long gap of updates is
needed before the opposite resize.

### Verification

The first 10 appends cost 25 total units: 10 writes and 15 copies. The bound
$25<3(10)$ holds.

### Common wrong turn

Amortized cost is not the cost of every operation and is not an expectation over
random inputs.

## E0.14.03 Audit hashing contracts and collisions

### Key idea

Correct collision handling is unconditional; expected constant cost is
conditional.

### Reasoning

The chains, in insertion order, are:

```text
0: [0, 8, 16]
1: [1, 9]
2: [2, 10, 18]
3: []
4: []
5: []
6: []
7: []
```

There are 8 keys and 8 buckets, so $\alpha=1$. Lookup of `18` checks `2`, `10`,
and `18`: three equality checks. Unsuccessful lookup of `26` also checks all
three entries because `26 % 8 == 2`.

The key family $0,8,16,\ldots$ can place all $n$ keys in one chain, making lookup
$\Theta(n)$. Expected $O(1+\alpha)$ is defensible only after stating a model such
as simple uniform hashing, controlled load through resizing, and keys or hash
randomness that do not force systematic collisions.

Tests:

1. insert colliding keys, then retrieve and update each distinct key;
2. delete a key from the head, middle, and tail of a collision chain without
   losing the others;
3. cross a resize threshold and verify every preexisting mapping afterward.

### Verification

The bucket counts sum to 8, and every inserted key appears exactly once.

### Common wrong turn

Load factor one does not imply every chain has length one.

## E0.14.04 Repair and test a min-heap

### Key idea

Insertion repairs upward; minimum removal repairs downward.

### Reasoning

The initial array satisfies all parent-child comparisons:

```text
2 <= 7,4
7 <= 9,8
4 <= 6
```

Insert `1`:

```text
[2, 7, 4, 9, 8, 6, 1]  append
[2, 7, 1, 9, 8, 6, 4]  swap with parent 4
[1, 7, 2, 9, 8, 6, 4]  swap with parent 2
```

Remove the minimum and move final `4` to the root:

```text
[4, 7, 2, 9, 8, 6]
[2, 7, 4, 9, 8, 6]     swap with smaller child 2
```

Code check:

```python
from algorithms import MinHeap

heap = MinHeap()
for value in (5, 1, 5):
    heap.push(value)
assert [heap.pop(), heap.pop(), heap.pop()] == [1, 5, 5]
```

A complete binary tree with $n$ nodes has height $\lfloor\log_2 n\rfloor$.
Each repair changes the current index to its parent or one child, so it examines
at most one path and takes $O(\log n)$ time.

`[1, 4, 2, 9, 7, 8]` is a valid min-heap and is not sorted because `4 > 2`.

### Verification

Every final parent-child comparison holds, and repeated pop returns
nondecreasing values.

### Common wrong turn

Swapping downward with the left child without comparing the right child can
leave the smaller right child below a larger parent.

## E0.14.05 Preserve stability through merge sort

### Key idea

A stable merge takes from the left run when keys tie.

### Reasoning

The recursive leaves are the original records. Merging singleton and larger
runs yields final output

```text
[(1, "b"), (1, "d"), (2, "a"), (2, "c"), (2, "e")]
```

Merge invariant:

> Before each iteration, the output is the stable sorted merge of exactly the
> consumed prefixes, and the unconsumed suffixes remain sorted.

If the next keys tie, every left-run record preceded every right-run record in
the original sequence. Taking left first preserves that relation. Taking right
first can reverse `a` and `c`, or `b` and `d`, at the first merge where equal
keys meet across halves.

```python
from algorithms import merge_sort

records = [(2, "a"), (1, "b"), (2, "c"), (1, "d"), (2, "e")]
result = merge_sort(records, key=lambda item: item[0])
assert result == [(1, "b"), (1, "d"), (2, "a"), (2, "c"), (2, "e")]
assert records == [(2, "a"), (1, "b"), (2, "c"), (1, "d"), (2, "e")]
```

There are $\Theta(\log n)$ merge levels and $\Theta(n)$ work per level, giving
$\Theta(n\log n)$ time. The array implementation owns $\Theta(n)$ merged output
space, in addition to recursion metadata.

### Verification

Keys are nondecreasing, labels for key 1 remain `b,d`, labels for key 2 remain
`a,c,e`, and the input is unchanged.

### Common wrong turn

Sorted by key does not imply stable. Stability constrains equal-key records.

## E0.14.06 Prove a duplicate-aware binary search

### Key idea

Maintain a half-open interval and return a boundary, not an arbitrary match.

### Reasoning

Traces for `[1, 3, 3, 3, 7, 9]` are:

```text
target 3:  (0,3,6) -> (0,1,3) -> (0,0,1) -> return 1
target 4:  (0,3,6) -> (4,5,6) -> (4,4,5) -> return 4
target 0:  (0,3,6) -> (0,1,3) -> (0,0,1) -> return 0
target 10: (0,3,6) -> (4,5,6) -> return 6
```

The trace tuple is `(lo, mid, hi)` before the update.

- Initialization: every candidate position lies in `[0,n)`.
- Preservation: when `values[mid] < target`, indices through `mid` are too
  small; otherwise `mid` and everything after it remain possible boundary
  positions.
- Termination: interval length decreases and reaches zero.
- Postcondition: every index below `lo` has value less than target, and every
  index at or above `lo` has value at least target.

Presence is

```python
from algorithms import binary_search_left

values = [1, 3, 3, 3, 7, 9]
target = 3
index = binary_search_left(values, target)
assert index < len(values) and values[index] == target
```

Boundary tests:

```python
from algorithms import binary_search_left

assert binary_search_left([], 4) == 0
assert binary_search_left([4], 4) == 0
assert binary_search_left([4], 5) == 1
assert binary_search_left([3, 3, 3], 3) == 0
assert binary_search_left([3, 3, 3], 2) == 0
assert binary_search_left([1, 3, 7], 4) == 2
assert binary_search_left([1, 3, 7], 8) == 3
```

Array insertion still shifts the suffix, so the complete insertion is $O(n)$.

### Verification

The postcondition can be checked directly for every returned boundary in the
examples.

### Common wrong turn

Using inclusive `hi` with half-open update rules causes skipped candidates or
nontermination.

## E0.14.07 Match graph frontiers to path contracts

### Key idea

The frontier order must match the path objective.

### Reasoning

Ignoring weights, an adjacency order such as

```python
graph = {"s": ["a", "b"], "a": ["g"], "b": ["a", "g"], "g": []}
```

lets BFS recover `s -> a -> g`, distance 2 edges. Dijkstra sees weighted edges
and recovers `s -> b -> a -> g`, total weight $1+2+1=4$, which beats direct
`b -> g` continuation and `s -> a -> g` cost 5.

```python
from algorithms import bfs_shortest_paths, dijkstra, recover_path

unweighted = {"s": ["a", "b"], "a": ["g"], "b": ["a", "g"], "g": []}
distance, parent = bfs_shortest_paths(unweighted, "s")
assert distance["g"] == 2
assert recover_path(parent, "s", "g") == ["s", "a", "g"]

weighted = {
    "s": [("a", 4.0), ("b", 1.0)],
    "a": [("g", 1.0)],
    "b": [("a", 2.0), ("g", 8.0)],
    "g": [],
}
distance, parent = dijkstra(weighted, "s")
assert distance["g"] == 4.0
assert recover_path(parent, "s", "g") == ["s", "b", "a", "g"]
```

Adding `("a", -3.0)` to `g` violates the function's global nonnegative-weight
contract and raises `ValueError`.

With adjacency lists, BFS examines each reachable vertex and outgoing edge once:
$\Theta(|V|+|E|)$. Binary-heap Dijkstra performs heap work for relaxations,
giving $O((|V|+|E|)\log|V|)$. An adjacency matrix scans $|V|$ possible neighbors
per removed vertex, making traversal $\Theta(|V|^2)$ even for a sparse graph.

### Verification

Each returned path begins at `s`, ends at `g`, follows graph edges, and matches
its algorithm's stated objective.

### Common wrong turn

BFS is not a weighted shortest-path algorithm merely because it returns a path
with few edges.

## E0.14.08 Maintain incremental connectivity

### Key idea

The abstract value is a partition; roots are replaceable implementation labels.

### Reasoning

The component partitions are:

```text
{01}{2}{3}{4}{5}{6}{7}
{01}{23}{4}{5}{6}{7}
{01}{23}{45}{6}{7}
{01}{23}{45}{67}
{0123}{45}{67}
{0123}{4567}
{01234567}
```

The parent forest invariant says every parent index is valid and every parent
path terminates at a self-parent root. The size stored at a root equals the
number of elements in that root's component. Path compression can change
internal parent pointers and tree shape, but it cannot change which root is
reached or which pairs are connected.

```python
from algorithms import DisjointSet

sets = DisjointSet(8)
for pair in ((0, 1), (2, 3), (4, 5), (6, 7), (0, 2), (4, 6), (0, 4)):
    assert sets.union(*pair)
roots = {sets.find(item) for item in range(8)}
assert len(roots) == 1
assert not sets.union(0, 7)
```

Union by size at least doubles the component size whenever a node's depth
increases, so depth is at most $\lfloor\log_2 n\rfloor$ without compression.
With both union by size and path compression, a sequence of $m$ operations costs
$O(m\alpha(n))$.

### Verification

Every union reduces component count by one until only one component remains;
the repeated union leaves the partition unchanged.

### Common wrong turn

Do not require a particular representative after union. That is not part of the
abstract connectivity contract.

## E0.14.09 Derive and recover a knapsack solution

### Key idea

The final decision for each state is exclude or legally include the final item.

### Reasoning

Let $D[i,w]$ be maximum value using item indices below $i$ with total weight at
most $w$. Base cases are $D[0,w]=0$ and $D[i,0]=0$.

Rows for capacities 0 through 7 are:

```text
i=0: 0 0 0 0 0 0  0  0
i=1: 0 0 3 3 3 3  3  3
i=2: 0 0 3 4 4 7  7  7
i=3: 0 0 3 4 8 8 11 12
i=4: 0 0 3 4 8 8 11 12
```

Each row depends only on the previous row, so row-major order is valid. At
`D[4,7]`, item 3 is not chosen because the value equals `D[3,7]`. At `D[3,7]`,
item 2 is chosen; remaining capacity is 3. At `D[2,3]`, item 1 is chosen. The
recovered indices are `(1, 2)`, with weight $3+4=7$ and value $4+8=12$.

```python
from algorithms import knapsack_01

value, chosen = knapsack_01([2, 3, 4, 5], [3, 4, 8, 8], 7)
assert value == 12
assert chosen == (1, 2)
```

Exhausting all $2^4$ subsets confirms no legal subset exceeds 12. Time is
$\Theta(nW)$ and table space is $\Theta(nW)$. Since binary capacity $W$ uses
only $\Theta(\log W)$ bits, this is pseudopolynomial. A one-row value table can
reduce space to $\Theta(W)$ by iterating capacity downward, but it discards the
full parent history unless extra reconstruction information is retained.

### Verification

Chosen indices are unique and valid, their total weight is within capacity, and
their total value equals the returned optimum.

### Common wrong turn

Iterating a one-row 0/1 knapsack table upward allows the same item to be reused,
turning the problem into unbounded knapsack.

## E0.14.10 Prove or reject a greedy schedule

### Key idea

Earliest finish is safe for cardinality because it leaves at least as much
remaining time as the first choice of an optimum.

### Reasoning

Treating intervals as half-open makes `start >= previous_end` compatible.
Sorting by finish and applying the rule selects `B=(1,2)`, `C=(2,4)`, and
`F=(5,6)`.

Let $g$ be the compatible interval with earliest finish and let $o$ be the first
interval in an optimal remaining schedule. Since $g$ finishes no later than
$o$, replacing $o$ by $g$ preserves compatibility with every later interval and
preserves schedule cardinality. Therefore some optimum begins with $g$. Remove
intervals conflicting with $g$ and apply the same argument inductively. The
greedy schedule is maximum-cardinality.

Earliest start fails on `(0,100), (1,2), (2,3), (3,4)`: it chooses one interval
instead of three.

With `A` weight 100 and all others weight 1, schedule `A,D,F` has weight 102,
while the cardinality-greedy schedule `B,C,F` has weight 3. The exchange
sentence "replacing $o$ by $g$ preserves the objective" fails: it preserves the
number of intervals but can destroy total weight.

For weighted scheduling, sort by finish, let $p(i)$ be the final interval ending
no later than interval $i$ starts, and define

$$
D[i]=\max\{D[i-1],\ w_i+D[p(i)]\}.
$$

### Verification

```python
from algorithms import interval_schedule

intervals = [(0, 3, "A"), (1, 2, "B"), (2, 4, "C"),
             (3, 5, "D"), (4, 7, "E"), (5, 6, "F")]
assert interval_schedule(intervals) == ((1, 2, "B"), (2, 4, "C"), (5, 6, "F"))
```

### Common wrong turn

A maximal schedule, to which no interval can be added, need not have maximum
cardinality.

## E0.14.11 Measure randomized quickselect honestly

### Key idea

Verify every output deterministically and summarize randomized work as a
distribution.

### Reasoning

One valid instrumented experiment copies the partition loop while incrementing
`work` by the current candidate length:

```python
import random
import statistics


def measured_select(values, rank, rng):
    candidates = list(values)
    work = 0
    while True:
        if len(candidates) == 1:
            return candidates[0], work
        work += len(candidates)
        pivot = candidates[rng.randrange(len(candidates))]
        lower = [value for value in candidates if value < pivot]
        equal = [value for value in candidates if value == pivot]
        higher = [value for value in candidates if value > pivot]
        if rank < len(lower):
            candidates = lower
        elif rank < len(lower) + len(equal):
            return pivot, work
        else:
            rank -= len(lower) + len(equal)
            candidates = higher


for size in (101, 501, 1001):
    observations = []
    for seed in range(30):
        values = list(range(size))
        random.Random(10_000 + seed).shuffle(values)
        result, work = measured_select(values, size // 2, random.Random(20_000 + seed))
        assert result == sorted(values)[size // 2]
        observations.append(work)
    ordered = sorted(observations)
    report = {
        "size": size,
        "median": statistics.median(observations),
        "p90": ordered[(9 * len(ordered) - 1) // 10],
        "maximum": max(observations),
        "median_per_n": statistics.median(observations) / size,
    }
    print(report)
```

Always choosing the smallest pivot while requesting the maximum gives

$$
T(n)=T(n-1)+\Theta(n)=\Theta(n^2).
$$

The finite trials verify selected outputs and describe observed work for the
recorded streams. They do not prove the expected-time theorem, sample every
pivot sequence, or exclude a quadratic run.

### Verification

Every selected result is compared with a trusted sorted reference before its
work count enters the report.

### Common wrong turn

A roughly constant observed `work / n` ratio is evidence from the tested range,
not a proof of expected linear time.

## E0.14.12 Design an evidence-backed algorithm

### Key idea

Repeated queries and updates make cache validity part of the algorithm contract.

### Reasoning

One complete design follows.

**Problem contract.** Vertices are hashable IDs. Each directed edge has finite,
nonnegative travel time. Parallel edges are allowed and each is considered.
Missing source or target is invalid. An unreachable target returns no path and
infinite distance. Equal-distance ties are resolved by stable adjacency order,
which is documented but not semantically important.

**Representation.** Use an adjacency list from each vertex to `(neighbor,
weight)` entries because the graph is sparse. Space is $\Theta(|V|+|E|)$ and
outgoing scans cost $\Theta(\deg^+(v))$. Reject an adjacency matrix because it
owns $\Theta(|V|^2)$ space and makes sparse neighbor scans quadratic overall.

**Algorithm.** Run Dijkstra from a source with a binary min-heap of tentative
`(distance, sequence, vertex)` entries, stale-entry skipping, a distance map,
and parent pointers. The sequence field makes heap ties deterministic without
requiring vertex ordering.

**Correctness.** The path-relaxation invariant says each finite tentative
value is the length of a discovered source path. The settled-set invariant says
every removed nonstale minimum has its true shortest distance. Nonnegative
weights make an unsettled detour unable to lower that minimum. Parent pointers
record the final improving edge and recover a legal path.

**Cost.** One source run costs
$O((|V|+|E|)\log|V|)$ with $O(|V|+|E|)$ graph storage and $O(|V|+|E|)$
worst-case frontier entries under duplicate pushes. Without caching, $q$ queries
multiply the run cost by $q$.

**Cache.** Cache complete distance and parent maps by source when sources repeat.
Any edge insertion, deletion, or weight change invalidates all cached
single-source results in the conservative design. More selective dynamic
shortest-path maintenance is outside the contract.

**Tests.** Include a single vertex; unreachable target; two equal paths; parallel
edges; zero-weight edge; negative, infinite, or NaN weight rejection; sparse
chain; dense adversarial graph; repeated source cache hit; and update
invalidation followed by changed result.

**Experiment.** Record graph generator or dataset provenance, graph checksum,
$|V|$, $|E|$, weight range, query distribution, update frequency, cache state,
Python and package versions, hardware, warmup, repeats, wall-clock observations,
heap pushes, relaxations, and limitations. Report preprocessing and update costs
separately.

**Invalidating change.** Allowing negative edges invalidates Dijkstra's settled-
minimum proof. A Bellman-Ford-family algorithm or a stronger graph restriction
would be required.

### Verification

The design states every requested ledger, uses all controlling size variables,
and names cache invalidation as a correctness obligation rather than a
performance detail.

### Common wrong turn

Caching by source without invalidating after edge updates returns plausible but
stale paths.

---

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)
