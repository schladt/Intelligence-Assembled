"""Behavioral tests for module 0.15 reference implementations."""

from __future__ import annotations

import itertools
import unittest

from complexity import (
    CNFGrammar,
    DFA,
    HaltStatus,
    TuringMachine,
    independent_set_to_vertex_cover,
    run_bounded,
    subset_sum_dp,
    verify_subset_sum,
    verify_vertex_cover,
    vertex_cover_2approx,
    vertex_cover_fpt,
)


class AutomataTests(unittest.TestCase):
    def test_dfa_accepts_exactly_binary_words_with_even_ones(self) -> None:
        machine = DFA(
            states=frozenset({"even", "odd"}),
            alphabet=frozenset({"0", "1"}),
            transition={
                ("even", "0"): "even",
                ("even", "1"): "odd",
                ("odd", "0"): "odd",
                ("odd", "1"): "even",
            },
            start="even",
            accepting=frozenset({"even"}),
        )
        cases = {"": True, "0": True, "1": False, "101": True, "111": False}
        for word, expected in cases.items():
            with self.subTest(word=word):
                self.assertEqual(machine.accepts(word), expected)
        with self.assertRaises(ValueError):
            machine.accepts("2")

    def test_dfa_requires_a_total_valid_transition_function(self) -> None:
        with self.assertRaisesRegex(ValueError, "every state-symbol"):
            DFA(
                states=frozenset({0, 1}),
                alphabet=frozenset({"a"}),
                transition={(0, "a"): 1},
                start=0,
                accepting=frozenset({1}),
            )
        with self.assertRaisesRegex(ValueError, "target"):
            DFA(
                states=frozenset({0}),
                alphabet=frozenset({"a"}),
                transition={(0, "a"): 1},
                start=0,
                accepting=frozenset(),
            )

    def test_cyk_decides_a_nonregular_context_free_language_slice(self) -> None:
        grammar = CNFGrammar(
            start="S",
            terminal_rules={"A": {"a"}, "B": {"b"}},
            binary_rules={"S": {("A", "B"), ("A", "C")}, "C": {("S", "B")}},
        )
        for word in (("a", "b"), ("a", "a", "b", "b"), ("a", "a", "a", "b", "b", "b")):
            with self.subTest(word=word):
                self.assertTrue(grammar.accepts(word))
        for word in ((), ("a",), ("a", "b", "b"), ("b", "a")):
            with self.subTest(word=word):
                self.assertFalse(grammar.accepts(word))

    def test_cyk_rejects_undeclared_variables_and_bad_tokens(self) -> None:
        with self.assertRaisesRegex(ValueError, "declared"):
            CNFGrammar("S", {"A": {"a"}}, {"S": {("A", "B")}})
        grammar = CNFGrammar("S", {"S": {"a"}}, {})
        with self.assertRaisesRegex(ValueError, "tokens"):
            grammar.accepts(("",))


class MachineTests(unittest.TestCase):
    @staticmethod
    def last_symbol_is_one_machine() -> TuringMachine[str, str]:
        return TuringMachine(
            states=frozenset({"scan", "seen0", "seen1", "accept", "reject"}),
            input_alphabet=frozenset({"0", "1"}),
            tape_alphabet=frozenset({"0", "1", "_"}),
            blank="_",
            transition={
                ("scan", "0"): ("seen0", "0", 1),
                ("scan", "1"): ("seen1", "1", 1),
                ("scan", "_"): ("reject", "_", 1),
                ("seen0", "0"): ("seen0", "0", 1),
                ("seen0", "1"): ("seen1", "1", 1),
                ("seen0", "_"): ("reject", "_", 1),
                ("seen1", "0"): ("seen0", "0", 1),
                ("seen1", "1"): ("seen1", "1", 1),
                ("seen1", "_"): ("accept", "_", 1),
            },
            start="scan",
            accept="accept",
            reject="reject",
        )

    def test_bounded_run_distinguishes_accept_reject_and_timeout(self) -> None:
        machine = self.last_symbol_is_one_machine()
        self.assertEqual(run_bounded(machine, "101", max_steps=4).status, HaltStatus.ACCEPT)
        self.assertEqual(run_bounded(machine, "110", max_steps=4).status, HaltStatus.REJECT)
        timeout = run_bounded(machine, "101", max_steps=3)
        self.assertEqual(timeout.status, HaltStatus.TIMEOUT)
        self.assertEqual(timeout.steps, 3)

    def test_bounded_run_rejects_invalid_input_and_undefined_transition(self) -> None:
        machine = self.last_symbol_is_one_machine()
        with self.assertRaisesRegex(ValueError, "input contains"):
            run_bounded(machine, "2", max_steps=1)
        partial = TuringMachine(
            states=frozenset({"q", "a", "r"}),
            input_alphabet=frozenset({"0"}),
            tape_alphabet=frozenset({"0", "_"}),
            blank="_",
            transition={},
            start="q",
            accept="a",
            reject="r",
        )
        with self.assertRaisesRegex(ValueError, "undefined"):
            run_bounded(partial, "0", max_steps=1)


class SubsetSumTests(unittest.TestCase):
    def test_verifier_checks_distinct_in_range_certificate_indices(self) -> None:
        values = [3, 5, 9, 12]
        self.assertTrue(verify_subset_sum(values, 17, [1, 3]))
        self.assertFalse(verify_subset_sum(values, 17, [1, 1, 2]))
        self.assertFalse(verify_subset_sum(values, 17, [8]))
        with self.assertRaises(TypeError):
            verify_subset_sum(values, 17, [True])

    def test_pseudopolynomial_solver_matches_exhaustive_reference(self) -> None:
        values = [0, 3, 5, 9, 12]
        for target in range(31):
            with self.subTest(target=target):
                witness = subset_sum_dp(values, target)
                reachable = any(
                    sum(values[index] for index in range(len(values)) if mask & (1 << index))
                    == target
                    for mask in range(1 << len(values))
                )
                self.assertEqual(witness is not None, reachable)
                if witness is not None:
                    self.assertTrue(verify_subset_sum(values, target, witness))

    def test_subset_sum_rejects_negative_and_noninteger_values(self) -> None:
        with self.assertRaises(ValueError):
            subset_sum_dp([1, -1], 2)
        with self.assertRaises(TypeError):
            subset_sum_dp([1, True], 2)


class VertexCoverTests(unittest.TestCase):
    @staticmethod
    def graph() -> dict[str, tuple[str, ...]]:
        return {
            "a": ("b", "c"),
            "b": ("a", "c"),
            "c": ("a", "b", "d"),
            "d": ("c",),
            "isolated": (),
        }

    def test_vertex_cover_verifier_and_reduction_preserve_yes_instances(self) -> None:
        graph = self.graph()
        self.assertTrue(verify_vertex_cover(graph, {"b", "c"}))
        self.assertFalse(verify_vertex_cover(graph, {"a"}))
        reduced, budget = independent_set_to_vertex_cover(graph, 3)
        self.assertEqual(budget, 2)
        independent = {"a", "d", "isolated"}
        complement = set(graph) - independent
        self.assertTrue(verify_vertex_cover(reduced, complement))

    def test_fpt_solver_matches_exhaustive_optimum_on_small_graph(self) -> None:
        graph = self.graph()
        optimum = min(
            len(candidate)
            for size in range(len(graph) + 1)
            for candidate in itertools.combinations(graph, size)
            if verify_vertex_cover(graph, candidate)
        )
        self.assertEqual(optimum, 2)
        self.assertIsNone(vertex_cover_fpt(graph, optimum - 1))
        cover = vertex_cover_fpt(graph, optimum)
        self.assertIsNotNone(cover)
        self.assertLessEqual(len(cover), optimum)
        self.assertTrue(verify_vertex_cover(graph, cover or ()))

    def test_two_approximation_is_a_cover_within_twice_optimum(self) -> None:
        graph = self.graph()
        cover = vertex_cover_2approx(graph)
        self.assertTrue(verify_vertex_cover(graph, cover))
        optimum = len(vertex_cover_fpt(graph, 2) or ())
        self.assertLessEqual(len(cover), 2 * optimum)

    def test_graph_algorithms_reject_asymmetric_or_unknown_neighbors(self) -> None:
        with self.assertRaisesRegex(ValueError, "symmetric"):
            verify_vertex_cover({"a": ("b",), "b": ()}, {"a"})
        with self.assertRaisesRegex(ValueError, "neighbor"):
            vertex_cover_fpt({"a": ("missing",)}, 1)
        with self.assertRaises(ValueError):
            independent_set_to_vertex_cover(self.graph(), 6)

    def test_self_loop_forces_its_vertex(self) -> None:
        graph = {"x": ("x",), "y": ()}
        self.assertEqual(vertex_cover_fpt(graph, 1), ("x",))
        self.assertEqual(vertex_cover_2approx(graph), ("x",))


if __name__ == "__main__":
    unittest.main()
