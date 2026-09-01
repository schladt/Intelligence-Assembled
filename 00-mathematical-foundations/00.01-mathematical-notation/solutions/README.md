# Solutions for §0.01 Mathematical Notation

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Resources](../resources/README.md)

These are full worked solutions.
A correct route may use different words or intermediate steps, but it should preserve the same sets, terms, bounds, and shapes.

## E0.01.01 Parse the symbols

### Key idea

Translate each symbol into a set constraint or number-line operation before calculating.

### Reasoning

1. The interval $[-3,2)$ includes $-3$ and excludes $2$.
   Its integers are
   $$
   \{-3,-2,-1,0,1\}.
   $$

2. Using the smallest listed set:

   | Number | Smallest set | Reason |
   |---|---|---|
   | $-4$ | $\mathbb{Z}$ | integer but not natural |
   | $0$ | $\mathbb{N}$ | module convention includes zero |
   | $3/5$ | $\mathbb{Q}$ | ratio of integers, not an integer |
   | $\sqrt{2}$ | $\mathbb{R}$ | real and irrational |
   | $2+3i$ | $\mathbb{C}$ | nonreal complex number |

3. Distance from zero gives $|-2.7|=2.7$.
   The greatest integer at most $-2.7$ is $-3$, and the least integer at least $-2.7$ is $-2$:
   $$
   \lfloor-2.7\rfloor=-3,
   \qquad
   \lceil-2.7\rceil=-2.
   $$

4. The condition means that $x$ is less than two units from $3$:
   $$
   -2<x-3<2
   \iff
   1<x<5.
   $$
   Thus $x\in(1,5)$.

### Verification

Every listed integer satisfies $-3\le x<2$.
The floor and ceiling satisfy
$\lfloor x\rfloor\le x\le\lceil x\rceil$.
The endpoints $1$ and $5$ each have distance exactly $2$ from $3$, so the strict inequality excludes them.

### Common wrong turn

Do not "remove the decimal" to compute floor.
For negative values, truncation toward zero and floor are different operations.

## E0.01.02 Reindex without changing terms

### Key idea

Change bounds and every occurrence of the index with the same substitution.

### Reasoning

Set $j=i-1$, so $i=j+1$.
The old lower bound $i=2$ gives $j=1$, and $i=n+1$ gives $j=n$.
The summand becomes

$$
(i-1)x_i=jx_{j+1}.
$$

Therefore

$$
S=\sum_{j=1}^{n}j x_{j+1}.
$$

Before reindexing, the terms begin and end as

$$
1x_2+2x_3+3x_4+\cdots+nx_{n+1}.
$$

After reindexing they are

$$
1x_{1+1}+2x_{2+1}+3x_{3+1}+\cdots+nx_{n+1}.
$$

They match term for term.
The proposed $\sum_{j=1}^{n}jx_j$ instead begins with $x_1$ and ends with $nx_n$.
It shifts the data values while keeping the coefficients, so it is a different sum.

### Verification

Take $n=2$.
The original is $x_2+2x_3$, and the corrected reindexing is also $x_2+2x_3$.
The incorrect proposal is $x_1+2x_2$.

### Common wrong turn

Renaming a dummy index is free, but shifting an index is not mere renaming.
A shift changes the bounds and the subscripted object.

## E0.01.03 Split and telescope

### Key idea

A split partitions one index range into two disjoint adjacent ranges.

### Reasoning

The requested split is

$$
\sum_{k=0}^{T-1}(a_{k+1}-a_k)
=
\sum_{k=0}^{r-1}(a_{k+1}-a_k)
+
\sum_{k=r}^{T-1}(a_{k+1}-a_k).
$$

The first part telescopes to $a_r-a_0$.
The second telescopes to $a_T-a_r$.
Combining gives

$$
(a_r-a_0)+(a_T-a_r)=a_T-a_0.
$$

The artificial boundary $a_r$ appears once with each sign and cancels.
If the second range began at $r+1$, the term with $k=r$ would be missing.
That omitted term is $a_{r+1}-a_r$.

### Verification

The original range has $T$ indices: $0$ through $T-1$.
The two correct pieces contain $r$ and $T-r$ indices, totaling $T$.

### Common wrong turn

Do not split both pieces at $r$ inclusively.
That would count the $k=r$ term twice if the first upper bound were also $r$.

## E0.01.04 Reverse a triangular sum

### Key idea

Rewrite the set of index pairs, then describe that same set in the opposite order.

### Reasoning

The original bounds say

$$
1\le i\le n,
\qquad
0\le j\le i-1.
$$

Equivalently,

$$
0\le j<i\le n.
$$

For $n=4$, the pairs are

$$
(1,0),
(2,0),(2,1),
(3,0),(3,1),(3,2),
(4,0),(4,1),(4,2),(4,3).
$$

Across the region, $j$ ranges from $0$ through $n-1$.
For fixed $j$, the inequality $j<i$ makes the smallest $i$ equal to $j+1$, while the largest remains $n$.
Thus

$$
S_n
=
\sum_{j=0}^{n-1}\sum_{i=j+1}^{n}a_{ij}.
$$

For $n=4$, grouping by $j$ gives:

- $j=0$: $i=1,2,3,4$;
- $j=1$: $i=2,3,4$;
- $j=2$: $i=3,4$;
- $j=3$: $i=4$.

A rectangular rewrite includes pairs such as $(1,1)$ and $(1,4)$ that violate $j<i$.

### Verification

Both forms contain

$$
1+2+\cdots+n=\frac{n(n+1)}{2}
$$

terms, and the explicit $n=4$ lists match.

### Common wrong turn

Swapping sigma symbols without recomputing dependent bounds changes a triangular region into a different region.

### Alternate route

Draw rows indexed by $i$ and columns by $j$.
Mark cells below the strict diagonal $j=i$.
Reading marked cells by columns gives the reversed bounds directly.

## E0.01.05 Empty boundaries

### Key idea

Use the identity element of the operation when there are no terms.

### Reasoning

The standard values are

$$
S_0=0,
\qquad
P_0=1.
$$

At $n=1$,

$$
S_1=S_0+x_1=0+x_1=x_1,
$$

and

$$
P_1=P_0x_1=1\cdot x_1=x_1.
$$

If $P_0$ were zero, the recurrence would give $P_1=0\cdot x_1=0$, which is wrong for general $x_1$.
Zero gates should have combined neutral multiplier $1$ because no gate changes the incoming value.

### Verification

The empty values preserve the same recurrences used for all positive $n$.
That uniformity is the point of the convention.

### Common wrong turn

"There is nothing, so the answer is zero" fits addition but not multiplication.
Always ask for the operation's identity.

## E0.01.06 Function anatomy

### Key idea

Keep declarations, attained outputs, set preimages, and composition compatibility separate.

### Reasoning

1. For $f:\mathbb{R}\to\mathbb{R}$, the domain and codomain are both $\mathbb{R}$.
   Since $x^2\ge0$,
   $$
   f(x)=x^2-1\ge-1.
   $$
   Every value at least $-1$ is attained, so the image is $[-1,\infty)$.

2. The preimage condition is
   $$
   0\le x^2-1\le3.
   $$
   Adding one gives $1\le x^2\le4$, so
   $$
   f^{-1}([0,3])=[-2,-1]\cup[1,2].
   $$

3. One valid restriction is
   $$
   f|_{[0,\infty)}:[0,\infty)\to\mathbb{R}.
   $$
   It is one-to-one and has image $[-1,\infty)$.
   Restricting to $(-\infty,0]$ also works.

4. The inner function in $f\circ g$ is $g$, whose outputs are real and therefore valid inputs to $f$.
   So $f\circ g$ is defined on all $[0,\infty)$.
   For $g\circ f$, $g$ requires a nonnegative input, so we need
   $$
   f(x)=x^2-1\ge0.
   $$
   A valid domain is $(-\infty,-1]\cup[1,\infty)$.

5. The identity laws are
   $$
   f\circ\operatorname{id}_{\mathbb{R}}=f,
   \qquad
   \operatorname{id}_{\mathbb{R}}\circ f=f.
   $$

### Verification

For the preimage endpoints, $f(\pm1)=0$ and $f(\pm2)=3$.
For $g\circ f$, an excluded point such as $x=0$ would require $g(-1)$, which is outside $g$'s real domain.

### Common wrong turn

The arrow's right side is the codomain, not a promise that every codomain value is attained.

## E0.01.07 Accuracy as algebra

### Key idea

A zero-one condition can be summed to count and averaged to form a rate.

### Reasoning

Let the six predictions and labels be $\widehat{y}_i$ and $y_i$.
Accuracy is

$$
\frac{1}{6}\sum_{i=1}^{6}[\widehat{y}_i=y_i].
$$

The comparison values are

$$
(1,0,1,0,1,1).
$$

Their sum is $4$, so accuracy is

$$
\frac{4}{6}=\frac{2}{3}.
$$

Let $A=\{2\}$.
The number of predictions equal to class $2$ is

$$
\sum_{i=1}^{6}\mathbf{1}_{A}(\widehat{y}_i).
$$

Using a Kronecker delta, the same count is

$$
\sum_{i=1}^{6}\delta_{\widehat{y}_i,2}.
$$

Both evaluate to $2$.
Counting correct predictions produces a scalar.
Selecting correctly predicted examples uses the same condition as a mask and returns the corresponding examples or indices.

### Verification

The correct positions are $1,3,5,6$ under one-based indexing.
The predicted class $2$ occurs at positions $3$ and $4$.

### Common wrong turn

Do not divide a class count by $n$ unless the requested quantity is a class frequency rather than a count.

## E0.01.08 Expand Einstein notation

### Key idea

Repeated indices are contracted; free indices remain as output coordinates.

### Reasoning

1. Since $j$ ranges over three columns,
   $$
   y_i=A_{ij}x_j
   =\sum_{j=1}^{3}A_{ij}x_j,
   \qquad i\in\{1,2\}.
   $$
   Thus $\boldsymbol{y}$ has shape $(2,)$.

2. Matrix multiplication expands as
   $$
   C_{ik}=A_{ij}B_{jk}
   =\sum_{j=1}^{3}A_{ij}B_{jk},
   $$
   with $i\in\{1,2\}$ and $k\in\{1,2\}$.
   Therefore $\mathbf{C}$ has shape $2\times2$.

3. Compute the components:
   $$
   y_1=1(2)+0(1)+2(-1)=0,
   $$
   $$
   y_2=-1(2)+3(1)+1(-1)=0.
   $$
   Hence
   $$
   \boldsymbol{y}=\begin{bmatrix}0\\0\end{bmatrix}.
   $$

4. Diagnoses:

   - $z=A_{ij}x_j$ is invalid as a scalar equation because $i$ is free on the right but absent on the left. It could be repaired as $z_i=A_{ij}x_j$.
   - $D_{ij}=A_{ik}B_{kj}+x_i$ is shape-inconsistent unless $x_i$ is intended to broadcast across $j$ and that convention is stated. In strict component notation, use a term carrying both free indices, such as $x_i\mathbf{1}_j$, with the all-ones object defined.
   - $q_i=A_{ij}x_jx_j$ has $j$ three times in one term and is ambiguous under standard Einstein notation. Use explicit sums or distinct indices according to the intended operation.

### Verification

The free-index sets agree on both sides of the two valid equations.
The numerical result also equals ordinary matrix-vector multiplication.

### Common wrong turn

Do not treat every repeated-looking letter as automatically legal.
Count occurrences per multiplicative term.

## E0.01.09 Translate math and code

### Key idea

Make the mathematical range and resulting shape explicit in code, then assert a hand-computed result.

### Reasoning

1. Sum of squares:

```python
n = 5
square_sum = sum(i**2 for i in range(1, n + 1))
assert square_sum == 55
```

2. Product:

```python
from math import prod

probabilities = [0.5, 0.25, 0.8]
probability_product = prod(probabilities)
assert probability_product == 0.1
```

3. Accuracy:

```python
import numpy as np

predicted = np.array([1, 0, 2, 2, 1, 0])
actual = np.array([1, 2, 2, 0, 1, 0])
accuracy = (predicted == actual).mean()
assert np.isclose(accuracy, 2 / 3)
```

4. Final time step:

```python
import numpy as np

array = np.arange(24).reshape(2, 3, 4)
final_step = array[:, -1, :]
assert final_step.shape == (2, 4)
assert final_step.tolist() == [[8, 9, 10, 11], [20, 21, 22, 23]]
```

5. In part 1, Python must be told to include $n$ because the stop value is excluded.
   In part 4, `-1` selects the final zero-based position without needing to translate $T$ into `T - 1` explicitly.
   The integer index removes the time axis.

### Verification

The sum is $1+4+9+16+25=55$.
The product is $0.5\cdot0.25\cdot0.8=0.1$.
The final-step values are the last four entries in each batch block.

### Common wrong turn

`range(1, n)` stops at $n-1$ and omits the final mathematical term.
Also, `array[:, -1]` is valid here, but writing the final colon makes the retained feature axis explicit.

## E0.01.10 Repair ambiguous notation

### Key idea

Give each semantic axis one symbol, state shapes, and reserve superscript parentheses for labels such as layers and iterations.

### Reasoning

Problems in the draft include:

1. $t$ means both layer and training step.
2. The phrase "token $i$" conflicts with the required token-position convention $t$.
3. $x_i^t$ does not reveal whether $x$ is a scalar or vector.
4. $W^t_{ij}$ overloads $t$ and does not state matrix shape.
5. The update uses $x^t$ on both sides without distinguishing old and new values.
6. $L^2$ looks like a squared loss rather than a loss label.
7. The range of $\sum_i$ is absent.
8. $f^{-1}(x_i)$ could mean inverse function or preimage, but $x_i$ appears to be an element rather than a set.
9. The bracket compares a label $y_i$ with an object of undeclared type.
10. The contraction ranges and output shape are unstated.

One valid rewrite is:

> Let $\boldsymbol{h}_{t}^{(\ell,k)}\in\mathbb{R}^{d}$ denote the representation at token position $t\in\{1,\ldots,T\}$, layer $\ell\in\{0,\ldots,L\}$, and optimization iteration $k$. Let $\mathbf{W}^{(\ell,k)}\in\mathbb{R}^{d\times d}$. A linear layer update is
> $$
> h_{t,i}^{(\ell+1,k)}
> =
> \sum_{j=1}^{d}W_{ij}^{(\ell,k)}h_{t,j}^{(\ell,k)}.
> $$
> If $c:\mathbb{R}^{d}\to\{1,\ldots,C\}$ is a classifier and $y_t$ is the target label, define the error count
> $$
> L_{\mathrm{count}}
> \coloneqq
> \sum_{t=1}^{T}
> [y_t\ne c(\boldsymbol{h}_{t}^{(L,k)})].
> $$

This version avoids $f^{-1}$ because classification, not inversion or preimage, is the intended operation.
Einstein notation could replace the explicit sum if the local convention were stated.

### Verification

On the update's right side, $j$ is contracted and the free indices $t,i,\ell,k$ correspond to the left side after accounting for the layer increment.
The classifier consumes a vector in $\mathbb{R}^{d}$ and returns a label comparable with $y_t$.
The bracket returns a scalar zero or one, so the sum is scalar.

### Common wrong turn

Changing fonts without separating semantic roles does not resolve ambiguity.
The repair must make types, ranges, and state transitions reconstructible.

### Alternate route

If the intended objective is mean error rather than count, define

$$
L_{\mathrm{error}}
\coloneqq
\frac{1}{T}\sum_{t=1}^{T}
[y_t\ne c(\boldsymbol{h}_{t}^{(L,k)})].
$$

That change is semantic, not cosmetic, and should be stated.

## E0.01.11 Paper-notation archaeology

### Key idea

There is no single fixed answer.
A strong submission proves that the reader can reconstruct each paper's objects and equations without silently inventing meanings.

### Reasoning

A complete response should contain:

- two stable bibliographic links to publicly accessible papers;
- at least eight symbol entries per paper with type, role, range, and shape where applicable;
- one central equation from each paper decomposed into inputs, operations, bound indices, free indices, and output;
- a translation that follows this project's scalar, vector, matrix, array, and iteration conventions;
- explicit notes on every inferred fact not stated by the authors;
- a comparison that separates visual preference from error-detection value.

A useful symbol-table row looks like this:

| Original symbol | Paper meaning | Type or shape | Project translation | Evidence |
|---|---|---|---|---|
| $X$ | token representations | $T\times d$ matrix | $\mathbf{X}$ | equation dimensions and prose |

A useful translation log distinguishes:

- **Cosmetic:** replacing an unbolded vector $x$ with $\boldsymbol{x}$.
- **Structural:** adding explicit bounds to $\sum_i$.
- **Meaning-changing:** discovering that a superscript thought to be a power actually denotes a layer.

The final judgment should cite concrete consequences.
For example, "Paper A was easier" is weak.
"Paper A declared $\mathbf{X}\in\mathbb{R}^{T\times d}$ before attention, so every matrix product could be shape-checked; Paper B required inferring whether examples occupied rows or columns" is evaluable.

### Verification

A reviewer should be able to use the submitted symbol tables to reconstruct both chosen equations without reopening the papers.
Every inferred shape should satisfy the operations in its equation.
Every source link should resolve to the claimed paper.

### Common wrong turn

Do not summarize the papers' methods or results instead of analyzing notation.
The activity is about the interface between symbols and meaning.

### Alternate route

If neither paper has a named notation section, use the first pages on which symbols are introduced.
Document that choice and keep the same deliverables.

## Solution-set check

All exercise IDs and titles mirror the [exercise index](../exercises/README.md):

- E0.01.01 Parse the symbols
- E0.01.02 Reindex without changing terms
- E0.01.03 Split and telescope
- E0.01.04 Reverse a triangular sum
- E0.01.05 Empty boundaries
- E0.01.06 Function anatomy
- E0.01.07 Accuracy as algebra
- E0.01.08 Expand Einstein notation
- E0.01.09 Translate math and code
- E0.01.10 Repair ambiguous notation
- E0.01.11 Paper-notation archaeology

[Back to module](../README.md) | [Exercise set](../exercises/README.md)
