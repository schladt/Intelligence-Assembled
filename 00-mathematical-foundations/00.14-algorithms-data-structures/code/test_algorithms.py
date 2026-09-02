"""Behavioral tests for module 0.14 reference implementations."""

from __future__ import annotations

import itertools
import math
import random
import unittest

from algorithms import (
    DisjointSet,
    MinHeap,
    bfs_shortest_paths,
    binary_search_left,
    dijkstra,
    interval_schedule,
    knapsack_01,
    merge_sort,
    quickselect,
    recover_path,
    sparse_matvec,
)


class SearchAndSortTests(unittest.TestCase):
    def test_binary_search_returns_left_boundary_for_present_and_absent_values(self) -> None:
        values = [1, 3, 3, 3, 7, 9]
        cases = {3: 1, 4: 4, 0: 0, 10: 6, 1: 0, 9: 5}
        for target, expected in cases.items():
            with self.subTest(target=target):
                self.assertEqual(binary_search_left(values, target), expected)
        self.assertEqual(binary_search_left([], 4), 0)

    def test_merge_sort_is_stable_and_does_not_mutate_input(self) -> None:
        records = [(2, "a"), (1, "b"), (2, "c"), (1, "d"), (2, "e")]
        snapshot = list(records)
        result = merge_sort(records, key=lambda item: item[0])
        self.assertEqual(
            result,
            [(1, "b"), (1, "d"), (2, "a"), (2, "c"), (2, "e")],
        )
        self.assertEqual(records, snapshot)


class HeapTests(unittest.TestCase):
    def assert_heap_invariant(self, values: tuple[int, ...]) -> None:
        for index in range(1, len(values)):
            self.assertLessEqual(values[(index - 1) // 2], values[index])

    def test_heap_repairs_after_each_push_and_pop(self) -> None:
        heap = MinHeap([2, 7, 4, 9, 8, 6])
        self.assert_heap_invariant(heap.as_tuple())
        heap.push(1)
        self.assertEqual(heap.peek(), 1)
        self.assert_heap_invariant(heap.as_tuple())
        self.assertEqual(heap.pop(), 1)
        self.assert_heap_invariant(heap.as_tuple())
        self.assertEqual([heap.pop() for _ in range(len(heap))], [2, 4, 6, 7, 8, 9])

    def test_heap_empty_contract_and_duplicate_values(self) -> None:
        heap = MinHeap([5, 1, 5])
        self.assertEqual([heap.pop(), heap.pop(), heap.pop()], [1, 5, 5])
        with self.assertRaises(IndexError):
            heap.peek()
        with self.assertRaises(IndexError):
            heap.pop()


class GraphTests(unittest.TestCase):
    def test_bfs_returns_edge_counts_parents_and_unreachable_boundary(self) -> None:
        graph = {
            "s": ["a", "b"],
            "a": ["g"],
            "b": ["a", "g"],
            "g": [],
            "isolated": [],
        }
        distance, parent = bfs_shortest_paths(graph, "s")
        self.assertEqual(distance["g"], 2)
        self.assertEqual(recover_path(parent, "s", "g"), ["s", "a", "g"])
        self.assertEqual(recover_path(parent, "s", "isolated"), [])

    def test_bfs_rejects_missing_vertices_and_parent_cycles(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a graph vertex"):
            bfs_shortest_paths({"s": ["missing"]}, "s")
        with self.assertRaises(KeyError):
            bfs_shortest_paths({"s": []}, "missing")
        with self.assertRaisesRegex(ValueError, "cycle"):
            recover_path({"g": "a", "a": "g"}, "s", "g")

    def test_dijkstra_uses_weighted_frontier_and_supports_unorderable_vertices(self) -> None:
        first = object()
        second = object()
        goal = object()
        graph = {
            first: [(second, 1.0), (goal, 4.0)],
            second: [(goal, 2.0)],
            goal: [],
        }
        distance, parent = dijkstra(graph, first)
        self.assertEqual(distance[goal], 3.0)
        self.assertEqual(recover_path(parent, first, goal), [first, second, goal])

    def test_dijkstra_rejects_any_invalid_weight_before_search(self) -> None:
        invalid_weights = (-1.0, math.inf, math.nan, True, "1")
        for weight in invalid_weights:
            with self.subTest(weight=weight):
                graph = {"s": [("a", 1.0)], "a": [("s", weight)]}
                with self.assertRaises((TypeError, ValueError)):
                    dijkstra(graph, "s")


class StructureTests(unittest.TestCase):
    def test_disjoint_set_preserves_partition_and_reports_repeated_union(self) -> None:
        sets = DisjointSet(8)
        for left, right in ((0, 1), (2, 3), (4, 5), (6, 7), (0, 2), (4, 6), (0, 4)):
            self.assertTrue(sets.union(left, right))
        self.assertEqual(sets.component_count, 1)
        self.assertEqual(sets.component_size(7), 8)
        self.assertTrue(all(sets.connected(0, item) for item in range(8)))
        self.assertFalse(sets.union(0, 7))

    def test_disjoint_set_rejects_invalid_sizes_and_indices(self) -> None:
        with self.assertRaises(TypeError):
            DisjointSet(True)
        with self.assertRaises(ValueError):
            DisjointSet(-1)
        sets = DisjointSet(2)
        for item in (-1, 2):
            with self.subTest(item=item), self.assertRaises(IndexError):
                sets.find(item)
        with self.assertRaises(TypeError):
            sets.find(True)

    def test_sparse_matvec_visits_declared_entries_and_rejects_bad_contracts(self) -> None:
        rows = [{0: 2.0, 3: -1.0}, {}, {1: 4.0}]
        self.assertEqual(sparse_matvec(rows, [3.0, 5.0, 0.0, 7.0]), [-1.0, 0.0, 20.0])
        with self.assertRaises(IndexError):
            sparse_matvec([{4: 1.0}], [1.0, 2.0])
        with self.assertRaises(TypeError):
            sparse_matvec([{True: 1.0}], [1.0, 2.0])
        with self.assertRaises(ValueError):
            sparse_matvec([{0: math.nan}], [1.0])


class ParadigmTests(unittest.TestCase):
    def test_knapsack_matches_exhaustive_reference_and_recovers_witness(self) -> None:
        weights = [2, 3, 4, 5]
        values = [3, 4, 8, 8]
        capacity = 7
        optimum, chosen = knapsack_01(weights, values, capacity)
        legal = []
        for mask in range(1 << len(weights)):
            indices = tuple(index for index in range(len(weights)) if mask & (1 << index))
            weight = sum(weights[index] for index in indices)
            if weight <= capacity:
                legal.append((sum(values[index] for index in indices), indices))
        self.assertEqual(optimum, max(value for value, _ in legal))
        self.assertEqual(chosen, (1, 2))
        self.assertLessEqual(sum(weights[index] for index in chosen), capacity)
        self.assertEqual(sum(values[index] for index in chosen), optimum)

    def test_knapsack_rejects_shape_and_numeric_contract_violations(self) -> None:
        with self.assertRaises(ValueError):
            knapsack_01([1], [1, 2], 3)
        with self.assertRaises(ValueError):
            knapsack_01([0], [1], 3)
        with self.assertRaises(TypeError):
            knapsack_01([True], [1], 3)
        with self.assertRaises(ValueError):
            knapsack_01([1], [math.inf], 3)

    def test_interval_schedule_is_compatible_and_maximum_on_small_domains(self) -> None:
        intervals = [
            (0, 3, "A"),
            (1, 2, "B"),
            (2, 4, "C"),
            (3, 5, "D"),
            (4, 7, "E"),
            (5, 6, "F"),
        ]
        chosen = interval_schedule(intervals)
        self.assertEqual(chosen, ((1, 2, "B"), (2, 4, "C"), (5, 6, "F")))
        for left, right in itertools.pairwise(chosen):
            self.assertLessEqual(left[1], right[0])

        best = 0
        for mask in range(1 << len(intervals)):
            candidate = sorted(
                (intervals[index] for index in range(len(intervals)) if mask & (1 << index)),
                key=lambda item: item[0],
            )
            if all(left[1] <= right[0] for left, right in itertools.pairwise(candidate)):
                best = max(best, len(candidate))
        self.assertEqual(len(chosen), best)

    def test_interval_schedule_rejects_invalid_boundaries(self) -> None:
        for interval in ((1, 1, "x"), (2, 1, "x"), (0, math.inf, "x"), (True, 2, "x")):
            with self.subTest(interval=interval), self.assertRaises((TypeError, ValueError)):
                interval_schedule([interval])

    def test_quickselect_matches_sorted_reference_without_mutating_input(self) -> None:
        values = [7, 1, 5, 3, 5, 9, 0, 5]
        snapshot = list(values)
        for rank, expected in enumerate(sorted(values)):
            with self.subTest(rank=rank):
                self.assertEqual(quickselect(values, rank, rng=random.Random(100 + rank)), expected)
        self.assertEqual(values, snapshot)

    def test_quickselect_rejects_empty_and_invalid_rank(self) -> None:
        with self.assertRaises(ValueError):
            quickselect([], 0, rng=random.Random(1))
        with self.assertRaises(IndexError):
            quickselect([1], 1, rng=random.Random(1))
        with self.assertRaises(TypeError):
            quickselect([1], True, rng=random.Random(1))


if __name__ == "__main__":
    unittest.main()
