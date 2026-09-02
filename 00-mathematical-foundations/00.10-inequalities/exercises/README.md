# Exercises for §0.10 Inequalities

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Difficulty follows the
project's 1 through 5 scale. All implementation work uses the Python standard
library.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.10.01 | Audit order-preserving operations | conceptual and critique | 2 | preserve or reverse direction from signs and domains | 35 min |
| E0.10.02 | Prove triangle and reverse triangle bounds | proof and application | 3 | derive scalar and norm distance bounds with equality | 45 min |
| E0.10.03 | Optimize with AM-GM and audit equality | proof and calculation | 3 | use weighted and unweighted AM-GM legally | 50 min |
| E0.10.04 | Derive Cauchy-Schwarz from a quadratic | derivation and proof | 4 | connect inner products, norms, and linear dependence | 55 min |
| E0.10.05 | Match conjugate exponents in Hölder | derivation and calculation | 4 | derive and apply Hölder with equality conditions | 55 min |
| E0.10.06 | Derive Minkowski and break the p contract | derivation and critique | 4 | prove the norm triangle family and reject p below one | 60 min |
| E0.10.07 | Choose Jensen's direction and domain | proof and critique | 4 | apply finite convex and concave Jensen | 60 min |
| E0.10.08 | Build a finite log-Jensen lower bound | derivation and application | 4 | prepare the inequality pattern used downstream | 55 min |
| E0.10.09 | Measure union-bound overlap | calculation and experiment | 3 | use a finite union bound without independence | 50 min |
| E0.10.10 | Prove Bernoulli and locate equality | induction and critique | 4 | preserve direction through the integer induction | 50 min |
| E0.10.11 | Prove finite rearrangement by swaps | proof and experiment | 4 | optimize pairings and distinguish series rearrangement | 65 min |
| E0.10.12 | Select, implement, and audit an inequality | implementation and source audit | 5 | integrate contracts, equality, evidence, and provenance | 90 min |

## E0.10.01 Audit order-preserving operations

- **Type:** conceptual and critique
- **Difficulty:** 2
- **Objective:** Predict direction from signs, domains, and monotonicity.
- **Estimated time:** 35 minutes
- **Allowed tools:** Algebra and counterexamples.
- **Assumptions:** All named scalar variables are real unless restricted.

### Problem

1. Starting from $a\le b$, state what follows after adding $c$.
2. State separate conclusions after multiplying by $c>0$, $c=0$, and $c<0$.
3. Prove that $0<a\le b$ implies $1/a\ge1/b$ without assuming the result.
4. Explain why $a\le b$ does not generally imply $a^2\le b^2$.
5. Give the weakest sign condition in this module under which squaring both sides
   preserves order.
6. For each function, give a domain on which it is increasing or decreasing and
   state the resulting direction: $x^2$, $1/x$, and $\log x$.
7. Audit: "Since $x\le y$, multiplying by $z$ gives $xz\le yz$."
8. Audit: "Since $x^2\le y^2$, taking square roots gives $x\le y$."
9. Repair each argument with sufficient assumptions or provide a counterexample.

**Deliverable:** A direction ledger, two counterexamples, and two repaired claims.

## E0.10.02 Prove triangle and reverse triangle bounds

- **Type:** proof and application
- **Difficulty:** 3
- **Objective:** Derive scalar and norm distance bounds and audit equality.
- **Estimated time:** 45 minutes
- **Allowed tools:** Absolute-value definition and norm axioms.
- **Assumptions:** Scalars are real; vectors have the same finite dimension.

### Problem

1. Prove $|a+b|\le|a|+|b|$ from $-|t|\le t\le|t|$.
2. Prove $||a|-|b||\le|a-b|$ by applying triangle twice.
3. Determine exactly when equality holds in the scalar triangle inequality.
4. Use the norm triangle inequality to prove
   $|\lVert\boldsymbol{x}\rVert-\lVert\boldsymbol{y}\rVert|
   \le\lVert\boldsymbol{x}-\boldsymbol{y}\rVert$ for any norm.
5. If an approximation satisfies
   $\lVert\widehat{\boldsymbol{x}}-\boldsymbol{x}\rVert_2\le0.01$,
   bound the error in its Euclidean norm.
6. Give one strict and one equality example for both scalar and Euclidean triangle
   inequalities.
7. Explain why sampled vector checks do not prove the norm theorem.

**Deliverable:** Three proofs, four equality or strict examples, and one finite
evidence statement.

## E0.10.03 Optimize with AM-GM and audit equality

- **Type:** proof and calculation
- **Difficulty:** 3
- **Objective:** Use weighted and unweighted AM-GM with all assumptions visible.
- **Estimated time:** 50 minutes
- **Allowed tools:** Algebra, two-variable AM-GM, and finite Jensen if desired.
- **Assumptions:** Every use must state nonnegativity or positivity and weights.

### Problem

1. Derive two-variable AM-GM from a nonnegative square.
2. For $x,y\ge0$ with $x+y=18$, find the largest possible $xy$ and prove the
   equality case is attainable.
3. For $a,b,c>0$ with $abc=64$, find the smallest possible $a+b+c$.
4. Apply weighted AM-GM to $x_1=1$, $x_2=9$, $w_1=1/3$, $w_2=2/3$.
5. State whether equality holds and why.
6. Explain how zero values are handled when their weights are positive or zero.
7. Disprove unrestricted real AM-GM with one domain failure.
8. Prove that for $u,v>0$ and $\theta\in[0,1]$,
   $u^\theta v^{1-\theta}\le\theta u+(1-\theta)v$.
9. Use [`weighted_am_gm_sides`](../code/inequality_tools.py) to check at least 50
   deterministic valid cases and at least three invalid contracts.

**Deliverable:** Two optimization proofs, weighted calculation, equality audit,
and a bounded computational check.

## E0.10.04 Derive Cauchy-Schwarz from a quadratic

- **Type:** derivation and proof
- **Difficulty:** 4
- **Objective:** Connect the inner-product bound to linear dependence.
- **Estimated time:** 55 minutes
- **Allowed tools:** Algebra, finite sums, and Euclidean norms.
- **Assumptions:** $\boldsymbol{x},\boldsymbol{y}\in\mathbb{R}^n$.

### Problem

1. Handle the case $\boldsymbol{y}=\mathbf{0}$ separately.
2. Expand $\lVert\boldsymbol{x}-t\boldsymbol{y}\rVert_2^2\ge0$.
3. Choose the minimizing $t$ and derive Cauchy-Schwarz.
4. Prove that equality holds exactly for linearly dependent vectors.
5. Derive $(\sum_i x_i)^2\le n\sum_i x_i^2$ and its equality condition.
6. Bound $|2x_1-x_2+3x_3|$ using $\lVert\boldsymbol{x}\rVert_2$.
7. Compute both sides for $\boldsymbol{x}=(1,2,3)$ and
   $\boldsymbol{y}=(4,-5,6)$.
8. Give a nonzero equality example with a negative proportionality constant.
9. Explain why Cauchy-Schwarz gives a two-norm bound rather than an arbitrary
   pair of exponents.

**Deliverable:** Full derivation, equality proof, two applications, and one
interpretation.

## E0.10.05 Match conjugate exponents in Hölder

- **Type:** derivation and calculation
- **Difficulty:** 4
- **Objective:** Derive and apply finite Hölder with conjugate exponents.
- **Estimated time:** 55 minutes
- **Allowed tools:** Weighted AM-GM, finite sums, and module code.
- **Assumptions:** Use $1<p,q<\infty$ unless explicitly treating an endpoint.

### Problem

1. Given $p=3$, solve $1/p+1/q=1$ for $q$.
2. Derive Young's inequality $uv\le u^p/p+v^q/q$ for $u,v\ge0$.
3. Normalize two nonzero vectors and derive Hölder.
4. Handle a zero-vector case.
5. State the finite-exponent equality condition.
6. Compute both sides for $\boldsymbol{x}=(1,-2,4)$,
   $\boldsymbol{y}=(-3,5,2)$, and $p=3$.
7. Construct a nonzero equality example for $p=3$, $q=3/2$.
8. State and prove the $p=1,q=\infty$ endpoint directly.
9. Audit: "Use Hölder with $p=q=3$."
10. Explain the extra sign condition needed when bounding
    $|\sum_i x_i y_i|$ rather than $\sum_i|x_i y_i|$.

**Deliverable:** Young and Hölder derivations, endpoint proof, calculation, and
equality audit.

## E0.10.06 Derive Minkowski and break the p contract

- **Type:** derivation and critique
- **Difficulty:** 4
- **Objective:** Derive the $\ell^p$ triangle inequality and reject $p<1$.
- **Estimated time:** 60 minutes
- **Allowed tools:** Hölder, scalar triangle inequality, and standard-library code.
- **Assumptions:** Vectors are real and have the same finite length.

### Problem

1. For $1<p<\infty$, set $z_i=|x_i+y_i|$ and derive
   $\sum_i z_i^p\le\sum_i|x_i|z_i^{p-1}+\sum_i|y_i|z_i^{p-1}$.
2. Apply Hölder to both sums and use $(p-1)q=p$.
3. Complete the Minkowski proof, including the zero-norm case.
4. Prove the $p=1$ and $p=\infty$ cases directly.
5. State equality conditions for $1<p<\infty$, $p=1$, and $p=\infty$.
6. For $p=1/2$, compute the formula on $(1,1)$, $(1,0)$, and $(0,1)$ and show
   the norm triangle direction fails.
7. Explain why this single counterexample is logically stronger than a million
   passing sampled cases against the universal $p<1$ claim.
8. Run the code tests for exponents $1,3/2,2,4,\infty$ and record the finite
   evidence boundary.

**Deliverable:** Family derivation, endpoint proofs, equality ledger, and one
contract-breaking counterexample.

## E0.10.07 Choose Jensen's direction and domain

- **Type:** proof and critique
- **Difficulty:** 4
- **Objective:** Apply finite Jensen only after checking shape, domain, and weights.
- **Estimated time:** 60 minutes
- **Allowed tools:** Definition of convexity and finite induction.
- **Assumptions:** All combinations are finite.

### Problem

For each item, state the domain, weights, function shape, direction, and equality
condition.

1. Use convex $f(x)=x^2$ with values $-2,1,4$ and weights $1/4,1/2,1/4$.
2. Use concave $f(x)=\log x$ with positive values $1,4$ and equal weights.
3. Use affine $f(x)=3x-7$ with arbitrary normalized nonnegative weights.
4. Explain why $\log$ cannot be applied to an input value $0$ in this theorem.
5. Explain why weights $2,1$ do not satisfy this finite Jensen statement.
6. Normalize those weights and state what expression has changed.
7. Prove finite Jensen for $n$ points by induction from two-point convexity.
8. State strict-convex equality and the broader affine-on-the-hull possibility.
9. Give a function that is convex on one interval but not on all of $\mathbb{R}$,
   and explain why the declared domain matters.
10. Use `jensen_gap` on one convex, one affine, and one concave example. Explain
    why the helper cannot verify convexity.

**Deliverable:** Three complete applications, induction proof, two refusals, and
a computational evidence statement.

## E0.10.08 Build a finite log-Jensen lower bound

- **Type:** derivation and application
- **Difficulty:** 4
- **Objective:** Prepare the finite inequality pattern used in later latent-variable
  and information-theory derivations without teaching those topics.
- **Estimated time:** 55 minutes
- **Allowed tools:** Concavity of $\log$ and algebra.
- **Assumptions:** $r_i>0$, $w_i\ge0$, and $\sum_iw_i=1$.

### Problem

1. Derive
   $\log(\sum_iw_ir_i)\ge\sum_iw_i\log r_i$.
2. State why every $r_i$ with positive weight must be positive.
3. State the equality condition.
4. Evaluate both sides for $r=(1,4,16)$ and $w=(1/2,1/4,1/4)$.
5. Rewrite weighted AM-GM by exponentiating the inequality and justify why
   exponentiation preserves direction.
6. Let positive $q_i$ and $a_i$ satisfy $\sum_iq_i=1$. Substitute
   $r_i=a_i/q_i$ and derive
   $\log(\sum_i a_i)\ge\sum_iq_i\log(a_i/q_i)$.
7. State all assumptions introduced by that substitution.
8. Explain, in no more than three sentences, why the pattern is useful later
   without defining an ELBO, EM update, entropy, or divergence.
9. Audit: "Jensen always moves a logarithm inside an average and gives a lower
   bound."

**Deliverable:** Two derivations, numerical check, complete assumption ledger,
and repaired audit statement.

## E0.10.09 Measure union-bound overlap

- **Type:** calculation and experiment
- **Difficulty:** 3
- **Objective:** Use the finite union bound without inventing independence.
- **Estimated time:** 50 minutes
- **Allowed tools:** Finite sets, counting, and standard-library Python.
- **Assumptions:** Use the uniform sample space $\Omega=\{1,2,\ldots,12\}$.

### Problem

Let $A$ be the multiples of $2$, $B$ the multiples of $3$, and $C$ the values
at least $10$.

1. List $A,B,C$ and their union.
2. Compute each probability and the exact union probability.
3. Compute the uncapped and capped union bounds.
4. Identify every overlap responsible for looseness.
5. Construct three pairwise disjoint events on the same sample space and verify
   equality.
6. Construct three identical nonempty events and compare the true union with the
   sum bound.
7. Explain why independence was unnecessary in all cases.
8. Prove the finite union bound pointwise with indicators.
9. Write a finite enumerator that computes actual union probability and bound
   for these examples.
10. State why [`union_bound`](../code/inequality_tools.py) cannot recover the
    actual union from marginal probabilities alone.

**Deliverable:** Three event tables, indicator proof, executable enumerator, and
evidence boundary.

## E0.10.10 Prove Bernoulli and locate equality

- **Type:** induction and critique
- **Difficulty:** 4
- **Objective:** Preserve inequality direction through the integer induction.
- **Estimated time:** 50 minutes
- **Allowed tools:** Algebra and mathematical induction.
- **Assumptions:** $x\ge-1$ and integer $n\ge0$.

### Problem

1. Prove $(1+x)^n\ge1+nx$ by induction on $n$.
2. Identify where $x\ge-1$ is used.
3. Identify where $n\ge0$ is used.
4. Determine every equality case under the stated contract.
5. Evaluate both sides for $(x,n)=(0.1,10)$ and $(-0.5,4)$.
6. Give a counterexample if the condition $x\ge-1$ is dropped while integer
   $n\ge0$ is retained.
7. Explain why this theorem does not automatically cover noninteger exponents.
8. Audit: "$(1+x)^n\approx1+nx$, so the error is small."
9. Use `bernoulli_sides` over a declared finite grid and include invalid-input
   checks.

**Deliverable:** Complete induction, equality proof, boundary counterexample,
and finite audit.

## E0.10.11 Prove finite rearrangement by swaps

- **Type:** proof and experiment
- **Difficulty:** 4
- **Objective:** Optimize finite pairings and distinguish infinite series order.
- **Estimated time:** 65 minutes
- **Allowed tools:** Algebra, permutations, and standard-library Python.
- **Assumptions:** Two finite real sequences have equal length.

### Problem

1. For $a_i\le a_j$ and $b_r\le b_s$, derive the product-sum change between
   aligned and crossed pairing.
2. Use adjacent inversion removal to prove same-order pairing maximizes the sum.
3. Deduce that opposite-order pairing minimizes it.
4. State uniqueness when both sorted sequences are strict.
5. Explain how ties create additional equality permutations.
6. Compute minimum and maximum for $a=(-2,1,1,5)$ and $b=(-3,0,4,7)$.
7. Enumerate every permutation of $b$ and confirm the extrema.
8. Give one maximizing permutation different from the sorted order if ties allow it.
9. Explain in a short comparison table why this theorem is not the conditional
   series rearrangement theorem from §0.09.
10. State what exhaustive checking proves for this one finite input and what the
    swap proof proves universally.

**Deliverable:** Swap proof, equality audit, exhaustive finite check, and theorem
distinction table.

## E0.10.12 Select, implement, and audit an inequality

- **Type:** implementation and source audit
- **Difficulty:** 5
- **Objective:** Integrate theorem selection, equality, tests, and provenance.
- **Estimated time:** 90 minutes
- **Allowed tools:** Python standard library and sources opened directly from the
  resource guide.
- **Assumptions:** Run the repository's §0.10 tests before extending them.

### Problem

Build an inequality audit report that:

1. classifies 20 prompts by target structure before naming a theorem;
2. includes at least two valid uses each of triangle, AM-GM, Cauchy-Schwarz,
   Hölder, Minkowski, Jensen, union bound, Bernoulli, and rearrangement;
3. includes at least one refusal for each theorem due to a failed domain, sign,
   weight, exponent, finiteness, or ordering contract;
4. states direction and equality conditions for every accepted use;
5. runs all helpers in [`inequality_tools.py`](../code/inequality_tools.py) on
   hand-computed examples;
6. adds deterministic tests for at least 200 valid finite inputs and 20 invalid
   contracts;
7. includes the $p=1/2$ Minkowski counterexample and one reversed-Jensen mistake;
8. distinguishes exact arithmetic, floating-point checks, symbolic proof, cited
   theorem, and source metadata in an evidence table;
9. directly inspects the Boyd and Vandenberghe book pages and extracted theorem
   passages, OpenStax §2.3, MIT 6.042J §16.5, Levin §4.5, and Python 3.14 docs;
10. records URL, access date, exact support, extraction limit, and reuse boundary
    for each source;
11. confirms that no source exercise, solution, prose, table, code, or figure was
    copied;
12. critiques: "All tests passed, so the inequality is proved; equality cases do
    not matter; Jensen needs no domain check; and the union bound assumes
    independence" by identifying at least eight distinct defects;
13. runs with `PYTHONDONTWRITEBYTECODE=1` and removes any generated
    `__pycache__` directories.

**Deliverable:** Executable report, theorem-selection ledger, equality audit,
eight-part critique, provenance table, and limitations.

<details><summary>Hint 1</summary>

For each prompt, write target, domain, structure, parameters, direction, equality,
and evidence before the theorem name.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that your work
includes:

- every theorem's domain, sign, weight, exponent, and finiteness assumptions;
- the direction of every bound;
- equality conditions for every accepted application;
- an explicit refusal when a contract fails;
- no silent extension from finite sums to integrals or expectations;
- no claim that the union bound requires independence;
- no use of Minkowski as a norm triangle for $p<1$;
- a distinction between finite pairing and infinite series rearrangement;
- explicit limits on every computational check;
- directly inspected sources tied to exact claims.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)