# Solutions for §0.11 Graph Theory

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

These are full worked solutions. Equivalent arguments are valid when they state
the same graph model, assumptions, and evidence limits. Run Python excerpts from
the module's `code/` directory.

## E0.11.01 Declare a graph model and audit degree

### Key idea

Degree belongs to a graph model, not to a picture.

### Reasoning

The two $ab$ instances are parallel and $cc$ is a loop, both forbidden in a
simple graph. As an undirected multigraph,

$$
d(a)=2,\qquad d(b)=3,\qquad d(c)=3.
$$

The loop contributes two to $d(c)$. Thus $2+3+3=8=2(4)$.

For the directed instances, the degree pairs $(d^-,d^+)$ are

$$
a:(1,1),\qquad b:(1,2),\qquad c:(2,1).
$$

Both indegrees and outdegrees sum to four. An adjacency set collapses the two
$ab$ instances and cannot preserve edge identity for trails, capacities, or
weights. An edge list with unique edge IDs, or adjacency lists containing edge
records, preserves multiplicity.

```python
from graph_tools import undirected_adjacency

graph = undirected_adjacency(
    ("a", "b", "c"),
    (("a", "b"), ("a", "b"), ("b", "c"), ("c", "c")),
    allow_loops=True,
    allow_parallel=True,
)
assert tuple(map(len, graph.values())) == (2, 3, 3)
```

### Verification

The undirected degree sum and both directed degree sums count all four edge
instances exactly twice overall.

### Common wrong turn

Do not count a loop once in undirected degree merely because it is one edge.

## E0.11.02 Traverse components with BFS and DFS

### Key idea

Order is representation-dependent; the reached set is a connectivity fact.

### Reasoning

BFS queue states after each removal are

| Removed | Queue after neighbor processing |
|---|---|
| $a$ | $[b,c]$ |
| $b$ | $[c,d]$ |
| $c$ | $[d]$ |
| $d$ | $[]$ |

So BFS order is $(a,b,c,d)$. Reverse-push DFS visits $(a,b,d,c)$.
Restarting after that component gives $(e,f)$, so the component partition is
$\{a,b,c,d\}$ and $\{e,f\}$.

Changing $a$'s neighbors to $(c,b)$ changes the DFS order, but not the reached
set. For the invariant proof, the start is reachable by a length-zero path.
Whenever a traversal discovers $v$ from already reachable $u$, appending edge
$uv$ to a path to $u$ gives a path to $v$.

```python
from graph_tools import breadth_first_order, depth_first_order

graph = {
    "a": ("b", "c"), "b": ("a", "d"), "c": ("a", "d"),
    "d": ("b", "c"), "e": ("f",), "f": ("e",),
}
assert breadth_first_order(graph, "a") == ("a", "b", "c", "d")
assert depth_first_order(graph, "a") == ("a", "b", "d", "c")
```

### Verification

The first search reaches four of six declared vertices, so it certifies one
component but refutes connectedness of the whole graph.

### Common wrong turn

Do not infer a unique DFS order without specifying neighbor order and stack
convention.

## E0.11.03 Prove equivalent tree contracts

### Key idea

Connectivity supplies path existence; acyclicity supplies path uniqueness.

### Reasoning

In a connected acyclic graph, a path exists between every pair. If two distinct
simple paths joined $u$ and $v$, follow them to their first divergence and next
reunion. The two subpaths form a cycle, contradiction.

Conversely, unique paths imply connectedness. If a cycle existed, two vertices
on it would be joined by the two directions around the cycle, contradicting
uniqueness.

For edge count, the one-vertex tree has zero edges. A tree with $n\ge2$ has a
leaf. Remove the leaf and its unique edge; the remaining tree has $n-1$
vertices and, inductively, $n-2$ edges. Restore the edge to obtain $n-1$.

A triangle plus an isolated vertex has $n=4,m=3$ but is not a tree. Now let a
connected graph have $n-1$ edges. It has a spanning tree, which already uses
$n-1$ edges. Therefore the graph has no edges outside that tree and is itself a
tree.

Each forest component is a tree. If component $i$ has $n_i$ vertices, it has
$n_i-1$ edges, so

$$
m=\sum_{i=1}^c(n_i-1)=n-c.
$$

The final claim is false for a disconnected forest: removing an edge from one
nontrivial component does not increase separation between vertices in another
already separate component in the colloquial sense, though it does increase the
number of components. The precise repair is: every edge of a forest is a bridge,
so removing it increases the component count by one.

### Verification

Every equivalence uses both existence and uniqueness; the $n-1$ counterexample
shows why one scalar equation is insufficient.

### Common wrong turn

Do not use "acyclic" as a synonym for "tree" when the graph may be disconnected.

## E0.11.04 Build an MST and audit ties

### Key idea

Kruskal accepts light edges that join components; loops and cycle-closing edges
cannot help connectivity.

### Reasoning

The loop $aa:-5$ is considered first but rejected because it joins no distinct
components. Kruskal then accepts $ab:1$, $ac:1$, rejects $bc:2$ because it
closes the $abc$ cycle, and accepts $bd:3$. The returned tree is
$\{ab,ac,bd\}$ with weight $5$. Replacing $bd$ by tied edge $cd$ gives another
MST of weight $5$.

For cut $\{a\}\mid\{b,c,d\}$, the crossing weights are $1,1,8$.
Thus $ab$ is a minimum crossing edge and is safe for some MST. It is tied with
$ac$, so the cut does not prove either one belongs to every MST. Likewise the
two weight-3 edges can substitute for one another.

Adding isolated $e$ makes the graph disconnected, so no spanning tree exists
and the function must raise `ValueError`.

```python
from graph_tools import kruskal_mst

edges = (("a", "b", 1), ("a", "c", 1), ("b", "c", 2),
         ("b", "d", 3), ("c", "d", 3), ("a", "d", 8),
         ("a", "a", -5))
tree = kruskal_mst(("a", "b", "c", "d"), edges)
assert tree == (("a", "b", 1.0), ("a", "c", 1.0), ("b", "d", 3.0))
try:
    kruskal_mst(("a", "b", "c", "d", "e"), edges)
except ValueError:
    pass
else:
    raise AssertionError("disconnected input must be refused")
```

### Verification

Both proposed trees connect four vertices with three edges and weight five.

### Common wrong turn

Negative weight does not force a loop into an MST. A spanning tree cannot
contain any loop.

## E0.11.05 Quantify Hall's condition

### Key idea

Hall tests collective shortages, so every subset matters.

### Reasoning

The neighborhood table is

| $S$ | $N(S)$ |
|---|---|
| $\varnothing$ | $\varnothing$ |
| $\{1\}$ | $\{p,q\}$ |
| $\{2\}$ | $\{p,q\}$ |
| $\{3\}$ | $\{q,r\}$ |
| $\{1,2\}$ | $\{p,q\}$ |
| $\{1,3\}$ | $\{p,q,r\}$ |
| $\{2,3\}$ | $\{p,q,r\}$ |
| $X$ | $\{p,q,r\}$ |

Every row has $|N(S)|\ge|S|$. One covering matching is
$\{1p,2q,3r\}$. After deleting $3r$, all three left vertices have collective
neighborhood $\{p,q\}$, so $S=X$ violates Hall.

For necessity, a matching covering $X$ assigns distinct partners to the
vertices of every $S\subseteq X$. Those partners all lie in $N(S)$, so
$|N(S)|\ge|S|$.

The one-edge matching $\{1p\}$ is not maximal because another edge can be
added. A genuine maximal but nonmaximum example in the same graph is
$\{1q,3r\}$: every unused edge touches $1$, $q$, $3$, or $r$ except $2p$,
which can actually be added, so this attempt is maximum. Instead use
$\{1p,3q\}$: every edge touches a matched endpoint, making it maximal of size
two, while the displayed perfect matching has size three.

Maximal means inclusion cannot be extended, maximum means largest cardinality,
and perfect means every vertex is covered. A graph can have singleton and whole-
side checks pass while an intermediate group of three vertices has only two
neighbors, so those partial checks do not establish Hall.

### Verification

The violating set supplies a direct pigeonhole obstruction, while the original
matching explicitly witnesses sufficiency for this instance.

### Common wrong turn

Do not use "maximal" and "maximum" interchangeably.

## E0.11.06 Separate stable and maximum matching

### Key idea

Deferred acceptance changes tentative partners until no blocking pair can
survive.

### Reasoning

First proposals are $a\to x$, $b\to y$, $c\to x$. Receiver $x$ keeps $a$
over $c$; $y$ keeps $b$. Rejected $c$ proposes to $y$, which prefers $c$ to
$b$, so $b$ becomes free. Then $b$ proposes to $x$, which prefers $b$ to $a$.
Finally $a$ proposes to $y$, which prefers $a$ to $c$, and $c$ proposes to
$z$. The result is

$$
\{a\mathbin{-}y,b\mathbin{-}x,c\mathbin{-}z\}.
$$

Every proposer who prefers another receiver was rejected there in favor of a
partner that receiver ranks higher, so no unmatched pair blocks. Directly:
$a$ prefers $x$ but $x$ prefers $b$; $b$ prefers $y$ but $y$ prefers $a$;
$c$ prefers $x,y$ but each prefers its current partner.

```python
from graph_tools import stable_matching

result = stable_matching(
    {"a": ("x", "y", "z"), "b": ("y", "x", "z"),
     "c": ("x", "y", "z")},
    {"x": ("b", "a", "c"), "y": ("a", "c", "b"),
     "z": ("c", "b", "a")},
)
assert result == {"a": "y", "b": "x", "c": "z"}
```

With receivers proposing, first choices are $x\to b$, $y\to a$, $z\to c$;
all are accepted, giving the same matching in this instance. Equality of the
two outcomes is possible but not guaranteed generally.

The perfect matching $\{a z,b y,c x\}$ is unstable because $a$ and $y$
prefer each other to their assigned partners. Every perfect matching has maximum
cardinality three, but only a blocking-pair audit establishes stability.
Ties remove strict comparison, and incomplete lists remove the guarantee that
everyone ranks and accepts every opposite-side participant.

### Verification

The result covers all six participants and every unmatched pair fails at least
one side of the blocking condition.

### Common wrong turn

Do not claim reversing proposers must change the result; it can, but this input
has a common proposer- and receiver-optimal stable outcome.

## E0.11.07 Certify a chromatic number

### Key idea

Exact chromatic claims need a feasible coloring and an impossibility argument
for fewer colors.

### Reasoning

A proper $k$-coloring witnesses $\chi(G)\le k$. A clique of size $r$ has every
pair adjacent, so all $r$ vertices need distinct colors and $\chi(G)\ge r$.

Alternating two colors around $C_6$ works, and an edge requires at least two, so
$\chi(C_6)=2$. Alternation around $C_7$ returns to a conflict, so two colors
fail; three colors work, hence $\chi(C_7)=3$.

Every nontrivial tree is bipartite by parity of distance from a root and has an
edge, so its chromatic number is two. A universal vertex added to $C_5$ needs a
new color beyond the three required by the odd cycle, while four colors suffice;
the result is four.

First-fit on any vertex ordering of a path can use at most three because a
vertex has at most two previously colored neighbors. It can use three: for path
$1-2-3-4$, order $(1,4,2,3)$. Vertices $1,4$ get color 1, vertex $2$ gets 2,
and vertex $3$, adjacent to colors 2 and 1, gets 3. The path is nevertheless
2-colorable.

### Verification

Each exact value has both an upper and lower certificate.

### Common wrong turn

A three-coloring proves only $\chi(G)\le3$ until a lower bound is supplied.

## E0.11.08 Separate Euler and Hamilton coverage

### Key idea

Euler pairs arrivals and departures at vertices; Hamilton controls vertex
repetition instead.

### Reasoning

All positive-degree vertices must lie in one component. Then an Euler tour
exists exactly when every degree is even. In any trail, each internal visit uses
one edge to arrive and one to depart. Thus odd incident edges can remain only at
the two distinct endpoints of an open trail. A closed trail has none. The
handshake lemma rules out exactly one odd vertex.

For two triangles $vabv$ and $vcdv$, an Euler tour is
$v,a,b,v,c,d,v$. All degrees are even. A Hamiltonian cycle would have to visit
vertices in both sides of cut vertex $v$. Moving between the two triangles
requires visiting $v$ twice, impossible.

$K_4$ has Hamiltonian cycle $1,2,3,4,1$. Every vertex has degree three, so it
has no Euler tour. Parallel edges count separately and a loop contributes two,
so the parity theorem still applies to multigraphs.

Isolated vertices do not matter to edge coverage, which is why the precise
connectedness condition refers to positive-degree vertices. The claim "all even
degrees" needs that condition. A Hamiltonian cycle visits every vertex once and
may leave many edges unused.

### Verification

The shared-vertex example has Euler but not Hamilton; $K_4$ has Hamilton but not
Euler. Neither property implies the other.

### Common wrong turn

Do not apply the Euler parity theorem to vertex coverage.

## E0.11.09 Adjust Euler's planar formula

### Key idea

Components share one exterior face, which changes the constant.

### Reasoning

A planar $K_4$ drawing has $n=4,m=6,f=4$, so $4-6+4=2$. Two disjoint
triangles have $n=6,m=6,c=2$ and three faces: two interiors plus one shared
exterior. Therefore $6-6+3=3=1+c$.

Connect $c$ components with $c-1$ noncrossing bridge edges drawn through the
exterior face. Vertices and faces do not change, while edges become
$m+c-1$. Connected Euler gives

$$
n-(m+c-1)+f=2,
$$

so $n-m+f=1+c$.

In a connected simple planar graph with $n\ge3$, every face boundary has at
least three edge appearances and every edge borders two face sides. Hence
$3f\le2m$. Euler gives $f=2-n+m$, so

$$
3(2-n+m)\le2m\implies m\le3n-6.
$$

$K_5$ has $n=5,m=10$, but $10>9$, so it is nonplanar. Euler's equation is
only necessary: a nonplanar graph can have numbers satisfying the equation for
some integer labeled $f$, but that number is not a face count from a planar
embedding. Crossings also subdivide drawn regions without becoming graph
vertices, invalidating a face audit. General planarity testing belongs outside
this module.

### Verification

Both examples use the exterior face exactly once, and the edge bound contradicts
$K_5$ numerically.

### Common wrong turn

Do not count regions in an arbitrary crossing drawing as planar faces.

## E0.11.10 Order a computation DAG

### Key idea

A topological order linearizes dependencies without adding edges.

### Reasoning

Two valid orders are

$$
(x,w,b,m,s,a,L)
\quad\text{and}\quad
(b,w,x,m,a,s,L).
$$

In the first, each of $x,w$ precedes $m$; $b,m$ precede $a$; $m$ precedes
$s$; and $s,a$ precede $L$.

If a directed cycle existed, choose its vertex appearing last in a topological
order. Its outgoing cycle arc points to an earlier vertex, contradiction.

If every vertex of a finite digraph had positive indegree, start anywhere and
repeatedly follow an incoming arc. Finiteness forces a repeated vertex, creating
a directed cycle. Therefore a DAG has an indegree-zero vertex. Remove it; the
remainder is a DAG and has a topological order by induction. Prefix the removed
vertex.

```python
from graph_tools import topological_order

vertices = ("x", "w", "m", "s", "b", "a", "L")
arcs = (("x", "m"), ("w", "m"), ("m", "s"), ("b", "a"),
        ("m", "a"), ("s", "L"), ("a", "L"))
order = topological_order(vertices, arcs)
position = {vertex: index for index, vertex in enumerate(order)}
assert all(position[left] < position[right] for left, right in arcs)
try:
    topological_order(vertices, arcs + (("L", "m"),))
except ValueError:
    pass
else:
    raise AssertionError("cycle must be refused")
```

Reverse-mode processes operations in reverse topological order so all child
contributions are accumulated before their parents. Reversing an evaluation
schedule does not add reverse arcs to the original computation graph.

### Verification

The position-map assertion checks every arc, not only visually adjacent items.

### Common wrong turn

Do not confuse reverse traversal of a DAG with turning the computation into a
cycle.

## E0.11.11 Translate graph matrix views

### Key idea

The incidence matrix records differences; the Laplacian records their squared
energy independent of arbitrary orientation.

### Reasoning

The matrices are

$$
\mathbf{A}=\begin{bmatrix}0&1&0\\1&0&1\\0&1&0\end{bmatrix},
\quad
\mathbf{D}=\begin{bmatrix}1&0&0\\0&2&0\\0&0&1\end{bmatrix},
$$

$$
\mathbf{B}=\begin{bmatrix}-1&1&0\\0&-1&1\end{bmatrix}.
$$

Multiplication gives

$$
\mathbf{B}^{\top}\mathbf{B}
=\begin{bmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{bmatrix}
=\mathbf{D}-\mathbf{A}=\mathbf{L}.
$$

Every row sum of $\mathbf{L}$ is zero, so
$\mathbf{L}\boldsymbol{1}_3=\mathbf0$. For
$\boldsymbol{x}=(1,4,9)^{\top}$,

$$
\boldsymbol{x}^{\top}\mathbf{L}\boldsymbol{x}
=(4-1)^2+(9-4)^2=9+25=34.
$$

Direct multiplication gives
$\mathbf{L}\boldsymbol{x}=(-3,-2,5)^{\top}$ and dotting with
$\boldsymbol{x}$ gives $-3-8+45=34$.

Reversing one orientation negates one row of $\mathbf{B}$. Its outer product
with itself is unchanged, so $\mathbf{B}^{\top}\mathbf{B}$ is unchanged. In
a directed adjacency matrix, row sums are outdegrees and column sums are
indegrees under the lesson convention. Parallel edges can be encoded by
multiplicity entries and repeated incidence rows. A signed loop incidence row
is zero, so it cannot recover the loop's degree contribution; that limitation
must be stated. No eigenvalue analysis or spectral algorithm has been used.

### Verification

The two energy calculations agree and are nonnegative.

### Common wrong turn

Do not transpose the incidence convention silently: edge-by-vertex
$\mathbf{B}$ makes $\mathbf{B}^{\top}\mathbf{B}$ vertex-by-vertex.

## E0.11.12 Certify max flow with a minimum cut

### Key idea

A feasible flow and equal-capacity cut form matching primal and dual
certificates.

### Reasoning

One feasible flow is

$$
f(s,a)=3,\quad f(s,b)=2,\quad f(a,b)=1,
\quad f(a,t)=2,\quad f(b,t)=3.
$$

Every value is between zero and capacity. At $a$, inflow $3$ equals outflow
$1+2$. At $b$, inflow $2+1$ equals outflow $3$. The value is five.

Cut $S=\{s\}$, $T=\{a,b,t\}$ has capacity $3+2=5$. Weak duality gives

$$
5=|f|\le\text{maximum flow}\le\text{minimum cut}\le5,
$$

so both certificates are optimal.

One Edmonds-Karp trace augments $s-a-t$ by $2$, then $s-b-t$ by $2$, then
$s-a-b-t$ by $1$. The total is five. Residual reverse arcs permit a later path
to cancel and reroute earlier flow rather than making greedy choices permanent.

```python
from graph_tools import edmonds_karp

capacities = {
    ("s", "a"): 3, ("s", "b"): 2, ("a", "b"): 1,
    ("a", "t"): 2, ("b", "t"): 3,
}
result = edmonds_karp(capacities, "s", "t")
assert result.value == 5
assert result.source_side == frozenset({"s"})
cut_capacity = sum(
    capacity
    for (left, right), capacity in capacities.items()
    if left in result.source_side and right in result.sink_side
)
assert cut_capacity == result.value

zero = edmonds_karp({("s", "a"): 2}, "s", "t")
assert zero.value == 0
try:
    edmonds_karp({("s", "t"): -1}, "s", "t")
except ValueError:
    pass
else:
    raise AssertionError("negative capacity must be refused")
```

Finite tests establish behavior on these networks. Max-flow min-cut for every
finite directed capacitated network requires the proof. This implementation
refuses antiparallel original arcs so original and residual reverse arcs remain
easy to distinguish. The theorem permits antiparallel arcs under a richer edge-
identity representation.

### Verification

Capacity, conservation, flow value, and cut capacity all agree. Residual
reachability returns the same cut used in the certificate.

### Common wrong turn

Do not sum capacities of arcs from $T$ back to $S$ into the directed cut
capacity.

[Back to module](../README.md) | [Exercise set](../exercises/README.md)