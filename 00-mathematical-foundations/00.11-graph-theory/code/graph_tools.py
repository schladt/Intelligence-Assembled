"""Small, explicit graph algorithms for module 0.11.

The implementations favor visible mathematical contracts over a broad API.
Vertices must be hashable, traversal order follows input neighbor order, and
invalid graph models are rejected instead of being silently repaired.
"""

from collections import deque
from collections.abc import Hashable, Iterable, Mapping, Sequence
from math import isfinite
from numbers import Real
from typing import NamedTuple, TypeVar


Vertex = TypeVar("Vertex", bound=Hashable)


class FlowResult(NamedTuple):
    value: float
    flow: dict[tuple[Hashable, Hashable], float]
    source_side: frozenset[Hashable]
    sink_side: frozenset[Hashable]


def _vertex_tuple(vertices: Iterable[Vertex]) -> tuple[Vertex, ...]:
    result = tuple(vertices)
    try:
        unique_count = len(set(result))
    except TypeError as error:
        raise ValueError("vertices must be unique and hashable") from error
    if unique_count != len(result):
        raise ValueError("vertices must be unique and hashable")
    return result


def undirected_adjacency(
    vertices: Iterable[Vertex],
    edges: Iterable[tuple[Vertex, Vertex]],
    *,
    allow_loops: bool = False,
    allow_parallel: bool = False,
) -> dict[Vertex, tuple[Vertex, ...]]:
    """Validate an undirected graph and return multiplicity-aware adjacency.

    Each loop is stored twice at its endpoint, so adjacency length equals
    degree under the convention that a loop contributes two.
    """
    vertex_order = _vertex_tuple(vertices)
    vertex_set = set(vertex_order)
    adjacency: dict[Vertex, list[Vertex]] = {vertex: [] for vertex in vertex_order}
    seen: set[frozenset[Vertex]] = set()

    for edge in edges:
        if len(edge) != 2:
            raise ValueError("each edge must have exactly two endpoints")
        left, right = edge
        if left not in vertex_set or right not in vertex_set:
            raise ValueError("every edge endpoint must be a declared vertex")
        if left == right and not allow_loops:
            raise ValueError("loops are not allowed by this graph contract")
        key = frozenset((left, right))
        if key in seen and not allow_parallel:
            raise ValueError("parallel edges are not allowed by this graph contract")
        seen.add(key)
        adjacency[left].append(right)
        adjacency[right].append(left)

    return {vertex: tuple(neighbors) for vertex, neighbors in adjacency.items()}


def _checked_adjacency(
    adjacency: Mapping[Vertex, Iterable[Vertex]], start: Vertex
) -> dict[Vertex, tuple[Vertex, ...]]:
    graph = {vertex: tuple(neighbors) for vertex, neighbors in adjacency.items()}
    if start not in graph:
        raise ValueError("start must be a vertex in the graph")
    vertices = set(graph)
    if any(neighbor not in vertices for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("every neighbor must be a declared vertex")
    return graph


def breadth_first_order(
    adjacency: Mapping[Vertex, Iterable[Vertex]], start: Vertex
) -> tuple[Vertex, ...]:
    """Return vertices reachable from start in breadth-first order."""
    graph = _checked_adjacency(adjacency, start)
    queue = deque([start])
    seen = {start}
    order: list[Vertex] = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return tuple(order)


def depth_first_order(
    adjacency: Mapping[Vertex, Iterable[Vertex]], start: Vertex
) -> tuple[Vertex, ...]:
    """Return vertices reachable from start in iterative depth-first order."""
    graph = _checked_adjacency(adjacency, start)
    stack = [start]
    seen: set[Vertex] = set()
    order: list[Vertex] = []
    while stack:
        vertex = stack.pop()
        if vertex in seen:
            continue
        seen.add(vertex)
        order.append(vertex)
        stack.extend(reversed(graph[vertex]))
    return tuple(order)


def topological_order(
    vertices: Iterable[Vertex], edges: Iterable[tuple[Vertex, Vertex]]
) -> tuple[Vertex, ...]:
    """Return a topological order, or refuse a directed cycle."""
    vertex_order = _vertex_tuple(vertices)
    vertex_set = set(vertex_order)
    outgoing: dict[Vertex, list[Vertex]] = {vertex: [] for vertex in vertex_order}
    indegree = {vertex: 0 for vertex in vertex_order}
    for source, target in edges:
        if source not in vertex_set or target not in vertex_set:
            raise ValueError("every arc endpoint must be a declared vertex")
        outgoing[source].append(target)
        indegree[target] += 1

    queue = deque(vertex for vertex in vertex_order if indegree[vertex] == 0)
    result: list[Vertex] = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for target in outgoing[vertex]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)

    if len(result) != len(vertex_order):
        raise ValueError("directed graph contains a cycle")
    return tuple(result)


class _DisjointSet:
    def __init__(self, vertices: Iterable[Vertex]) -> None:
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in self.parent}

    def find(self, vertex: Vertex) -> Vertex:
        root = vertex
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[vertex] != vertex:
            parent = self.parent[vertex]
            self.parent[vertex] = root
            vertex = parent
        return root

    def union(self, left: Vertex, right: Vertex) -> bool:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return False
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1
        return True


def kruskal_mst(
    vertices: Iterable[Vertex],
    weighted_edges: Iterable[tuple[Vertex, Vertex, Real]],
) -> tuple[tuple[Vertex, Vertex, float], ...]:
    """Return one MST of a connected undirected weighted graph.

    Equal-weight edges retain input order. Parallel edges are permitted; loops
    are ignored because they cannot belong to a tree.
    """
    vertex_order = _vertex_tuple(vertices)
    if not vertex_order:
        raise ValueError("an MST requires at least one vertex")
    vertex_set = set(vertex_order)
    edges: list[tuple[Vertex, Vertex, float]] = []
    for left, right, weight in weighted_edges:
        if left not in vertex_set or right not in vertex_set:
            raise ValueError("every edge endpoint must be a declared vertex")
        if isinstance(weight, bool) or not isinstance(weight, Real) or not isfinite(weight):
            raise ValueError("edge weights must be finite real numbers")
        edges.append((left, right, float(weight)))

    forest = _DisjointSet(vertex_order)
    result: list[tuple[Vertex, Vertex, float]] = []
    for left, right, weight in sorted(edges, key=lambda edge: edge[2]):
        if left != right and forest.union(left, right):
            result.append((left, right, weight))
            if len(result) == len(vertex_order) - 1:
                return tuple(result)
    if len(vertex_order) == 1:
        return ()
    raise ValueError("MST requires a connected underlying graph")


def stable_matching(
    proposer_preferences: Mapping[Vertex, Sequence[Vertex]],
    receiver_preferences: Mapping[Vertex, Sequence[Vertex]],
) -> dict[Vertex, Vertex]:
    """Return the proposer-optimal stable matching for complete strict lists."""
    proposers = tuple(proposer_preferences)
    receivers = tuple(receiver_preferences)
    if len(proposers) != len(receivers):
        raise ValueError("the two sides must have the same size")
    proposer_set = set(proposers)
    receiver_set = set(receivers)
    if any(
        len(preferences) != len(receivers) or set(preferences) != receiver_set
        for preferences in proposer_preferences.values()
    ):
        raise ValueError("each proposer must rank every receiver exactly once")
    if any(
        len(preferences) != len(proposers) or set(preferences) != proposer_set
        for preferences in receiver_preferences.values()
    ):
        raise ValueError("each receiver must rank every proposer exactly once")

    rank = {
        receiver: {proposer: index for index, proposer in enumerate(preferences)}
        for receiver, preferences in receiver_preferences.items()
    }
    free = deque(proposers)
    next_choice = {proposer: 0 for proposer in proposers}
    receiver_partner: dict[Vertex, Vertex] = {}

    while free:
        proposer = free.popleft()
        receiver = proposer_preferences[proposer][next_choice[proposer]]
        next_choice[proposer] += 1
        current = receiver_partner.get(receiver)
        if current is None:
            receiver_partner[receiver] = proposer
        elif rank[receiver][proposer] < rank[receiver][current]:
            receiver_partner[receiver] = proposer
            free.append(current)
        else:
            free.append(proposer)

    return {proposer: receiver for receiver, proposer in receiver_partner.items()}


def edmonds_karp(
    capacities: Mapping[tuple[Vertex, Vertex], Real], source: Vertex, sink: Vertex
) -> FlowResult:
    """Compute a maximum flow and residual minimum cut with Edmonds-Karp."""
    if source == sink:
        raise ValueError("source and sink must differ")
    capacity: dict[tuple[Vertex, Vertex], float] = {}
    vertices = {source, sink}
    for (left, right), value in capacities.items():
        if left == right:
            raise ValueError("flow-network arcs may not be loops")
        if isinstance(value, bool) or not isinstance(value, Real) or not isfinite(value):
            raise ValueError("capacities must be finite real numbers")
        if value < 0:
            raise ValueError("capacities must be nonnegative")
        if (right, left) in capacity:
            raise ValueError("this implementation refuses antiparallel arcs")
        capacity[(left, right)] = float(value)
        vertices.update((left, right))

    residual = dict(capacity)
    neighbors = {vertex: [] for vertex in vertices}
    for left, right in capacity:
        residual.setdefault((right, left), 0.0)
        neighbors[left].append(right)
        neighbors[right].append(left)

    total = 0.0
    while True:
        parent: dict[Vertex, Vertex | None] = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            left = queue.popleft()
            for right in neighbors[left]:
                if right not in parent and residual[(left, right)] > 0:
                    parent[right] = left
                    queue.append(right)
        if sink not in parent:
            break

        bottleneck = float("inf")
        right = sink
        while parent[right] is not None:
            left = parent[right]
            bottleneck = min(bottleneck, residual[(left, right)])
            right = left
        right = sink
        while parent[right] is not None:
            left = parent[right]
            residual[(left, right)] -= bottleneck
            residual[(right, left)] += bottleneck
            right = left
        total += bottleneck

    reachable = {source}
    queue = deque([source])
    while queue:
        left = queue.popleft()
        for right in neighbors[left]:
            if right not in reachable and residual[(left, right)] > 0:
                reachable.add(right)
                queue.append(right)

    flow = {
        edge: value - residual[edge]
        for edge, value in capacity.items()
        if value - residual[edge] > 0
    }
    return FlowResult(
        total,
        flow,
        frozenset(reachable),
        frozenset(vertices - reachable),
    )