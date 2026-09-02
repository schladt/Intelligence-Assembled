# Exercises for §0.09 Sums, Series, and Asymptotics

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Difficulty follows the project's 1 through 5 scale. All implementation work uses the Python standard library.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.09.01 | Derive three finite sums | derivation and calculation | 2 | derive arithmetic, geometric, and telescoping formulas | 35 min |
| E0.09.02 | Prove convergence from monotone bounds | proof | 3 | separate convergence existence from limit identification | 45 min |
| E0.09.03 | Build partial sums and use the nth-term test | conceptual and critique | 3 | distinguish terms, partial sums, and necessary conditions | 40 min |
| E0.09.04 | Apply direct and limit comparison | proof and critique | 4 | check positivity, direction, ratio limits, and boundary cases | 55 min |
| E0.09.05 | Use integrals to bound sums and tails | derivation and proof | 4 | verify integral-test and remainder hypotheses | 60 min |
| E0.09.06 | Apply and refuse ratio and root tests | analysis and critique | 4 | classify limits below, above, and at one | 55 min |
| E0.09.07 | Classify alternating and signed series | proof and calculation | 4 | distinguish absolute, conditional, and failed tests | 55 min |
| E0.09.08 | Rearrange a conditional series carefully | proof and experiment | 4 | explain order sensitivity and shrinking overshoot | 60 min |
| E0.09.09 | Certify harmonic approximations | derivation and implementation | 4 | combine asymptotics with explicit finite error bounds | 60 min |
| E0.09.10 | Use Stirling with finite error discipline | derivation and implementation | 4 | preserve meaning, log scale, and a certified interval | 65 min |
| E0.09.11 | Prove asymptotic relations and separations | proof and critique | 4 | distinguish O, Omega, Theta, o, omega, and equivalence | 65 min |
| E0.09.12 | Implement and audit an asymptotic claim | implementation and source audit | 5 | integrate tests, finite evidence, theorem hypotheses, and provenance | 90 min |

## E0.09.01 Derive three finite sums

- **Type:** derivation and calculation
- **Difficulty:** 2
- **Objective:** Derive finite formulas before taking any infinite limit.
- **Estimated time:** 35 minutes
- **Allowed tools:** Pencil and paper; exact Python arithmetic after deriving.
- **Assumptions:** $N$ is a nonnegative integer. Empty sums equal zero.

### Problem

1. Derive the sum of $N$ terms of an arithmetic sequence with first term $a$ and difference $d$ by pairing a forward and reversed copy.
2. Evaluate $7+12+17+\cdots+202$ after proving that $202$ is a term and finding the term count.
3. Derive the finite geometric formula for ratio $r\ne1$ by subtracting $rS_N$ from $S_N$.
4. State and justify the separate case $r=1$.
5. Evaluate $\sum_{k=0}^{9}3(2/3)^k$ exactly.
6. Find a closed form for $\sum_{n=1}^{N}2/[n(n+2)]$ by partial fractions. Keep every surviving boundary term.
7. Take the valid limit of the telescoping expression.
8. Explain why no infinite-series rule was needed for items 1 through 6.
9. Verify all three finite formulas using `Fraction` and direct sums for at least 20 deterministic parameter choices.

**Deliverable:** Three derivations, three evaluated sums, exact assertions, and an evidence-boundary note.

<details><summary>Hint 1</summary>

For the telescoping sum, $2/[n(n+2)]=1/n-1/(n+2)$ leaves two terms at each end.
</details>

## E0.09.02 Prove convergence from monotone bounds

- **Type:** proof
- **Difficulty:** 3
- **Objective:** Prove that a sequence converges before solving for its limit.
- **Estimated time:** 45 minutes
- **Allowed tools:** Algebra, induction, and the monotone convergence theorem.
- **Assumptions:** All sequences are real.

### Problem

Let $a_1=1$ and

$$
a_{n+1}=\sqrt{2+a_n}.
$$

1. Prove by induction that $1\le a_n<2$ for every $n$.
2. Prove that $(a_n)$ is increasing. You may square a nonnegative inequality after stating why this preserves order.
3. Apply the monotone convergence theorem with its exact hypotheses.
4. Let $L$ be the limit and derive $L=\sqrt{2+L}$.
5. Solve the resulting equation and reject any extraneous root using the established bounds.
6. Explain why solving the fixed-point equation before proving convergence is insufficient.
7. Give a bounded divergent sequence and a monotone divergent sequence.
8. State which missing hypothesis defeats monotone convergence in each counterexample.

**Deliverable:** A complete convergence proof, limit identification, and two counterexamples.

<details><summary>Hint 1</summary>

To compare $a_{n+1}$ and $a_n$, use $a_n<2$ to show $2+a_n>a_n^2$.
</details>

## E0.09.03 Build partial sums and use the nth-term test

- **Type:** conceptual and critique
- **Difficulty:** 3
- **Objective:** Keep sequence terms, partial sums, and test conclusions separate.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper; standard-library code for finite tables.
- **Assumptions:** Every series starts at $n=1$.

### Problem

For each series, write $a_n$, the first four partial sums, and the nth-term-test conclusion:

1. $\sum n/(n+1)$;
2. $\sum 1/n$;
3. $\sum 1/n^2$;
4. $\sum (-1)^n$;
5. $\sum (-1)^{n-1}/n$.

Then:

6. identify every case where the test proves divergence;
7. identify every case where it is inconclusive;
8. give one convergent and one divergent series whose terms both approach zero;
9. derive $a_N=S_N-S_{N-1}$ and use it to prove the necessary condition;
10. critique: "The millionth term is tiny, so the series converges";
11. explain why changing five initial terms cannot change convergence but can change the sum.

**Deliverable:** Five partial-sum ledgers, a proof of the necessary condition, and two critiques.

## E0.09.04 Apply direct and limit comparison

- **Type:** proof and critique
- **Difficulty:** 4
- **Objective:** Use comparison only in licensed directions and report inconclusive pairings.
- **Estimated time:** 55 minutes
- **Allowed tools:** Algebra and known geometric or $p$-series.
- **Assumptions:** Establish eventual positivity explicitly.

### Problem

Determine convergence or divergence and justify every comparison:

1. $\sum 1/(n^2+7)$ by direct comparison;
2. $\sum (4n+1)/(n^2+3)$ by limit comparison;
3. $\sum 1/(2^n+n)$ by direct comparison;
4. $\sum n/(n^3+1)$ by limit comparison;
5. $\sum (n^2+1)/(n^3+2)$ by limit comparison.

Audit these arguments:

6. "$0\le1/n^2\le1/n$, and the harmonic series diverges, so $\sum1/n^2$ diverges."
7. "$1/n\ge1/n^2$, and $\sum1/n^2$ converges, so the harmonic series converges."
8. If $a_n/b_n\to0$ and $\sum b_n$ diverges, construct one convergent and one divergent possible $\sum a_n$.
9. If $a_n/b_n\to\infty$ and $\sum b_n$ converges, construct one convergent and one divergent possible $\sum a_n$.
10. State what happens if the ratio limit does not exist.

**Deliverable:** Five classifications, two repaired arguments, four boundary examples, and a hypothesis ledger.

<details><summary>Hint 1</summary>

For zero-limit boundaries, take $b_n=1/n$ and choose $a_n=1/n^2$ or $a_n=1/(n\ln n)$ for $n\ge2$.
</details>

## E0.09.05 Use integrals to bound sums and tails

- **Type:** derivation and proof
- **Difficulty:** 4
- **Objective:** Verify the function contract and derive finite remainder bounds.
- **Estimated time:** 60 minutes
- **Allowed tools:** Single-variable integration; module rectangle figure.
- **Assumptions:** You may use $\int x^{-p}\,dx$.

### Problem

1. Prove $\ln(n+1)\le H_n\le1+\ln n$ from rectangles or interval inequalities.
2. Use the lower bound to prove harmonic divergence.
3. Use both bounds to prove $H_n=\Theta(\ln n)$ and $H_n\sim\ln n$.
4. State every integral-test hypothesis for $\sum_{n=2}^{\infty}1/[n(\ln n)^2]$ and determine convergence.
5. Determine the behavior of $\sum_{n=2}^{\infty}1/(n\ln n)$.
6. For $p>1$, derive the two-sided remainder bound for $\sum1/n^p$ after $N$ terms.
7. Find the smallest integer $N$ for which the integral upper bound guarantees the tail of $\sum1/n^3$ is below $10^{-4}$.
8. Explain why the corresponding integral is not usually the series sum.
9. Give a positive sequence for which the obvious continuous extension is not decreasing, so the integral test as stated is unavailable.

**Deliverable:** Harmonic proof, two logarithmic-series classifications, a general tail bound, and one refusal.

## E0.09.06 Apply and refuse ratio and root tests

- **Type:** analysis and critique
- **Difficulty:** 4
- **Objective:** Treat one and absent limits as inconclusive rather than failed mathematics.
- **Estimated time:** 55 minutes
- **Allowed tools:** Algebra, logarithms, and known $p$-series.
- **Assumptions:** Check eventual nonzero terms for ratios.

### Problem

Use the named test or refuse it with a precise reason:

1. $\sum 5^n/n!$ by ratio;
2. $\sum n!/4^n$ by ratio;
3. $\sum [(2n+1)/(5n+3)]^n$ by root;
4. $\sum (1+1/n)^{-n^2}$ by root;
5. $\sum1/n^3$ by both ratio and root;
6. $\sum(-1)^n/n$ by ratio;
7. a series with ratio limit one that converges;
8. a series with ratio limit one that diverges;
9. a series whose root diagnostic has no limit but which converges absolutely;
10. explain why $L>1$ implies divergence rather than merely failure of absolute convergence.

**Deliverable:** Six test calculations, four boundary examples or explanations, and explicit conclusions.

<details><summary>Hint 1</summary>

For item 9, alternate terms shaped like $(1/2)^n$ and $(1/3)^n$.
</details>

## E0.09.07 Classify alternating and signed series

- **Type:** proof and calculation
- **Difficulty:** 4
- **Objective:** Check alternation, monotone magnitudes, zero limits, and absolute convergence separately.
- **Estimated time:** 55 minutes
- **Allowed tools:** Alternating, comparison, ratio, and nth-term tests.
- **Assumptions:** A finite nonmonotone prefix is allowed when the tail is monotone.

### Problem

Classify each as absolutely convergent, conditionally convergent, divergent, or not settled by the requested test:

1. $\sum(-1)^{n-1}/n$;
2. $\sum(-1)^{n-1}/n^2$;
3. $\sum(-1)^{n-1}n/(n+1)$;
4. $\sum(-1)^{n-1}/\sqrt n$;
5. $\sum(-1)^{n-1}(n+2)/2^n$;
6. $\sum(-1)^{n-1}b_n$ where $b_n=1/n$ for even $n$ and $b_n=1/n^2$ for odd $n$.

Then:

7. for every applicable alternating series, state both hypotheses;
8. for item 1, find an $N$ guaranteeing error at most $10^{-3}$;
9. explain why the next-term bound requires the alternating-test hypotheses;
10. prove that absolute convergence implies convergence by splitting into positive and negative parts or by comparison.

**Deliverable:** Six classifications, one finite error guarantee, and one proof.

## E0.09.08 Rearrange a conditional series carefully

- **Type:** proof and experiment
- **Difficulty:** 4
- **Objective:** Explain why conditional sums depend on order and what a finite rearrangement experiment cannot prove.
- **Estimated time:** 60 minutes
- **Allowed tools:** Pencil and paper; Python standard library for a finite experiment.
- **Assumptions:** Use the positive terms $1/(2k-1)$ and negative terms $-1/(2k)$ of the alternating harmonic series.

### Problem

Fix target $T=1$.

1. Add unused positive terms until the running sum exceeds $T$.
2. Add unused negative terms until it falls below $T$.
3. Repeat for at least 10,000 selected terms and record the last 20 crossings.
4. Prove that the positive subseries diverges to $+\infty$ and the negative magnitudes diverge to $+\infty$.
5. Prove that each crossing overshoots by at most the last selected term's magnitude.
6. Use term magnitudes tending to zero to prove that the crossing subsequences approach $T$.
7. Explain why every original term is eventually selected.
8. Conclude that the complete rearranged series converges to $T$.
9. Contrast this with absolute convergence.
10. State exactly what the finite experiment contributes.

**Deliverable:** Rearrangement algorithm, convergence proof, finite trace, and limitation statement.

## E0.09.09 Certify harmonic approximations

- **Type:** derivation and implementation
- **Difficulty:** 4
- **Objective:** Use asymptotic terms only with an explicit finite remainder.
- **Estimated time:** 60 minutes
- **Allowed tools:** Module bounds; Python standard library including `fsum` and `Decimal`.
- **Assumptions:** Use $\gamma=0.5772156649015328606\ldots$.

### Problem

For

$$
A_n=\ln n+\gamma+\frac1{2n}-\frac1{12n^2},
$$

use the bound $0<H_n-A_n<1/(120n^4)$.

1. Compute $H_n$ with `fsum` for $n=1,10,100,1000,10000$.
2. Verify the coarse integral bounds.
3. Verify $0<H_n-\ln n-\gamma\le1/n$.
4. Verify the sharper interval around $A_n$.
5. Find the smallest $n$ for which the certified sharp remainder is below $10^{-12}$.
6. Compare this guarantee with the observed binary64 error.
7. Explain why an observed smaller error is not a stronger theorem.
8. Derive $H_n\sim\ln n$ from the coarse bounds without using decimal data.
9. State which parts are proof, sourced theorem, and finite computation.

**Deliverable:** Derivation, executable table, certified threshold, and evidence ledger.

## E0.09.10 Use Stirling with finite error discipline

- **Type:** derivation and implementation
- **Difficulty:** 4
- **Objective:** Keep counting meaning, leading asymptotics, correction bounds, and floating-point representation distinct.
- **Estimated time:** 65 minutes
- **Allowed tools:** Module inequalities; Python `factorial`, `lgamma`, `Decimal`, and `Fraction`.
- **Assumptions:** $n\ge1$ is an integer.

### Problem

Define

$$
L_n=\left(n+\frac12\right)\ln n-n+\frac12\ln(2\pi).
$$

1. Explain what $n!$ counts in §0.08 terms.
2. State what $n!\sim e^{L_n}$ does and does not say.
3. Use the module inequality to give a certified interval for $\ln(n!)$.
4. Exponentiate it to bound $n!$ multiplicatively.
5. Compute exact $n!$ and compare with the leading approximation for $n=1,2,5,10,50,100$.
6. Verify the log interval with at least 60 decimal digits, not only `lgamma`.
7. Prove that the correction interval has width $1/(360n^3)$.
8. Find the smallest $n$ for which that log-width is below $10^{-12}$.
9. Explain why binary64 endpoints may coincide even when the mathematical interval has positive width.
10. Critique: "Stirling is exact for large $n$."

**Deliverable:** Meaning statement, finite bounds, high-precision check, threshold, and critique.

## E0.09.11 Prove asymptotic relations and separations

- **Type:** proof and critique
- **Difficulty:** 4
- **Objective:** Use quantified or ratio definitions with an explicit limiting process.
- **Estimated time:** 65 minutes
- **Allowed tools:** Definitions in the module; elementary limits.
- **Assumptions:** Comparison functions are eventually positive.

### Problem

As $n\to\infty$ unless another direction is stated:

1. prove $7n^3-2n+4=\Theta(n^3)$ with explicit constants and threshold;
2. prove $7n^3-2n+4\sim7n^3$;
3. show it is not asymptotic to $n^3$;
4. prove $\ln n=o(n^{1/2})$;
5. prove $n^5=o(2^n)$ using a ratio argument or a cited elementary growth result;
6. prove $f=o(g)\implies f=O(g)$;
7. give a counterexample to the converse;
8. prove $f\sim g\implies f=\Theta(g)$;
9. give a counterexample to the converse;
10. as $h\to0$, classify $h^3$ relative to $h^2$ using $O$ and $o$;
11. explain why the direction change does not make big-O and little-o interchangeable;
12. determine which of $n^2=O(n^3)$, $n^2=\Omega(n)$, $n^2=\omega(n)$, and $3n^2\sim n^2$ are true.

**Deliverable:** Eight proofs or classifications, explicit witnesses, and two counterexamples.

## E0.09.12 Implement and audit an asymptotic claim

- **Type:** implementation and source audit
- **Difficulty:** 5
- **Objective:** Integrate exact formulas, theorem contracts, numerical limits, and directly inspected evidence.
- **Estimated time:** 90 minutes
- **Allowed tools:** Python standard library and sources opened directly from the resource guide.
- **Assumptions:** Run the repository's §0.09 tests before extending them.

### Problem

Build one executable report that:

1. tests arithmetic and geometric formulas against exact direct sums for at least 200 deterministic cases;
2. tests telescoping boundary terms for at least 100 values of $N$;
3. verifies harmonic integral and Euler-constant bounds through $n=10,000$;
4. verifies the sharp harmonic remainder at 60 or more decimal digits for selected $n$;
5. tests the alternating next-term error through at least 5,000 terms;
6. verifies Stirling correction inequalities with high-precision decimal arithmetic;
7. demonstrates ratio/root inconclusiveness on at least one convergent and one divergent $p$-series;
8. checks explicit witnesses for four $O/\Omega/\Theta$ claims over finite ranges while labeling them finite checks;
9. audits: "The ratio looks like one, so the series converges; $f=O(g)$ means $f/g\to0$; Stirling is exact after a large threshold; and 10,000 passing cases prove all of this";
10. identify at least eight distinct errors or missing assumptions in that claim;
11. directly inspect OpenStax Chapter 5, MIT 18.01SC Unit 5, NIST DLMF §§2.1 and 5.11, Princeton's §1.4 algorithms page, and Python `math` documentation;
12. record URL, access date, exact supported claim, extraction limit, and reuse boundary for each source;
13. confirm that no source exercise, solution, prose, table, code, or figure was copied;
14. remove any generated `__pycache__` directories after running.

**Deliverable:** Executable report, results table, eight-part critique, source ledger, and limitations.

<details><summary>Hint 1</summary>

Keep mathematical proof, cited theorem, exact finite arithmetic, floating-point experiment, API behavior, and licensing in separate evidence rows.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that your work includes:

- a finite partial sum before every infinite limit;
- all theorem hypotheses, including eventual thresholds;
- every named inconclusive boundary;
- the direction of every comparison inequality;
- separate tests for ordinary and absolute convergence;
- a finite error bound beside every numerical use of harmonic or Stirling asymptotics;
- a stated limit direction for every asymptotic relation;
- no claim that big-O and little-o are interchangeable;
- explicit limits on every computational experiment;
- directly inspected sources tied to exact claims.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)