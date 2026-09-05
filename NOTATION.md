# Notation and Terminology

## Purpose

This is the default notation and terminology reference for **Intelligence, Assembled**. Its job is to keep symbols, shapes, math-to-code translations, and overloaded terms consistent across the curriculum.

Modules should follow it unless a different convention is part of the lesson. When a source uses another convention, explain the difference before translating its result.

## Contents

- [General rules](#general-rules) and [object typography](#object-typography)
- [Vectors, matrices, and arrays](#vectors-matrices-and-arrays); [sets, logic, and functions](#sets-logic-and-functions)
- [Calculus](#calculus), [matrix calculus](#matrix-calculus), and [automatic differentiation](#automatic-differentiation)
- [Probability and statistics](#probability-and-statistics); [optimization and machine learning](#optimization-and-machine-learning)
- [Information theory](#information-theory); [neural networks and transformers](#neural-networks-and-transformers)
- [Evolutionary computation and reinforcement learning](#evolutionary-computation-and-reinforcement-learning); [signals and time series](#signals-and-time-series)
- [Mathematics-to-code bridge](#mathematics-to-code-bridge), [overloaded symbols](#commonly-overloaded-symbols), and [local notation tables](#local-notation-table)
- [Terminology](#terminology) and [references](#references)

Authoring and review guidance lives in [CONTRIBUTING.md](CONTRIBUTING.md#review-checklist).

## General Rules

- Define every symbol on first use in a module.
- State the domain or shape of important objects.
- Use the same notation in the lesson, examples, practice, worked solutions, and code when practical.
- Treat dimensions as part of the meaning.
- Pair dense notation with a plain-English interpretation.
- State local exceptions rather than silently changing conventions.
- Use $`\coloneqq`$ or `:=` for definitions, $`=`$ for equality, $`\approx`$ for approximation, and $`\gets`$ for assignment.
- Use GitHub's protected inline form, ``$`\boldsymbol{x}_i`$``, for inline mathematics. Its backticks keep TeX subscripts, matrices, quoted formulas, and expressions next to punctuation from being interpreted as ordinary Markdown. Keep display mathematics in `$$` blocks.
- In ordinary display-math source, write TeX row separators as `\\\\` so GitHub passes two backslashes to MathJax. Inside protected inline mathematics, use the normal TeX `\\`: the backticks preserve both backslashes without another escape layer.
- In Markdown table cells, use `\lvert` and `\rvert` instead of literal vertical bars inside mathematics so GFM does not split the cell.
- Never put `=` alone on a line inside display math; keep it with the left- or right-hand expression so GFM does not parse it as a setext heading underline.
- Use `\lbrace` and `\rbrace` for visible set braces, as in $`\lbrace 0,1\rbrace`$. GFM can consume the backslash in `\{` or `\}`, silently hiding the brace or breaking `\left` and `\bigl` delimiters. Write `\left\lbrace ... \right\rbrace` when scalable braces are needed.
- Write superscript stars as `^{\ast}`, as in $`\Sigma^{\ast}`$, rather than `^*` or `^{*}`. Markdown emphasis processing can otherwise change the asterisk before MathJax receives it.

## Object Typography

| Object | Convention | Example |
|---|---|---|
| Scalar | italic lowercase | $`x`$, $`a`$, $`\lambda`$ |
| Vector | bold lowercase | $`\boldsymbol{x}`$, $`\boldsymbol{w}`$ |
| Matrix | bold uppercase | $`\mathbf{A}`$, $`\mathbf{W}`$ |
| Rank-3 or higher array | sans-serif uppercase | $`\mathsf{X}`$ |
| Set | calligraphic uppercase | $`\mathcal{X}`$, $`\mathcal{D}`$ |
| Standard number system | blackboard bold | $`\mathbb{R}`$, $`\mathbb{N}`$ |
| Scalar random variable | italic uppercase | $`X`$, $`Y`$ |
| Random vector | bold uppercase | $`\boldsymbol{X}`$ |
| Event | italic uppercase | $`A`$, $`B`$ |
| Named function or operator | roman | $`\mathrm{softmax}`$ |

Use `\mathrm{...}` for named functions and operators. GitHub's math renderer rejects the alternative named-operator macro.

Field-standard exceptions such as transformer $`Q`$, $`K`$, and $`V`$ are allowed. Define them locally.

## Vectors, Matrices, and Arrays

Vectors are column vectors by default:

$$
\boldsymbol{x}\in\mathbb{R}^{d}.
$$

The transpose $`\boldsymbol{x}^{\top}`$ is a row vector.

For a matrix:

$$
\mathbf{A}\in\mathbb{R}^{m\times n},
\qquad
A_{ij}\text{ is the entry in row }i\text{ and column }j.
$$

If $`\boldsymbol{x}\in\mathbb{R}^{n}`$, then $`\mathbf{A}\boldsymbol{x}\in\mathbb{R}^{m}`$.

For a higher-rank array, state the axes:

$$
\mathsf{X}\in\mathbb{R}^{b\times T\times d},
$$

where $`b`$ is batch size, $`T`$ is sequence length, and $`d`$ is feature dimension.

### Indexing

Mathematics is one-indexed by default. Python, NumPy, JAX, and PyTorch are zero-indexed. When code implements an indexed derivation, call out the shift when an off-by-one error is plausible.

Use:

- $`i`$ for example or component index;
- $`j`$ for feature or coordinate;
- $`k`$ for optimization iteration;
- $`t`$ for physical or sequence time;
- $`\ell`$ for neural-network layer.

A module may differ, but it should state the mapping.

### Common Operations

- Inner product: $`\langle\boldsymbol{x},\boldsymbol{y}\rangle=\boldsymbol{x}^{\top}\boldsymbol{y}`$
- Outer product: $`\boldsymbol{x}\boldsymbol{y}^{\top}`$
- Elementwise product: $`\boldsymbol{x}\odot\boldsymbol{y}`$
- Vector norm: $`\lVert\boldsymbol{x}\rVert_p`$
- Frobenius norm: $`\lVert\mathbf{A}\rVert_F`$
- Identity matrix: $`\mathbf{I}_n`$
- Zero object: $`\mathbf{0}`$, with shape stated when unclear
- Ones vector: $`\boldsymbol{1}_n`$

Do not write `matrix norm` without naming the norm.

## Sets, Logic, and Functions

Use:

- $`x\in A`$ for membership;
- $`A\subseteq B`$ for subset, allowing equality;
- $`A\subsetneq B`$ for proper subset;
- $`\varnothing`$ for the empty set;
- $`|A|`$ for finite cardinality;
- $`A\times B`$ for Cartesian product;
- $`A\setminus B`$ for set difference.

Use $`\neg`$, $`\land`$, $`\lor`$, $`\implies`$, and $`\iff`$ for logic. Use $`\forall`$ and $`\exists`$ for quantifiers.

Declare a function with its domain and codomain:

$$
f:\mathcal{X}\to\mathcal{Y}.
$$

Composition is $`(f\circ g)(x)=f(g(x))`$. Do not treat $`f^{-1}`$ as an inverse function unless $`f`$ is bijective or the domain has been restricted appropriately.

## Calculus

For scalar $`f:\mathbb{R}\to\mathbb{R}`$, use $`df/dx`$ or $`f'(x)`$. Use partial derivatives when several variables are present:

$$
\frac{\partial f}{\partial x_i}.
$$

Use the differential to emphasize linear approximation:

$$
f(\boldsymbol{x}+d\boldsymbol{x}) =
f(\boldsymbol{x})+Df(\boldsymbol{x})[d\boldsymbol{x}]
+o(\lVert d\boldsymbol{x}\rVert).
$$

Write an integration variable explicitly:

$$
\int_a^b f(x)\,dx.
$$

## Matrix Calculus

Matrix calculus has incompatible layout conventions. This curriculum uses an operator-first view and numerator-layout Jacobians [1].

For $`f:\mathbb{R}^{n}\to\mathbb{R}^{m}`$, the derivative is a linear map:

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

with $`(\mathbf{J}_f)_{ij}=\partial f_i/\partial x_j`$. Rows correspond to outputs and columns to inputs.

For scalar $`f:\mathbb{R}^{n}\to\mathbb{R}`$, the gradient is a column vector:

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

For composition $`g\circ f`$:

$$
\mathbf{J}_{g\circ f}(\boldsymbol{x}) =
\mathbf{J}_g(f(\boldsymbol{x}))\mathbf{J}_f(\boldsymbol{x}).
$$

Check shapes for every nontrivial chain-rule product.

For scalar functions of matrices, prefer differential and trace notation:

$$
df =
\mathrm{tr}\left((\nabla_{\mathbf{X}}f)^{\top}d\mathbf{X}\right).
$$

When translating a source that uses denominator or mixed layout:

1. identify every shape;
2. rewrite the relationship as a differential;
3. derive the result using project conventions;
4. state any transpose introduced.

## Automatic Differentiation

Use:

- $`\mathrm{JVP}(f,\boldsymbol{x},\boldsymbol{v})=\mathbf{J}_f(\boldsymbol{x})\boldsymbol{v}`$;
- $`\mathrm{VJP}(f,\boldsymbol{x},\boldsymbol{u})=\boldsymbol{u}^{\top}\mathbf{J}_f(\boldsymbol{x})`$;
- $`\bar{\boldsymbol{x}}`$ for a reverse-mode adjoint when bar notation is helpful.

Explain how a framework represents the result because it may preserve the input shape rather than expose a row vector.

## Probability and Statistics

Use uppercase for random variables and lowercase for observations:

$$
X\sim p_X,
\qquad
X=x.
$$

Use:

- $`\Pr(A)`$ for an event probability;
- $`p_X(x)`$ for a probability mass or density function;
- $`F_X(x)=\Pr(X\le x)`$ for a cumulative distribution function;
- $`\mathbb{E}[X]`$ for expectation;
- $`\mathrm{Var}(X)`$ for variance;
- $`\mathrm{Cov}(X,Y)`$ for covariance;
- $`X\perp\!\!\!\perp Y`$ for independence;
- $`X\perp\!\!\!\perp Y\mid Z`$ for conditional independence.

A density value is not itself a probability. State the parameterization of distributions with multiple conventions, such as Gamma, Geometric, and Negative Binomial.

For data $`\mathcal{D}`$ and parameters $`\boldsymbol{\theta}`$, define likelihood as

$$
\mathcal{L}(\boldsymbol{\theta};\mathcal{D})
\coloneqq
p(\mathcal{D}\mid\boldsymbol{\theta}).
$$

The semicolon emphasizes that the data are fixed while the likelihood is viewed as a function of the parameters.

Use a hat for an estimator: $`\widehat{\theta}`$. Use $`\theta^{\ast}`$ for a true or optimal value only after stating which meaning applies.

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

Use $`\boldsymbol{x}^{\ast}`$ for an optimizer and $`f^{\ast}`$ for the optimal value.

An iterative update uses superscript parentheses:

$$
\boldsymbol{x}^{(k+1)} =
\boldsymbol{x}^{(k)}-\eta_k\nabla f(\boldsymbol{x}^{(k)}).
$$

Distinguish:

- pointwise loss $`L(\widehat{y},y)`$;
- population risk $`R(\boldsymbol{\theta})=\mathbb{E}[L]`$;
- empirical risk $`\widehat{R}_n(\boldsymbol{\theta})=n^{-1}\sum_iL_i`$;
- regularized objective $`\widehat{R}_n+\lambda\Omega(\boldsymbol{\theta})`$.

Optimization defaults to minimization. If an evolutionary algorithm maximizes fitness, say so explicitly.

A supervised dataset is

$$
\mathcal{D}=\lbrace (\boldsymbol{x}_i,y_i)\rbrace_{i=1}^{n}.
$$

For a tabular batch:

$$
\mathbf{X}\in\mathbb{R}^{n\times d},
\qquad
\boldsymbol{y}\in\mathbb{R}^{n}.
$$

Examples are rows and features are columns.

Use $`y`$ for a target, $`\widehat{y}`$ for a prediction, $`\boldsymbol{z}`$ or $`\boldsymbol{\ell}`$ for logits, and $`f_{\boldsymbol{\theta}}`$ for a parameterized model.

## Information Theory

Natural logarithms and nats are the default in machine learning:

$$
\log x\equiv\ln x.
$$

Use $`\log_2`$ explicitly for bits. State the unit when reporting entropy numerically.

Use:

$$
H(X)=-\sum_xp(x)\log p(x),
$$

$$
H(p,q)=-\sum_xp(x)\log q(x),
$$

$$
D_{\mathrm{KL}}(p\Vert q) =
\sum_xp(x)\log\frac{p(x)}{q(x)}.
$$

KL divergence is ordered, asymmetric, and not a metric. Use $`0\log0=0`$ by the limiting convention.

## Neural Networks and Transformers

For layer $`\ell`$:

$$
\boldsymbol{z}^{(\ell)} =
\mathbf{W}^{(\ell)}\boldsymbol{a}^{(\ell-1)}
+
\boldsymbol{b}^{(\ell)},
$$

$$
\boldsymbol{a}^{(\ell)} =
\phi^{(\ell)}(\boldsymbol{z}^{(\ell)}).
$$

If the layer has $`d_{\ell-1}`$ inputs and $`d_{\ell}`$ outputs:

$$
\mathbf{W}^{(\ell)}
\in
\mathbb{R}^{d_{\ell}\times d_{\ell-1}}.
$$

For batches, put examples in rows and state the batch shape explicitly.

For transformer notation, use:

- $`b`$: batch size;
- $`T`$: sequence length;
- $`d_{\mathrm{model}}`$: model width;
- $`h`$: number of heads;
- $`d_k`$, $`d_v`$: key and value dimensions;
- $`V`$: vocabulary size;
- $`\mathcal{V}`$: vocabulary;
- $`t_i`$: token at position $`i`$;
- $`\boldsymbol{\ell}_i`$: logits at position $`i`$.

Scaled dot-product attention is

$$
\mathrm{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V}) =
\mathrm{softmax}\left(
\frac{\mathbf{Q}\mathbf{K}^{\top}}{\sqrt{d_k}}+\mathbf{M}
\right)\mathbf{V}.
$$

Use $`\mathbf{M}`$ for an additive mask with $`0`$ at allowed positions and $`-\infty`$ at blocked positions. If code uses a Boolean mask, state what `True` means because frameworks differ.

The autoregressive factorization is

$$
p(t_{1:T}) =
\prod_{i=1}^{T}p(t_i\mid t_{<i}).
$$

## Evolutionary Computation and Reinforcement Learning

For evolutionary computation, use:

- $`\mathcal{P}^{(g)}`$: population at generation $`g`$;
- $`\mu`$: parent population size;
- $`\lambda`$: offspring population size;
- $`\boldsymbol{x}^{(g)}_i`$: individual $`i`$ at generation $`g`$;
- $`f(\boldsymbol{x})`$: fitness, with maximization stated explicitly;
- $`\mathcal{G}`$ and $`\mathcal{X}`$: genotype and phenotype spaces.

Preserve the standard $`(\mu+\lambda)`$ and $`(\mu,\lambda)`$ notation and explain the survival difference.

For reinforcement learning, use

$$
\mathcal{M}=(\mathcal{S},\mathcal{A},P,R,\gamma).
$$

Use $`S_t`$ and $`A_t`$ for random state and action, $`s_t`$ and $`a_t`$ for realizations, $`R_{t+1}`$ for the next reward, $`G_t`$ for return, $`\pi(a\mid s)`$ for policy, $`V^{\pi}(s)`$ for state value, and $`Q^{\pi}(s,a)`$ for action value. This follows the Sutton and Barto reward-index convention [2].

## Signals and Time Series

Use $`x[t]`$ for a deterministic discrete-time signal and $`X_t`$ for a stochastic process. State the difference when both appear.

Use $`\omega`$ for angular frequency and $`f`$ for cycles per unit time. State units and the discrete Fourier transform normalization because libraries differ.

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
| $`\mathbf{A}\mathbf{B}`$ | `A @ B` |
| $`\mathbf{A}\odot\mathbf{B}`$ | `A * B` |
| $`\mathbf{A}^{\top}`$ | `A.T` or explicit axis transpose |
| $`\sum_i x_i`$ | `x.sum()` |
| $`\arg\max_i x_i`$ | `argmax(x)` |
| $`\mathbf{A}^{-1}\boldsymbol{b}`$ | `solve(A, b)`, not `inv(A) @ b` |

When broadcasting is nontrivial, state input shapes, aligned shapes, and output shape.

Use numerical tolerances rather than exact floating-point equality, and explain the chosen tolerances.

## Commonly Overloaded Symbols

| Symbol | Common meanings | Preferred clarification |
|---|---|---|
| $`X`$ | random variable, data matrix, feature space | $`X`$, $`\mathbf{X}`$, $`\mathcal{X}`$ |
| $`L`$ | loss, Lagrangian, Laplacian, length | $`L`$, $`\mathcal{L}`$, $`\mathbf{L}`$, $`T`$ |
| $`H`$ | entropy, Hessian, hypothesis class | $`H`$, $`\mathbf{H}`$, $`\mathcal{H}`$ |
| $`P`$ | probability, transition matrix, projection | $`\Pr`$, $`\mathbf{P}`$, named local symbol |
| $`Q`$ | action value, query matrix | $`Q^{\pi}`$ or bold $`\mathbf{Q}`$ |
| $`\lambda`$ | eigenvalue, regularization, rate, offspring count | Name the role on first use |
| $`\sigma`$ | standard deviation, sigmoid, strategy | Use $`\mathrm{sigmoid}`$ when ambiguous |
| $`\pi`$ | constant, policy, stationary distribution | Use arguments or a descriptive subscript |
| $`t`$ | time, token, iteration | Prefer $`k`$ for optimization iteration |
| $`V`$ | value, vertices, vocabulary size | Use $`\mathcal{V}`$ for a set |

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

## Terminology

These concise definitions distinguish meanings used across mathematics, statistics, machine learning, computational intelligence, and modern AI. Each entry preserves the important overloads and common confusions; the named roadmap modules own full explanations.

### Activation

**Primary meaning:** The output of a neuron or layer after applying an activation function (§10.03).

**Also used for:** The activation function itself, activation statistics used for debugging, and stored activations used during backpropagation.

**Common confusion:** Activation checkpointing stores or recomputes intermediate values. It is not a kind of activation function.

### Algorithm

**Primary meaning:** A finite, well-defined procedure for solving a class of problems (§0.14).

**Also used for:** A high-level method whose implementation leaves choices unspecified, such as `the EM algorithm` or `gradient descent`.

**Common confusion:** A model describes a relationship or distribution; an algorithm computes, estimates, trains, searches, or acts.

### Attention

**Primary meaning:** A learned weighted combination of values in which weights depend on query-key compatibility (§12.02).

**Variants:** Self-attention, cross-attention, multi-head attention, and an individual attention weight or head.

**Common confusion:** An attention weight is one scalar in the mechanism. It is not automatically a causal explanation of the model's decision.

### Bias

**Statistical bias:** The systematic difference between an estimator's expected value and the target parameter (§4.03).

**Neural-network bias:** An additive learned parameter in a layer (§10.05).

**Social or measurement bias:** Systematic differences arising from data, labels, institutions, or deployment (§7.16).

**Common confusion:** These meanings are related only loosely. Always write `statistical bias`, `bias parameter`, or `social bias` when context could be unclear.

### Capacity

**Primary meaning:** The range or complexity of functions a model class can represent (§8.16).

**Also used for:** Channel capacity in information theory (§6.07), system throughput, and expert capacity in mixture-of-experts models (§12.08).

**Common confusion:** More model capacity can reduce approximation error while increasing estimation or optimization difficulty. It is not synonymous with performance.

### Convergence

**Mathematics and probability:** A sequence approaches a limit, under a named mode such as almost sure or in probability (§3.11).

**Optimization:** Iterates, objective values, or gradients approach a target condition (§5.06).

**MCMC:** A chain approaches its stationary distribution (§4.12).

**Common confusion:** Always state what converges, to what, and under which assumptions.

### Dimension

**Primary meaning:** The number of basis vectors in a vector space (§2.01).

**Also used for:** An array axis, feature count, latent width, model width, and physical unit.

**Common confusion:** Matrix rank is not the same as the number of columns, though it cannot exceed it.

### Distribution

**Probability:** A rule assigning probabilities to outcomes of a random variable (§3.01).

**Data:** The empirical pattern of observed values.

**Systems:** The act of spreading computation or data across machines.

**Common confusion:** A probability distribution is a mathematical object. An empirical distribution is constructed from finite observations.

### Embedding

**Primary meaning:** A representation of an object as a vector in a space where geometry carries useful structure (§10.17).

**Also used for:** A mathematical structure-preserving map, a token lookup, or a latent representation.

**Common confusion:** An embedding is not necessarily low-dimensional, interpretable, or unique.

### Entropy

**Primary meaning:** Expected surprisal under a probability distribution (§6.01).

**Related terms:** Cross-entropy compares a target distribution with a model distribution. KL divergence measures an ordered discrepancy between distributions.

**Common confusion:** Entropy, cross-entropy, and KL divergence are related but not interchangeable.

### Epoch

**Machine learning:** One nominal pass through a training dataset.

**Evolutionary computation:** Sometimes used informally for a generation or migration interval.

**Common confusion:** With sampling, shuffling, streaming, or distributed training, an epoch may not mean every example was seen exactly once.

### Estimator and Estimate

**Estimator:** A rule or random variable that maps data to a proposed parameter value (§4.01).

**Estimate:** The realized value produced for one dataset.

**Common confusion:** Before observing data, $`\widehat{\theta}`$ is random. After observing data, its computed value is fixed.

### Feature

**Primary meaning:** An input variable or derived measurement used by a model (§7.07).

**Representation learning:** A learned direction or pattern that responds to some property of the data.

**Interpretability:** A hypothesized meaningful component in an internal representation (§14.16).

**Common confusion:** A feature need not correspond to one human-readable concept.

### Fitness

**Primary meaning:** The quantity used to evaluate or rank individuals in an evolutionary algorithm (§9.04).

**Common confusion:** Some algorithms maximize fitness while others minimize cost. State the direction explicitly. Fitness may differ from the original objective after scaling, penalties, or multi-objective ranking.

### Generalization

**Primary meaning:** Performance on relevant unseen data (§8.16).

**Variants:** Generalization gap, length generalization, compositional generalization, and out-of-distribution generalization.

**Common confusion:** Good performance on a fixed test set does not establish every kind of generalization.

### Gradient

**Primary meaning:** The vector representing the derivative of a scalar-valued function under an inner product (§1.09, §2.12).

**Gradient descent:** An optimization algorithm that moves opposite the gradient (§5.06).

**Stochastic gradient:** An estimate of a population or full-data gradient (§5.09).

**Common confusion:** The gradient is a mathematical object. Gradient descent is an algorithm that uses it.

### Hyperparameter

**Primary meaning:** A setting chosen outside the fitted parameter update, such as regularization strength, tree depth, or learning-rate schedule (§8.18).

**Common confusion:** A value can be a parameter in one formulation and a hyperparameter in another. State how it is selected.

### Information

**Self-information:** The surprisal $`-\log p(x)`$ of an outcome (§6.01).

**Mutual information:** The reduction in uncertainty about one variable from observing another (§6.02).

**Fisher information:** The sensitivity of a likelihood to a parameter (§4.04).

**Common confusion:** These share a name and mathematical relationships, but they answer different questions.

### Iteration

**Primary meaning:** One update of an algorithm.

**Related terms:** A batch step, epoch, generation, time step, and decoding step are different units of progress.

**Common confusion:** Report which unit a metric or schedule uses.

### Latent Variable

**Primary meaning:** A variable included in a model but not directly observed (§8.14).

**Also used for:** A latent code or representation produced by an encoder (§11.03).

**Common confusion:** `Latent` means hidden in the model, not necessarily meaningful, causal, or disentangled.

### Likelihood

**Primary meaning:** The probability model for observed data viewed as a function of its parameters (§4.02).

$$
\mathcal{L}(\theta;\mathcal{D})=p(\mathcal{D}\mid\theta).
$$

**Common confusion:** A likelihood is not automatically a probability distribution over $`\theta`$.

### Loss, Risk, and Objective

**Loss:** A penalty for one prediction or example.

**Population risk:** Expected loss under the data-generating distribution.

**Empirical risk:** Average loss over a finite dataset.

**Objective:** The complete quantity optimized, possibly including regularization or constraints (§5.01, §8.01).

**Common confusion:** Calling all four `loss` can hide which quantity a theorem or implementation actually uses.

### Model

**Statistical model:** A family of probability distributions (§4.01).

**Predictive model:** A function mapping inputs to predictions (§8.01).

**Neural model:** A parameterized neural network.

**Causal model:** A structure describing interventions and counterfactuals (§14.14).

**Common confusion:** Specify the kind of model when its commitments matter.

### Parameter

**Primary meaning:** A value learned or estimated from data.

**Common confusion:** Parameters, hyperparameters, inputs, hidden states, and optimizer states play different roles even when all are stored as arrays.

### Probability and Density

**Probability:** A number assigned to an event, between zero and one.

**Density:** A function whose integral over a region gives probability (§3.04).

**Common confusion:** A continuous density can exceed one. The probability of one exact continuous value is usually zero.

### Regularization

**Primary meaning:** A preference or constraint that discourages certain solutions to improve generalization, stability, or identifiability (§8.03).

**Examples:** Penalties, priors, early stopping, dropout, data augmentation, and architectural constraints.

**Common confusion:** Weight decay and L2 regularization are equivalent for ordinary SGD under common formulations but differ under adaptive optimizers.

### Representation

**Primary meaning:** The form in which information is encoded for computation.

**Evolutionary computation:** The genotype and its mapping to a candidate solution (§9.03).

**Deep learning:** Learned activations or embeddings (§10.17).

**Common confusion:** A useful representation depends on the operations and task applied to it.

### Sample and Sampling

**Data sample:** One observation or a finite dataset, depending on context.

**Probability sampling:** Drawing a realization from a distribution (§3.04).

**Monte Carlo:** Estimating a quantity using random samples.

**Common confusion:** State whether `sample` means one observation, the dataset, or the act of drawing.

### State

**Dynamical systems:** The information needed to evolve a system forward (§8.21).

**Reinforcement learning:** The environment representation used by the decision process (§14.02).

**Software:** Mutable program data at a point in execution.

**Common confusion:** An observation need not be a complete state.

### Token

**Primary meaning:** A discrete unit produced by a tokenizer and represented by an integer ID (§13.02).

**Common confusion:** A token is not necessarily a word or character. Token boundaries depend on the tokenizer and vocabulary.

### Training

**Primary meaning:** Adjusting model parameters using data and an objective.

**Related terms:** Fitting, optimization, pretraining, fine-tuning, and post-training describe different scopes or stages.

**Common confusion:** Training loss measures objective performance on training data. It does not by itself measure generalization.

### Variance

**Probability:** Expected squared deviation from a mean (§3.03).

**Statistics:** Variation of an estimator across repeated samples (§4.03).

**Machine learning:** One component of the bias-variance decomposition (§8.17).

**Common confusion:** Data variance, estimator variance, predictive variance, and uncertainty are not interchangeable.

## References

[1] A. Edelman, S. G. Johnson, and P. Bright, *Matrix Calculus for Machine Learning and Beyond*. MIT OpenCourseWare, 2023. https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-iap-2023/

[2] R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed. MIT Press, 2018. http://incompleteideas.net/book/the-book-2nd.html
