"""Contract-focused reference implementations for module 0.14."""

from __future__ import annotations

from collections import deque
from collections.abc import Callable, Hashable, Iterable, Mapping, Sequence
from dataclasses import dataclass
import heapq
import itertools
import math
from numbers import Integral, Real
import random
from typing import Any, Generic, TypeVar


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V", bound=Hashable)
P = TypeVar("P")


def _identity(value: T) -> T:
    return value


def binary_search_left(values: Sequence[T], target: K, *, key: Callable[[T], K] = _identity) -> int:
    """Return the first index whose key is not less than ``target``.

    ``values`` must already be sorted in nondecreasing key order. The function
    returns an insertion boundary whether or not the target is present.
    """

    lo = 0
    hi = len(values)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if key(values[mid]) < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def merge_sort(values: Sequence[T], *, key: Callable[[T], K] = _identity) -> list[T]:
    """Return a stable sorted copy of ``values`` using merge sort."""

    if len(values) < 2:
        return list(values)

    middle = len(values) // 2
    left = merge_sort(values[:middle], key=key)
    right = merge_sort(values[middle:], key=key)
    merged: list[T] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        left_key = key(left[left_index])
        right_key = key(right[right_index])
        if right_key < left_key:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


@dataclass
class MinHeap(Generic[T]):
    """Array-backed min-heap that exposes only heap-safe operations."""

    _values: list[T]

    def __init__(self, values: Iterable[T] = ()) -> None:
        self._values = []
        for value in values:
            self.push(value)

    def __len__(self) -> int:
        return len(self._values)

    def as_tuple(self) -> tuple[T, ...]:
        """Return an immutable snapshot of the internal heap array."""

        return tuple(self._values)

    def peek(self) -> T:
        """Return the minimum without removing it."""

        if not self._values:
            raise IndexError("peek from empty heap")
        return self._values[0]

    def push(self, value: T) -> None:
        """Insert one value and restore the heap invariant upward."""

        self._values.append(value)
        index = len(self._values) - 1
        while index > 0:
            parent = (index - 1) // 2
            if not self._values[index] < self._values[parent]:
                break
            self._values[index], self._values[parent] = (
                self._values[parent],
                self._values[index],
            )
            index = parent

    def pop(self) -> T:
        """Remove and return the minimum, restoring the invariant downward."""

        if not self._values:
            raise IndexError("pop from empty heap")
        minimum = self._values[0]
        final = self._values.pop()
        if not self._values:
            return minimum

        self._values[0] = final
        index = 0
        while True:
            left = 2 * index + 1
            if left >= len(self._values):
                break
            right = left + 1
            smaller = left
            if right < len(self._values) and self._values[right] < self._values[left]:
                smaller = right
            if not self._values[smaller] < self._values[index]:
                break
            self._values[index], self._values[smaller] = (
                self._values[smaller],
                self._values[index],
            )
            index = smaller
        return minimum


def _materialize_unweighted_graph(graph: Mapping[V, Iterable[V]]) -> dict[V, tuple[V, ...]]:
    adjacency = {vertex: tuple(neighbors) for vertex, neighbors in graph.items()}
    vertices = set(adjacency)
    for vertex, neighbors in adjacency.items():
        for neighbor in neighbors:
            if neighbor not in vertices:
                raise ValueError(f"neighbor {neighbor!r} from {vertex!r} is not a graph vertex")
    return adjacency


def bfs_shortest_paths(
    graph: Mapping[V, Iterable[V]], start: V
) -> tuple[dict[V, int], dict[V, V | None]]:
    """Return minimum edge counts and parents from ``start`` in a directed graph."""

    adjacency = _materialize_unweighted_graph(graph)
    if start not in adjacency:
        raise KeyError(f"start vertex {start!r} is not in the graph")

    distance = {start: 0}
    parent: dict[V, V | None] = {start: None}
    frontier = deque([start])
    while frontier:
        vertex = frontier.popleft()
        for neighbor in adjacency[vertex]:
            if neighbor in distance:
                continue
            distance[neighbor] = distance[vertex] + 1
            parent[neighbor] = vertex
            frontier.append(neighbor)
    return distance, parent


def recover_path(parent: Mapping[V, V | None], start: V, goal: V) -> list[V]:
    """Recover a parent-pointer path, or return an empty list if goal is absent."""

    if goal not in parent:
        return []

    reverse_path: list[V] = []
    seen: set[V] = set()
    current: V | None = goal
    while current is not None:
        if current in seen:
            raise ValueError("parent mapping contains a cycle")
        seen.add(current)
        reverse_path.append(current)
        if current == start:
            reverse_path.reverse()
            return reverse_path
        if current not in parent:
            raise ValueError("parent chain terminates before reaching start")
        current = parent[current]
    raise ValueError("parent chain terminates before reaching start")


def _materialize_weighted_graph(
    graph: Mapping[V, Iterable[tuple[V, Real]]],
) -> dict[V, tuple[tuple[V, float], ...]]:
    vertices = set(graph)
    adjacency: dict[V, tuple[tuple[V, float], ...]] = {}
    for vertex, edges in graph.items():
        normalized: list[tuple[V, float]] = []
        for neighbor, raw_weight in edges:
            if neighbor not in vertices:
                raise ValueError(f"neighbor {neighbor!r} from {vertex!r} is not a graph vertex")
            if isinstance(raw_weight, bool) or not isinstance(raw_weight, Real):
                raise TypeError("edge weights must be real numbers")
            weight = float(raw_weight)
            if not math.isfinite(weight) or weight < 0:
                raise ValueError("Dijkstra requires finite nonnegative edge weights")
            normalized.append((neighbor, weight))
        adjacency[vertex] = tuple(normalized)
    return adjacency


def dijkstra(
    graph: Mapping[V, Iterable[tuple[V, Real]]], start: V
) -> tuple[dict[V, float], dict[V, V | None]]:
    """Return shortest distances and parents under nonnegative edge weights."""

    adjacency = _materialize_weighted_graph(graph)
    if start not in adjacency:
        raise KeyError(f"start vertex {start!r} is not in the graph")

    distance = {start: 0.0}
    parent: dict[V, V | None] = {start: None}
    order = itertools.count()
    frontier: list[tuple[float, int, V]] = [(0.0, next(order), start)]

    while frontier:
        current_distance, _, vertex = heapq.heappop(frontier)
        if current_distance != distance.get(vertex):
            continue
        for neighbor, weight in adjacency[vertex]:
            candidate = current_distance + weight
            if candidate < distance.get(neighbor, math.inf):
                distance[neighbor] = candidate
                parent[neighbor] = vertex
                heapq.heappush(frontier, (candidate, next(order), neighbor))
    return distance, parent


class DisjointSet:
    """Maintain a partition with union by size and path compression."""

    def __init__(self, size: int) -> None:
        if isinstance(size, bool) or not isinstance(size, Integral):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be nonnegative")
        self._parent = list(range(size))
        self._size = [1] * size
        self.component_count = size

    def __len__(self) -> int:
        return len(self._parent)

    def _validate(self, item: int) -> int:
        if isinstance(item, bool) or not isinstance(item, Integral):
            raise TypeError("item must be an integer index")
        normalized = int(item)
        if not 0 <= normalized < len(self._parent):
            raise IndexError("item index out of range")
        return normalized

    def find(self, item: int) -> int:
        """Return the representative and compress the traversed path."""

        item = self._validate(item)
        root = item
        while self._parent[root] != root:
            root = self._parent[root]
        while self._parent[item] != item:
            parent = self._parent[item]
            self._parent[item] = root
            item = parent
        return root

    def union(self, left: int, right: int) -> bool:
        """Merge two components and report whether the partition changed."""

        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return False
        if self._size[left_root] < self._size[right_root]:
            left_root, right_root = right_root, left_root
        self._parent[right_root] = left_root
        self._size[left_root] += self._size[right_root]
        self.component_count -= 1
        return True

    def connected(self, left: int, right: int) -> bool:
        """Return whether two items belong to the same component."""

        return self.find(left) == self.find(right)

    def component_size(self, item: int) -> int:
        """Return the number of items in one component."""

        return self._size[self.find(item)]


def sparse_matvec(rows: Sequence[Mapping[int, Real]], vector: Sequence[Real]) -> list[float]:
    """Multiply row dictionaries by a dense vector, visiting stored entries only."""

    normalized_vector: list[float] = []
    for raw_value in vector:
        if isinstance(raw_value, bool) or not isinstance(raw_value, Real):
            raise TypeError("vector entries must be real numbers")
        value = float(raw_value)
        if not math.isfinite(value):
            raise ValueError("vector entries must be finite")
        normalized_vector.append(value)

    result: list[float] = []
    for row in rows:
        total = 0.0
        for raw_column, raw_value in row.items():
            if isinstance(raw_column, bool) or not isinstance(raw_column, Integral):
                raise TypeError("sparse column indices must be integers")
            column = int(raw_column)
            if not 0 <= column < len(normalized_vector):
                raise IndexError("sparse column index out of range")
            if isinstance(raw_value, bool) or not isinstance(raw_value, Real):
                raise TypeError("sparse values must be real numbers")
            value = float(raw_value)
            if not math.isfinite(value):
                raise ValueError("sparse values must be finite")
            total += value * normalized_vector[column]
        result.append(total)
    return result


def _integer_contract(value: int, name: str, *, minimum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise TypeError(f"{name} must be an integer")
    normalized = int(value)
    if normalized < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return normalized


def knapsack_01(
    weights: Sequence[int], values: Sequence[Real], capacity: int
) -> tuple[float, tuple[int, ...]]:
    """Return optimum 0/1 knapsack value and one recovered item-index tuple."""

    if len(weights) != len(values):
        raise ValueError("weights and values must have equal length")
    normalized_capacity = _integer_contract(capacity, "capacity", minimum=0)
    normalized_weights = [
        _integer_contract(weight, f"weight[{index}]", minimum=1)
        for index, weight in enumerate(weights)
    ]
    normalized_values: list[float] = []
    for index, raw_value in enumerate(values):
        if isinstance(raw_value, bool) or not isinstance(raw_value, Real):
            raise TypeError(f"value[{index}] must be a real number")
        value = float(raw_value)
        if not math.isfinite(value):
            raise ValueError(f"value[{index}] must be finite")
        normalized_values.append(value)

    item_count = len(normalized_weights)
    table = [
        [0.0] * (normalized_capacity + 1)
        for _ in range(item_count + 1)
    ]
    take = [
        [False] * (normalized_capacity + 1)
        for _ in range(item_count + 1)
    ]

    for item in range(1, item_count + 1):
        weight = normalized_weights[item - 1]
        value = normalized_values[item - 1]
        for available in range(normalized_capacity + 1):
            best = table[item - 1][available]
            if weight <= available:
                candidate = table[item - 1][available - weight] + value
                if candidate > best:
                    best = candidate
                    take[item][available] = True
            table[item][available] = best

    chosen: list[int] = []
    available = normalized_capacity
    for item in range(item_count, 0, -1):
        if take[item][available]:
            chosen.append(item - 1)
            available -= normalized_weights[item - 1]
    chosen.reverse()
    return table[item_count][normalized_capacity], tuple(chosen)


def interval_schedule(intervals: Iterable[tuple[Real, Real, P]]) -> tuple[tuple[Real, Real, P], ...]:
    """Return an earliest-finish maximum-cardinality half-open schedule."""

    normalized: list[tuple[float, float, P, tuple[Real, Real, P]]] = []
    for interval in intervals:
        if len(interval) != 3:
            raise ValueError("each interval must contain start, finish, and payload")
        raw_start, raw_finish, payload = interval
        if (
            isinstance(raw_start, bool)
            or isinstance(raw_finish, bool)
            or not isinstance(raw_start, Real)
            or not isinstance(raw_finish, Real)
        ):
            raise TypeError("interval boundaries must be real numbers")
        start = float(raw_start)
        finish = float(raw_finish)
        if not math.isfinite(start) or not math.isfinite(finish) or not start < finish:
            raise ValueError("intervals require finite start < finish")
        normalized.append((start, finish, payload, interval))

    normalized.sort(key=lambda item: item[1])
    chosen: list[tuple[Real, Real, P]] = []
    previous_finish = -math.inf
    for start, finish, _, original in normalized:
        if start >= previous_finish:
            chosen.append(original)
            previous_finish = finish
    return tuple(chosen)


def quickselect(values: Sequence[T], rank: int, *, rng: random.Random) -> T:
    """Return the zero-based rank under a caller-owned random generator."""

    if not values:
        raise ValueError("quickselect requires at least one value")
    normalized_rank = _integer_contract(rank, "rank", minimum=0)
    if normalized_rank >= len(values):
        raise IndexError("rank out of range")

    candidates = list(values)
    while True:
        if len(candidates) == 1:
            return candidates[0]
        pivot = candidates[rng.randrange(len(candidates))]
        lower = [value for value in candidates if value < pivot]
        equal = [value for value in candidates if not value < pivot and not pivot < value]
        higher = [value for value in candidates if pivot < value]
        if normalized_rank < len(lower):
            candidates = lower
        elif normalized_rank < len(lower) + len(equal):
            return pivot
        else:
            normalized_rank -= len(lower) + len(equal)
            candidates = higher
