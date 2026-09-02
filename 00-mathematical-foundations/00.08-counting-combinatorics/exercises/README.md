# Exercises for §0.08 Counting and Combinatorics

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Difficulty follows the project's 1 through 5 scale. All implementation work uses the Python standard library.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.08.01 | Specify the outcome before counting | conceptual and critique | 2 | distinguish sequences, sets, multisets, and physical samples | 30 min |
| E0.08.02 | Apply and audit the four counting rules | calculation and proof | 3 | justify sum, product, bijection, and division | 40 min |
| E0.08.03 | Build the sampling model matrix | derivation and implementation | 3 | derive all four order/replacement counts | 45 min |
| E0.08.04 | Count permutations, combinations, and multisets | calculation and derivation | 3 | explain factorial denominators through fibers | 45 min |
| E0.08.05 | Derive binomial and multinomial expansions | derivation | 3 | connect coefficients to choices from factors | 45 min |
| E0.08.06 | Prove Pascal and Vandermonde two ways | combinatorial proof | 4 | prove identities by partitions and coefficients | 50 min |
| E0.08.07 | Translate compositions with stars and bars | bijection and calculation | 4 | handle zero, positive, and shifted lower bounds | 50 min |
| E0.08.08 | Repair overcounting with inclusion-exclusion | proof and calculation | 4 | track intersection multiplicities | 55 min |
| E0.08.09 | Use pigeonhole and double counting | proof | 4 | turn cardinality inequalities into structural conclusions | 50 min |
| E0.08.10 | Extract coefficients from finite choices | implementation and derivation | 4 | use convolution for constrained counts | 60 min |
| E0.08.11 | Derive Fibonacci and Catalan counts | proof and experiment | 4 | prove recursive decompositions and boundary formulas | 60 min |
| E0.08.12 | Implement and audit a counting argument | implementation and critique | 5 | integrate exact tests, evidence boundaries, and provenance | 75 min |

## E0.08.01 Specify the outcome before counting

- **Type:** conceptual and critique
- **Difficulty:** 2
- **Objective:** State the carrier, equality rule, order, replacement, and labels before choosing a formula.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper.

### Problem

For three draws from labels $\{A,B,C,D,E\}$, define one outcome and compute the count under each model:

1. ordered with replacement;
2. ordered without replacement;
3. unordered with replacement;
4. unordered without replacement.

Then:

5. give two sequences merged by forgetting order;
6. give one outcome removed by forbidding replacement;
7. explain why three physically distinct balls labeled `A` may change a physical-object count but not a visible-label count;
8. critique: "There are $\binom53$ samples because drawing means choosing."

**Deliverable:** Four set descriptions, four counts, two witnesses, and a repaired statement.

<details><summary>Hint 1</summary>

Write outcomes as tuples, subsets, or multiplicity vectors before writing a formula.
</details>

## E0.08.02 Apply and audit the four counting rules

- **Type:** calculation and proof
- **Difficulty:** 3
- **Objective:** Justify sum, product, bijection, and division rules from finite-set structure.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper; exact arithmetic.

### Problem

1. Count length-five binary strings with exactly one or exactly four ones. Name the disjoint cases.
2. Count length-five strings over $\{0,1,2\}$ with no equal adjacent symbols. Explain why continuation counts are uniform.
3. Give a bijection between subsets of $[n]$ and length-$n$ binary strings.
4. Use it to prove $|\mathcal{P}([n])|=2^n$.
5. Let $A$ be all ordered triples of distinct elements from $[7]$, and let $B$ be all three-element subsets. Define the forget-order map $A\to B$.
6. Prove every fiber has size $3!$, then compute $|B|$.
7. Give a surjection with nonuniform fibers and explain why one global division factor fails.

**Deliverable:** Four counts or proofs and one division-rule counterexample.

<details><summary>Hint 1</summary>

For item 2, the first symbol has three choices and each later position has two.
</details>

## E0.08.03 Build the sampling model matrix

- **Type:** derivation and implementation
- **Difficulty:** 3
- **Objective:** Derive and verify the four ordered/unordered, replacement/no-replacement formulas.
- **Estimated time:** 45 minutes
- **Allowed tools:** Python standard library.

### Problem

1. Derive each cell for population size $n$ and sample size $k$.
2. State boundary values for $k=0$, $n=0$, and $k>n$ without replacement.
3. For $n=4,k=2$, list every outcome in all four models.
4. Verify list lengths with `itertools.product`, `permutations`, `combinations`, and `combinations_with_replacement`.
5. Explain why `combinations("AAB", 2)` treats the two `A` positions as distinct inputs even when output values match.
6. State why none of the four counts assigns probabilities.

**Deliverable:** A formula table, boundary ledger, executable enumeration, and semantics note.

<details><summary>Hint 1</summary>

The unordered-with-replacement cell is a weak composition of $k$ across $n$ types.
</details>

## E0.08.04 Count permutations, combinations, and multisets

- **Type:** calculation and derivation
- **Difficulty:** 3
- **Objective:** Derive falling-factorial, combination, and multinomial counts through labeled preimages.
- **Estimated time:** 45 minutes
- **Allowed tools:** Pencil and paper; `math` for verification.

### Problem

1. Count injective functions from a four-element set to a nine-element set.
2. Count six-element subsets of a fourteen-element set.
3. Count distinct words with multiplicities $(4,3,2)$.
4. Derive the multinomial formula by temporarily labeling identical copies.
5. Derive it again by choosing positions successively.
6. Prove $\sum_{k_1+\cdots+k_m=n}\binom{n}{k_1,\ldots,k_m}=m^n$ combinatorially.
7. Check the cases $(4,3,2)$ and $m=3,n\le7$ with exact code.

**Deliverable:** Three counts, three derivations, and executable assertions.

<details><summary>Hint 1</summary>

Every visible word with multiplicities $(k_i)$ has exactly $\prod_i k_i!$ labeled preimages.
</details>

## E0.08.05 Derive binomial and multinomial expansions

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Interpret polynomial coefficients as choices from labeled factors.
- **Estimated time:** 45 minutes
- **Allowed tools:** Algebra and finite sums.

### Problem

1. Derive the binomial theorem by choosing the factors that contribute $b$.
2. Expand $(2+x)^5$ and identify the coefficient of $x^3$ before arithmetic simplification.
3. Derive $\sum_k\binom nk=2^n$ algebraically and combinatorially.
4. Derive the alternating row sum for $n\ge1$.
5. Derive the multinomial theorem.
6. Find the coefficient of $x^2y^3z$ in $(x+y+z)^6$.
7. Explain why an exponent tuple must sum to the number of factors.

**Deliverable:** Two theorem derivations, four coefficient identities, and one scope explanation.

<details><summary>Hint 1</summary>

For each monomial, record how many factors supplied each variable.
</details>

## E0.08.06 Prove Pascal and Vandermonde two ways

- **Type:** combinatorial proof
- **Difficulty:** 4
- **Objective:** Count one finite set through a disjoint partition and through coefficient extraction.
- **Estimated time:** 50 minutes
- **Allowed tools:** Proof methods from §0.06; binomial theorem.

### Problem

1. Prove Pascal's identity by whether a distinguished element is selected.
2. Verify its $k=0$ and $k=n$ boundaries under the zero convention.
3. Prove $\binom nk=\binom n{n-k}$ with a bijection.
4. Prove Vandermonde's identity combinatorially for disjoint groups of sizes $m,n$.
5. Prove it algebraically by extracting $[x^r]$.
6. Evaluate $\sum_k\binom7k\binom5{6-k}$ without summing term by term.
7. State the common set counted in each combinatorial proof.

**Deliverable:** Four proofs, boundary checks, and one numerical evaluation.

<details><summary>Hint 1</summary>

For Vandermonde, partition $r$-subsets by how many elements come from the first group.
</details>

## E0.08.07 Translate compositions with stars and bars

- **Type:** bijection and calculation
- **Difficulty:** 4
- **Objective:** Convert nonnegative, positive, and shifted-lower-bound equations into bar-position choices.
- **Estimated time:** 50 minutes
- **Allowed tools:** Pencil and paper; exact enumeration for checks.

### Problem

1. Prove the weak-composition formula with an explicit inverse map.
2. List the strings for $x_1+x_2+x_3=3$ and confirm the count.
3. Derive the positive-composition formula.
4. Count solutions to $x_1+x_2+x_3+x_4=20$ with $x_1\ge2,x_2\ge1,x_3\ge0,x_4\ge4$.
5. Handle the boundary cases of zero parts and zero total.
6. Explain why plain stars and bars does not enforce $x_i\le M_i$.
7. Verify items 2 and 4 by exhaustive finite code.

**Deliverable:** Two bijections, two counts, a boundary ledger, and assertions.

<details><summary>Hint 1</summary>

Subtract each lower bound before counting the remaining nonnegative total.
</details>

## E0.08.08 Repair overcounting with inclusion-exclusion

- **Type:** proof and calculation
- **Difficulty:** 4
- **Objective:** Derive finite inclusion-exclusion and apply it through the required intersection depth.
- **Estimated time:** 55 minutes
- **Allowed tools:** Pencil and paper; Python standard library for finite checks.

### Problem

1. Derive the three-set formula by tracking an object in zero, one, two, or three sets.
2. Extend the contribution argument to $m$ sets.
3. Count integers in $[120]$ divisible by $2$, $3$, or $5$.
4. Count permutations of five objects with no fixed point.
5. Count nonnegative solutions to $x_1+x_2+x_3=9$ with every $x_i\le4$.
6. For each application, name the universe and bad sets.
7. Verify all three counts by exhaustive enumeration.

**Deliverable:** A general proof, three applications, exact checks, and model declarations.

<details><summary>Hint 1</summary>

For bounded variables, bad event $A_i$ is $x_i\ge5$; shift that coordinate by five.
</details>

## E0.08.09 Use pigeonhole and double counting

- **Type:** proof
- **Difficulty:** 4
- **Objective:** Use cardinality and incidence counts to force collisions and prove identities.
- **Estimated time:** 50 minutes
- **Allowed tools:** Proof techniques from §0.06.

### Problem

1. Prove that among 101 length-ten binary strings, two are equal.
2. Prove that assigning 73 jobs to 8 queues puts at least 10 jobs in one queue.
3. Show that a function between finite sets of equal size is injective iff surjective.
4. Double count pairs $(S,s)$ where $S\subseteq[n]$, $|S|=k$, and $s\in S$.
5. Deduce $k\binom nk=n\binom{n-1}{k-1}$.
6. Double count all subset-element incidences to prove $\sum_k k\binom nk=n2^{n-1}$.
7. State every finite and positivity assumption used.

**Deliverable:** Three pigeonhole proofs and two incidence proofs with assumptions.

<details><summary>Hint 1</summary>

Count $(S,s)$ first by choosing $S$, then by choosing $s$.
</details>

## E0.08.10 Extract coefficients from finite choices

- **Type:** implementation and derivation
- **Difficulty:** 4
- **Objective:** Connect polynomial multiplication, convolution, and constrained finite choices.
- **Estimated time:** 60 minutes
- **Allowed tools:** Python standard library; module code.

### Problem

1. Prove the coefficient convolution formula for two finite polynomials.
2. Derive the generating polynomial for $x_1+x_2+x_3=8$ with maxima $(2,4,5)$.
3. Compute $[x^8]$ by hand or staged convolution.
4. Implement convolution without symbolic algebra.
5. Compare the coefficient with exhaustive enumeration.
6. Prove the sum of all coefficients equals the total number of unconstrained independent choices.
7. Explain why no convergence statement is needed.
8. Explain why truncating after degree eight is safe if only $[x^8]$ is requested.

**Deliverable:** Derivation, coefficient, implementation, assertions, and formal-series boundary note.

<details><summary>Hint 1</summary>

Use $(1+x+x^2)(1+x+\cdots+x^4)(1+x+\cdots+x^5)$.
</details>

## E0.08.11 Derive Fibonacci and Catalan counts

- **Type:** proof and experiment
- **Difficulty:** 4
- **Objective:** Establish recursive counts from unique decompositions and verify closed forms on finite domains.
- **Estimated time:** 60 minutes
- **Allowed tools:** Induction from §0.07; Python standard library.

### Problem

1. Derive the square-domino tiling recurrence and prove $T_n=F_{n+1}$.
2. Derive the formal Fibonacci identity $F(x)=x/(1-x-x^2)$ coefficientwise.
3. Prove the unique `(u)v` decomposition for nonempty balanced parenthesis words.
4. Derive the Catalan recurrence.
5. Explain the reflection subtraction $\binom{2n}{n}-\binom{2n}{n+1}$.
6. Generate all parenthesis words for $n\le5$ and filter by prefix balance.
7. Compare enumeration, recurrence, and closed form.
8. State why agreement on $n\le5$ is not the general proof.

**Deliverable:** Two decomposition proofs, two generating identities, executable checks, and limitations.

<details><summary>Hint 1</summary>

The first return to height zero determines where `u` ends in `(u)v`.
</details>

## E0.08.12 Implement and audit a counting argument

- **Type:** implementation and critique
- **Difficulty:** 5
- **Objective:** Integrate outcome modeling, exact implementation, independent enumeration, proof boundaries, and source provenance.
- **Estimated time:** 75 minutes
- **Allowed tools:** Python standard library and directly opened module sources.

### Problem

Build one executable report that:

1. tests all four sampling formulas for $0\le n\le6$ and $0\le k\le6$ against `itertools`;
2. tests multinomial counts by successive combinations;
3. tests weak and positive compositions by exhaustive tuples;
4. tests inclusion-exclusion against direct unions for at least 20 deterministic finite families;
5. tests bounded-sum coefficients against enumeration;
6. verifies Pascal, Vandermonde, row-sum, and alternating-row identities;
7. verifies Fibonacci and Catalan recurrences through at least index 12;
8. includes invalid-input and empty-structure cases;
9. audits: "The formula is right because Python returned it, all samples are equally likely, and a generating function converges wherever we use it";
10. identifies at least six distinct errors or missing assumptions in that claim;
11. records a source ledger for MIT 6.042J, Guichard, Levin, Python `math`, and Python `itertools` with access date, supported claim, and reuse boundary;
12. confirms that no source exercise, solution, prose, code, table, or figure was copied.

**Deliverable:** Executable report, results table, six-part critique, source ledger, and limitations.

<details><summary>Hint 1</summary>

Keep mathematical proof, exhaustive fixed-instance checking, API documentation, probability modeling, and licensing in separate evidence rows.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that every count names:

- the finite set being counted;
- when two outcomes are equal;
- whether order and repetition matter;
- why cases are disjoint or how overlaps are repaired;
- why every division fiber is uniform;
- which boundaries and empty structures are included;
- whether code exhausts a fixed instance or supports a general proof;
- which source supports each external claim.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)