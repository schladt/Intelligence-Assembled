# Exercises for §0.03 Exponentials and Logarithms

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Hints become progressively more specific but do not state final answers. Difficulty follows the project's 1 through 5 scale.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.03.01 | Audit exponent laws and domains | critique | 2 | enforce exponent-law conditions | 20 min |
| E0.03.02 | Solve exponential and logarithmic equations | calculation | 2 | solve equations and check domains | 25 min |
| E0.03.03 | Move from compound to continuous growth | derivation | 3 | derive compounding and time formulas | 30 min |
| E0.03.04 | Compare finite and eventual growth | derivation | 3 | qualify asymptotic comparisons | 25 min |
| E0.03.05 | Turn a product into a log-likelihood | applied | 3 | convert products to log sums | 25 min |
| E0.03.06 | Find floating-point range failures | experiment | 3 | diagnose overflow and underflow | 35 min |
| E0.03.07 | Derive stable log-sum-exp | derivation | 3 | derive bounds and max shifting | 30 min |
| E0.03.08 | Derive log-softmax and class NLL | derivation | 3 | connect logits to stable class loss | 30 min |
| E0.03.09 | Preserve small changes with log1p and expm1 | experiment | 3 | diagnose cancellation near zero | 25 min |
| E0.03.10 | Implement a log-domain toolkit | implementation | 4 | implement and test stable operations | 50 min |
| E0.03.11 | Investigate growth crossovers visually | visual experiment | 4 | distinguish windows from limits | 45 min |
| E0.03.12 | Critique logarithm claims and sources | critique | 4 | repair misconceptions and attribution | 35 min |

## E0.03.01 Audit exponent laws and domains

- **Type:** critique
- **Difficulty:** 2
- **Objective:** Interpret exponents and enforce the real-domain conditions behind exponent laws.
- **Estimated time:** 20 minutes
- **Allowed tools:** Pencil and paper; no calculator needed.
- **Assumptions:** Work over the real numbers. Reduce rational exponents before classifying their domains.

### Problem

A classmate writes:

$$
(-16)^{3/4}=((-16)^3)^{1/4}=-8,
$$

$$
(-8)^{2/6}=\sqrt[6]{64}=2,
$$

$$
0^{-2}=0,
\qquad
x^{1/2}x^{3/2}=x^2\text{ for every real }x,
$$

and

$$
(a^x)^y=a^{xy}\text{ for all real }a,x,y.
$$

1. Classify each claim as valid, invalid, or valid only under added conditions.
2. For every invalid claim, identify the first expression that leaves the real domain or violates a definition.
3. Repair each statement with the weakest simple conditions you can justify.
4. Evaluate $27^{-2/3}$ and $(-27)^{-2/3}$ over the reals, showing the reciprocal and root steps.
5. Explain why $a^x=\exp(x\log a)$ is a dependable real-valued definition for $a>0$ but not a universal repair for $a<0$.

**Deliverable:** A five-row audit table, two exact evaluations, and a short explanation of the positive-base restriction.

<details>
<summary>Hint 1</summary>

Ask whether each root and denominator exists before applying an exponent law.
</details>

<details>
<summary>Hint 2</summary>

Reduce $2/6$ before interpreting the root. For negative integer powers, take the reciprocal only after evaluating the corresponding positive power.
</details>

## E0.03.02 Solve exponential and logarithmic equations

- **Type:** calculation
- **Difficulty:** 2
- **Objective:** Move between exponential and logarithmic form, use change of base, and reject invalid candidates.
- **Estimated time:** 25 minutes
- **Allowed tools:** Pencil and paper; calculator for final decimals.
- **Assumptions:** All logarithms are real. Unqualified $\log$ means natural logarithm.

### Problem

Solve each equation. State restrictions before transformations, give exact answers, and verify in the original equation.

1. $4^{2x-1}=32$.
2. $7e^{0.3t}=19$.
3. $\log_3(x-2)=4$.
4. $\log_2(x-1)+\log_2(x-5)=4$.
5. $\log(x+1)-\log(x-1)=\log 3$.
6. Use change of base to approximate $\log_7 50$ to five decimal places, then check by exponentiation.

For parts 4 and 5, identify every algebraic candidate that is rejected by the original domain.

**Deliverable:** Exact solutions, decimal checks where requested, and an explicit domain check for every logarithmic equation.

<details>
<summary>Hint 1</summary>

Write each log argument inequality before combining logarithms.
</details>

<details>
<summary>Hint 2</summary>

After combining logs, exponentiate to obtain an algebraic equation. Keep its roots as candidates until substitution into the original equation.
</details>

## E0.03.03 Move from compound to continuous growth

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Derive repeated-compounding, continuous-growth, doubling-time, and half-life formulas.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper; calculator or Python standard library for numerical checks.
- **Assumptions:** The rate is constant within each stated model. Rates and time units are compatible.

### Problem

An initial amount $P=2500$ grows at nominal annual rate $r=0.048$ for $t=12$ years.

1. Derive the amount after $nt$ equal compounding periods when there are $n$ compounds per year.
2. Compute the annual, monthly, daily using 365 days, and continuous-compounding amounts.
3. Starting from the finite formula, identify the substitution that turns its limit into the defining limit for $e$.
4. For the continuous model, derive the doubling time and evaluate it numerically.
5. A separate quantity decays as $Q(t)=600e^{-0.18t}$. Derive and compute its half-life.
6. State one modeling assumption not justified by the algebra alone.
7. Verify that every exponent is dimensionless and label the time units of both characteristic times.

**Deliverable:** Derivations, a comparison table, unit checks, and a modeling limitation.

<details>
<summary>Hint 1</summary>

The per-period multiplier is $1+r/n$, and the number of periods is $nt$.
</details>

<details>
<summary>Hint 2</summary>

For the limit, set $m=n/r$ informally when $r>0$, or rewrite $(1+r/n)^n$ as a power of an expression approaching the standard $e$ limit. Keep the outer exponent $rt$ visible.
</details>

## E0.03.04 Compare finite and eventual growth

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Distinguish finite comparisons from eventual asymptotic ordering.
- **Estimated time:** 25 minutes
- **Allowed tools:** Pencil and paper; a short computation is optional.
- **Assumptions:** $n$ is a positive integer and all compared functions are positive.

### Problem

Compare

$$
f(n)=1000\log n,
\qquad
g(n)=n^6,
\qquad
h(n)=1.2^n.
$$

1. Compare all three values at $n=10$, $100$, and $1000$ without overflowing. You may compare natural logarithms of the values.
2. State the eventual ordering using little-$o$ notation.
3. Explain why your three-point table cannot prove that ordering.
4. Show how to compare $n^6$ and $1.2^n$ by comparing $6\log n$ with $n\log1.2$.
5. Define both a **first-win crossover** and a **sustained-through-limit crossover** for a finite search ending at $N$.
6. Give an example of a plotting window that could support a false verbal claim about the eventual ordering.
7. Critique the sentence "exponential algorithms are slower than polynomial algorithms" and rewrite it with the required asymptotic and implementation qualifications.

**Deliverable:** A value or log-value table, two crossover definitions, and a qualified conclusion.

<details>
<summary>Hint 1</summary>

The asymptotic statement fixes the polynomial degree and exponential base before sending $n$ to infinity.
</details>

<details>
<summary>Hint 2</summary>

A finite search can show that one function wins on tested inputs. It cannot exclude another crossing beyond $N$.
</details>

## E0.03.05 Turn a product into a log-likelihood

- **Type:** applied
- **Difficulty:** 3
- **Objective:** Convert a product of positive factors into a log sum and state exactly what taking logs preserves.
- **Estimated time:** 25 minutes
- **Allowed tools:** Pencil and paper; calculator optional.
- **Assumptions:** Treat the supplied factors as positive likelihood contributions. No probability independence claim is required.

### Problem

Two parameter settings produce per-observation factors

$$
\boldsymbol{p}^{(A)}=(0.8,0.7,0.4,0.9,0.6),
$$

$$
\boldsymbol{p}^{(B)}=(0.75,0.75,0.5,0.8,0.65).
$$

1. Compute each product likelihood.
2. Compute each natural log-likelihood as a sum of logs.
3. Verify that both representations rank $A$ and $B$ in the same order.
4. Write each negative log-likelihood and state the resulting minimization order.
5. Prove in one paragraph that a strictly increasing logarithm preserves an argmax over positive likelihoods.
6. Explain why this does not mean an optimizer follows identical steps on likelihood and log-likelihood.
7. Extend each vector by repeating its five factors 400 times. Predict what happens to direct binary64 products and what happens to log sums.

**Deliverable:** Product and log tables, the argmax argument, and a numerical-range prediction.

<details>
<summary>Hint 1</summary>

Use $\log\prod_i p_i=\sum_i\log p_i$. Multiplying an objective by $-1$ reverses maximization to minimization.
</details>

<details>
<summary>Hint 2</summary>

Monotonicity preserves ordering of objective values. Scale, differences, derivatives, and curvature are different questions.
</details>

## E0.03.06 Find floating-point range failures

- **Type:** experiment
- **Difficulty:** 3
- **Objective:** Diagnose overflow, normal and subnormal ranges, harmful underflow, and harmless shifted-term underflow.
- **Estimated time:** 35 minutes
- **Allowed tools:** Python 3 and NumPy. Do not install additional packages.
- **Assumptions:** Record Python, NumPy, platform, and dtype information. Warning suppression must be local and documented.

### Problem

Design and run a numerical range laboratory for `numpy.float32` and `numpy.float64`.

1. Record `finfo.max`, `finfo.smallest_normal`, `finfo.smallest_subnormal`, and their natural logs for both dtypes.
2. Find the first tested integer $x$ for which `exp(x)` becomes infinite and the last for which it remains finite.
3. Find the first tested negative integer whose exponential becomes zero. Record whether subnormal values appear first.
4. For repeated factors $0.1$, $0.01$, and $0.9$, find the first tested product length that becomes zero in each dtype.
5. Compare naive and max-shifted LSE on at least four vectors that include large positive, all-small negative, and widely separated values.
6. Construct one shifted case in which a nonmaximum exponential becomes zero while the final LSE remains accurate to a float64 reference.
7. Explain why part 6 is usually harmless but all-term underflow in naive LSE is harmful.
8. Repeat enough trials to distinguish a threshold from a one-off observation.

**Deliverable:** Executable code with assertions, a compact result table, observations, and limitations.

<details>
<summary>Hint 1</summary>

Use `np.errstate(over="ignore", under="ignore", divide="ignore")` around only the operations expected to cross range boundaries.
</details>

<details>
<summary>Hint 2</summary>

After max shifting, one exponent is exactly zero before `exp`, so one exponential is exactly one. A distant tail can vanish without making the whole sum zero.
</details>

## E0.03.07 Derive stable log-sum-exp

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Derive LSE bounds, max shifting, and a stable two-term specialization.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper; Python or NumPy only for verification.
- **Assumptions:** Let $\boldsymbol{x}\in\mathbb{R}^{n}$ with $n\ge1$ and $m=\max_i x_i$.

### Problem

1. Starting from the definition, prove
   $$
   m\le\mathrm{LSE}(\boldsymbol{x})\le m+\log n.
   $$
2. Derive
   $$
   \mathrm{LSE}(\boldsymbol{x})
   =m+\log\sum_i e^{x_i-m}.
   $$
3. Explain separately why the shift prevents overflow and why it prevents all terms from underflowing.
4. For two values $a$ and $b$, derive a formula involving $\max(a,b)$ and $\log(1+e^{-|a-b|})$.
5. Identify where `log1p` improves that two-term formula.
6. Evaluate the stable formula for $(1000,999,998)$ to four decimal places and check the bounds.
7. Evaluate it for $(-1000,-1001)$ and explain why the answer is greater than $-1000$.
8. State what the bounds say when all $x_i$ are equal.

**Deliverable:** Complete derivation, two numerical checks, and an overflow/underflow explanation.

<details>
<summary>Hint 1</summary>

At least one exponential equals $e^m$, and every exponential is at most $e^m$.
</details>

<details>
<summary>Hint 2</summary>

For two terms, factor out the larger exponential. The smaller shifted exponent is the negative absolute difference.
</details>

## E0.03.08 Derive log-softmax and class NLL

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Derive stable log-softmax and class-index negative log-likelihood from logits.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper; NumPy for verification.
- **Assumptions:** $\boldsymbol{z}\in\mathbb{R}^{C}$, target $y\in\{1,\ldots,C\}$ in mathematics, and no class weighting or label smoothing.

### Problem

1. Define softmax and prove its components are positive and sum to one.
2. Derive
   $$
   \log\mathrm{softmax}(\boldsymbol{z})_c
   =z_c-\mathrm{LSE}(\boldsymbol{z}).
   $$
3. Using a one-hot target, reduce
   $$
   -\sum_c[c=y]\log p_c
   $$
   to a class-index NLL.
4. Derive the stable class loss
   $$
   -z_y+\mathrm{LSE}(\boldsymbol{z}).
   $$
5. Prove that adding the same constant to every logit changes neither softmax nor the class loss.
6. Compute log-softmax and the loss for $\boldsymbol{z}=(1000,999,998)$ with target class $1$.
7. Translate the target to Python indexing and state the input and output shapes for a batch of $B$ examples and $C$ classes.
8. Explain why this exercise is an NLL preview rather than a complete information-theory treatment of cross-entropy.

**Deliverable:** Derivation, invariance proof, hand calculation, and shape/index translation.

<details>
<summary>Hint 1</summary>

Take the logarithm of a quotient and recognize the denominator's log as LSE.
</details>

<details>
<summary>Hint 2</summary>

In a one-hot sum, every term except the target class is multiplied by zero. For shift invariance, factor $e^k$ from numerator and denominator.
</details>

## E0.03.09 Preserve small changes with log1p and expm1

- **Type:** experiment
- **Difficulty:** 3
- **Objective:** Diagnose cancellation near zero and select stable elementary functions.
- **Estimated time:** 25 minutes
- **Allowed tools:** Python 3 standard library and NumPy.
- **Assumptions:** Compare against algebraic expectations and, where useful, Python's `decimal` module with a stated precision.

### Problem

Investigate

$$
\log(1+x)
\quad\text{and}\quad
e^x-1
$$

for $x\in\{10^{-4},10^{-8},10^{-12},10^{-16},-10^{-12}\}$.

1. Compare `log(1 + x)` with `log1p(x)`.
2. Compare `exp(x) - 1` with `expm1(x)`.
3. Report absolute and relative error against a high-precision or series-based reference.
4. Identify the first listed positive $x$ for which forming `1 + x` loses all of $x$ in binary64.
5. Explain the cancellation mechanism in each naive expression.
6. Verify the local expectations $\log(1+x)\approx x$ and $e^x-1\approx x$ without claiming they are exact.
7. State the real domain of `log1p(x)` and test one invalid input deliberately, recording the library response.

**Deliverable:** Executable comparison table, error interpretation, and domain note.

<details>
<summary>Hint 1</summary>

Print more than the default number of digits and inspect whether `1.0 + x == 1.0`.
</details>

<details>
<summary>Hint 2</summary>

For a short independent reference, use the first few alternating terms of $\log(1+x)$ and positive terms of $e^x-1$, or use `decimal` consistently.
</details>

## E0.03.10 Implement a log-domain toolkit

- **Type:** implementation
- **Difficulty:** 4
- **Objective:** Implement and test stable product, addition, LSE, log-softmax, and class-NLL operations.
- **Estimated time:** 50 minutes
- **Allowed tools:** Python 3 and NumPy. SciPy may be used only as an optional comparison if already installed.
- **Assumptions:** Inputs to `log_product` are strictly positive. Reject empty inputs or define and document their behavior.

### Problem

Implement:

1. `log_product(values)` returning $\sum_i\log v_i$.
2. `logaddexp_pair(a, b)` using a max shift and `log1p`.
3. `logsumexp(values, axis=None, keepdims=False)` for NumPy arrays.
4. `log_softmax(logits, axis=-1)`.
5. `class_nll(logits, targets)` for a two-dimensional `(batch, classes)` array and zero-based class-index targets.

Your tests must include:

- hand-computed ordinary inputs;
- logits near $1000$ and $-1000$;
- shift invariance after adding a constant to every class in a row;
- LSE bounds for at least three vectors;
- agreement between `logaddexp_pair` and `numpy.logaddexp`;
- probabilities reconstructed from log-softmax summing to one;
- expected errors for an invalid target and a nonpositive product factor;
- dtype and shape checks.

If SciPy is installed, compare against `scipy.special.logsumexp` but do not make SciPy a requirement.

**Deliverable:** Executable implementation, assertions, API assumptions, and a concise test report.

<details>
<summary>Hint 1</summary>

For array LSE, compute the maximum with `keepdims=True`, perform the shifted reduction, then squeeze only if the public argument requests it.
</details>

<details>
<summary>Hint 2</summary>

For a pair, let $m=\max(a,b)$ and use $m+\log(1+e^{-|a-b|})$. For class NLL, gather one log-probability from each row.
</details>

## E0.03.11 Investigate growth crossovers visually

- **Type:** visual experiment
- **Difficulty:** 4
- **Objective:** Investigate growth crossovers while separating plotted evidence from asymptotic proof.
- **Estimated time:** 45 minutes
- **Allowed tools:** Python standard library; NumPy and a plotting library if already installed. A carefully labeled table is acceptable when plotting is unavailable.
- **Assumptions:** Every plot must label axes, transformations, function formulas, and the inspected range. Use line styles or markers in addition to color.

### Problem

Investigate the families $\log n$, $n^k$, and $a^n$.

1. Choose at least three $(k,a)$ pairs, including $(2,2)$, $(10,2)$, and one base $a$ between $1$ and $1.2$.
2. Before computing, predict which pair will have the latest apparent exponential crossover and explain why.
3. Search using log values so neither $n^k$ nor $a^n$ must be formed.
4. Report every crossing in the tested range, not only the first.
5. Plot either raw values where safe or a clearly labeled transformed vertical coordinate. Mark crossings and the search boundary.
6. Produce two windows for one pair: one that suggests polynomial dominance and one that reveals later exponential dominance.
7. Vary one control at a time to test the effect of $k$, $a$, and a multiplicative coefficient.
8. Write a conclusion with separate `Observation`, `Asymptotic result`, and `Limitation` paragraphs.

**Deliverable:** Hypotheses, controlled comparison table, accessible visual, code, observations, and limitations.

<details>
<summary>Hint 1</summary>

Compare $k\log n+\log c$ with $n\log a$ for $cn^k$ versus $a^n$.
</details>

<details>
<summary>Hint 2</summary>

A crossing occurs where the sign of the log difference changes. A first win need not be the final crossing.
</details>

## E0.03.12 Critique logarithm claims and sources

- **Type:** critique
- **Difficulty:** 4
- **Objective:** Repair mathematical, numerical, historical, and sourcing misconceptions.
- **Estimated time:** 35 minutes
- **Allowed tools:** Module references, official documentation, and source pages linked in the resource guide. Open every source used.
- **Assumptions:** Do not use search-result snippets or generated summaries as evidence.

### Problem

A draft lesson claims:

> Napier invented modern natural logarithms by himself in 1614, and Briggs later changed them to base 10 without Napier's involvement. Since logs turn every operation into addition, $\log(x+y)=\log x+\log y$. Taking a log leaves an optimization problem unchanged. A finite plot proves that $2^n$ is always larger than $n^{10}$. Python, calculators, and machine learning all use base-10 `log`. Softmax first exponentiates logits, so overflow is unavoidable. Max shifting is exact on a computer, and any shifted exponential that underflows makes the result invalid. Cross-entropy is always a different quantity from negative log-likelihood.

1. Identify at least twelve distinct errors, missing conditions, or unsupported claims.
2. Correct them in a table with columns `Claim`, `Diagnosis`, `Repair`, and `Evidence type`.
3. Support the historical correction using both the Napier and Briggs biographies.
4. Explain what the historical sources do and do not establish about modern base language.
5. Support at least two software-behavior corrections with official documentation.
6. Distinguish exact algebraic equivalence from floating-point behavior for max shifting.
7. Rewrite the paragraph accurately in at most 220 words.
8. List every opened URL and state which sentence it supports.

**Deliverable:** Diagnosis table, source ledger, and corrected paragraph.

<details>
<summary>Hint 1</summary>

Separate invention, publication, collaboration, table construction, and modern reinterpretation. Then separate algebra, asymptotics, objective ordering, numerical range, and API convention.
</details>

<details>
<summary>Hint 2</summary>

Taking logs preserves an argmax for positive likelihood because log is increasing. It does not preserve objective values, derivatives, or every optimizer step. A one-hot class target makes cross-entropy reduce to NLL for that target.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that your work includes:

- real-domain conditions for every fractional or negative exponent;
- original-domain substitution checks for logarithmic equations;
- units and model assumptions in growth calculations;
- the word `eventually` or equivalent asymptotic qualification in growth claims;
- a distinction between preserved argmax and changed objective geometry;
- dtype, shape, and range records for numerical experiments;
- LSE bounds and a max-shift derivation;
- zero-based target translation in code;
- error evidence for `log1p` and `expm1`;
- direct source inspection for every historical or API claim.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)
