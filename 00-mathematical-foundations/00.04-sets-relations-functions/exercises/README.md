# Exercises for §0.04 Sets, Relations, and Functions

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Hints become progressively more specific but do not state final answers. Difficulty follows the project's 1 through 5 scale.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.04.01 | Separate members from subsets | conceptual | 2 | distinguish membership and containment | 20 min |
| E0.04.02 | Prove identities by membership | proof | 3 | use extensionality and set laws | 30 min |
| E0.04.03 | Build products, power sets, and tagged unions | calculation | 2 | construct finite set structures | 25 min |
| E0.04.04 | Classify finite relations | derivation | 3 | diagnose relation properties | 35 min |
| E0.04.05 | Move between equivalence relations and partitions | proof | 3 | prove the correspondence | 35 min |
| E0.04.06 | Read a divisibility poset | visual proof | 3 | analyze orders, chains, and extrema | 35 min |
| E0.04.07 | Audit images and preimages | proof and counterexample | 3 | derive exact mapping laws | 35 min |
| E0.04.08 | Design and invert functions | derivation | 3 | classify mappings and inverses | 30 min |
| E0.04.09 | Implement a relation-property checker | implementation | 4 | verify finite relations exhaustively | 50 min |
| E0.04.10 | Enumerate rationals without duplicates | experiment | 4 | construct a countable enumeration | 50 min |
| E0.04.11 | Diagonalize a proposed enumeration | proof | 4 | prove Cantor-style uncountability | 40 min |
| E0.04.12 | Audit Russell's paradox and its sources | critique | 4 | separate bounded notation from comprehension | 45 min |

## E0.04.01 Separate members from subsets

- **Type:** conceptual
- **Difficulty:** 2
- **Objective:** Distinguish membership, singleton containment, proper containment, and empty-set edge cases.
- **Estimated time:** 20 minutes
- **Allowed tools:** Pencil and paper; module notation table.
- **Assumptions:** Treat numerals as ordinary numbers, not von Neumann set encodings.

### Problem

Let

$$
A=\{1,\{1\},\{1,2\},\varnothing\},
\qquad
B=\{1,2\}.
$$

1. Classify each statement as true or false:
   $$
   1\in A,
   \quad
   1\subseteq A,
   \quad
   \{1\}\in A,
   \quad
   \{1\}\subseteq A,
   $$
   $$
   B\in A,
   \quad
   B\subseteq A,
   \quad
   \varnothing\in A,
   \quad
   \varnothing\subseteq B.
   $$
2. State whether $\{\varnothing\}\subseteq A$ and whether $\{\varnothing\}\in A$.
3. List every member of $\mathcal{P}(B)$ and classify $1\in\mathcal{P}(B)$ versus $\{1\}\in\mathcal{P}(B)$.
4. Prove from the definition that $x\in S$ if and only if $\{x\}\subseteq S$.
5. Give one set $C$ for which $\varnothing\subseteq C$ but $\varnothing\notin C$, and one for which both statements are true.

**Deliverable:** A truth table with a one-sentence justification per row, the power set, and the short equivalence proof.

<details>
<summary>Hint 1</summary>

For $X\subseteq A$, inspect every member of $X$. For $X\in A$, inspect the objects listed directly inside $A$.
</details>

<details>
<summary>Hint 2</summary>

The only member of $\{x\}$ is $x$. The empty set has no member that can violate a subset condition.
</details>

## E0.04.02 Prove identities by membership

- **Type:** proof
- **Difficulty:** 3
- **Objective:** Prove set equalities by extensionality and track the ambient universe for complements.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper; no truth-table software.
- **Assumptions:** Let $A,B,C\subseteq U$. Complements are relative to $U$.

### Problem

Prove each identity by taking an arbitrary $x\in U$ and writing a chain of membership equivalences.

1. $(A\cap B)^c=A^c\cup B^c$.
2. $A\setminus(B\cap C)=(A\setminus B)\cup(A\setminus C)$.
3. $A\mathbin{\triangle}B=(A\cup B)\setminus(A\cap B)$.
4. For an indexed family $(A_i)_{i\in I}$,
   $$
   \left(\bigcup_{i\in I}A_i\right)^c
   =\bigcap_{i\in I}A_i^c.
   $$
5. Explain why the indexed proof still works when $I=\varnothing$ under
   $$
   \bigcup_{i\in\varnothing}A_i=\varnothing,
   \qquad
   \bigcap_{i\in\varnothing}A_i=U.
   $$
6. Find a counterexample to the false identity $A\setminus(B\cup C)=(A\setminus B)\cup(A\setminus C)$.

**Deliverable:** Four extensional proofs, an empty-index explanation, and one explicit finite counterexample.

<details>
<summary>Hint 1</summary>

Translate union to "or," intersection to "and," complement to "not," and difference to "in the first and not in the second."
</details>

<details>
<summary>Hint 2</summary>

For the indexed identity, "not in any $A_i$" means "for every $i$, not in $A_i$." For the counterexample, try one element that belongs to $B$ but not $C$.
</details>

## E0.04.03 Build products, power sets, and tagged unions

- **Type:** calculation
- **Difficulty:** 2
- **Objective:** Construct and count Cartesian products, power sets, sequences, and tagged disjoint unions.
- **Estimated time:** 25 minutes
- **Allowed tools:** Pencil and paper; Python standard library for verification only.
- **Assumptions:** Ordered pairs and tags are compared componentwise.

### Problem

Let $A=\{a,b\}$ and $B=\{b,c,d\}$.

1. List $A\times B$ and $B\times A$. State their cardinalities and whether they are equal.
2. List $\mathcal{P}(A)$ and $\mathcal{P}(A\times\{0\})$.
3. Compute $A\cup B$ and explain which source information is lost.
4. Construct
   $$
   A\sqcup B=(A\times\{0\})\cup(B\times\{1\})
   $$
   and list all members.
5. Compare $|A\cup B|$ with $|A\sqcup B|$ and explain the difference.
6. List every length-$2$ sequence in $A$ by treating it as a function from $\{0,1\}$ to $A$. Compare this set with $\mathcal{P}(A)$.
7. Prove for finite $X,Y$ that $|X\sqcup Y|=|X|+|Y|$, even when $X\cap Y\ne\varnothing$.

**Deliverable:** Explicit rosters, cardinalities, and a short injective-tag argument.

<details>
<summary>Hint 1</summary>

A product records coordinate order. A power set contains subsets. A length-$2$ sequence permits repetition.
</details>

<details>
<summary>Hint 2</summary>

In the tagged union, the left and right parts are disjoint because no ordered pair can have both tag $0$ and tag $1$.
</details>

## E0.04.04 Classify finite relations

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Classify reflexive, irreflexive, symmetric, antisymmetric, asymmetric, and transitive relations using witnesses.
- **Estimated time:** 35 minutes
- **Allowed tools:** Pencil and paper; code only after hand classification.
- **Assumptions:** Every relation is on the explicitly stated base set.

### Problem

Let $A=\{1,2,3\}$. Classify each relation for all six properties.

$$
R_1=\{(1,1),(2,2),(3,3)\},
$$

$$
R_2=\{(1,2),(2,1)\},
$$

$$
R_3=\{(1,2),(2,3),(1,3)\},
$$

$$
R_4=\{(1,1),(2,2),(3,3),(1,2),(2,1)\},
$$

$$
R_5=\{(1,2),(2,3)\}.
$$

1. Produce one row per relation and one column per property.
2. For every failed property, provide a specific missing pair, reverse pair, diagonal pair, or triple witness.
3. Identify every equivalence relation and every partial order.
4. Explain why $R_1$ is both symmetric and antisymmetric but not asymmetric.
5. Explain why $R_3$ is asymmetric and also antisymmetric.
6. Add the fewest pairs to $R_5$ to make it transitive, then separately add the fewest pairs to make it reflexive and transitive.

**Deliverable:** Classification table, witness ledger, and both repaired versions of $R_5$.

<details>
<summary>Hint 1</summary>

Reflexivity checks all three diagonal pairs. Transitivity checks only composable pairs whose middle coordinates agree.
</details>

<details>
<summary>Hint 2</summary>

For antisymmetry, seek distinct elements related in both directions. For asymmetry, even a diagonal pair causes failure.
</details>

## E0.04.05 Move between equivalence relations and partitions

- **Type:** proof
- **Difficulty:** 3
- **Objective:** Construct equivalence classes and prove both directions of the equivalence-relation and partition correspondence.
- **Estimated time:** 35 minutes
- **Allowed tools:** Pencil and paper.
- **Assumptions:** $A$ is nonempty. A partition contains nonempty blocks whose union is $A$ and whose distinct blocks are disjoint.

### Problem

Let $A=\{0,1,2,3,4,5,6,7\}$ and define $aRb$ when $a\equiv b\pmod 3$.

1. Prove that $R$ is an equivalence relation on $A$.
2. Compute every distinct equivalence class and write $A/R$.
3. Verify directly that the classes form a partition.
4. Prove in general that if $R$ is an equivalence relation, then two classes $[a]_R$ and $[b]_R$ are equal or disjoint.
5. Starting with an arbitrary partition $\Pi$ of a set $X$, define $x\sim_\Pi y$ by shared block and prove reflexivity, symmetry, and transitivity.
6. Show that applying both constructions to the concrete modulo-$3$ example returns the original partition and relation.
7. Explain why overlapping community labels do not define a partition, while a single hard cluster label per item does.

**Deliverable:** Concrete quotient, two general proofs, and a precise clustering interpretation.

<details>
<summary>Hint 1</summary>

For transitivity of congruence, write $3\mid(a-b)$ and $3\mid(b-c)$ and add the differences.
</details>

<details>
<summary>Hint 2</summary>

If two equivalence classes share $z$, use symmetry and transitivity to relate their representatives. If two partition blocks share $y$, disjointness forces them to be the same block.
</details>

## E0.04.06 Read a divisibility poset

- **Type:** visual proof
- **Difficulty:** 3
- **Objective:** Analyze partial orders, Hasse diagrams, chains, antichains, and extremal elements.
- **Estimated time:** 35 minutes
- **Allowed tools:** Pencil and paper or Mermaid for the diagram; no graph-layout library.
- **Assumptions:** Let $D$ be the positive divisors of $36$, ordered by divisibility.

### Problem

1. List $D$ and prove that divisibility is a partial order on it.
2. Determine whether the order is total and provide an incomparable pair if not.
3. Draw the Hasse diagram. Use upward paths for divisibility and omit reflexive and transitive edges.
4. Give one chain containing at least four elements.
5. Give one antichain containing at least three elements, or prove that no such antichain exists.
6. Identify the least, greatest, minimal, and maximal elements of $D$.
7. Repeat the extremal analysis for
   $$
   S=\{2,3,4,6,9,12,18\}\subseteq D.
   $$
8. Explain why a minimal element of $S$ need not be least and why a maximal element need not be greatest.
9. Interpret a Hasse edge as an immediate dependency and state why transitive edges should be omitted from the drawing but not from the order.

**Deliverable:** Accessible Hasse diagram, proofs, chain and antichain, and two extremal-element tables.

<details>
<summary>Hint 1</summary>

The divisors are $1,2,3,4,6,9,12,18,36$. A cover $a\prec b$ has no listed divisor strictly between them.
</details>

<details>
<summary>Hint 2</summary>

For $S$, inspect which elements have no smaller or larger comparable member inside $S$. Then test whether any one candidate compares in the required direction with every element.
</details>

## E0.04.07 Audit images and preimages

- **Type:** proof and counterexample
- **Difficulty:** 3
- **Objective:** Derive exact image and preimage laws and identify the role of injectivity.
- **Estimated time:** 35 minutes
- **Allowed tools:** Pencil and paper; a finite exhaustive search for verification.
- **Assumptions:** Let $f:A\to B$, $S_1,S_2\subseteq A$, and $T_1,T_2\subseteq B$.

### Problem

1. Prove
   $$
   f^{-1}(T_1\cup T_2)=f^{-1}(T_1)\cup f^{-1}(T_2).
   $$
2. Prove
   $$
   f^{-1}(T_1\cap T_2)=f^{-1}(T_1)\cap f^{-1}(T_2).
   $$
3. Prove the relative-complement law
   $$
   f^{-1}(B\setminus T_1)=A\setminus f^{-1}(T_1).
   $$
4. Prove $f(S_1\cup S_2)=f(S_1)\cup f(S_2)$.
5. Prove only the always-valid direction
   $$
   f(S_1\cap S_2)\subseteq f(S_1)\cap f(S_2).
   $$
6. Construct the smallest finite counterexample you can to equality in part 5.
7. Prove equality in part 5 under the additional assumption that $f$ is injective.
8. For $f:\mathbb{Z}\to\mathbb{Z}$, $f(n)=n^2$, compute
   $$
   f^{-1}(\{0,1,4\}),
   \qquad
   f(\{-2,-1,0\}),
   $$
   and explain why the first expression is not an inverse function call.

**Deliverable:** Six membership proofs or inclusions, one minimal counterexample, and the concrete computations.

<details>
<summary>Hint 1</summary>

For preimages, begin with one input $x$ and unfold $f(x)\in T$. For images, membership introduces an input witness.
</details>

<details>
<summary>Hint 2</summary>

Strict image intersection needs two distinct inputs with the same output, with one input placed only in each source subset.
</details>

## E0.04.08 Design and invert functions

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Classify total and partial mappings, injectivity, surjectivity, bijectivity, restrictions, and inverses.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper.
- **Assumptions:** Function properties are evaluated relative to declared domains and codomains.

### Problem

For each declaration, classify injectivity and surjectivity. If bijective, derive the inverse. If not bijective, state the smallest natural restriction or codomain change that makes an inverse possible.

1. $f:\mathbb{Z}\to\mathbb{Z}$, $f(n)=n+3$.
2. $g:\mathbb{R}\to\mathbb{R}$, $g(x)=x^2$.
3. $h:[0,\infty)\to[0,\infty)$, $h(x)=x^2$.
4. $p:\mathbb{Z}\to\{0,1,2\}$, $p(n)$ is the remainder modulo $3$.
5. $q:\{0,1,2\}\to\mathbb{Z}$, $q(n)=n^2$.

Then answer:

6. Let $R=\{(0,a),(1,b),(2,b)\}$. Give a domain and codomain making $R$ a function graph, then classify it.
7. Add one pair to make $R$ fail the function condition, and remove one pair to make it represent a partial but not total function on the same domain.
8. Write the inverse relation $R^{-1}$ and explain whether it is a function graph.
9. Distinguish $h^{-1}(\{1,4\})$ as a preimage from $h^{-1}(4)$ as inverse-function evaluation.

**Deliverable:** Classification table, inverse derivations, and graph-relation analysis.

<details>
<summary>Hint 1</summary>

Surjectivity asks whether every declared codomain value is attained. The same assignment rule can change classification when the codomain changes.
</details>

<details>
<summary>Hint 2</summary>

The inverse relation is a function exactly when the original function is injective. It is total on the original codomain exactly when the original is surjective.
</details>

## E0.04.09 Implement a relation-property checker

- **Type:** implementation
- **Difficulty:** 4
- **Objective:** Implement exhaustive finite relation checks with useful counterexample witnesses.
- **Estimated time:** 50 minutes
- **Allowed tools:** Python 3 standard library only.
- **Assumptions:** Base sets are finite and contain hashable values. A relation is represented by a set of ordered pairs.

### Problem

Implement

```python
analyze_relation(base_set, relation)
```

returning for each property both a Boolean and either `None` or a witness.

Required properties:

- reflexive;
- irreflexive;
- symmetric;
- antisymmetric;
- asymmetric;
- transitive.

Required behavior:

1. Reject a relation containing a pair outside `base_set x base_set`.
2. For reflexivity failure, return a missing diagonal element.
3. For symmetry or asymmetry failure, return a pair and its reverse status.
4. For antisymmetry failure, return distinct elements related both ways.
5. For transitivity failure, return `(a, b, c)` with `aRb` and `bRc` but not `aRc`.
6. Test equality, strict less-than, non-strict less-than, congruence modulo $2$, and at least three hand-built relations on a base set with four elements.
7. Include assertions for every known trap: equality is symmetric and antisymmetric; $<$ is asymmetric; $\le$ is antisymmetric but not asymmetric; congruence is symmetric but not antisymmetric on a suitable set.
8. Compare predictions made before execution with output after execution.
9. State exactly what the finite exhaustive test proves and what it cannot prove about corresponding infinite relations.

**Deliverable:** Executable implementation, assertions, prediction table, witness report, and limitations.

<details>
<summary>Hint 1</summary>

Use `itertools.product(base_set, repeat=2)` for pairs and `repeat=3` for triples. A direct triple scan is acceptable for this small finite lab.
</details>

<details>
<summary>Hint 2</summary>

Return the first witness under a deterministic sorted order so failed tests are reproducible. Keep the witness separate from the Boolean result.
</details>

## E0.04.10 Enumerate rationals without duplicates

- **Type:** experiment
- **Difficulty:** 4
- **Objective:** Construct and test a duplicate-free enumeration of rational numbers.
- **Estimated time:** 50 minutes
- **Allowed tools:** Python 3 standard library only, including `fractions.Fraction` and `math.gcd`.
- **Assumptions:** Canonical pairs have positive denominator and coprime numerator magnitude and denominator.

### Problem

Design an enumeration by increasing height $|p|+q$, where $p\in\mathbb{Z}$ and $q\in\mathbb{N}_{>0}$.

1. Before coding, explain why raw pairs contain duplicates and why every diagonal of fixed height is finite.
2. Specify a deterministic within-height order, including how signs are ordered.
3. Emit only pairs satisfying $\gcd(|p|,q)=1$ and $q>0$.
4. Generate results through heights $4,8,16,32$.
5. At each height, report raw pair count, distinct `Fraction` count, emitted reduced count, and duplicates removed.
6. Assert that emitted values contain no duplicates and all denominators are positive.
7. Assert that outputs are nested as height increases.
8. For every raw pair through height $16$, verify that its normalized `Fraction` appears by the height of its reduced canonical pair.
9. State the proof that every rational appears exactly once in the infinite process.
10. Explain why the finite experiment illustrates but does not prove countability.
11. Compare filtering raw pairs with relying on a set of `Fraction` objects. State which approach makes the mathematical reason for uniqueness visible.

**Deliverable:** Hypothesis, method, executable assertions, result table, proof, controls, and limitations.

<details>
<summary>Hint 1</summary>

At height $H$, choose $q\in\{1,\ldots,H\}$ and set $|p|=H-q$. Emit zero once and nonzero numerators with both signs.
</details>

<details>
<summary>Hint 2</summary>

Every rational has a unique reduced representation $p/q$ with $q>0$. Its finite canonical height tells you when it appears.
</details>

## E0.04.11 Diagonalize a proposed enumeration

- **Type:** proof
- **Difficulty:** 4
- **Objective:** Prove Cantor's theorem, uncountability of binary sequences, and uncountability of the reals without representation ambiguity.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper; a finite Python prefix check for illustration only.
- **Assumptions:** Natural numbers begin at $0$. Infinite sequences are functions $\mathbb{N}\to\{0,1\}$.

### Problem

1. Suppose $s_0,s_1,s_2,\ldots$ is claimed to list every binary sequence. Define a sequence $t$ that differs from row $n$ at coordinate $n$ and prove $t$ is absent.
2. Explain why changing only one fixed coordinate would not suffice.
3. Prove that $\mathcal{P}(\mathbb{N})$ is bijective with $\{0,1\}^{\mathbb{N}}$.
4. For an arbitrary set $A$ and function $f:A\to\mathcal{P}(A)$, define
   $$
   D=\{a\in A:a\notin f(a)\}
   $$
   and prove $D$ is not in the range of $f$.
5. Give the singleton injection $A\to\mathcal{P}(A)$ and combine it with part 4 to state Cantor's theorem.
6. Explain the ambiguity in mapping binary sequences to $[0,1]$ by ordinary binary expansions. Give a concrete number with two expansions.
7. Define
   $$
   \Phi(s)=\sum_{n=0}^{\infty}\frac{2s(n)}{3^{n+1}}
   $$
   and prove injectivity by bounding the tail after the first differing digit.
8. Conclude that $[0,1]$ and $\mathbb{R}$ are uncountable without claiming that $\Phi$ is onto $[0,1]$.
9. Implement a $6\times6$ finite-prefix diagonal demonstration and explain why it is not the proof.

**Deliverable:** Three linked proofs, the representation warning, finite illustration, and limitations.

<details>
<summary>Hint 1</summary>

Set $t(n)=1-s_n(n)$. If $t$ were row $k$, compare the two sequences at coordinate $k$.
</details>

<details>
<summary>Hint 2</summary>

At the first ternary digit where two encoded sequences differ, the leading gap is $2/3^{k+1}$. The largest possible opposing tail is $1/3^{k+1}$.
</details>

## E0.04.12 Audit Russell's paradox and its sources

- **Type:** critique
- **Difficulty:** 4
- **Objective:** Distinguish unrestricted comprehension, bounded separation, Cantor diagonalization, and historically supported claims.
- **Estimated time:** 45 minutes
- **Allowed tools:** The module references, the Stanford Encyclopedia of Philosophy entries, and the Open Logic Project pages. Open every source used. No generated summaries as evidence.
- **Assumptions:** Use only historical claims directly supported by an inspected source.

### Problem

Audit this draft paragraph:

> Russell single-handedly discovered all set-theoretic paradoxes in 1901 and proved that sets do not exist. His paradox says ordinary notation $\{x\in U:P(x)\}$ is inconsistent. Zermelo fixed everything by declaring $R=\{x:x\notin x\}$ empty, and ZF is the only coherent foundation. Cantor's diagonal proof is unrelated because it concerns real decimals, whose representations are always unique. Since Python sets reject mutable sets as members, Python has implemented ZF and cannot express the paradox.

1. Identify at least twelve mathematical, historical, or software errors and unsupported claims.
2. Correct them in a table with columns `Claim`, `Diagnosis`, `Repair`, and `Evidence`.
3. Derive the contradiction from unrestricted $R=\{x:x\notin x\}$ in both directions.
4. Explain why $R_U=\{x\in U:x\notin x\}$ leads to $R_U\notin U$ rather than the same unrestricted contradiction.
5. Compare the logical shape of Russell's set with Cantor's diagonal set $D=\{a\in A:a\notin f(a)\}$.
6. Use the 2026 SEP Russell entry to describe at least three historically distinct responses without declaring one the only response.
7. Use the SEP set theory entry or Open Logic Project to explain bounded separation at preview level.
8. Use official Python documentation to explain what `set` and `frozenset` do, and why implementation restrictions are not an axiomatization of mathematical foundations.
9. Rewrite the paragraph accurately in at most 220 words.
10. Submit a source ledger listing every opened URL and the exact sentence or claim it supports.

**Deliverable:** Diagnosis table, two derivations, corrected paragraph, and source ledger.

<details>
<summary>Hint 1</summary>

Separate discovery from anticipation, one paradox from related paradoxes, unrestricted comprehension from bounded selection, and mathematical foundations from a programming container API.
</details>

<details>
<summary>Hint 2</summary>

The SEP entry discusses Zermelo-style separation, Russell's type approaches, set-class approaches, and alternatives. Python hashability protects container invariants, not consistency of set theory.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that your work includes:

- a type or level check for every membership and subset statement;
- an ambient universe for every complement;
- explicit witnesses for failed relation properties;
- exact distinctions among antisymmetric, asymmetric, minimal, and least;
- declared domains and codomains for every function;
- image inclusion versus preimage equality handled correctly;
- duplicate filtering in rational enumeration;
- a diagonal proof that handles every listed row;
- an explicit response to binary representation ambiguity;
- direct source inspection for historical and software claims;
- limitations separating finite experiments from infinite proofs.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)
