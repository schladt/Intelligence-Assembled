"""Contract-focused reference implementations for module 0.15."""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from enum import Enum
from numbers import Integral
from typing import Generic, TypeVar


State = TypeVar("State", bound=Hashable)
Symbol = TypeVar("Symbol", bound=Hashable)
Vertex = TypeVar("Vertex", bound=Hashable)


def _integer(value: int, name: str, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise TypeError(f"{name} must be an integer")
    result = int(value)
    if result < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return result


@dataclass(frozen=True)
class DFA(Generic[State, Symbol]):
    """A deterministic finite automaton with a total transition function."""

    states: frozenset[State]
    alphabet: frozenset[Symbol]
    transition: Mapping[tuple[State, Symbol], State]
    start: State
    accepting: frozenset[State]

    def __post_init__(self) -> None:
        states = frozenset(self.states)
        alphabet = frozenset(self.alphabet)
        accepting = frozenset(self.accepting)
        transition = dict(self.transition)
        if not states:
            raise ValueError("a DFA must have at least one state")
        if self.start not in states:
            raise ValueError("start state is not in states")
        if not accepting <= states:
            raise ValueError("accepting states must be DFA states")
        expected = {(state, symbol) for state in states for symbol in alphabet}
        if set(transition) != expected:
            raise ValueError("transition function must contain every state-symbol pair exactly once")
        if any(target not in states for target in transition.values()):
            raise ValueError("every transition target must be a DFA state")
        object.__setattr__(self, "states", states)
        object.__setattr__(self, "alphabet", alphabet)
        object.__setattr__(self, "accepting", accepting)
        object.__setattr__(self, "transition", transition)

    def accepts(self, word: Iterable[Symbol]) -> bool:
        """Return whether the automaton accepts ``word``."""

        state = self.start
        for symbol in word:
            if symbol not in self.alphabet:
                raise ValueError(f"symbol {symbol!r} is outside the alphabet")
            state = self.transition[state, symbol]
        return state in self.accepting


@dataclass(frozen=True)
class CNFGrammar:
    """A context-free grammar in Chomsky normal form, without epsilon rules."""

    start: str
    terminal_rules: Mapping[str, Iterable[str]]
    binary_rules: Mapping[str, Iterable[tuple[str, str]]]

    def __post_init__(self) -> None:
        terminal_rules = {
            left: frozenset(terminals) for left, terminals in self.terminal_rules.items()
        }
        binary_rules = {
            left: frozenset(pairs) for left, pairs in self.binary_rules.items()
        }
        variables = set(terminal_rules) | set(binary_rules)
        if not variables or self.start not in variables:
            raise ValueError("start must be a declared grammar variable")
        if any(not variable for variable in variables):
            raise ValueError("grammar variables must be nonempty strings")
        if any(not terminal for terminals in terminal_rules.values() for terminal in terminals):
            raise ValueError("terminals must be nonempty strings")
        for pairs in binary_rules.values():
            for left_child, right_child in pairs:
                if left_child not in variables or right_child not in variables:
                    raise ValueError("binary rules must reference declared variables")
        object.__setattr__(self, "terminal_rules", terminal_rules)
        object.__setattr__(self, "binary_rules", binary_rules)

    def accepts(self, tokens: Sequence[str]) -> bool:
        """Decide membership with the CYK algorithm in cubic time."""

        if not tokens:
            return False
        if any(not isinstance(token, str) or not token for token in tokens):
            raise ValueError("tokens must be nonempty strings")

        terminal_parents: dict[str, set[str]] = {}
        for parent, terminals in self.terminal_rules.items():
            for terminal in terminals:
                terminal_parents.setdefault(terminal, set()).add(parent)
        binary_parents: dict[tuple[str, str], set[str]] = {}
        for parent, pairs in self.binary_rules.items():
            for pair in pairs:
                binary_parents.setdefault(pair, set()).add(parent)

        size = len(tokens)
        table = [[set() for _ in range(size + 1)] for _ in range(size)]
        for start, token in enumerate(tokens):
            table[start][1].update(terminal_parents.get(token, ()))

        for length in range(2, size + 1):
            for start in range(size - length + 1):
                cell = table[start][length]
                for left_length in range(1, length):
                    right_start = start + left_length
                    right_length = length - left_length
                    for left_variable in table[start][left_length]:
                        for right_variable in table[right_start][right_length]:
                            cell.update(binary_parents.get((left_variable, right_variable), ()))
        return self.start in table[0][size]


class HaltStatus(Enum):
    ACCEPT = "accept"
    REJECT = "reject"
    TIMEOUT = "timeout"


@dataclass(frozen=True)
class TuringMachine(Generic[State, Symbol]):
    """A deterministic one-tape Turing machine with explicit halting states."""

    states: frozenset[State]
    input_alphabet: frozenset[Symbol]
    tape_alphabet: frozenset[Symbol]
    blank: Symbol
    transition: Mapping[tuple[State, Symbol], tuple[State, Symbol, int]]
    start: State
    accept: State
    reject: State

    def __post_init__(self) -> None:
        states = frozenset(self.states)
        input_alphabet = frozenset(self.input_alphabet)
        tape_alphabet = frozenset(self.tape_alphabet)
        transition = dict(self.transition)
        if not states:
            raise ValueError("a machine must have states")
        if not {self.start, self.accept, self.reject} <= states:
            raise ValueError("start, accept, and reject must be machine states")
        if self.accept == self.reject:
            raise ValueError("accept and reject states must differ")
        if self.blank not in tape_alphabet or self.blank in input_alphabet:
            raise ValueError("blank must be a tape symbol outside the input alphabet")
        if not input_alphabet <= tape_alphabet:
            raise ValueError("input alphabet must be contained in tape alphabet")
        for (state, symbol), (target, written, move) in transition.items():
            if state not in states or state in {self.accept, self.reject}:
                raise ValueError("transitions must leave nonhalting machine states")
            if symbol not in tape_alphabet or written not in tape_alphabet:
                raise ValueError("transitions must read and write tape symbols")
            if target not in states or move not in {-1, 1}:
                raise ValueError("transition target or head movement is invalid")
        object.__setattr__(self, "states", states)
        object.__setattr__(self, "input_alphabet", input_alphabet)
        object.__setattr__(self, "tape_alphabet", tape_alphabet)
        object.__setattr__(self, "transition", transition)


@dataclass(frozen=True)
class RunResult(Generic[State, Symbol]):
    status: HaltStatus
    steps: int
    state: State
    head: int
    nonblank_tape: Mapping[int, Symbol]


def run_bounded(
    machine: TuringMachine[State, Symbol],
    word: Iterable[Symbol],
    *,
    max_steps: int,
) -> RunResult[State, Symbol]:
    """Simulate at most ``max_steps`` transitions; timeout is not rejection."""

    limit = _integer(max_steps, "max_steps")
    symbols = tuple(word)
    if any(symbol not in machine.input_alphabet for symbol in symbols):
        raise ValueError("input contains a symbol outside the input alphabet")
    tape = {index: symbol for index, symbol in enumerate(symbols)}
    state = machine.start
    head = 0
    steps = 0

    while state not in {machine.accept, machine.reject} and steps < limit:
        scanned = tape.get(head, machine.blank)
        action = machine.transition.get((state, scanned))
        if action is None:
            raise ValueError("machine transition is undefined for the reached configuration")
        state, written, move = action
        if written == machine.blank:
            tape.pop(head, None)
        else:
            tape[head] = written
        head += move
        steps += 1

    if state == machine.accept:
        status = HaltStatus.ACCEPT
    elif state == machine.reject:
        status = HaltStatus.REJECT
    else:
        status = HaltStatus.TIMEOUT
    return RunResult(status, steps, state, head, dict(tape))


def verify_subset_sum(
    values: Sequence[int], target: int, certificate: Iterable[int]
) -> bool:
    """Verify that distinct certified indices sum to ``target``."""

    normalized_target = _integer(target, "target")
    normalized_values = [
        _integer(value, f"values[{index}]") for index, value in enumerate(values)
    ]
    indices = tuple(certificate)
    if any(isinstance(index, bool) or not isinstance(index, Integral) for index in indices):
        raise TypeError("certificate indices must be integers")
    normalized_indices = tuple(int(index) for index in indices)
    if len(set(normalized_indices)) != len(normalized_indices):
        return False
    if any(index < 0 or index >= len(normalized_values) for index in normalized_indices):
        return False
    return sum(normalized_values[index] for index in normalized_indices) == normalized_target


def subset_sum_dp(values: Sequence[int], target: int) -> tuple[int, ...] | None:
    """Return one subset-sum witness in O(n * target) time, or ``None``."""

    normalized_target = _integer(target, "target")
    normalized_values = [
        _integer(value, f"values[{index}]") for index, value in enumerate(values)
    ]
    witnesses: dict[int, tuple[int, ...]] = {0: ()}
    for index, value in enumerate(normalized_values):
        additions: dict[int, tuple[int, ...]] = {}
        for partial, witness in tuple(witnesses.items()):
            candidate = partial + value
            if candidate <= normalized_target and candidate not in witnesses:
                additions.setdefault(candidate, witness + (index,))
        witnesses.update(additions)
    return witnesses.get(normalized_target)


def _undirected_graph(
    graph: Mapping[Vertex, Iterable[Vertex]],
) -> tuple[tuple[Vertex, ...], tuple[tuple[Vertex, Vertex], ...]]:
    vertices = tuple(graph)
    vertex_set = set(vertices)
    adjacency = {vertex: frozenset(neighbors) for vertex, neighbors in graph.items()}
    for vertex, neighbors in adjacency.items():
        if not neighbors <= vertex_set:
            raise ValueError("every neighbor must be a graph vertex")
        if any(vertex not in adjacency[neighbor] for neighbor in neighbors):
            raise ValueError("the graph must be undirected and symmetric")
    order = {vertex: index for index, vertex in enumerate(vertices)}
    edges: list[tuple[Vertex, Vertex]] = []
    for left in vertices:
        for right in adjacency[left]:
            if order[left] <= order[right]:
                edges.append((left, right))
    return vertices, tuple(edges)


def verify_vertex_cover(
    graph: Mapping[Vertex, Iterable[Vertex]], certificate: Iterable[Vertex]
) -> bool:
    """Verify that every undirected edge has a certified endpoint."""

    vertices, edges = _undirected_graph(graph)
    cover = set(certificate)
    if not cover <= set(vertices):
        return False
    return all(left in cover or right in cover for left, right in edges)


def independent_set_to_vertex_cover(
    graph: Mapping[Vertex, Iterable[Vertex]], k: int
) -> tuple[dict[Vertex, tuple[Vertex, ...]], int]:
    """Map an independent-set instance (G, k) to (G, |V| - k)."""

    requested = _integer(k, "k")
    vertices, _ = _undirected_graph(graph)
    if requested > len(vertices):
        raise ValueError("k cannot exceed the vertex count")
    return {vertex: tuple(graph[vertex]) for vertex in vertices}, len(vertices) - requested


def vertex_cover_fpt(
    graph: Mapping[Vertex, Iterable[Vertex]], k: int
) -> tuple[Vertex, ...] | None:
    """Return a cover of size at most k by O(2^k poly(n)) branching."""

    budget = _integer(k, "k")
    vertices, edges = _undirected_graph(graph)

    def search(remaining: tuple[tuple[Vertex, Vertex], ...], left: int) -> set[Vertex] | None:
        if not remaining:
            return set()
        if left == 0:
            return None
        u, v = remaining[0]
        choices = (u,) if u == v else (u, v)
        for chosen in choices:
            reduced = tuple(edge for edge in remaining if chosen not in edge)
            suffix = search(reduced, left - 1)
            if suffix is not None:
                suffix.add(chosen)
                return suffix
        return None

    cover = search(edges, budget)
    if cover is None:
        return None
    return tuple(vertex for vertex in vertices if vertex in cover)


def vertex_cover_2approx(
    graph: Mapping[Vertex, Iterable[Vertex]],
) -> tuple[Vertex, ...]:
    """Return the endpoint set of a maximal matching, a 2-approximate cover."""

    vertices, edges = _undirected_graph(graph)
    cover: set[Vertex] = set()
    for left, right in edges:
        if left in cover or right in cover:
            continue
        cover.add(left)
        cover.add(right)
    return tuple(vertex for vertex in vertices if vertex in cover)
