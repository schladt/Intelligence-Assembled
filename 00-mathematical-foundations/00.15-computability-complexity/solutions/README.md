# Worked solutions for §0.15 Computability and Complexity

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

These are representative solutions. Equivalent encodings, machines, and proofs
are valid when they preserve the stated contracts.

## E0.15.01 Specify languages and computational tasks

1. Encode a Boolean formula in a fixed grammar. Its bit length is the serialized
   formula length. SAT decision asks whether the encoding belongs to the set of
   satisfiable formulas.
2. Returning an assignment is search. A corresponding decision language is SAT.
3. Returning a minimum tour is optimization. With binary-encoded edge costs and
   bound $B$, TSP decision asks whether a tour of cost at most $B$ exists. Input
   length includes graph, costs, and $\log B$.
4. Returning the number of proper 3-colorings is counting. The paired decision
   question asks whether at least one proper 3-coloring exists.
5. This is recognition of programs whose execution eventually prints `done`.
   Simulation accepts members but may run forever on nonmembers.

A class such as NP contains decision languages. A related search, optimization,
or counting interface needs its own reduction and resource claim.

## E0.15.02 Trace and minimize finite-state memory

Use states $q_0,q_1,q_2$, where $q_r$ means the number of `1` symbols seen is
$r\pmod3$. Reading `0` preserves the state; reading `1` advances cyclically.
Start and accept in $q_0$.

For `101101`, the state trace is

```text
q0, q1, q1, q2, q0, q0, q1
```

so the string is rejected. A direct exhaustive check is:

```python
from itertools import product
from complexity import DFA

states = frozenset({0, 1, 2})
machine = DFA(
    states=states,
    alphabet=frozenset({"0", "1"}),
    transition={(q, bit): (q + (bit == "1")) % 3 for q in states for bit in "01"},
    start=0,
    accepting=frozenset({0}),
)
for length in range(7):
    for symbols in product("01", repeat=length):
        word = "".join(symbols)
        assert machine.accepts(word) == (word.count("1") % 3 == 0)
```

Prefixes with 0, 1, and 2 ones are pairwise distinguishable. Appending respectively
0, 2, or 1 ones can make exactly one residue class accepting. Therefore no two
can share a DFA state, so at least three states are necessary. Longer input adds
transitions, not states.

## E0.15.03 Parse a context-free language with CYK

Derivations include $S\Rightarrow AB\Rightarrow ab$ and

$$
S\Rightarrow AC\Rightarrow ASB\Rightarrow AABB\Rightarrow aabb.
$$

For `aaabbb`, length-one cells are `{A}`, `{A}`, `{A}`, `{B}`, `{B}`, `{B}`.
Nonempty longer cells are:

- length 2 at start 2 contains `{S}` for `ab`; all other length-2 cells are
  empty;
- length 3 at start 2 contains `{C}` for `abb`;
- length 4 at start 1 contains `{S}` for `aabb`;
- length 5 at start 1 contains `{C}` for `aabbb`;
- length 6 at start 0 contains `{S}` for `aaabbb`.

Each `C` cell follows from `C -> SB`; each larger `S` cell follows from
`S -> AC`. Those cells expose exactly the dependencies that build the final
parse.

The invariant is: $A\in D[i,\ell]$ exactly when variable $A$ derives the token
substring beginning at $i$ of length $\ell$. The code accepts `ab`, `aabb`, and
`aaabbb`, rejects `abb`, and rejects empty input. There are $O(n^2)$ cells and
$O(n)$ splits per cell. Rule lookup adds a fixed-grammar constant or an explicit
factor depending on representation. The implementation has no epsilon-rule
contract, so empty input is always rejected.

## E0.15.04 Separate acceptance rejection and timeout

For `101`, the scanner successively reads `1`, `0`, `1`, and blank. Its states
record the latest input symbol. At the blank after the third input symbol, the
`seen1` state transitions to accept. Bounds 0 and 3 report timeout; bound 4
reports accept. `110` reaches `seen0` before blank, then reject on the fourth
transition.

A partial machine with start state `q`, input symbol `0`, and no transition for
`(q,0)` violates the reached-configuration contract. The simulator raises an
error because no formal state transition says reject.

One million unfinished steps establish only a finite prefix of execution. A
decider has a proof that every input reaches accept or reject; a bounded simulator
has a third outcome and supplies no general nonhalting proof.

## E0.15.05 Reconstruct the halting diagonal argument

Assume total correct $H(M,w)$. Define $D(x)$ to loop when $H(x,x)$ says that
$x(x)$ halts, and halt when $H(x,x)$ says it does not.

On $D(D)$:

- if $H(D,D)$ says halts, $D(D)$ loops;
- if $H(D,D)$ says does not halt, $D(D)$ halts.

Both contradict correctness, while totality ensures $H(D,D)$ returns one of the
two answers. Therefore a total correct $H$ cannot exist.

Universal simulation recognizes $HALT$: simulate $M(w)$ and accept when it
halts. Suppose the complement were also recognizable. Dovetail the two
recognizers one step at a time. One must eventually accept, giving a total YES or
NO procedure for $HALT$, a contradiction. This is an impossibility for every
total algorithm, not a lower bound on a particularly slow one.

## E0.15.06 Point reductions in the useful direction

Given input $x$ for $A$, compute $f(x)$ and run the decider for $B$. Because $f$
is total and answer-preserving, the composite halts and decides $A$. Thus, if
$A$ is undecidable and $A\le_m B$, then $B$ cannot be decidable.

To prove $B$ undecidable from known-undecidable $A$, use $A\le_m B$. A reduction
$B\le_m HALT$ merely makes a hypothetical HALT decider useful for $B$. Since no
such decider exists, that implication gives no contradiction and proves no
hardness.

For composition, use $h(x)=g(f(x))$. If $f$ runs in polynomial time, its output
length is polynomially bounded because a machine cannot write more symbols than
its running time. The polynomial running time of $g$ in that polynomial length
remains polynomial in $|x|$. Solver reuse reads the arrow backward from a solver
for the target; hardness transfers forward from source to target.

## E0.15.07 Classify P NP hardness and completeness

1. True. A deterministic polynomial decider is a verifier that ignores its
   certificate.
2. False. NP means nondeterministic polynomial time, equivalently polynomial
   certificate verification.
3. False. NP-hard functions and undecidable languages can lie outside NP.
4. True. Every NP language reduces to the NP-complete language and can use its
   polynomial solver.
5. Unknown without qualification. It is false if $P=NP$ and is believed true
   only conditionally on $P\ne NP$.
6. True. Certificates are an assignment, subset indices, one color per vertex,
   and a tour permutation. Formula evaluation, summation, edge checks, and tour
   checks are polynomial in encoded input plus certificate length.
7. True. Optimization output is not itself a decision language, though an
   associated decision version may be NP-complete.
8. False as a known implication. That implication for all NP languages would
   establish $P=NP$.

## E0.15.08 Compose a canonical hardness argument

Define `INDEPENDENT-SET` as encodings $(G,k)$ for which $G$ has at least $k$
pairwise nonadjacent vertices. Define `VERTEX-COVER` as encodings $(G,b)$ for
which at most $b$ vertices touch every edge.

Map $(G,k)$ to $(G,|V|-k)$. If $S$ is independent, no edge has both endpoints in
$S$, so every edge has an endpoint in $V\setminus S$. The complement is a cover
of size at most $|V|-k$. Conversely, if $C$ is a cover of size at most $|V|-k$,
then $V\setminus C$ has size at least $k$ and cannot contain both endpoints of an
edge, so it is independent.

Counting vertices and rewriting the bound takes polynomial time and output size.
A vertex-cover certificate lists at most $b$ vertices; verify membership and scan
every edge. Thus vertex cover is in NP. The reduction from NP-complete independent
set establishes NP-hardness, and the verifier establishes membership, so vertex
cover is NP-complete.

For the test graph, independent set `{a, d, isolated}` maps to complementary
cover `{b, c}` with budget 2. Reversing the reduction would not transfer the
assumed hardness to vertex cover.

## E0.15.09 Diagnose pseudopolynomial subset sum

Reachable sums at most 17 are:

```text
start: {0}
after 3: {0, 3}
after 5: {0, 3, 5, 8}
after 9: {0, 3, 5, 8, 9, 12, 14, 17}
after 12: {0, 3, 5, 8, 9, 12, 14, 15, 17}
```

One witness is indices `(1, 3)`, values 5 and 12. There are $n$ rounds and at most
$T+1$ retained sums, giving $O(nT)$ time and $O(T)$ state, apart from witness
storage.

Targets $2^{10}$ and $2^{40}$ differ by a factor of $2^{30}$ in table width but
need about 11 and 41 binary bits. Thus the bound is exponential in the target's
bit length in the worst case. Target zero has empty witness. Duplicate values
remain distinct by index. An unreachable target returns `None`; repeated or
out-of-range certificate indices fail verification. Fast verification and hard
search are exactly the distinction encoded by NP.

## E0.15.10 Prove a vertex-cover approximation guarantee

After selecting edge $e$, the algorithm removes every edge incident to either
endpoint. No later selected edge shares an endpoint with $e$, so selected edges
form a matching $M$. Any cover must contain at least one endpoint from every
edge in $M$. Since matching edges are disjoint, $OPT\ge|M|$. The algorithm chooses
at most two vertices per matching edge, so

$$
|C|\le2|M|\le2OPT.
$$

All returned candidates should still be checked with `verify_vertex_cover`.
Exact search on the small requested graphs supplies optima for ratios. A path of
three vertices can expose ratio 2 if the first selected edge has the center and
one leaf: the algorithm returns two vertices while the center alone is optimum.
Observed ratios below 2 describe the sample and edge order; the proof's universal
upper bound remains 2.

## E0.15.11 Amplify randomized decision procedures

A YES instance is missed in every independent run with probability at most
$(1/2)^r=2^{-r}$. We need

$$
r\ge\lceil\log_2 10^6\rceil=20.
$$

Independence permits multiplying failure probabilities. Correlated repeated
runs may repeat the same mistake. For coRP, repeat and reject if any run rejects.

For BPP, "accept if any" causes false accepts to accumulate on NO instances.
Use an odd number of independent runs and majority vote, then apply a
concentration bound. A seeded simulation should record seed, runs per experiment,
experiment count, and empirical failure intervals. It can test code and illustrate
the bound, but cannot prove independence, the per-run premise, or complexity-class
membership. Randomized quicksort keeps a deterministic answer and random cost;
RP and BPP allow answer error under explicit bounds.

## E0.15.12 Design a hardness response for AI

A sound memo can use this contract table:

| Method | Scope | Guarantee | Failure status | Structural lever |
|---|---|---|---|---|
| branch-and-bound or integer programming | finite encoded instances | exact if completed | timeout with incumbent and lower bound | good bounds, sparse conflicts |
| dynamic programming | bounded horizon or treewidth | exact within stated model | resource exhaustion, not infeasible | horizon, treewidth |
| parameterized branching | parameter $k$ | exact in $f(k)n^c$ | timeout, unless search exhausts | exceptions or plan length |
| relaxation plus rounding | promised cost structure | stated bound only if proved | feasible candidate or no candidate | metric or convex structure |
| heuristic search | measured distribution | no universal quality claim | timeout with best verified incumbent | learned ordering |

Encode states, transitions, costs, constraints, and $B$ explicitly. Decision asks
for existence under $B$; search returns one plan; optimization minimizes cost.
A verifier checks start, every transition, constraints, goal, and summed cost.
Under $P\ne NP$, NP-completeness rules out a general polynomial-time exact
decider, not efficient special cases or typical performance.

Useful parameters include plan length, treewidth of the interaction graph, number
of violated soft constraints allowed, branching factor, and number of exceptional
operators. Benchmarks should cross total size with parameter values and distinct
instance distributions. Report solved fraction, verified plan quality, lower
bounds, runtime distributions, and seeds. Timeout means unknown unless a complete
proof bound has established infeasibility. The evidence cannot establish a
universal polynomial bound or approximation ratio from benchmarks alone.

Hardness guides modular architecture: always verify incumbents, preserve unknown
as a status, expose parameters, combine exact and heuristic methods, and record
which guarantee each path owns. It does not make useful computation impossible.

---

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)
