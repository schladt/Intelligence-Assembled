"""Boundary-focused tests for the module 0.11 graph algorithms."""

import unittest

from graph_tools import (
    breadth_first_order,
    depth_first_order,
    edmonds_karp,
    kruskal_mst,
    stable_matching,
    topological_order,
    undirected_adjacency,
)


class GraphToolsTests(unittest.TestCase):
    def test_simple_graph_validation_and_degree(self) -> None:
        graph = undirected_adjacency(("a", "b", "c"), (("a", "b"), ("b", "c")))
        self.assertEqual(graph, {"a": ("b",), "b": ("a", "c"), "c": ("b",)})
        self.assertEqual(sum(map(len, graph.values())), 4)

    def test_multigraph_loop_contributes_two_to_degree(self) -> None:
        graph = undirected_adjacency(
            ("a", "b"),
            (("a", "a"), ("a", "b"), ("a", "b")),
            allow_loops=True,
            allow_parallel=True,
        )
        self.assertEqual(len(graph["a"]), 4)
        self.assertEqual(len(graph["b"]), 2)
        self.assertEqual(sum(map(len, graph.values())), 6)

    def test_simple_graph_refuses_loops_parallel_edges_and_unknown_vertices(self) -> None:
        with self.assertRaises(ValueError):
            undirected_adjacency((1, 2), ((1, 1),))
        with self.assertRaises(ValueError):
            undirected_adjacency((1, 2), ((1, 2), (2, 1)))
        with self.assertRaises(ValueError):
            undirected_adjacency((1, 2), ((1, 3),))
        with self.assertRaisesRegex(ValueError, "hashable"):
            undirected_adjacency(([1], [2]), ())

    def test_bfs_and_dfs_visit_only_the_start_component(self) -> None:
        graph = {"a": ("b", "c"), "b": ("d",), "c": (), "d": (), "x": ()}
        self.assertEqual(breadth_first_order(graph, "a"), ("a", "b", "c", "d"))
        self.assertEqual(depth_first_order(graph, "a"), ("a", "b", "d", "c"))
        self.assertEqual(breadth_first_order(graph, "x"), ("x",))

    def test_traversal_refuses_malformed_adjacency(self) -> None:
        with self.assertRaises(ValueError):
            breadth_first_order({"a": ("missing",)}, "a")
        with self.assertRaises(ValueError):
            depth_first_order({"a": ()}, "missing")

    def test_topological_order_respects_every_arc(self) -> None:
        vertices = ("x", "w", "multiply", "loss")
        edges = (("x", "multiply"), ("w", "multiply"), ("multiply", "loss"))
        order = topological_order(vertices, edges)
        position = {vertex: index for index, vertex in enumerate(order)}
        self.assertTrue(all(position[left] < position[right] for left, right in edges))

    def test_topological_order_refuses_cycles(self) -> None:
        with self.assertRaisesRegex(ValueError, "cycle"):
            topological_order((1, 2, 3), ((1, 2), (2, 3), (3, 1)))
        self.assertEqual(topological_order(("solo",), ()), ("solo",))

    def test_kruskal_returns_tree_and_weight(self) -> None:
        tree = kruskal_mst(
            ("a", "b", "c", "d"),
            (
                ("a", "b", 1),
                ("a", "c", 1),
                ("b", "c", 2),
                ("b", "d", 3),
                ("c", "d", 3),
            ),
        )
        self.assertEqual(tree, (("a", "b", 1.0), ("a", "c", 1.0), ("b", "d", 3.0)))
        self.assertEqual(sum(edge[2] for edge in tree), 5)

    def test_kruskal_handles_parallel_edges_and_refuses_disconnection(self) -> None:
        self.assertEqual(kruskal_mst((1,), ((1, 1, -4),)), ())
        self.assertEqual(kruskal_mst((1, 2), ((1, 2, 5), (1, 2, 2)))[0][2], 2)
        with self.assertRaisesRegex(ValueError, "connected"):
            kruskal_mst((1, 2, 3), ((1, 2, 1),))

    def test_stable_matching_is_stable_and_proposer_optimal_example(self) -> None:
        proposers = {"a": ("x", "y"), "b": ("y", "x")}
        receivers = {"x": ("b", "a"), "y": ("a", "b")}
        self.assertEqual(stable_matching(proposers, receivers), {"a": "x", "b": "y"})

    def test_stable_matching_refuses_incomplete_or_unequal_sides(self) -> None:
        with self.assertRaises(ValueError):
            stable_matching({"a": ("x",), "b": ("x",)}, {"x": ("a", "b")})
        with self.assertRaises(ValueError):
            stable_matching({"a": ("x", "y"), "b": ("x", "y")}, {"x": ("a", "b"), "y": ("a", "a")})

    def test_edmonds_karp_returns_flow_and_minimum_cut(self) -> None:
        capacities = {
            ("s", "a"): 3,
            ("s", "b"): 2,
            ("a", "b"): 1,
            ("a", "t"): 2,
            ("b", "t"): 3,
        }
        result = edmonds_karp(capacities, "s", "t")
        self.assertEqual(result.value, 5)
        self.assertEqual(result.source_side, frozenset({"s"}))
        self.assertEqual(result.sink_side, frozenset({"a", "b", "t"}))
        self.assertEqual(sum(result.flow.get(("s", vertex), 0) for vertex in ("a", "b")), 5)

    def test_edmonds_karp_zero_flow_and_invalid_contracts(self) -> None:
        result = edmonds_karp({("s", "a"): 2}, "s", "t")
        self.assertEqual(result.value, 0)
        self.assertEqual(result.source_side, frozenset({"s", "a"}))
        with self.assertRaises(ValueError):
            edmonds_karp({("s", "t"): -1}, "s", "t")
        with self.assertRaisesRegex(ValueError, "antiparallel"):
            edmonds_karp({("s", "a"): 1, ("a", "s"): 1}, "s", "a")
        with self.assertRaises(ValueError):
            edmonds_karp({}, "s", "s")

    def test_edmonds_karp_preserves_tiny_positive_capacity(self) -> None:
        result = edmonds_karp({("s", "t"): 1e-15}, "s", "t")
        self.assertEqual(result.value, 1e-15)
        self.assertEqual(result.flow, {("s", "t"): 1e-15})
        self.assertEqual(result.source_side, frozenset({"s"}))


if __name__ == "__main__":
    unittest.main()