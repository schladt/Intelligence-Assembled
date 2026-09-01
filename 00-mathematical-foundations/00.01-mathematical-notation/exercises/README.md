# Exercises for §0.01 Mathematical Notation

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set.
The index below describes the task and offers progressive hints, but it does not reveal answers.
Difficulty follows the project's 1 through 5 scale.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.01.01 | Parse the symbols | conceptual | 1 | classify numbers and intervals | 10 min |
| E0.01.02 | Reindex without changing terms | derivation | 2 | reindex a finite sum | 15 min |
| E0.01.03 | Split and telescope | calculation | 2 | split and telescope sums | 15 min |
| E0.01.04 | Reverse a triangular sum | derivation | 3 | swap double-sum order | 25 min |
| E0.01.05 | Empty boundaries | conceptual | 2 | use empty sums and products | 15 min |
| E0.01.06 | Function anatomy | conceptual | 2 | distinguish function objects | 20 min |
| E0.01.07 | Accuracy as algebra | applied | 2 | use indicator notation | 15 min |
| E0.01.08 | Expand Einstein notation | calculation | 3 | expand contractions and infer shape | 20 min |
| E0.01.09 | Translate math and code | implementation | 3 | map indices, masks, and shapes | 25 min |
| E0.01.10 | Repair ambiguous notation | critique | 3 | diagnose overloaded indices | 25 min |
| E0.01.11 | Paper-notation archaeology | experiment | 4 | reconstruct a paper's notation | 45 min |

## E0.01.01 Parse the symbols

- **Type:** conceptual
- **Difficulty:** 1
- **Objective:** Classify numbers and interpret intervals, absolute value, floor, and ceiling.
- **Estimated time:** 10 minutes
- **Allowed tools:** Notes and a number line; no calculator needed.

### Problem

For each item, state the requested set or value and give one sentence of reasoning.
Use the module convention $0\in\mathbb{N}$.

1. List every integer in $[-3,2)$.
2. For each of $-4$, $0$, $3/5$, $\sqrt{2}$, and $2+3i$, name the smallest set among $\mathbb{N},\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$ that contains it.
3. Evaluate $|-2.7|$, $\lfloor-2.7\rfloor$, and $\lceil-2.7\rceil$.
4. Rewrite $|x-3|<2$ as an open interval condition on $x$.

<details>
<summary>Hint 1</summary>

Translate interval brackets into inequalities before listing integers.
</details>

<details>
<summary>Hint 2</summary>

For the last part, read absolute value as distance from $3$.
</details>

## E0.01.02 Reindex without changing terms

- **Type:** derivation
- **Difficulty:** 2
- **Objective:** Reindex a finite sum while preserving every term.
- **Estimated time:** 15 minutes
- **Allowed tools:** Pencil and paper.

### Problem

Let

$$
S=\sum_{i=2}^{n+1}(i-1)x_i.
$$

1. Reindex the sum using $j=i-1$.
2. Expand the first three and final terms before and after reindexing to verify that they match.
3. Explain exactly why $\sum_{j=1}^{n}j x_j$ is not equivalent to $S$.

<details>
<summary>Hint 1</summary>

Build a four-row table for old index, substitution, new bounds, and new summand.
</details>

<details>
<summary>Hint 2</summary>

After substituting, every occurrence of $i$ must be expressed in terms of $j$.
</details>

## E0.01.03 Split and telescope

- **Type:** calculation
- **Difficulty:** 2
- **Objective:** Split a sum at a boundary and identify telescoping cancellation.
- **Estimated time:** 15 minutes
- **Allowed tools:** Pencil and paper.

### Problem

For a sequence $a_0,a_1,\ldots,a_T$ and an integer $r$ with $0<r<T$:

1. Split $\sum_{k=0}^{T-1}(a_{k+1}-a_k)$ into ranges ending at $r-1$ and beginning at $r$.
2. Evaluate each part by telescoping.
3. Combine the results and verify that the artificial boundary value cancels.
4. State the off-by-one error produced if the second range begins at $r+1$.

<details>
<summary>Hint</summary>

Expand two terms at the beginning and end of each piece.
</details>

## E0.01.04 Reverse a triangular sum

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Swap the order of a double sum by preserving its index region.
- **Estimated time:** 25 minutes
- **Allowed tools:** Pencil and paper; a small grid is encouraged.

### Problem

Consider

$$
S_n=\sum_{i=1}^{n}\sum_{j=0}^{i-1}a_{ij}.
$$

1. Describe the index region as inequalities involving $i$, $j$, and $n$.
2. List all index pairs for $n=4$.
3. Rewrite $S_n$ with $j$ as the outer index.
4. Verify the new bounds by grouping your $n=4$ pairs by $j$.
5. Explain why replacing both upper bounds by $n$ changes the sum.

<details>
<summary>Hint 1</summary>

Determine the smallest and largest possible values of $j$ across the whole region.
</details>

<details>
<summary>Hint 2</summary>

Once $j$ is fixed, solve $j\le i-1$ for the smallest possible $i$.
</details>

## E0.01.05 Empty boundaries

- **Type:** conceptual
- **Difficulty:** 2
- **Objective:** Apply empty sum and product conventions at boundary cases.
- **Estimated time:** 15 minutes
- **Allowed tools:** Pencil and paper.

### Problem

Define

$$
S_n=\sum_{i=1}^{n}x_i,
\qquad
P_n=\prod_{i=1}^{n}x_i.
$$

1. Evaluate $S_0$ and $P_0$ under the standard conventions.
2. Check the recurrences $S_n=S_{n-1}+x_n$ and $P_n=P_{n-1}x_n$ at $n=1$.
3. Explain which recurrence fails if an empty product is defined as zero.
4. Let a layer apply zero multiplicative gates. Explain what the empty product convention says its combined neutral multiplier should be.

<details>
<summary>Hint</summary>

Ask which identity leaves a number unchanged under addition and which leaves it unchanged under multiplication.
</details>

## E0.01.06 Function anatomy

- **Type:** conceptual
- **Difficulty:** 2
- **Objective:** Distinguish domain, codomain, image, preimage, restriction, composition, and identity.
- **Estimated time:** 20 minutes
- **Allowed tools:** Notes.

### Problem

Let

$$
f:\mathbb{R}\to\mathbb{R},\quad f(x)=x^2-1,
\qquad
g:[0,\infty)\to\mathbb{R},\quad g(x)=\sqrt{x}+2.
$$

1. State the domain, codomain, and image of $f$.
2. Compute $f^{-1}([0,3])$ as a preimage.
3. Give a restriction of $f$ that is one-to-one and has image $[-1,\infty)$.
4. Determine whether $f\circ g$ and $g\circ f$ are defined on all of their stated first-function domains. If not, state a valid domain restriction.
5. Write both identity laws that apply to $f$ with explicit identity-function subscripts.

<details>
<summary>Hint 1</summary>

For a preimage, solve the compound inequality $0\le x^2-1\le3$.
</details>

<details>
<summary>Hint 2</summary>

A composition is valid only when outputs of the inner function lie in the domain of the outer function.
</details>

## E0.01.07 Accuracy as algebra

- **Type:** applied
- **Difficulty:** 2
- **Objective:** Use indicators and Iverson brackets to express counts and rates.
- **Estimated time:** 15 minutes
- **Allowed tools:** Pencil and paper or a Python REPL.

### Problem

A classifier produces predictions $(1,0,2,2,1,0)$ for labels $(1,2,2,0,1,0)$.

1. Write empirical accuracy using an Iverson bracket.
2. Evaluate each bracket and compute the accuracy.
3. Express the number of predictions equal to class $2$ using an indicator function for a set.
4. Express the same class-$2$ count using a Kronecker delta.
5. Explain the difference between counting correct predictions and selecting the correctly predicted examples.

<details>
<summary>Hint</summary>

All three notations produce zero or one; what differs is the condition they emphasize.
</details>

## E0.01.08 Expand Einstein notation

- **Type:** calculation
- **Difficulty:** 3
- **Objective:** Expand Einstein contractions and infer output shapes from free indices.
- **Estimated time:** 20 minutes
- **Allowed tools:** Pencil and paper; calculator optional.

### Problem

Let $A_{ij}$ have shape $2\times3$, $B_{jk}$ have shape $3\times2$, and $x_j$ have length $3$.

1. Expand $y_i=A_{ij}x_j$ with explicit sigma notation and state the shape of $\boldsymbol{y}$.
2. Expand $C_{ik}=A_{ij}B_{jk}$ and state the shape of $\mathbf{C}$.
3. Let
   $\mathbf{A}=\begin{bmatrix}1&0&2\\-1&3&1\end{bmatrix}$ and
   $\boldsymbol{x}=\begin{bmatrix}2\\1\\-1\end{bmatrix}$.
   Compute $\boldsymbol{y}$.
4. Diagnose each expression: $z=A_{ij}x_j$, $D_{ij}=A_{ik}B_{kj}+x_i$, and $q_i=A_{ij}x_jx_j$.

<details>
<summary>Hint 1</summary>

Free indices determine the output coordinates. Repeated indices are summed away.
</details>

<details>
<summary>Hint 2</summary>

Under the standard convention, an index appearing three times in one term is not a valid unambiguous contraction.
</details>

## E0.01.09 Translate math and code

- **Type:** implementation
- **Difficulty:** 3
- **Objective:** Translate one-based sums, indicators, and shape operations into Python and NumPy.
- **Estimated time:** 25 minutes
- **Allowed tools:** Python standard library and NumPy; execution is optional.

### Problem

Translate each expression into a short, internally checkable Python snippet with at least one `assert`.

1. $\sum_{i=1}^{n}i^2$ for $n=5$ using a generator expression.
2. $\prod_{i=1}^{n}p_i$ for `probabilities = [0.5, 0.25, 0.8]` using `math.prod`.
3. $n^{-1}\sum_{i=1}^{n}[\widehat{y}_i=y_i]$ using NumPy arrays.
4. For $\mathsf{X}\in\mathbb{R}^{b\times T\times d}$ represented by an array with shape `(2, 3, 4)`, select the final time step for every batch and feature.
5. Explain the one-based to zero-based shift in parts 1 and 4.

<details>
<summary>Hint 1</summary>

Python's `range(1, n + 1)` includes the mathematical indices $1$ through $n$.
</details>

<details>
<summary>Hint 2</summary>

A Boolean NumPy array can be averaged directly after comparison.
</details>

## E0.01.10 Repair ambiguous notation

- **Type:** critique
- **Difficulty:** 3
- **Objective:** Diagnose and repair overloaded subscripts and superscripts.
- **Estimated time:** 25 minutes
- **Allowed tools:** Module notation guide.

### Problem

A draft paper states:

> Let $x^t_i$ be token $i$ at layer $t$. We update $x^t_i=W^t_{ij}x^t_j$, where $t$ is also the training step. The loss is $L^2=\sum_i[y_i=f^{-1}(x_i)]$.

Identify at least six ambiguities or errors.
Then rewrite the passage using project conventions so that:

- token position uses $t$;
- layer uses $\ell$;
- optimization iteration uses $k$;
- vectors and matrices have declared shapes;
- the contraction is explicit or valid Einstein notation;
- the bracket condition and meaning of $f^{-1}$ are unambiguous;
- the loss is named without suggesting it is squared unless squaring is intended.

<details>
<summary>Hint 1</summary>

List every role assigned to each index before rewriting anything.
</details>

<details>
<summary>Hint 2</summary>

Ask whether the argument to $f^{-1}$ is a set, whether $f$ is bijective, and whether an inverse is actually intended.
</details>

## E0.01.11 Paper-notation archaeology

- **Type:** experiment
- **Difficulty:** 4
- **Objective:** Reconstruct and compare notation used in real ML papers.
- **Estimated time:** 45 minutes
- **Allowed tools:** Two publicly accessible ML papers, their supplements, and the project notation guide. No generative summary tools.

### Problem

Choose two papers on related ML topics from different research groups or publication years.
For each paper, inspect the abstract, notation or preliminaries, and one central method equation.

Submit:

1. bibliographic links to both papers;
2. a symbol table containing at least eight entries per paper;
3. declared or inferred shapes for every vector, matrix, and higher-rank array in the chosen equation;
4. a line-by-line translation of each equation into this project's notation;
5. a comparison of indexing base, indicator style, transpose convention, superscript meanings, and explicit versus implicit summation;
6. two ambiguities you resolved from context, or a reason you found none;
7. a 150 to 250 word judgment about which notation makes reconstruction easier and why.

Do not evaluate the papers' scientific conclusions.
This activity evaluates notation as an interface for reading.

<details>
<summary>Hint 1</summary>

Start with nouns: dataset, example, label, parameter, layer, token, feature, and output.
Then map each noun to symbols.
</details>

<details>
<summary>Hint 2</summary>

Classify each translation change as cosmetic, structural, or meaning-changing.
A missing shape declaration can be more consequential than a different font.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that your work includes:

- explicit bounds after every reindexing or sum swap;
- domains and codomains for every function you introduce;
- free and contracted indices for every Einstein expression;
- expected shapes in every code translation;
- citations and URLs for the paper-archaeology activity.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)
