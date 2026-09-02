# Exercises for §0.07 Induction, Recursion, and Invariants

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Hints become progressively more specific without replacing the proof. Difficulty follows the project's 1 through 5 scale.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.07.01 | Plan an induction and align its base | planning and critique | 2 | state predicates, domains, bases, and steps | 30 min |
| E0.07.02 | Prove identities by weak induction | proof | 3 | carry algebra through an inductive step | 40 min |
| E0.07.03 | Cover multiple bases and step sizes | proof and critique | 3 | match bases to recursive reachability | 40 min |
| E0.07.04 | Use strong induction on smaller parts | proof | 4 | apply all-smaller hypotheses to decompositions | 45 min |
| E0.07.05 | Build a least-counterexample proof | proof and critique | 4 | establish and minimize a counterexample set | 45 min |
| E0.07.06 | Follow constructors with structural induction | proof | 4 | use one case per constructor and one IH per child | 50 min |
| E0.07.07 | Audit recursive definitions and termination | derivation and critique | 4 | prove coverage, unambiguity, and decrease | 50 min |
| E0.07.08 | Prove a state-machine invariant | proof and implementation | 4 | separate initialization, preservation, and safety | 50 min |
| E0.07.09 | Design loop invariants and prove correctness | proof and implementation | 4 | connect maintenance, exit, and termination | 55 min |
| E0.07.10 | Solve linear recurrences by characteristic roots | derivation | 4 | handle distinct and repeated roots | 55 min |
| E0.07.11 | Apply and refuse the Master Theorem | analysis and critique | 4 | check every theorem hypothesis | 55 min |
| E0.07.12 | Implement, experiment, and audit sources | implementation and critique | 5 | test claims without overstating evidence | 75 min |

## E0.07.01 Plan an induction and align its base

- **Type:** planning and critique
- **Difficulty:** 2
- **Objective:** State the predicate, quantified domain, base cases, inductive hypothesis, step target, and conclusion before proving.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper; module obligation diagrams.
- **Assumptions:** Natural numbers begin at $0$. Do not complete the algebraic proofs.

### Problem

For each claim, write an induction ledger with columns `Predicate`, `Domain`, `Base obligation`, `Arbitrary step index`, `Inductive hypothesis`, `Step target`, and `Conclusion`.

1. For every $n\ge0$, $\sum_{i=0}^{n}(2i+1)=(n+1)^2$.
2. For every $n\ge3$, $2^n>n$.
3. For every even $n\ge0$, $3^n-1$ is divisible by $8$.
4. A sequence satisfies $a_0=2$, $a_1=3$, and $a_{n+2}=a_{n+1}+2a_n$. Plan a proof of $a_n\le3^n$.
5. Every full binary tree satisfies $L(t)=N(t)+1$.

Then audit these proposals:

6. Item 2 uses base $n=0$ and a step valid only for $k\ge3$.
7. Item 3 uses step $P(k)\implies P(k+2)$ but claims every natural number.
8. Item 4 checks only $a_0$ and assumes only the bound for $a_k$ in the step.
9. Item 5 says "induct on the number of leaves" but supplies one hypothesis for only the left child.
10. Explain why writing "assume the theorem for all $n$" would be circular while assuming $P(k)$ inside the step is not.

**Deliverable:** Five ledgers and a diagnosis with the smallest repair for each broken proposal.

<details>
<summary>Hint 1</summary>

Align the first base with the theorem's lower bound. A step of size two reaches one residue class from one base.
</details>

<details>
<summary>Hint 2</summary>

A second-order recurrence step needs bounds for two preceding terms. A binary-tree constructor has two recursive children.
</details>

## E0.07.02 Prove identities by weak induction

- **Type:** proof
- **Difficulty:** 3
- **Objective:** Write complete weak-induction proofs and identify the exact use of each inductive hypothesis.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper; Python standard library only for finite checks after proving.
- **Assumptions:** Use ordinary integer algebra and finite-sum notation from §0.01.

### Problem

Prove all three claims by weak induction.

1. For every $n\ge0$,
   $$
   \sum_{i=0}^{n}(2i+1)=(n+1)^2.
   $$
2. For every $n\ge1$,
   $$
   1+3+3^2+\cdots+3^n=\frac{3^{n+1}-1}{2}.
   $$
3. For every $n\ge1$, $5\mid(6^n-1)$.

For each proof:

4. name the predicate and lower bound;
5. label the base, arbitrary $k$, inductive hypothesis, step target, and conclusion;
6. mark the first line that uses the hypothesis;
7. verify cases through $n=20$ with exact integer arithmetic;
8. state why the finite verification is not the universal proof;
9. mutate one sign or index in the proposed formula and report the first finite failure.

**Deliverable:** Three complete proofs, executable assertions, and an evidence-boundary note.

<details>
<summary>Hint 1</summary>

Split the final term from each sum. For divisibility, rewrite $6^{k+1}-1$ using $6(6^k-1)+5$.
</details>

<details>
<summary>Hint 2</summary>

For item 2, the next geometric term is $3^{k+1}$ when the current formula ends at exponent $k$.
</details>

## E0.07.03 Cover multiple bases and step sizes

- **Type:** proof and critique
- **Difficulty:** 3
- **Objective:** Determine which base cases a larger step or recurrence requires and prove every intended residue class is reached.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper; a short Python reachability check.
- **Assumptions:** Stamp counts are nonnegative integers.

### Problem

1. Prove that every integer $n\ge18$ can be written as $4a+7b$ for $a,b\in\mathbb{N}$.
2. Use bases $18,19,20,21$ and the step from $k$ to $k+4$.
3. Explain why bases $18$ and $19$ alone do not support that step for every $n\ge18$.
4. Identify the residue class reached from each base.
5. Give a valid induction for a theorem only about integers congruent to $2$ modulo $4$ using one base and step size four.
6. Let $a_0=1$, $a_1=2$, and $a_{n+2}=2a_{n+1}+a_n$. Prove $a_n<3^{n+1}$ using two base cases and two hypotheses in the step.
7. Audit a draft that proves bases $0,1$ for a third-order recurrence and then assumes three prior claims.
8. Implement a finite graph whose edges are $k\to k+4$ and verify which values through $50$ are reachable from each proposed base set.
9. Explain which part of the general proof is represented by the finite graph and which part remains symbolic.

**Deliverable:** Two proofs, residue-class audit, executable reachability check, and limitations.

<details>
<summary>Hint 1</summary>

Find explicit stamp expressions for four consecutive values. Adding one $4$-stamp preserves representability.
</details>

<details>
<summary>Hint 2</summary>

For the recurrence bound, use $2\cdot3^{k+1}+3^k<3^{k+2}$ after applying both hypotheses.
</details>

## E0.07.04 Use strong induction on smaller parts

- **Type:** proof
- **Difficulty:** 4
- **Objective:** Use strong induction when the current object decomposes into arbitrary smaller parts.
- **Estimated time:** 45 minutes
- **Allowed tools:** Pencil and paper; no prime-factorization library.
- **Assumptions:** An integer $n\ge2$ is composite exactly when $n=ab$ for integers $2\le a,b<n$.

### Problem

1. Prove by strong induction that every integer $n\ge2$ is a product of primes.
2. State why both factors lie inside the strong-hypothesis range.
3. Define $q(n)$ as the minimum number of moves needed to reduce $n$ to $1$ when a move subtracts $1$ or, if even, divides by $2$. Prove by strong induction that $q(n)$ exists for every $n\ge1$.
4. Prove that $q(n)\le n-1$.
5. Explain why the division branch naturally asks for $P(n/2)$ rather than $P(n-1)$.
6. Convert the prime-product proof to weak induction by defining a cumulative predicate $Q(n)$ that contains every earlier case.
7. Identify the base details hidden when strong induction is stated as one all-smaller step.
8. Explain why strong induction is equivalent to weak induction over $\mathbb{N}$ but may produce a shorter proof.
9. Give one invalid strong-induction step that includes the current case in its hypothesis and diagnose the circularity.

**Deliverable:** Two strong-induction proofs, one weak-induction reformulation, and a scope audit.

<details>
<summary>Hint 1</summary>

For the existence of $q(n)$, it is enough that every allowed recursive choice leads to a smaller positive integer and that at least one move is available.
</details>

<details>
<summary>Hint 2</summary>

Use $Q(n)=\forall j\,(2\le j\le n\implies P(j))$ for the weak-induction reformulation.
</details>

## E0.07.05 Build a least-counterexample proof

- **Type:** proof and critique
- **Difficulty:** 4
- **Objective:** Negate a universal claim, establish a nonempty counterexample set, choose its least member, and use minimality legally.
- **Estimated time:** 45 minutes
- **Allowed tools:** Pencil and paper; §0.06 contradiction guidance.
- **Assumptions:** Use the well-ordering principle for nonempty subsets of $\mathbb{N}$.

### Problem

1. Prove by least counterexample that every integer $n\ge24$ can be written as $5a+7b$ for $a,b\in\mathbb{N}$.
2. Define the counterexample set before choosing its minimum.
3. Establish directly that $24,25,26,27,28$ are representable.
4. Explain why the least counterexample must be at least $29$.
5. Use subtraction by $5$ and minimality to obtain the contradiction.
6. Rewrite the proof as strong induction and compare the obligations.
7. Prove from well-ordering that ordinary induction is valid, at proof-sketch level.
8. Prove from ordinary induction that every nonempty subset of $\mathbb{N}$ has a least element, at proof-sketch level.
9. Audit: "Let $m$ be the least counterexample. If there are none, we are done." Explain the logical order problem.
10. Audit: choose a least positive real counterexample from a nonempty subset of $(0,1)$. Explain why natural-number well-ordering cannot justify it.

**Deliverable:** Complete least-counterexample proof, strong-induction version, equivalence sketches, and two diagnoses.

<details>
<summary>Hint 1</summary>

The negation of the universal claim supplies nonemptiness. Five consecutive bases cover every residue modulo five.
</details>

<details>
<summary>Hint 2</summary>

If $m\ge29$, then $m-5\ge24$. Minimality says $m-5$ is representable.
</details>

## E0.07.06 Follow constructors with structural induction

- **Type:** proof
- **Difficulty:** 4
- **Objective:** Follow all constructors of recursive data and use one inductive hypothesis for every recursive child.
- **Estimated time:** 50 minutes
- **Allowed tools:** Pencil and paper; Python standard library for structural tests.
- **Assumptions:** Lists and full binary expression trees use the constructors stated in the module.

### Problem

1. Prove by structural induction on list `xs` that
   $$
   reverse(xs\mathbin{+\!+}ys)=reverse(ys)\mathbin{+\!+}reverse(xs).
   $$
2. State the recursive definitions of append and reverse used by your proof.
3. For expression trees with `Number`, `Add`, and `Multiply`, prove that the number of nodes is odd.
4. Prove $size(t)=2L(t)-1$ for every full binary expression tree.
5. Mark the two independent hypotheses in each binary-constructor case.
6. Extend the syntax with unary `Negate(child)`. State how the odd-size theorem changes and add the required structural case.
7. Give a tree with unary negation showing the original odd-size theorem is false.
8. Contrast the structural proof of item 4 with strong induction on numeric tree size.
9. Extend the module's dataclasses and finite generator with `Negate`, then test your repaired size claim through depth two.
10. Explain why passing generated tests is not the structural proof.

**Deliverable:** Three structural proofs or repairs, constructor ledger, executable tests, and limitations.

<details>
<summary>Hint 1</summary>

For reverse of `cons(x, xs)`, use a one-element list appended after `reverse(xs)`.
</details>

<details>
<summary>Hint 2</summary>

A unary constructor changes size by one, so parity alternates. A universally valid repaired claim can track size modulo two together with the number of unary nodes.
</details>

## E0.07.07 Audit recursive definitions and termination

- **Type:** derivation and critique
- **Difficulty:** 4
- **Objective:** Check base clauses, recursive clauses, coverage, unambiguity, and a strictly decreasing nonnegative measure.
- **Estimated time:** 50 minutes
- **Allowed tools:** Pencil and paper; Python standard library for executable variants.
- **Assumptions:** Inputs are integers in the domains stated for each definition.

### Problem

Audit each proposed definition.

1. $f(0)=1$ and $f(n)=nf(n-1)$ for $n\ge1$.
2. $g(n)=g(n+1)-1$ for $n\ge0$.
3. $h(0)=0$, $h(2n)=h(n)+1$, and $h(2n+1)=h(n)+1$ for $n\ge0$.
4. $r(0)=0$, $r(1)=1$, and $r(n)=r(n-1)+r(n-2)$ for $n\ge1$.
5. $d(a,0)=a$ and $d(a,b)=d(b,a\bmod b)$ for $a\ge0,b>0$.

For each:

6. report coverage and clause overlap;
7. state whether overlap is consistent;
8. propose a natural-valued decreasing measure for every recursive call, or show why none of the obvious argument measures decreases;
9. repair every invalid or ambiguous definition with the smallest clear change;
10. distinguish mathematical termination from Python's recursion limit;
11. implement factorial and Euclidean gcd recursively and iteratively, with assertions that every recursive measure decreases;
12. state the correctness invariant for Euclidean gcd separately from its termination measure.

**Deliverable:** Five-row audit table, repaired definitions, termination proofs, executable implementations, and a correctness/termination distinction.

<details>
<summary>Hint 1</summary>

Check item 3 at zero and item 4 at $n=1$. Overlapping clauses may disagree or call themselves without decrease.
</details>

<details>
<summary>Hint 2</summary>

For gcd, the next second argument is a remainder strictly smaller than the current positive second argument.
</details>

## E0.07.08 Prove a state-machine invariant

- **Type:** proof and implementation
- **Difficulty:** 4
- **Objective:** Separate reachable states, initialization, preservation, safety consequence, invariant strength, and termination.
- **Estimated time:** 50 minutes
- **Allowed tools:** Pencil and paper; Python standard library for bounded reachability.
- **Assumptions:** The machine state is $(x,y)\in\mathbb{Z}^2$, starts at $(0,0)$, and uses the transitions below.

### Problem

Transitions are

$$
A:(x,y)\to(x+2,y+1),
$$

$$
B:(x,y)\to(x+1,y+2).
$$

1. Prove that $x+y$ is divisible by $3$ in every reachable state.
2. Prove that $x,y\ge0$ is also invariant.
3. Use the invariants to prove safety property $x+y\ne10$.
4. Give an unreachable state satisfying both invariants.
5. Explain why invariant satisfaction does not imply reachability.
6. Show that $x-y$ being even is not invariant by identifying initialization or preservation failure.
7. Add a terminal condition $x+y\ge12$. Prove that every execution choosing either transition terminates.
8. Name a decreasing natural-valued variant for the terminal machine.
9. Implement bounded breadth-first reachability and return the first reachable counterexample to each candidate predicate.
10. Mutate transition $B$ to $(x+1,y+1)$ and show which proof obligation fails.
11. State exactly what the bounded search proves.

**Deliverable:** Invariant and safety proofs, termination proof, unreachable witness, mutation diagnosis, executable checker, and limitations.

<details>
<summary>Hint 1</summary>

Each original transition increases $x+y$ by three. Safety follows because ten is not divisible by three.
</details>

<details>
<summary>Hint 2</summary>

For termination, use a clipped remaining-distance measure such as $\max(0,12-(x+y))$ and analyze nonterminal steps.
</details>

## E0.07.09 Design loop invariants and prove correctness

- **Type:** proof and implementation
- **Difficulty:** 4
- **Objective:** Prove initialization, maintenance, exit-to-postcondition, and termination for two loops.
- **Estimated time:** 55 minutes
- **Allowed tools:** Pencil and paper; Python 3 standard library with assertions.
- **Assumptions:** Inputs are finite Python sequences; arithmetic uses mathematical integers as modeled by Python integers.

### Problem

1. Write a loop returning $\sum_{j=0}^{n-1}(2j+1)$ for $n\ge0$.
2. Use invariant
   $$
   total=i^2
   \quad\text{and}\quad
   0\le i\le n.
   $$
3. Prove initialization, maintenance, postcondition at exit, and termination.
4. Implement the loop with assertions at the loop head and after exit.
5. Write a loop returning the first index of the minimum value in a nonempty list.
6. Propose an invariant describing the processed prefix and tie-breaking rule.
7. Prove initialization, maintenance, returned postcondition, and termination.
8. Explain why "the current candidate is a minimum" is too vague unless its comparison domain is named.
9. Mutate the update from `<` to `<=`. State how the tie-breaking postcondition changes.
10. Give a loop that preserves a safety invariant but never terminates, and identify why partial correctness is not total correctness.
11. Test both implementations on boundaries, duplicates, and negative integers.

**Deliverable:** Two complete correctness proofs, executable asserted loops, mutation analysis, and one nontermination counterexample.

<details>
<summary>Hint 1</summary>

The odd-number update is $(i+1)^2-i^2=2i+1$.
</details>

<details>
<summary>Hint 2</summary>

For first minimum, after processing `values[:i]`, keep the earliest index whose value equals the minimum of that prefix.
</details>

## E0.07.10 Solve linear recurrences by characteristic roots

- **Type:** derivation
- **Difficulty:** 4
- **Objective:** Derive characteristic polynomials, handle distinct and repeated roots, use all initial conditions, and verify residuals.
- **Estimated time:** 55 minutes
- **Allowed tools:** Pencil and paper; Python standard library for exact verification.
- **Assumptions:** Recurrences hold for $n\ge2$ and initial indices are $0,1$.

### Problem

Solve each recurrence.

1. $a_n=4a_{n-1}-3a_{n-2}$, with $a_0=2,a_1=4$.
2. $b_n=8b_{n-1}-16b_{n-2}$, with $b_0=1,b_1=8$.
3. $c_n=2c_{n-1}+3c_{n-2}$, with $c_0=0,c_1=4$.
4. Derive Binet's formula for Fibonacci numbers from the two characteristic roots.
5. For each, write the ansatz, polynomial, roots with multiplicity, general family, initial-condition system, and final formula.
6. Substitute each formula into both the recurrence and initial conditions.
7. Explain why item 2 needs a factor of $n$.
8. Show that omitting one initial condition leaves one free parameter.
9. Implement exact generators and assert zero residuals through $n=40$.
10. Compare exact Fibonacci recurrence values with floating Binet values and state why irrational cancellation is exact mathematically but approximate numerically.
11. Diagnose the sign error produced by writing $r^2-2r+3$ for item 3.

**Deliverable:** Four derivations, exact residual tests, floating-point limitation note, and sign audit.

<details>
<summary>Hint 1</summary>

The characteristic polynomial for $x_n=p x_{n-1}+q x_{n-2}$ is $r^2-pr-q$.
</details>

<details>
<summary>Hint 2</summary>

Item 2 has $(r-4)^2$. Item 3 has roots $3$ and $-1$.
</details>

## E0.07.11 Apply and refuse the Master Theorem

- **Type:** analysis and critique
- **Difficulty:** 4
- **Objective:** Check recurrence form, constants, polynomial separation, regularity, base assumptions, and theorem limits.
- **Estimated time:** 55 minutes
- **Allowed tools:** Pencil and paper; module theorem statement; exact Python level-work tables.
- **Assumptions:** For applicable recurrences, use powers of $b$, suppress rounding, and assume $T(1)=\Theta(1)$.

### Problem

For each recurrence, decide whether the basic Master Theorem applies. If it does, identify $a,b,f(n),p=\log_ba$, the case, every side condition, and the result. If it does not, identify the first failed hypothesis without guessing a bound.

1. $T(n)=9T(n/3)+n$.
2. $T(n)=3T(n/3)+n$.
3. $T(n)=3T(n/3)+n^2$.
4. $T(n)=T(n/4)+\sqrt n$.
5. $T(n)=T(n/3)+T(2n/3)+n$.
6. $T(n)=nT(n/2)+n$.
7. $T(n)=2T(n/2)+n/\log n$.
8. $T(n)=2T(n/2)-n$.
9. Use the oscillating $f$ from Worked example 24 and demonstrate failure of regularity.
10. For every applicable case 3, compute a valid constant $c<1$.
11. Build level-work tables for items 1 through 4 and compare their geometric trends with the theorem result.
12. Explain why a recursion tree is intuition and why empirical level ratios are not a proof of $\Theta$ bounds.
13. State how floors and ceilings were suppressed and why an actual algorithm analysis must account for them or cite a version that does.

**Deliverable:** Applicability table, four complete theorem applications, five refusal diagnoses, level-work code, and limitations.

<details>
<summary>Hint 1</summary>

Compare $f(n)$ with $n^{\log_ba}$ by a polynomial factor, not by which expression merely looks larger.
</details>

<details>
<summary>Hint 2</summary>

For item 4, $p=0$ and $f(n)=n^{1/2}$. Check $f(n/4)/f(n)$ for regularity.
</details>

## E0.07.12 Implement, experiment, and audit sources

- **Type:** implementation and critique
- **Difficulty:** 5
- **Objective:** Integrate recursive correctness, memoization, invariant checks, recurrence verification, empirical limits, and direct source inspection.
- **Estimated time:** 75 minutes
- **Allowed tools:** Python 3 standard library; directly opened module sources. No third-party packages and no generated summary as evidence.
- **Assumptions:** Execute the lesson's code fences in document order before reusing their helpers.

### Problem

Build one reproducible audit script or literate report that does all of the following:

1. compare recursive and iterative factorial for $0\le n\le100$;
2. count naive Fibonacci body entries through $n=30$;
3. clear `fibonacci_cached` before each trial and record misses, hits, and current cache size;
4. explain why cached body counts are misses rather than all wrapper calls;
5. verify every Euclidean gcd remainder strictly decreases and compare results with `math.gcd`;
6. generate expression trees through depth two and verify evaluation plus structural size properties;
7. check both a valid and invalid invariant on a bounded reachable state graph and return a counterexample for the invalid one;
8. run the loop-invariant assertions from E0.07.09 on boundary and duplicate cases;
9. verify all formulas from E0.07.10 by initial values and recurrence residuals;
10. produce level-work tables for one recurrence in each Master case;
11. trigger or safely demonstrate the practical recursion-limit issue without changing the global limit;
12. explain why recursion depth is not mathematical nontermination;
13. audit this claim: "Memoization makes every recursion polynomial, invariant checks prove all executions safe, and matching empirical ratios prove a Master-Theorem bound." Identify at least six errors or missing assumptions;
14. directly inspect the Python `functools.cache` and recursion-limit documentation, Cornell's Master-method notes, MIT 6.042J's reading index, and *Mathematics in Lean* Chapter 5;
15. record a source ledger with URL, access date, exact supported claim, and reuse boundary;
16. confirm that no source example or exercise was copied into the report.

**Deliverable:** Executable report, results table, six-part claim audit, source ledger, and limitations.

<details>
<summary>Hint 1</summary>

`cache_clear()` resets stored entries and statistics. Compare `cache_info()` before and after each call.
</details>

<details>
<summary>Hint 2</summary>

Separate mathematical proof, exhaustive finite checking, sampled measurement, software documentation, and licensing into different evidence rows.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that your work includes:

- an explicit predicate and quantified domain for every induction;
- bases aligned with the lower bound and step size;
- only earlier cases inside every inductive hypothesis;
- a nonempty counterexample set before a least element is chosen;
- one structural case per constructor and one hypothesis per recursive child;
- coverage, unambiguity, and a decreasing measure for recursive definitions;
- enough initial values for each recurrence order;
- characteristic-root multiplicities handled correctly;
- initialization, preservation, safety, exit, and termination kept distinct;
- every Master-Theorem hypothesis checked before naming a case;
- finite and empirical evidence limited to the declared domain;
- directly opened sources tied to exact claims.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)
