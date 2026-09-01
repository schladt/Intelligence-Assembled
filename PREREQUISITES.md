# Prerequisites

## Purpose

`ROADMAP.md` shows the curriculum and gives each section a prerequisite graph. This document explains how to use those prerequisites in practice:

- where to start;
- what is truly required;
- what can be learned alongside a section;
- when you can skip material you already know;
- what to do when you discover a gap halfway through.

It is a navigation guide, not a second roadmap. Module descriptions remain in `ROADMAP.md`, and individual module READMEs will eventually hold the most precise prerequisites.

## Types of Prerequisites

### Required

You need this material to follow the module's central explanations, derivations, or implementation.

Example: matrix multiplication is required before deriving backpropagation through a linear layer.

### Recommended

The module remains usable without it, but the additional preparation improves depth or fluency.

Example: Fourier analysis is recommended for spectral time-series methods but is not required for basic ARIMA forecasting.

### Needed Later

You can start the section without it, but an advanced module within the section will require it. Dotted arrows in roadmap prerequisite graphs show this relationship.

Example: you can begin Probability without multivariable change of variables, but §3.08 eventually needs it.

### Corequisite

Two topics explain each other and may be studied together.

Example: Data Analysis and introductory Machine Learning should reinforce each other rather than becoming one long gate.

## Assumed Starting Point

Section 0 has no formal prerequisites. It includes the mathematical, programming, and algorithmic foundations used later.

You do not need to complete every Section 0 module before beginning calculus or linear algebra. In particular:

- §0.01 through §0.03 support early mathematics;
- §0.04 through §0.10 support proofs, probability, and theory;
- §0.13 through §0.15 support implementation and algorithms;
- §0.11 and §0.12 can be learned when graph or number-theoretic applications arise.

The expected programming language is Python. The scientific-computing baseline is NumPy-style array programming, plotting, tests, environments, Git, and reproducibility.

## Recommended Foundation Sequence

The roadmap deliberately interleaves calculus and linear algebra:

1. §0.01-§0.03: notation, algebra, exponentials, and logarithms
2. §1.01-§1.08: single-variable calculus
3. §2.01-§2.11: linear algebra
4. §1.09-§1.13: multivariable calculus and optional analysis depth
5. §2.12-§2.13: matrix calculus and automatic differentiation
6. §2.14: Fourier and signal foundations when relevant

This differs from programs that teach multivariable calculus before linear algebra. For this curriculum, linear algebra first makes gradients, Jacobians, Hessians, and multivariable chain rules easier to express and connect to machine learning.

Section 0's proof and computational modules can run alongside this sequence.

## Quick Self-Diagnostics

These are routing questions, not exams. If one answer is uncertain, review the named module. If several are uncertain, begin there instead of trying to push through downstream notation.

### Programming and Algorithms

Before implementation-heavy modules, can you:

- write and test a Python function;
- explain the shape of a NumPy array before and after broadcasting;
- distinguish matrix multiplication from elementwise multiplication;
- choose among a list, dictionary, set, queue, heap, and graph representation;
- estimate the time and space complexity of a loop or basic algorithm;
- reproduce a run using a recorded environment and seed?

If not, begin with §0.13 and §0.14. Review §0.15 before complexity-heavy classical AI or theoretical ML.

### Single-Variable Calculus

Before multivariable calculus or optimization, can you:

- apply product, quotient, and chain rules;
- interpret a derivative as a local linear approximation;
- compute and interpret a definite integral;
- write a second-order Taylor approximation;
- explain what convergence of a sequence means?

If not, review §1.01-§1.07.

### Linear Algebra

Before matrix calculus, probability, or machine learning, can you:

- multiply a matrix by a vector and predict the result shape;
- explain span, independence, basis, and rank;
- solve a small linear system;
- interpret least squares as projection;
- explain eigenvectors and singular vectors geometrically;
- recognize a positive semidefinite matrix?

If not, review §2.01-§2.09.

### Probability

Before statistics or probabilistic machine learning, can you:

- translate a verbal experiment into events and random variables;
- use conditional probability and Bayes' theorem;
- distinguish probability mass, density, and cumulative probability;
- compute expectation and variance;
- explain independence and conditional independence;
- state what the law of large numbers and central limit theorem provide?

If not, begin with §3.01.

### Statistics

Before advanced machine learning evaluation, can you:

- distinguish an estimator from an estimate;
- explain likelihood as a function of parameters;
- interpret a confidence interval correctly;
- explain Type I error, Type II error, power, and a p-value;
- distinguish a confidence interval from a credible interval;
- design a train, validation, and test split without leakage?

If not, review the relevant parts of §4 and §7.

## Learning Routes

These routes are suggestions, not separate curricula. Local prerequisite statements take precedence.

### Foundations and Theory

Use when your goal is mathematical depth or learning theory.

1. Section 0 foundations
2. Sections 1 and 2 in the recommended interleaving
3. Probability and Statistics
4. Optimization and Information Theory
5. Statistical Learning Theory in §8.16
6. Optional analysis and measure-theory modules as needed

### Applied Data and Classical Machine Learning

Use when your goal is principled model building and evaluation.

1. §0.13-§0.14 programming foundations
2. Core calculus, linear algebra, probability, and statistics
3. Learn Section 7 alongside Section 8
4. Prioritize model selection, evaluation, leakage, and practical ML
5. Add specialized models as the problem demands

### Neural Networks and Large Language Models

Use when your goal is modern deep learning.

1. Programming and array foundations
2. Differential and matrix calculus
3. Linear algebra through SVD
4. Core probability, cross-entropy, and gradient-based optimization
5. §8.01-§8.05 for the learning setup and linear models
6. Neural Networks, Deep Learning, Transformers, then LLMs
7. Backfill specialized statistics, information theory, or systems material when required

Do not skip the backpropagation and numerical-stability foundations merely to reach transformers faster.

### Evolutionary and Computational Intelligence

Use when your goal is evolutionary algorithms, swarm methods, or fuzzy systems.

1. Combinatorics, probability, and scientific computing
2. Optimization framing and black-box methods
3. Section 9
4. §14.10-§14.12
5. Add neural networks for neuroevolution and statistics for experimental methodology

### Classical AI and Reinforcement Learning

Use when your goal is search, planning, sequential decisions, or agents.

1. Graphs, algorithms, and complexity
2. Probability and Markov chains
3. Classical AI in §14.01
4. Tabular RL in §14.02-§14.03
5. Add optimization and neural networks before deep RL
6. Continue to model-based, offline, multi-agent, and hierarchical RL

### Causality, Interpretability, and Safety

These are advanced branches with different prerequisites:

- Causality builds on probability, statistics, and graphical models.
- Mechanistic interpretability builds on neural networks and transformers.
- Alignment and safety draw from RL, LLMs, robustness, evaluation, and human-AI interaction.

Do not treat `Beyond` as meaning `after everything else`. Its modules are parallel branches.

## Skipping Material

You may skip a prerequisite when you can demonstrate the relevant capability, not merely recognize the vocabulary.

Good evidence includes:

- solving the prerequisite check without notes;
- deriving the key result;
- implementing the central algorithm;
- explaining assumptions and failure cases;
- completing a representative exercise.

If you are unsure, begin the downstream module and watch for friction. Repeated confusion about notation, unexplained algebra, or implementation mechanics usually signals a prerequisite gap rather than a lack of ability.

## Remediation

When you hit a gap:

1. name the exact missing skill;
2. follow the nearest module reference;
3. complete its prerequisite check;
4. read only as far as needed to resolve the gap;
5. do one representative exercise;
6. return to the original module and confirm the blocked step now makes sense.

For several accumulated gaps, stop and complete the relevant foundation sequence. Backfilling one concept at a time works until every paragraph requires a detour.

## Module Prerequisite Metadata

Future module READMEs should use:

```yaml
prerequisites: ["01.04", "02.08"]
recommended: ["02.10"]
```

Keep the categories small and honest.

- `prerequisites` means required at entry.
- `recommended` means helpful but not blocking.

Explain unusual dependencies in prose. Do not list an entire earlier section when only two ideas are needed.

## Maintaining This Guide

Update this file when:

- a module repeatedly exposes an unlisted prerequisite;
- a listed prerequisite proves unnecessary;
- a new route becomes useful to readers;
- module ownership changes;
- diagnostics fail to predict readiness.

Prerequisites should be tested against actual learners and module content. They are hypotheses about what someone needs, not permanent facts.
