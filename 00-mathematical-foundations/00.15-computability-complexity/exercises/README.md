# Exercises for §0.15 Computability and Complexity

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening its solution. State the encoding, model,
termination contract, reduction direction, and resource measure whenever they
matter.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.15.01 | Specify languages and computational tasks | classification and critique | 2 | 1 | 30-45 min |
| E0.15.02 | Trace and minimize finite-state memory | derivation and implementation | 3 | 2 | 40-60 min |
| E0.15.03 | Parse a context-free language with CYK | derivation and implementation | 3 | 2 | 45-70 min |
| E0.15.04 | Separate acceptance rejection and timeout | trace and critique | 3 | 2, 3 | 40-60 min |
| E0.15.05 | Reconstruct the halting diagonal argument | proof | 4 | 3 | 45-70 min |
| E0.15.06 | Point reductions in the useful direction | proof and critique | 4 | 4 | 45-70 min |
| E0.15.07 | Classify P NP hardness and completeness | classification and proof | 4 | 5, 6 | 50-75 min |
| E0.15.08 | Compose a canonical hardness argument | reduction and proof | 5 | 4-6 | 70-110 min |
| E0.15.09 | Diagnose pseudopolynomial subset sum | derivation and implementation | 4 | 6, 7 | 50-80 min |
| E0.15.10 | Prove a vertex-cover approximation guarantee | proof and implementation | 4 | 8 | 55-85 min |
| E0.15.11 | Amplify randomized decision procedures | probability and critique | 4 | 8 | 50-75 min |
| E0.15.12 | Design a hardness response for AI | applied synthesis | 5 | 8, 9 | 90-150 min |

## E0.15.01 Specify languages and computational tasks

- **Type:** classification and critique
- **Difficulty:** 2
- **Objective:** 1
- **Estimated time:** 30-45 minutes

### Problem

For each task, identify an encoding, the input-length variable, and whether the
requested output is decision, search, optimization, counting, or recognition.
When possible, give a threshold decision version.

1. Determine whether a Boolean formula is satisfiable.
2. Return one satisfying assignment.
3. Find a minimum-cost tour through weighted cities.
4. Count the proper 3-colorings of a graph.
5. Accept every Python program that eventually prints `done`, with no required
   behavior for programs that never do.

Explain why complexity-class membership for a decision language does not
silently classify every related output interface.

### Hint

Write the YES set before naming a class. For optimization, add a numeric bound to
form a decision question.

## E0.15.02 Trace and minimize finite-state memory

- **Type:** derivation and implementation
- **Difficulty:** 3
- **Objective:** 2
- **Estimated time:** 40-60 minutes

### Problem

Over alphabet $\{0,1\}$, let $L$ contain exactly the strings whose number of `1`
symbols is divisible by three.

1. Construct a DFA and label each state's invariant.
2. Trace `101101`, including the initial and final states.
3. Implement it with `DFA` and test every binary string of length at most six
   against a direct counter.
4. Prove that three states are necessary by giving three prefixes that require
   distinguishable future behavior.
5. Explain why adding more input length does not add machine memory.

### Hint

Use the residue of the count modulo three. Distinguish prefixes by appending a
suffix that makes exactly one total divisible by three.

## E0.15.03 Parse a context-free language with CYK

- **Type:** derivation and implementation
- **Difficulty:** 3
- **Objective:** 2
- **Estimated time:** 45-70 minutes

### Problem

Use the Chomsky-normal-form grammar

$$
S\to AB\mid AC,\qquad C\to SB,\qquad A\to a,\qquad B\to b.
$$

1. Show derivations for `ab` and `aabb`.
2. Fill every nonempty CYK cell for `aaabbb`.
3. State the substring invariant of cell $D[i,\ell]$.
4. Use `CNFGrammar.accepts` to check `ab`, `aabb`, `aaabbb`, `abb`, and the empty
   token sequence.
5. Derive the cubic bound and identify where grammar size enters.
6. Explain the implementation's empty-string boundary.

### Hint

Length-one cells come from terminal rules. Longer cells combine every split and
binary production.

## E0.15.04 Separate acceptance rejection and timeout

- **Type:** trace and critique
- **Difficulty:** 3
- **Objective:** 2, 3
- **Estimated time:** 40-60 minutes

### Problem

Use the module test machine that scans right and accepts exactly nonempty binary
strings ending in `1`.

1. Trace state, head, scanned symbol, and transition for `101`.
2. Run with bounds 0, 3, and 4. Explain each status.
3. Trace `110` to rejection.
4. Give a partial machine that reaches an undefined transition and explain why
   this is a malformed implementation contract, not a formal rejection.
5. Critique: "Any machine still running after a million steps does not halt."
6. State how a decider differs from a bounded simulator.

### Hint

The final decision occurs only after the scan reaches the blank symbol.

## E0.15.05 Reconstruct the halting diagonal argument

- **Type:** proof
- **Difficulty:** 4
- **Objective:** 3
- **Estimated time:** 45-70 minutes

### Problem

Assume a total decider $H(M,w)$ for $HALT$.

1. Define a program $D(x)$ that does the opposite of $H(x,x)$ with respect to
   halting.
2. Analyze both possible outputs of $H(D,D)$.
3. Identify exactly which assumption is contradicted.
4. Explain why simulation recognizes $HALT$.
5. Prove that the complement of $HALT$ is not recognizable, using dovetailing or
   closure under complement for decidable languages.
6. Explain why the result is stronger than "some programs take a long time."

### Hint

Your contradiction must use self-input. Keep "returns NO" separate from "does
not return."

## E0.15.06 Point reductions in the useful direction

- **Type:** proof and critique
- **Difficulty:** 4
- **Objective:** 4
- **Estimated time:** 45-70 minutes

### Problem

Let $A\le_m B$ through total computable function $f$.

1. Prove that a decider for $B$ yields a decider for $A$.
2. State and prove the contrapositive used for undecidability.
3. If $A$ is known undecidable and you want to prove $B$ undecidable, which
   reduction direction is useful?
4. Critique: "I reduced my new problem $B$ to $HALT$, so $B$ is undecidable."
5. Given $A\le_p B$ and $B\le_p C$, prove $A\le_p C$, including an output-length
   argument.
6. Draw separate arrows for solver reuse and hardness transfer.

### Hint

The same arrow supports two readings. A solver travels backward; hardness travels
forward.

## E0.15.07 Classify P NP hardness and completeness

- **Type:** classification and proof
- **Difficulty:** 4
- **Objective:** 5, 6
- **Estimated time:** 50-75 minutes

### Problem

For each claim, mark it true, false, or unknown, then justify it.

1. $P\subseteq NP$.
2. NP means problems that require non-polynomial time.
3. Every NP-hard problem is a decision problem in NP.
4. If one NP-complete language is in P, then $P=NP$.
5. No NP-complete problem has a polynomial-time algorithm.
6. SAT, subset sum decision, graph 3-colorability, and TSP decision have
   polynomially checkable certificates.
7. An optimization problem can be NP-hard without being a language in NP.
8. A problem with a fast verifier must have a known fast solver.

For item 6, state each certificate and a polynomial verification bound.

### Hint

Separate definitions, proved inclusions, conditional statements, and the open
$P$ versus $NP$ question.

## E0.15.08 Compose a canonical hardness argument

- **Type:** reduction and proof
- **Difficulty:** 5
- **Objective:** 4-6
- **Estimated time:** 70-110 minutes

### Problem

Assume `INDEPENDENT-SET` is NP-complete. Reduce it to `VERTEX-COVER`.

1. Define both decision languages with graph and integer encodings.
2. Map $(G,k)$ to $(G,|V|-k)$.
3. Prove both directions of the YES equivalence using set complements.
4. Bound transformation time and output size.
5. Prove `VERTEX-COVER` is in NP by specifying a certificate and verifier.
6. Conclude NP-completeness, naming both required obligations.
7. Use `independent_set_to_vertex_cover` and `verify_vertex_cover` on the graph
   from the code tests.
8. Explain why a reduction from vertex cover to independent set would not prove
   the requested hardness result from the given premise.

### Hint

For each edge, "not both endpoints are independent" is equivalent to "at least
one endpoint lies in the complement."

## E0.15.09 Diagnose pseudopolynomial subset sum

- **Type:** derivation and implementation
- **Difficulty:** 4
- **Objective:** 6, 7
- **Estimated time:** 50-80 minutes

### Problem

For values `[3, 5, 9, 12]` and target 17:

1. List reachable sums after each item, keeping only sums at most 17.
2. Recover one witness and verify it with `verify_subset_sum`.
3. Derive the $O(nT)$ time and $O(T)$ retained-state bounds of the dictionary or
   Boolean-table method.
4. Compare targets $T=2^{10}$ and $T=2^{40}$ by numeric magnitude and binary
   encoding length.
5. Explain why $O(nT)$ does not place binary-encoded subset sum in P.
6. Test target zero, duplicate values, unreachable targets, and malformed
   certificates.
7. State why fast certificate verification is consistent with NP-completeness.

### Hint

Each item may be used once. Update from a snapshot or descending sum order so it
cannot be reused in the same round.

## E0.15.10 Prove a vertex-cover approximation guarantee

- **Type:** proof and implementation
- **Difficulty:** 4
- **Objective:** 8
- **Estimated time:** 55-85 minutes

### Problem

The algorithm repeatedly selects an uncovered edge and adds both endpoints to
its cover.

1. Prove the selected edges form a matching.
2. Prove every vertex cover contains at least one endpoint from each selected
   edge.
3. Derive the factor-2 guarantee.
4. Run `vertex_cover_2approx` on a path, a cycle, a star, a clique of four
   vertices, an isolated vertex, and a self-loop.
5. Use `vertex_cover_fpt` or exhaustive search to find each small optimum and
   check the ratio.
6. Give an instance on which the algorithm can return twice optimum under an
   unfavorable edge order.
7. Explain why observed ratios below 2 do not strengthen the theorem.

### Hint

The matching is a lower-bound certificate for optimum cover size.

## E0.15.11 Amplify randomized decision procedures

- **Type:** probability and critique
- **Difficulty:** 4
- **Objective:** 8
- **Estimated time:** 50-75 minutes

### Problem

An RP algorithm never accepts a NO instance and accepts a YES instance with
probability at least $1/2$ per independent run.

1. If you repeat it $r$ times and accept if any run accepts, derive the false-
   rejection bound.
2. Choose the smallest $r$ making this bound at most $10^{-6}$.
3. Explain why independence matters.
4. State the dual aggregation for coRP.
5. Explain why "accept if any accepts" is not sound amplification for a BPP
   procedure with two-sided error.
6. Design a seeded simulation that compares empirical RP failure with the bound,
   and list what the experiment cannot prove.
7. Contrast random answer error with randomized running time.

### Hint

All $r$ runs miss a YES witness with probability at most $(1/2)^r$.

## E0.15.12 Design a hardness response for AI

- **Type:** applied synthesis
- **Difficulty:** 5
- **Objective:** 8, 9
- **Estimated time:** 90-150 minutes

### Problem

An AI planner receives a weighted state-transition graph, start state, goal
condition, hard constraints, and budget $B$. The general decision question asks
whether a valid plan of cost at most $B$ exists. A proposed plan can be checked
in polynomial time, and a documented reduction establishes NP-completeness.

Prepare an engineering memo that:

1. fixes the encoding, decision, search, and optimization interfaces;
2. states exactly what NP-completeness implies, conditionally on $P\ne NP$;
3. identifies at least three structural parameters and how each could support an
   FPT or special-case method;
4. proposes one exact method, one relaxation or approximation strategy, and one
   heuristic, keeping their guarantees separate;
5. decides whether randomization changes correctness, runtime, or both;
6. defines certificate and incumbent checks that every returned plan must pass;
7. designs benchmarks across instance size, parameter values, and distributions;
8. states timeout semantics and what must be returned when no plan is found;
9. names one claim that the evidence cannot support;
10. explains why the hardness result guides architecture without making the
    project pointless.

### Hint

Use a table with columns for method, scope, guarantee, failure status, parameter,
and evidence. Never translate timeout into infeasibility without a proof bound.

---

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)
