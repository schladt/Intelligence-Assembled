# Resources for §0.14 Algorithms and Data Structures

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)

These resources deepen the module without replacing its main learning path.
Every source below was directly inspected for the stated support on 2026-09-01.

## Core route

### MIT 6.006 Introduction to Algorithms

- **Use for:** a coherent undergraduate sequence and the contract for a complete
  algorithmic answer.
- **Directly inspected:** syllabus, prerequisites, course description, coding
  and theory expectations, and the calendar sequence covering cost models,
  sorting, heaps, trees, hashing, BFS, DFS, shortest paths, Dijkstra,
  Bellman-Ford, dynamic programming, reconstruction, and complexity.
- **Why it helps:** the syllabus explicitly requires description, example,
  correctness argument, and time and space analysis rather than code alone.
- **Boundary:** this module synthesizes the sequence and does not reproduce MIT
  problem sets or solutions.
- **License:** MIT OpenCourseWare CC BY-NC-SA 4.0.
- **Link:** https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/

### Open Data Structures

- **Use for:** representation invariants and proved operation costs.
- **Directly inspected:** contents plus chapters on array-based lists, linked
  lists, hash tables, binary trees, heaps, sorting algorithms, and graph
  representations.
- **Why it helps:** each interface is tied to a concrete representation and
  analysis. The array-list chapter explicitly separates expensive resize events
  from $O(1)$ amortized sequence cost.
- **Boundary:** the site offers several language editions; the pseudocode edition
  was used for language-independent reasoning. The module's Python code is
  original.
- **License:** CC BY 2.5 Canada for the book and accompanying source code.
- **Links:** https://opendatastructures.org/ and
  https://opendatastructures.org/ods-python/

## Algorithm-design route

### Jeff Erickson, Algorithms

- **Use for:** recursive design, dynamic programming, greedy exchange arguments,
  graph algorithms, and shortest paths.
- **Directly inspected:** book index and the dynamic-programming and greedy
  chapters, including subproblem design, evaluation order, interval scheduling,
  and the exchange-proof pattern.
- **Why it helps:** the text treats proof structure as part of algorithm design
  and repeatedly distinguishes a plausible heuristic from a proved algorithm.
- **Boundary:** the book assumes prior exposure to basic data structures. Use
  Open Data Structures or this module first when the containers are unfamiliar.
- **License:** the textbook is CC BY 4.0. Additional lecture notes on the same
  page can use CC BY-NC-SA 4.0, so check the specific artifact before reuse.
- **Link:** https://jeffe.cs.illinois.edu/teaching/algorithms/

### Algorithms, 4th Edition booksite

- **Use for:** focused visual and implementation references for sorting,
  priority queues, symbol tables, graphs, and analysis.
- **Directly inspected:** the home page and topic indexes for fundamentals,
  sorting, searching, graphs, and context.
- **Why it helps:** the site connects textbook topics to code, exercises,
  visualizations, and datasets.
- **Boundary:** it is a companion site to a commercial textbook. Link to it;
  do not assume its text or code has an open-content license.
- **Link:** https://algs4.cs.princeton.edu/home/

## Python mapping route

### collections.deque

- **Directly inspected:** end append and pop operations, bounded deques,
  rotation, indexing behavior, and recipes.
- **Use for:** mapping the abstract deque interface to Python while retaining the
  distinction between end operations and middle access.
- **License:** PSF License Version 2; documentation code examples additionally
  fall under the Python documentation terms.
- **Link:** https://docs.python.org/3.14/library/collections.html#collections.deque

### heapq

- **Directly inspected:** zero-based min-heap invariant, child indexes,
  `heappush`, `heappop`, combined operations, merge, and extreme-value helpers.
- **Use for:** comparing the module's explicit `MinHeap` repair operations with
  a trusted standard-library implementation.
- **Boundary:** `heapq` operates on lists and does not wrap them in an ownership-
  enforcing priority-queue class.
- **License:** PSF License Version 2.
- **Link:** https://docs.python.org/3.14/library/heapq.html

### bisect

- **Directly inspected:** left and right boundaries, `key`, insertion helpers,
  performance notes, and thread-safety warning.
- **Use for:** reinforcing that logarithmic boundary search is followed by
  linear insertion when the representation is a Python list.
- **License:** PSF License Version 2.
- **Link:** https://docs.python.org/3.14/library/bisect.html

## Suggested sequence

1. Read the primary module through the operation table and amortized-array
   derivation.
2. Use Open Data Structures to inspect one array structure, one hash table, one
   heap, and both graph representations.
3. Implement and test the module code before replacing any mechanism with a
   library call.
4. Read Erickson's dynamic-programming and greedy chapters while completing
   E0.14.09 and E0.14.10.
5. Compare the teaching implementations with `deque`, `heapq`, and `bisect`.
6. Use the Princeton booksite for additional drills and visualizations, while
   respecting its reuse boundary.

## Provenance and originality ledger

| Source | Accessed | Exact support used | Inspection limit | Reuse boundary |
|---|---|---|---|---|
| MIT 6.006 OCW | 2026-09-01 | course scope, topic order, complete-answer contract | Fall 2011 public materials | summarized; no problem-set reuse |
| Morin, Open Data Structures | 2026-09-01 | interfaces, representations, amortization, hashing, heaps, graphs | public pseudocode HTML | CC BY 2.5 CA; module prose and code are original |
| Erickson, Algorithms | 2026-09-01 | DP workflow, interval scheduling, exchange arguments | public book chapters | textbook CC BY 4.0; no exercise copying |
| Sedgewick and Wayne booksite | 2026-09-01 | topic organization and supporting-material scope | public booksite pages | linked and summarized only |
| Python `collections` | 2026-09-01 | deque contracts and operation boundaries | Python 3.14 docs | PSF terms |
| Python `heapq` | 2026-09-01 | min-heap invariant and API semantics | Python 3.14 docs | PSF terms |
| Python `bisect` | 2026-09-01 | insertion boundaries and performance warning | Python 3.14 docs | PSF terms |

All lesson prose, exercises, worked solutions, diagrams, SVG figures, and module
code are original to this repository. Source material supports definitions,
contracts, and standard results; it is not copied into the teaching package.

---

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)
