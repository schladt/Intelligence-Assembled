# Exercises for §0.02 Algebra, Functions, and Precalculus Backfill

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. The hints become progressively more specific but do not state final answers. Difficulty follows the project's 1 through 5 scale.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.02.01 | Change form without changing meaning | calculation | 1 | expand, factor, and preserve restrictions | 15 min |
| E0.02.02 | Roots, holes, and asymptotes | applied | 2 | analyze polynomial and rational behavior | 25 min |
| E0.02.03 | Complete the square and find the range | derivation | 2 | complete the square and reason about range | 20 min |
| E0.02.04 | Transform a parent function | visual | 2 | construct and interpret transformations | 25 min |
| E0.02.05 | Compose, restrict, and invert | derivation | 3 | track composition domains and inverses | 30 min |
| E0.02.06 | Decompose a rational function | calculation | 3 | compute and verify partial fractions | 25 min |
| E0.02.07 | Radians and inverse trigonometry | calculation | 2 | use radians and principal inverse ranges | 20 min |
| E0.02.08 | Multiply in the complex plane | calculation | 2 | use conjugates, modulus, and polar form | 25 min |
| E0.02.09 | Investigate roots of unity | derivation | 3 | construct and verify roots of unity | 30 min |
| E0.02.10 | Compare tanh and sigmoid | applied | 3 | analyze hyperbolic and logistic functions | 30 min |
| E0.02.11 | Build a transformation laboratory | implementation | 4 | implement and test visual transformations | 50 min |
| E0.02.12 | Critique a chain of misconceptions | critique | 3 | diagnose algebra and function errors | 30 min |

## E0.02.01 Change form without changing meaning

- **Type:** calculation
- **Difficulty:** 1
- **Objective:** Expand, factor, simplify, and preserve restrictions.
- **Estimated time:** 15 minutes
- **Allowed tools:** Pencil and paper; calculator optional.
- **Assumptions:** Work over the real numbers.

### Problem

For each expression, produce the requested form and state any input restrictions.

1. Expand $(2x-5)(x+3)$ and verify the constant and linear coefficients separately.
2. Factor $6x^2-x-2$ completely over the integers.
3. Simplify
   $$
   \frac{x^2-5x+6}{x^2-4}
   $$
   as far as possible, while preserving the original domain.
4. Explain which form in parts 1 through 3 makes roots easiest to see and which makes coefficients easiest to see.

**Deliverable:** Three transformed expressions, a domain statement for part 3, and a two-sentence representation comparison.

<details>
<summary>Hint 1</summary>

For part 2, seek two numbers whose product is $6(-2)$ and whose sum is $-1$.
</details>

<details>
<summary>Hint 2</summary>

Factor the numerator and denominator in part 3 before canceling. Record every denominator zero before changing the formula.
</details>

## E0.02.02 Roots, holes, and asymptotes

- **Type:** applied
- **Difficulty:** 2
- **Objective:** Analyze polynomial multiplicity, rational discontinuities, and end behavior.
- **Estimated time:** 25 minutes
- **Allowed tools:** Pencil and paper; graphing software only for the final verification.
- **Assumptions:** All graph statements concern real inputs and outputs.

### Problem

Let

$$
p(x)=-2(x+2)^2(x-1)^3
$$

and

$$
r(x)=\frac{(x+2)(x-1)}{(x+2)(x-3)^2}.
$$

1. List every real root of $p$, with multiplicity.
2. Predict whether the graph of $p$ crosses or touches the horizontal axis at each root.
3. State the left and right end behavior of $p$.
4. State the original domain of $r$.
5. Classify each excluded input of $r$ as a hole or a vertical asymptote. Give the hole's coordinate when one exists.
6. State the horizontal asymptote of $r$.
7. Use a graph only after completing the analysis. Report whether it agrees and identify one feature a coarse plotting window could hide.

**Deliverable:** A compact sign and behavior table plus the graph-verification note.

<details>
<summary>Hint 1</summary>

Use multiplicity parity for $p$. For end behavior, multiply the degrees and leading coefficients of the factors.
</details>

<details>
<summary>Hint 2</summary>

For $r$, cancel only after recording the original excluded inputs. A canceled zero and a remaining denominator zero behave differently.
</details>

## E0.02.03 Complete the square and find the range

- **Type:** derivation
- **Difficulty:** 2
- **Objective:** Complete the square and infer a quadratic's vertex, range, and roots.
- **Estimated time:** 20 minutes
- **Allowed tools:** Pencil and paper.
- **Assumptions:** Work over the real numbers until asked about complex roots.

### Problem

Consider

$$
f(x)=-3x^2+12x-7.
$$

1. Complete the square, showing what you add and subtract inside the expression.
2. State the vertex, axis of symmetry, and real range.
3. Solve $f(x)=0$ from the completed-square form.
4. Compute the discriminant from the expanded form and reconcile it with your number of real roots.
5. Replace the constant term $-7$ by $-13$. Without repeating every step, determine whether the new quadratic has two, one, or no real roots, then state its complex roots if needed.

**Deliverable:** A derivation, geometric interpretation, and discriminant cross-check.

<details>
<summary>Hint 1</summary>

Factor $-3$ from the quadratic and linear terms before completing the square.
</details>

<details>
<summary>Hint 2</summary>

After writing vertex form, set it equal to zero. The sign of the remaining squared quantity decides whether real roots exist.
</details>

## E0.02.04 Transform a parent function

- **Type:** visual
- **Difficulty:** 2
- **Objective:** Construct and interpret horizontal and vertical transformations.
- **Estimated time:** 25 minutes
- **Allowed tools:** Graph paper or plotting software.
- **Assumptions:** Use $f(x)=|x|$ as the parent function.

### Problem

Define

$$
g(x)=-\frac{1}{2}f(2(x-3))+4.
$$

1. Describe every transformation from $f$ to $g$, distinguishing input changes from output changes.
2. Transform the parent landmarks $(-2,2)$, $(0,0)$, and $(2,2)$ into landmarks of $g$.
3. State the domain and range of $g$.
4. Sketch both functions on the same labeled axes. Use a solid line for $f$ and a dashed line for $g$ so the distinction does not depend on color.
5. A classmate says the factor $2$ makes the graph twice as wide. Diagnose the error using one landmark.

**Deliverable:** Transformation sequence, landmark table, domain and range, and accessible sketch.

<details>
<summary>Hint 1</summary>

To transform a parent point $(u,f(u))$, solve $2(x-3)=u$ for the new horizontal coordinate.
</details>

<details>
<summary>Hint 2</summary>

The outside factor acts on the old output; the final $+4$ then shifts that output.
</details>

## E0.02.05 Compose, restrict, and invert

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Track composition order, natural domains, and restrictions needed for inverses.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper.
- **Assumptions:** Functions are real-valued.

### Problem

Let

$$
f(x)=(x-1)^2,
\qquad
g(x)=\sqrt{x+2}.
$$

1. Find formulas and natural domains for $f\circ g$ and $g\circ f$.
2. Give one input that lies in one composition domain but not the other, or prove that no such input exists in one direction.
3. Explain why $f$ has no inverse function on all of $\mathbb{R}$.
4. Restrict $f$ to $[1,\infty)$, choose a codomain that makes it bijective, and derive its inverse.
5. Repeat part 4 using the restriction $(-\infty,1]$.
6. Verify both inverse formulas by composing in both orders on their stated domains.

**Deliverable:** Two composition analyses and two fully declared restricted inverses.

<details>
<summary>Hint 1</summary>

In each composition, write the outer function's input constraint after substituting the inner formula.
</details>

<details>
<summary>Hint 2</summary>

When solving $y=(x-1)^2$, the sign of $x-1$ is fixed by the chosen domain restriction.
</details>

## E0.02.06 Decompose a rational function

- **Type:** calculation
- **Difficulty:** 3
- **Objective:** Compute and verify a partial-fraction decomposition with a repeated factor.
- **Estimated time:** 25 minutes
- **Allowed tools:** Pencil and paper; symbolic software only for verification.
- **Assumptions:** Work over the real numbers and preserve the original domain.

### Problem

Decompose

$$
\frac{2x^2+3x+5}{(x-1)^2(x+2)}
$$

into partial fractions.

1. Write the complete proposed form before solving coefficients.
2. Clear denominators and solve for every coefficient. Use substitutions and coefficient comparison as appropriate.
3. Recombine your result over a common denominator.
4. Verify the numerator term by term.
5. State the excluded inputs and explain why decomposition does not remove them.
6. Name one later calculus operation that becomes easier after this decomposition.

**Deliverable:** Coefficient derivation, recombination verification, and domain statement.

<details>
<summary>Hint 1</summary>

A repeated factor $(x-1)^2$ requires terms for both $(x-1)$ and $(x-1)^2$.
</details>

<details>
<summary>Hint 2</summary>

After clearing denominators, substituting each distinct denominator zero isolates some coefficients. Use one more convenient input or compare coefficients for the rest.
</details>

## E0.02.07 Radians and inverse trigonometry

- **Type:** calculation
- **Difficulty:** 2
- **Objective:** Convert radians, use core identities, and respect principal inverse ranges.
- **Estimated time:** 20 minutes
- **Allowed tools:** Unit-circle table; no calculator needed.
- **Assumptions:** Angles are in radians unless explicitly labeled otherwise.

### Problem

1. Convert $150$ degrees and $-45$ degrees to radians.
2. Convert $7\pi/6$ radians to degrees.
3. Evaluate exactly:
   $$
   \sin(5\pi/6),\qquad
   \cos(5\pi/6),\qquad
   \tan(5\pi/6).
   $$
4. Evaluate exactly:
   $$
   \arcsin(\sin(5\pi/6)),
   \qquad
   \arccos(\cos(5\pi/6)),
   \qquad
   \arctan(\tan(5\pi/6)).
   $$
5. Explain why the three outer inverse functions do not all return the original angle.
6. Verify the cosine value using an addition identity rather than a memorized unit-circle coordinate.

**Deliverable:** Exact values and a principal-range explanation.

<details>
<summary>Hint 1</summary>

Use $180$ degrees $=\pi$ radians and identify the reference angle for $5\pi/6$.
</details>

<details>
<summary>Hint 2</summary>

Before applying an inverse, write its principal output interval. Find the coterminal or reflected angle in that interval.
</details>

## E0.02.08 Multiply in the complex plane

- **Type:** calculation
- **Difficulty:** 2
- **Objective:** Use conjugates, modulus, polar form, multiplication, and division.
- **Estimated time:** 25 minutes
- **Allowed tools:** Pencil and paper; calculator for decimal checking only.
- **Assumptions:** Principal arguments may be stated in $(-\pi,\pi]$.

### Problem

Let $z=1+\sqrt{3}i$ and $w=-1+i$.

1. Compute $\overline{z}$, $|z|$, and $z\overline{z}$.
2. Convert $z$ and $w$ to polar form with exact moduli and arguments.
3. Compute $zw$ in polar form, then convert it to rectangular form.
4. Compute $z/w$ by multiplying numerator and denominator by $\overline{w}$.
5. Compute $z/w$ again in polar form and reconcile the two forms.
6. Describe the scale and rotation applied when any complex number is multiplied by $z$.

**Deliverable:** Exact rectangular and polar calculations plus a geometric interpretation.

<details>
<summary>Hint 1</summary>

Plot each point by quadrant before choosing an argument. The tangent ratio alone does not identify a quadrant.
</details>

<details>
<summary>Hint 2</summary>

In polar form, multiplication adds arguments and division subtracts them. Normalize an argument by adding or subtracting $2\pi$ when useful.
</details>

## E0.02.09 Investigate roots of unity

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Construct, verify, and interpret roots of unity.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper; a short standard-library or NumPy check is optional.
- **Assumptions:** Use Euler's formula and exact symbolic values where practical.

### Problem

Work with the sixth roots of unity.

1. Derive the general formula from $z^6=1$ in polar form.
2. List all six roots in exponential form.
3. Convert them to rectangular form.
4. Verify directly that the root with argument $\pi/3$ has sixth power $1$.
5. Show that multiplication by that root permutes the six-root set.
6. Show that the sum of all six roots is zero using either geometry or a finite geometric sum. State why your method is valid.
7. Explain, in one precise sentence, how roots of unity connect to Fourier analysis without claiming that the picture alone proves Fourier theory.

**Deliverable:** Derivation, exact root list, two algebraic verifications, and the connection sentence.

<details>
<summary>Hint 1</summary>

Write $1=e^{i2\pi m}$, divide every possible argument by $6$, and reduce modulo $2\pi$.
</details>

<details>
<summary>Hint 2</summary>

For the sum, let $\omega=e^{i2\pi/6}$ and use $1+\omega+\cdots+\omega^5$ together with $\omega^6=1$ and $\omega\ne1$.
</details>

## E0.02.10 Compare tanh and sigmoid

- **Type:** applied
- **Difficulty:** 3
- **Objective:** Analyze domains, ranges, limits, and the exact relation between tanh and sigmoid.
- **Estimated time:** 30 minutes
- **Allowed tools:** Algebra and a calculator or plotting tool for verification.
- **Assumptions:** You may use the exponential definitions from the module.

### Problem

Let

$$
s(x)=\frac{1}{1+e^{-x}},
\qquad
h(x)=\tanh x.
$$

1. Prove from the formulas that $s(x)\in(0,1)$ and $h(x)\in(-1,1)$ for every real $x$.
2. Derive $s(x)=(1+h(x/2))/2$ using algebra only.
3. State the limits of both functions as $x\to\infty$ and $x\to-\infty$.
4. Evaluate $s(0)$ and $h(0)$ and compare the centers of their ranges.
5. Solve $p=s(x)$ for $x$ and state the domain of the inverse expression.
6. Make a value table at $x\in\{-4,-2,0,2,4\}$ to three decimal places. Identify where each function appears saturated.
7. Critique: "Tanh and sigmoid are the same activation because one can be rescaled into the other." State what is mathematically exact and what practical distinctions remain.

**Deliverable:** Algebraic derivation, range and limit analysis, value table, and a careful critique.

<details>
<summary>Hint 1</summary>

For the ranges, note that $e^x$ is positive. Compare numerator and denominator rather than relying on a graph.
</details>

<details>
<summary>Hint 2</summary>

To derive the relation, rewrite tanh using $e^x$ after substituting $x/2$, then simplify $(1+\tanh(x/2))/2$.
</details>

## E0.02.11 Build a transformation laboratory

- **Type:** implementation
- **Difficulty:** 4
- **Objective:** Implement transformed functions and test visual predictions.
- **Estimated time:** 50 minutes
- **Allowed tools:** Python standard library; NumPy and a plotting library are allowed.
- **Assumptions:** If plotting is unavailable, submit sampled tables and an ASCII or hand-drawn graph. State package versions if you execute code.

### Problem

Implement

$$
g(x)=a f(b(x-h))+k
$$

for a supplied scalar function `f`.

1. Write a function with named parameters for $a$, $b$, $h$, and $k$.
2. Test it with $f(x)=x^2$ at three hand-computed inputs.
3. Generate comparable samples for the parent and at least four transformations, changing one parameter at a time.
4. Visualize or tabulate the samples over a stated interval.
5. Test these hypotheses:
   - changing $h$ translates identifiable landmarks by $h$;
   - changing $k$ adds $k$ to every sampled output;
   - replacing $a$ by $-a$ reflects outputs;
   - doubling $|b|$ halves horizontal distances between corresponding landmarks.
6. Repeat one test with $f(x)=\sin x$ or $f(x)=\tanh x$. Explain one ambiguity caused by periodicity or saturation.
7. Include assertions, labels, and a short conclusion separating observed evidence from a general proof.

**Deliverable:** Executable snippet, assertions, visual or table, parameter record, observations, and limitations.

<details>
<summary>Hint 1</summary>

Compute `inner = b * (x - h)` before calling `f`; then apply the outside scale and shift.
</details>

<details>
<summary>Hint 2</summary>

Landmarks are more reliable than comparing arbitrary pixels. For $x^2$, use the vertex and points at a fixed height. For sine, use zeros and peaks.
</details>

## E0.02.12 Critique a chain of misconceptions

- **Type:** critique
- **Difficulty:** 3
- **Objective:** Diagnose algebraic, functional, trigonometric, hyperbolic, and complex-number errors.
- **Estimated time:** 30 minutes
- **Allowed tools:** Module notes; no computer required.
- **Assumptions:** Interpret all unqualified functions as real-valued.

### Problem

A draft solution claims:

> Since $(x^2-1)/(x-1)=x+1$, the two functions have the same domain. Every cubic has three distinct real roots by the fundamental theorem of algebra. Also, $f(x-2)$ shifts a graph left by two. Because squaring has inverse $\sqrt{x}$, $\sqrt{x^2}=x$ for every real $x$. Angles have no units, so $\sin(90)=1$ in ordinary mathematical software. Since $\arcsin$ undoes sine, $\arcsin(\sin(3\pi/4))=3\pi/4$. Hyperbolic functions describe circles with a different parameter, and $\tanh x$ reaches $1$ once $x$ is large enough. Finally, $i$ was invented by Descartes, every complex number has one unique argument, and multiplying by $i$ reflects a point across the imaginary axis.

1. Identify at least ten distinct errors or unsupported claims.
2. Correct each one in a numbered table with columns `Claim`, `Diagnosis`, and `Repair`.
3. Supply a counterexample or domain statement for at least six repairs.
4. Rewrite the paragraph as accurate prose of at most 180 words.
5. Mark which corrected statements are algebraic facts, convention-sensitive statements, or historical claims requiring a source.

**Deliverable:** Diagnosis table, evidence, and corrected paragraph.

<details>
<summary>Hint 1</summary>

Check domains, multiplicity, coefficient fields, transformation direction, principal inverse ranges, angle units, limiting values, and argument periodicity separately.
</details>

<details>
<summary>Hint 2</summary>

For the historical sentence, correction may mean removing an unsupported priority claim and replacing it with a source-backed distributed history.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that your work includes:

- every original domain restriction after simplification;
- multiplicities rather than only distinct roots;
- principal ranges for inverse trigonometric functions;
- declared domains and codomains for inverse functions;
- both rectangular and polar checks for complex arithmetic;
- tolerances and residuals for any floating-point verification;
- labeled, non-color-dependent visual distinctions;
- a distinction between evidence, theorem, and analogy.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)
