# Notation Guide

## Purpose

This is the default notation contract for **Intelligence, Assembled**. Its job is to keep symbols, shapes, and math-to-code translations consistent across the curriculum.

Modules should follow it unless a different convention is part of the lesson. When a source uses another convention, explain the difference before translating its result.

## General Rules

- Define every symbol on first use in a module.
- State the domain or shape of important objects.
- Use the same notation in notes, examples, exercises, solutions, and code when practical.
- Treat dimensions as part of the meaning.
- Pair dense notation with a plain-English interpretation.
- State local exceptions rather than silently changing conventions.
- Use $\coloneqq$ or `:=` for definitions, $=$ for equality, $\approx$ for approximation, and $\gets$ for assignment.

## Object Typography

| Object | Convention | Example |
|---|---|---|
| Scalar | italic lowercase | $x$, $a$, $\lambda$ |
| Vector | bold lowercase | $\boldsymbol{x}$, $\boldsymbol{w}$ |
| Matrix | bold uppercase | $\mathbf{A}$, $\mathbf{W}$ |
| Rank-3 or higher array | sans-serif uppercase | $\mathsf{X}$ |
| Set | calligraphic uppercase | $\mathcal{X}$, $\mathcal{D}$ |
| Standard number system | blackboard bold | $\mathbb{R}$, $\mathbb{N}$ |
| Scalar random variable | italic uppercase | $X$, $Y$ |
| Random vector | bold uppercase | $\boldsymbol{X}$ |
| Event | italic uppercase | $A$, $B$ |
| Named function or operator | roman | $\operatorname{softmax}$ |

Field-standard exceptions such as transformer $Q$, $K$, and $V$ are allowed. Define them locally.

## Vectors, Matrices, and Arrays

Vectors are column vectors by default:

$$
\boldsymbol{x}\in\mathbb{R}^{d}.
$$

The transpose $\boldsymbol{x}^{\top}$ is a row vector.

For a matrix:

$$
\mathbf{A}\in\mathbb{R}^{m\times n},
\qquad
A_{ij}\text{ is the entry in row }i\text{ and column }j.
$$

If $\boldsymbol{x}\in\mathbb{R}^{n}$, then $\mathbf{A}\boldsymbol{x}\in\mathbb{R}^{m}$.

For a higher-rank array, state the axes:

$$
\mathsf{X}\in\mathbb{R}^{b\times T\times d},
$$

where $b$ is batch size, $T$ is sequence length, and $d$ is feature dimension.

### Indexing

Mathematics is one-indexed by default. Python, NumPy, JAX, and PyTorch are zero-indexed. When code implements an indexed derivation, call out the shift when an off-by-one error is plausible.

Use:

- $i$ for example or component index;
- $j$ for feature or coordinate;
- $k$ for optimization iteration;
- $t$ for physical or sequence time;
- $\ell$ for neural-network layer.

A module may differ, but it should state the mapping.

### Common Operations

- Inner product: $\langle\boldsymbol{x},\boldsymbol{y}\rangle=\boldsymbol{x}^{\top}\boldsymbol{y}$
- Outer product: $\boldsymbol{x}\boldsymbol{y}^{\top}$
- Elementwise product: $\boldsymbol{x}\odot\boldsymbol{y}$
- Vector norm: $\lVert\boldsymbol{x}\rVert_p$
- Frobenius norm: $\lVert\mathbf{A}\rVert_F$
- Identity matrix: $\mathbf{I}_n$
- Zero object: $\mathbf{0}$, with shape stated when unclear
- Ones vector: $\boldsymbol{1}_n$

Do not write `matrix norm` without naming the norm.

## Sets, Logic, and Functions

Use:

- $x\in A$ for membership;
- $A\subseteq B$ for subset, allowing equality;
- $A\subsetneq B$ for proper subset;
- $\varnothing$ for the empty set;
- $|A|$ for finite cardinality;
- $A\times B$ for Cartesian product;
- $A\setminus B$ for set difference.

Use $\neg$, $\land$, $\lor$, $\implies$, and $\iff$ for logic. Use $\forall$ and $\exists$ for quantifiers.

Declare a function with its domain and codomain:

$$
f:\mathcal{X}\to\mathcal{Y}.
$$

Composition is $(f\circ g)(x)=f(g(x))$. Do not treat $f^{-1}$ as an inverse function unless $f$ is bijective or the domain has been restricted appropriately.

## Calculus

For scalar $f:\mathbb{R}\to\mathbb{R}$, use $df/dx$ or $f'(x)$. Use partial derivatives when several variables are present:

$$
\frac{\partial f}{\partial x_i}.
$$

Use the differential to emphasize linear approximation:

$$
f(\boldsymbol{x}+d\boldsymbol{x})
=
f(\boldsymbol{x})+Df(\boldsymbol{x})[d\boldsymbol{x}]
+o(\lVert d\boldsymbol{x}\rVert).
$$

Write an integration variable explicitly:

$$
\int_a^b f(x)\,dx.
$$

## Matrix Calculus

Matrix calculus has incompatible layout conventions. This curriculum uses an operator-first view and numerator-layout Jacobians [1].

For $f:\mathbb{R}^{n}\to\mathbb{R}^{m}$, the derivative is a linear map:

$$
Df(\boldsymbol{x}):\mathbb{R}^{n}\to\mathbb{R}^{m}.
$$

The Jacobian is

$$
\mathbf{J}_f(\boldsymbol{x})
\coloneqq
\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{x}}
\in\mathbb{R}^{m\times n},
$$

with $(\mathbf{J}_f)_{ij}=\partial f_i/\partial x_j$. Rows correspond to outputs and columns to inputs.

For scalar $f:\mathbb{R}^{n}\to\mathbb{R}$, the gradient is a column vector:

$$
\nabla_{\boldsymbol{x}}f\in\mathbb{R}^{n},
\qquad
df=(\nabla_{\boldsymbol{x}}f)^{\top}d\boldsymbol{x}.
$$

The Hessian is

$$
\mathbf{H}_f(\boldsymbol{x})
\coloneqq
\nabla^2_{\boldsymbol{x}}f
\in\mathbb{R}^{n\times n}.
$$

For composition $g\circ f$:

$$
\mathbf{J}_{g\circ f}(\boldsymbol{x})
=
\mathbf{J}_g(f(\boldsymbol{x}))\mathbf{J}_f(\boldsymbol{x}).
$$

Check shapes for every nontrivial chain-rule product.

For scalar functions of matrices, prefer differential and trace notation:

$$
df
=
\operatorname{tr}\left((\nabla_{\mathbf{X}}f)^{\top}d\mathbf{X}\right).
$$

When translating a source that uses denominator or mixed layout:

1. identify every shape;
2. rewrite the relationship as a differential;
3. derive the result using project conventions;
4. state any transpose introduced.

## Automatic Differentiation

Use:

- $\operatorname{JVP}(f,\boldsymbol{x},\boldsymbol{v})=\mathbf{J}_f(\boldsymbol{x})\boldsymbol{v}$;
- $\operatorname{VJP}(f,\boldsymbol{x},\boldsymbol{u})=\boldsymbol{u}^{\top}\mathbf{J}_f(\boldsymbol{x})$;
- $\bar{\boldsymbol{x}}$ for a reverse-mode adjoint when bar notation is helpful.

Explain how a framework represents the result because it may preserve the input shape rather than expose a row vector.

## Probability and Statistics

Use uppercase for random variables and lowercase for observations:

$$
X\sim p_X,
\qquad
X=x.
$$

Use:

- $\Pr(A)$ for an event probability;
- $p_X(x)$ for a probability mass or density function;
- $F_X(x)=\Pr(X\le x)$ for a cumulative distribution function;
- $\mathbb{E}[X]$ for expectation;
- $\operatorname{Var}(X)$ for variance;
- $\operatorname{Cov}(X,Y)$ for covariance;
- $X\perp\!\!\!\perp Y$ for independence;
- $X\perp\!\!\!\perp Y\mid Z$ for conditional independence.

A density value is not itself a probability. State the parameterization of distributions with multiple conventions, such as Gamma, Geometric, and Negative Binomial.

For data $\mathcal{D}$ and parameters $\boldsymbol{\theta}$, define likelihood as

$$
\mathcal{L}(\boldsymbol{\theta};\mathcal{D})
\coloneqq
p(\mathcal{D}\mid\boldsymbol{\theta}).
$$

The semicolon emphasizes that the data are fixed while the likelihood is viewed as a function of the parameters.

Use a hat for an estimator: $\widehat{\theta}$. Use $\theta^{*}$ for a true or optimal value only after stating which meaning applies.

For Bayesian inference:

$$
p(\boldsymbol{\theta}\mid\mathcal{D})
\propto
p(\mathcal{D}\mid\boldsymbol{\theta})p(\boldsymbol{\theta}).
$$

Name the prior, likelihood, posterior, and evidence on first use.

## Optimization and Machine Learning

A generic optimization problem is

$$
\min_{\boldsymbol{x}\in\mathcal{X}} f(\boldsymbol{x}).
$$

Use $\boldsymbol{x}^{*}$ for an optimizer and $f^{*}$ for the optimal value.

An iterative update uses superscript parentheses:

$$
\boldsymbol{x}^{(k+1)}
=
\boldsymbol{x}^{(k)}-\eta_k\nabla f(\boldsymbol{x}^{(k)}).
$$

Distinguish:

- pointwise loss $L(\widehat{y},y)$;
- population risk $R(\boldsymbol{\theta})=\mathbb{E}[L]$;
- empirical risk $\widehat{R}_n(\boldsymbol{\theta})=n^{-1}\sum_iL_i$;
- regularized objective $\widehat{R}_n+\lambda\Omega(\boldsymbol{\theta})$.

Optimization defaults to minimization. If an evolutionary algorithm maximizes fitness, say so explicitly.

A supervised dataset is

$$
\mathcal{D}=\{(\boldsymbol{x}_i,y_i)\}_{i=1}^{n}.
$$

For a tabular batch:

$$
\mathbf{X}\in\mathbb{R}^{n\times d},
\qquad
\boldsymbol{y}\in\mathbb{R}^{n}.
$$

Examples are rows and features are columns.

Use $y$ for a target, $\widehat{y}$ for a prediction, $\boldsymbol{z}$ or $\boldsymbol{\ell}$ for logits, and $f_{\boldsymbol{\theta}}$ for a parameterized model.

## Information Theory

Natural logarithms and nats are the default in machine learning:

$$
\log x\equiv\ln x.
$$

Use $\log_2$ explicitly for bits. State the unit when reporting entropy numerically.

Use:

$$
H(X)=-\sum_xp(x)\log p(x),
$$

$$
H(p,q)=-\sum_xp(x)\log q(x),
$$

$$
D_{\mathrm{KL}}(p\Vert q)
=
\sum_xp(x)\log\frac{p(x)}{q(x)}.
$$

KL divergence is ordered, asymmetric, and not a metric. Use $0\log0=0$ by the limiting convention.

## Neural Networks and Transformers

For layer $\ell$:

$$
\boldsymbol{z}^{(\ell)}
=
\mathbf{W}^{(\ell)}\boldsymbol{a}^{(\ell-1)}
+
\boldsymbol{b}^{(\ell)},
$$

$$
\boldsymbol{a}^{(\ell)}
=
\phi^{(\ell)}(\boldsymbol{z}^{(\ell)}).
$$

If the layer has $d_{\ell-1}$ inputs and $d_{\ell}$ outputs:

$$
\mathbf{W}^{(\ell)}
\in
\mathbb{R}^{d_{\ell}\times d_{\ell-1}}.
$$

For batches, put examples in rows and state the batch shape explicitly.

For transformer notation, use:

- $b$: batch size;
- $T$: sequence length;
- $d_{\mathrm{model}}$: model width;
- $h$: number of heads;
- $d_k$, $d_v$: key and value dimensions;
- $V$: vocabulary size;
- $\mathcal{V}$: vocabulary;
- $t_i$: token at position $i$;
- $\boldsymbol{\ell}_i$: logits at position $i$.

Scaled dot-product attention is

$$
\operatorname{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V})
=
\operatorname{softmax}\left(
\frac{\mathbf{Q}\mathbf{K}^{\top}}{\sqrt{d_k}}+\mathbf{M}
\right)\mathbf{V}.
$$

Use $\mathbf{M}$ for an additive mask with $0$ at allowed positions and $-\infty$ at blocked positions. If code uses a Boolean mask, state what `True` means because frameworks differ.

The autoregressive factorization is

$$
p(t_{1:T})
=
\prod_{i=1}^{T}p(t_i\mid t_{<i}).
$$

## Evolutionary Computation and Reinforcement Learning

For evolutionary computation, use:

- $\mathcal{P}^{(g)}$: population at generation $g$;
- $\mu$: parent population size;
- $\lambda$: offspring population size;
- $\boldsymbol{x}^{(g)}_i$: individual $i$ at generation $g$;
- $f(\boldsymbol{x})$: fitness, with maximization stated explicitly;
- $\mathcal{G}$ and $\mathcal{X}$: genotype and phenotype spaces.

Preserve the standard $(\mu+\lambda)$ and $(\mu,\lambda)$ notation and explain the survival difference.

For reinforcement learning, use

$$
\mathcal{M}=(\mathcal{S},\mathcal{A},P,R,\gamma).
$$

Use $S_t$ and $A_t$ for random state and action, $s_t$ and $a_t$ for realizations, $R_{t+1}$ for the next reward, $G_t$ for return, $\pi(a\mid s)$ for policy, $V^{\pi}(s)$ for state value, and $Q^{\pi}(s,a)$ for action value. This follows the Sutton and Barto reward-index convention [2].

## Signals and Time Series

Use $x[t]$ for a deterministic discrete-time signal and $X_t$ for a stochastic process. State the difference when both appear.

Use $\omega$ for angular frequency and $f$ for cycles per unit time. State units and the discrete Fourier transform normalization because libraries differ.

For a time series, state whether the index is equally spaced and whether the process is assumed stationary.

## Mathematics-to-Code Bridge

Use shape annotations for the first nontrivial implementation of an operation:

```python
# features: (batch_size, input_features)
# weights: (output_features, input_features)
logits = features @ weights.T + bias
# logits: (batch_size, output_features)
```

Common translations:

| Mathematics | Python / array code |
|---|---|
| $\mathbf{A}\mathbf{B}$ | `A @ B` |
| $\mathbf{A}\odot\mathbf{B}$ | `A * B` |
| $\mathbf{A}^{\top}$ | `A.T` or explicit axis transpose |
| $\sum_i x_i$ | `x.sum()` |
| $\arg\max_i x_i$ | `argmax(x)` |
| $\mathbf{A}^{-1}\boldsymbol{b}$ | `solve(A, b)`, not `inv(A) @ b` |

When broadcasting is nontrivial, state input shapes, aligned shapes, and output shape.

Use numerical tolerances rather than exact floating-point equality, and explain the chosen tolerances.

## Commonly Overloaded Symbols

| Symbol | Common meanings | Preferred clarification |
|---|---|---|
| $X$ | random variable, data matrix, feature space | $X$, $\mathbf{X}$, $\mathcal{X}$ |
| $L$ | loss, Lagrangian, Laplacian, length | $L$, $\mathcal{L}$, $\mathbf{L}$, $T$ |
| $H$ | entropy, Hessian, hypothesis class | $H$, $\mathbf{H}$, $\mathcal{H}$ |
| $P$ | probability, transition matrix, projection | $\Pr$, $\mathbf{P}$, named local symbol |
| $Q$ | action value, query matrix | $Q^{\pi}$ or bold $\mathbf{Q}$ |
| $\lambda$ | eigenvalue, regularization, rate, offspring count | Name the role on first use |
| $\sigma$ | standard deviation, sigmoid, strategy | Use $\operatorname{sigmoid}$ when ambiguous |
| $\pi$ | constant, policy, stationary distribution | Use arguments or a descriptive subscript |
| $t$ | time, token, iteration | Prefer $k$ for optimization iteration |
| $V$ | value, vertices, vocabulary size | Use $\mathcal{V}$ for a set |

## Local Notation Table

Notation-heavy modules should include a short table near the beginning:

```markdown
| Symbol | Type / shape | Meaning |
|---|---|---|
| $n$ | positive integer | number of observations |
| $d$ | positive integer | number of features |
| $\mathbf{X}$ | $\mathbb{R}^{n\times d}$ | design matrix |
| $\boldsymbol{\theta}$ | $\mathbb{R}^{d}$ | model parameters |
```

Include symbols used throughout the module. Define one-off symbols near their use.

## Review Checklist

- [ ] Important symbols are defined on first use.
- [ ] Object typography follows this guide.
- [ ] Shapes are stated for nontrivial operations.
- [ ] Math and code indexing are translated where needed.
- [ ] Jacobians use numerator layout and gradients are columns.
- [ ] Chain-rule products pass a shape check.
- [ ] Random variables and observations are distinct.
- [ ] Probability, density, likelihood, and posterior are not conflated.
- [ ] Logarithm bases and information units are stated.
- [ ] Loss, risk, and objective are distinguished.
- [ ] Maximization and minimization directions are explicit.
- [ ] Attention-mask semantics are explicit.
- [ ] Fourier normalization and reward indexing are explicit when used.
- [ ] Code operations match the mathematics.
- [ ] Overloaded symbols are clarified locally.
- [ ] Important notation has a plain-English reading.

## References

[1] A. Edelman, S. G. Johnson, and P. Bright, *Matrix Calculus for Machine Learning and Beyond*. MIT OpenCourseWare, 2023. https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-iap-2023/

[2] R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed. MIT Press, 2018. http://incompleteideas.net/book/the-book-2nd.html
