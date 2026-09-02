# Exercises for §0.11 Graph Theory

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Difficulty follows the
project's 1 through 5 scale. All programming uses the Python standard library.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.11.01 | Declare a graph model and audit degree | conceptual and proof | 2 | distinguish simple, directed, and multigraph contracts | 40 min |
| E0.11.02 | Traverse components with BFS and DFS | calculation and implementation | 3 | connect traversal invariants to reachability | 50 min |
| E0.11.03 | Prove equivalent tree contracts | proof and critique | 4 | use connectedness, acyclicity, and edge count correctly | 55 min |
| E0.11.04 | Build an MST and audit ties | derivation and implementation | 4 | apply the cut property and Kruskal contract | 60 min |
| E0.11.05 | Quantify Hall's condition | proof and calculation | 4 | test every subset and distinguish matching sizes | 55 min |
| E0.11.06 | Separate stable and maximum matching | calculation and critique | 4 | trace deferred acceptance and audit blocking pairs | 60 min |
| E0.11.07 | Certify a chromatic number | proof and application | 3 | pair coloring upper bounds with structural lower bounds | 45 min |
| E0.11.08 | Separate Euler and Hamilton coverage | proof and critique | 4 | distinguish edge and vertex tours under assumptions | 55 min |
| E0.11.09 | Adjust Euler's planar formula | derivation and proof | 4 | handle faces and disconnected components | 55 min |
| E0.11.10 | Order a computation DAG | proof and implementation | 4 | prove and use DAG iff topological order | 60 min |
| E0.11.11 | Translate graph matrix views | calculation and derivation | 4 | derive incidence and Laplacian identities | 65 min |
| E0.11.12 | Certify max flow with a minimum cut | derivation and implementation | 5 | integrate capacity, conservation, residual reachability, and evidence | 90 min |

## E0.11.01 Declare a graph model and audit degree

- **Type:** conceptual and proof
- **Difficulty:** 2
- **Objective:** Distinguish simple, directed, and multigraph contracts.
- **Estimated time:** 40 minutes
- **Allowed tools:** Definitions and hand calculation.
- **Assumptions:** Every graph is finite. State any additional convention.

### Problem

Let $V=\{a,b,c\}$. Consider edge instances $e_1=ab$, $e_2=ab$,
$e_3=bc$, and $e_4=cc$.

1. Explain why these data do not define a simple undirected graph.
2. Treat them as an undirected multigraph. Compute every degree, counting a loop
   twice, and verify the handshake identity.
3. Orient the instances as $a\to b$, $b\to a$, $b\to c$, $c\to c$.
   Compute indegree and outdegree and verify both directed sums.
4. State what information is lost if an adjacency **set** is used for the
   multigraph.
5. State a representation that preserves edge-instance identity.
6. Use `undirected_adjacency` to encode the multigraph and explain why the loop
   appears twice.

**Deliverable:** A model contract, two degree ledgers, both handshake audits,
and a representation diagnosis.

## E0.11.02 Traverse components with BFS and DFS

- **Type:** calculation and implementation
- **Difficulty:** 3
- **Objective:** Connect traversal invariants to reachability.
- **Estimated time:** 50 minutes
- **Allowed tools:** Hand tracing and module code.
- **Assumptions:** Neighbor order is exactly the order displayed.

### Problem

Use

```text
a: b, c
b: a, d
c: a, d
d: b, c
e: f
f: e
```

1. Trace BFS from $a$, recording queue contents after each removal.
2. Trace iterative DFS from $a$ using the module's reverse-push convention.
3. Give the reached set and identify all connected components.
4. Give one different neighbor ordering that changes DFS order without changing
   the reached set.
5. Prove that every vertex discovered by either traversal is reachable from the
   start.
6. Run both module functions and compare with your traces.
7. Explain why one traversal from $a$ cannot certify that the entire graph is
   connected unless it reaches all declared vertices.

**Deliverable:** Two traces, the component partition, a short invariant proof,
and executable checks.

## E0.11.03 Prove equivalent tree contracts

- **Type:** proof and critique
- **Difficulty:** 4
- **Objective:** Use connectedness, acyclicity, and edge count correctly.
- **Estimated time:** 55 minutes
- **Allowed tools:** Graph definitions, induction, and contradiction.
- **Assumptions:** Simple finite undirected graphs.

### Problem

1. Prove that a connected acyclic graph has a unique path between every pair of
   vertices.
2. Prove the converse.
3. Prove by leaf removal that a tree on $n\ge1$ vertices has $n-1$ edges.
4. Give a graph with $n-1$ edges that is not a tree.
5. Prove that a connected graph with $n-1$ edges is a tree.
6. For a forest with $n$ vertices and $c$ components, derive $m=n-c$.
7. Audit the claim: "Removing any edge of an acyclic graph disconnects it."

**Deliverable:** Four proof directions, two counterexamples or repairs, and the
forest edge formula.

## E0.11.04 Build an MST and audit ties

- **Type:** derivation and implementation
- **Difficulty:** 4
- **Objective:** Apply the cut property and Kruskal contract.
- **Estimated time:** 60 minutes
- **Allowed tools:** Hand tracing, exchange arguments, and module code.
- **Assumptions:** Connected undirected weighted multigraph; loops may occur.

### Problem

Use vertices $a,b,c,d$ and weighted edge instances

$$
ab:1,\quad ac:1,\quad bc:2,\quad bd:3,\quad cd:3,\quad ad:8,
\quad aa:-5.
$$

1. Trace Kruskal in the listed tie order.
2. Explain why the negative loop is rejected from the tree.
3. Give the returned edge set and total weight.
4. Give a different MST with the same total weight.
5. Prove that selecting $ab$ is safe using a cut.
6. Explain why neither weight-3 edge belongs to every MST.
7. State what the function must do if vertex $e$ is added with no incident edge.
8. Run `kruskal_mst`, including its disconnected refusal.

**Deliverable:** A full trace, two MSTs, one cut proof, and boundary tests.

## E0.11.05 Quantify Hall's condition

- **Type:** proof and calculation
- **Difficulty:** 4
- **Objective:** Test every subset and distinguish matching sizes.
- **Estimated time:** 55 minutes
- **Allowed tools:** Sets and proof.
- **Assumptions:** Finite simple bipartite graph with left part $X$.

### Problem

Let $X=\{1,2,3\}$, $Y=\{p,q,r\}$, with

$$
N(1)=\{p,q\},\qquad N(2)=\{p,q\},\qquad N(3)=\{q,r\}.
$$

1. List $N(S)$ for all eight subsets $S\subseteq X$.
2. Verify Hall's condition and exhibit a matching covering $X$.
3. Delete edge $3r$. Find a subset that now violates Hall and prove no matching
   covers $X$.
4. Prove the necessary direction of Hall's theorem in general.
5. Give a maximal matching in the original graph that is not maximum.
6. Explain the difference among maximal, maximum, and perfect.
7. Explain why checking only $S=X$ and singleton sets can miss a violation.

**Deliverable:** A complete subset table, two matching audits, Hall necessity,
and terminology distinctions.

## E0.11.06 Separate stable and maximum matching

- **Type:** calculation and critique
- **Difficulty:** 4
- **Objective:** Trace deferred acceptance and audit blocking pairs.
- **Estimated time:** 60 minutes
- **Allowed tools:** Preference tables and module code.
- **Assumptions:** Equal sides with complete strict rankings.

### Problem

Use proposers

$$
a:x\succ y\succ z,\quad b:y\succ x\succ z,\quad c:x\succ y\succ z
$$

and receivers

$$
x:b\succ a\succ c,\quad y:a\succ c\succ b,\quad z:c\succ b\succ a.
$$

1. Trace proposer-side deferred acceptance round by round.
2. Report the final matching.
3. Check every unmatched pair for blocking.
4. Run `stable_matching` and compare.
5. Reverse the proposing side, recompute, and compare the stable outcome.
6. Explain why both outcomes have maximum cardinality under this contract but
   that cardinality does not establish stability.
7. Give a perfect matching for these participants that is unstable and identify
   a blocking pair.
8. State which assumptions fail with ties or incomplete lists.

**Deliverable:** Two traces, blocking-pair audits, and a precise stable-versus-
maximum explanation.

## E0.11.07 Certify a chromatic number

- **Type:** proof and application
- **Difficulty:** 3
- **Objective:** Pair coloring upper bounds with structural lower bounds.
- **Estimated time:** 45 minutes
- **Allowed tools:** Hand coloring and graph arguments.
- **Assumptions:** Nonempty simple undirected graphs.

### Problem

1. Prove that a proper $k$-coloring is an upper-bound certificate for $\chi(G)$.
2. Prove that a clique of size $r$ is a lower-bound certificate.
3. Determine $\chi(C_6)$ and $\chi(C_7)$, proving both bounds.
4. Determine the chromatic number of a nontrivial tree.
5. Add one universal vertex to $C_5$ and determine the new chromatic number.
6. Give a greedy ordering of a path that uses more colors than necessary, or
   explain why ordinary first-fit on a path cannot exceed three.
7. Explain why a displayed three-coloring alone does not prove $\chi(G)=3$.

**Deliverable:** Five paired upper/lower certificates and one algorithmic
critique.

## E0.11.08 Separate Euler and Hamilton coverage

- **Type:** proof and critique
- **Difficulty:** 4
- **Objective:** Distinguish edge and vertex tours under assumptions.
- **Estimated time:** 55 minutes
- **Allowed tools:** Degree arguments and explicit tours.
- **Assumptions:** Finite undirected multigraphs; isolate handling must be stated.

### Problem

1. State the connectedness and parity contract for an Euler tour.
2. Prove why a closed Euler trail has zero odd-degree vertices and an open Euler
   trail has exactly two odd-degree endpoints.
3. Analyze two triangles sharing exactly one vertex: find an Euler tour and
   prove there is no Hamiltonian cycle.
4. Analyze $K_4$: prove it has a Hamiltonian cycle and no Euler tour.
5. Explain how parallel edges and loops affect the Euler degree test.
6. Explain why isolated vertices need special wording in the Euler theorem.
7. Audit: "Every graph with all even degrees has an Euler tour."
8. Audit: "A Hamiltonian cycle uses every edge exactly once."

**Deliverable:** Two contrasting examples, one parity proof, and two repaired
claims.

## E0.11.09 Adjust Euler's planar formula

- **Type:** derivation and proof
- **Difficulty:** 4
- **Objective:** Handle faces and disconnected components.
- **Estimated time:** 55 minutes
- **Allowed tools:** Connected Euler formula and double counting.
- **Assumptions:** Finite planar embeddings; exterior face counted once.

### Problem

1. Verify $n-m+f=2$ for a planar drawing of $K_4$.
2. Compute $n,m,f,c$ for two disjoint triangles and verify $n-m+f=1+c$.
3. Derive the component-adjusted formula by adding $c-1$ noncrossing bridges.
4. Prove that a connected simple planar graph with $n\ge3$ satisfies
   $m\le3n-6$.
5. Use the bound to prove $K_5$ is nonplanar.
6. Explain why satisfying Euler's equation does not prove planarity.
7. Explain why counting regions in a drawing with crossings is invalid.
8. State which part is outside scope if asked for a general planarity-testing
   algorithm.

**Deliverable:** Two audits, two derivations, one nonplanarity proof, and scope
language.

## E0.11.10 Order a computation DAG

- **Type:** proof and implementation
- **Difficulty:** 4
- **Objective:** Prove and use DAG iff topological order.
- **Estimated time:** 60 minutes
- **Allowed tools:** Induction and module code.
- **Assumptions:** Finite digraphs.

### Problem

For arcs

$$
x\to m,\quad w\to m,\quad m\to s,\quad b\to a,\quad m\to a,
\quad s\to L,\quad a\to L,
$$

1. Give two distinct topological orders.
2. Verify every arc against one order.
3. Prove that a topological order forbids a directed cycle.
4. Prove every finite DAG has an indegree-zero vertex.
5. Complete the converse proof by induction.
6. Run `topological_order` and validate its result by an arc-position map.
7. Add $L\to m$ and verify cycle refusal.
8. Explain why a reverse-mode autodiff pass uses reverse topological order and
   why this does not make the computation graph cyclic.

**Deliverable:** Two orders, the iff proof, executable validation, and the
autodiff interpretation.

## E0.11.11 Translate graph matrix views

- **Type:** calculation and derivation
- **Difficulty:** 4
- **Objective:** Derive incidence and Laplacian identities.
- **Estimated time:** 65 minutes
- **Allowed tools:** Hand matrix arithmetic.
- **Assumptions:** Loopless simple undirected graph unless stated otherwise.

### Problem

Use the path $1$-$2$-$3$, order vertices as $(1,2,3)$, and orient edges
$1\to2$, $2\to3$.

1. Write the adjacency matrix $\mathbf{A}$ and degree matrix $\mathbf{D}$.
2. Write the edge-by-vertex incidence matrix $\mathbf{B}$.
3. Compute $\mathbf{B}^{\top}\mathbf{B}$ and verify
   $\mathbf{L}=\mathbf{D}-\mathbf{A}$.
4. Verify $\mathbf{L}\boldsymbol{1}_3=\mathbf{0}$.
5. For $\boldsymbol{x}=(1,4,9)^{\top}$, compute
   $\boldsymbol{x}^{\top}\mathbf{L}\boldsymbol{x}$ two ways.
6. Reverse one edge orientation and prove $\mathbf{L}$ is unchanged.
7. State how a directed adjacency matrix changes degree recovery.
8. State how parallel edges and a loop interact with adjacency and signed
   incidence conventions.
9. Explain why these identities do not constitute spectral graph theory.

**Deliverable:** Four matrices, two energy calculations, and three convention
audits.

## E0.11.12 Certify max flow with a minimum cut

- **Type:** derivation and implementation
- **Difficulty:** 5
- **Objective:** Integrate capacity, conservation, residual reachability, and evidence.
- **Estimated time:** 90 minutes
- **Allowed tools:** Hand calculation and module code.
- **Assumptions:** Finite directed network with nonnegative capacities.

### Problem

Use capacities

$$
c(s,a)=3,\quad c(s,b)=2,\quad c(a,b)=1,\quad
c(a,t)=2,\quad c(b,t)=3.
$$

1. Give a feasible flow of value $5$.
2. Verify every capacity constraint and conservation at $a,b$.
3. Give an $s$-$t$ cut of capacity $5$.
4. Use weak duality to prove your flow is maximum and cut is minimum.
5. Trace at least one sequence of BFS augmenting paths and bottlenecks.
6. Run `edmonds_karp`; verify its value, flow, and returned partition.
7. Compute the returned cut capacity from original arcs.
8. Test a network with no $s$-$t$ path and a negative-capacity refusal.
9. Explain the role of residual reverse arcs.
10. Explain why passing finite tests does not prove max-flow min-cut.
11. State the implementation's antiparallel-arc limitation and distinguish it
    from the theorem's scope.

**Deliverable:** A primal flow, dual cut, equality certificate, augmentation
trace, boundary tests, and evidence statement.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)