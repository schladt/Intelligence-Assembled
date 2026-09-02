# 00. Mathematical Foundations

> The language everything else is written in.

[Project home](../README.md) | [Roadmap](../ROADMAP.md) | [Prerequisites](../PREREQUISITES.md) | Next section: §1 Calculus (not yet published)

## Why This Section Exists

AI is usually taught as though its notation, algebra, proofs, and computational habits arrived fully formed. They did not. A line such as

$$
\widehat{\boldsymbol{\theta}} =
\arg\min_{\boldsymbol{\theta}\in\mathbb{R}^{d}}
\frac{1}{n}\sum_{i=1}^{n}
L\left(f_{\boldsymbol{\theta}}(\boldsymbol{x}_i),y_i\right)
$$

compresses a remarkable amount of prior knowledge. You need to recognize an estimator, a parameter space, an optimization operator, a finite average, a loss, a parameterized function, vectors, examples, labels, and several indexing conventions. None of those ideas is individually impossible. Together, they can make one line feel like a locked door.

This section gives you the keys.

It covers the mathematical language, reasoning patterns, and computational foundations used throughout the project. You do not need to complete all fifteen modules before touching calculus or linear algebra. The first cluster runs alongside those subjects, and later clusters become useful as the curriculum asks more sophisticated questions.

## Prerequisite Check

There are no formal prerequisites.

You are in the right place if any of these questions cause friction:

- What is the difference between the codomain and image of a function?
- How do you reindex a sum without changing what it means?
- Why does $\log(xy)=\log x+\log y$ matter to a computer?
- How do you negate a statement containing both $\forall$ and $\exists$?
- What makes a proof by induction valid?
- How do you choose between a list, hash table, heap, and graph?
- What does NP-complete actually tell you about a problem?

If those questions already feel comfortable, use this section as a reference and take the routes that fit your goals.

## Section Map

```mermaid
flowchart TD
  A["Language of Mathematics<br/>§0.01-§0.03"]
  B["Discrete Reasoning<br/>§0.04-§0.08"]
  C["Bounds and Asymptotics<br/>§0.09-§0.10"]
  D["Computational Foundations<br/>§0.11-§0.15"]

  A --> B
  A --> C
  B --> C
  B --> D
  C --> D

  A --> CALC["§1 Calculus"]
  A --> LA["§2 Linear Algebra"]
  B --> PROB["§3 Probability"]
  D --> ML["§7-§10 Data and Learning"]
```

The arrows show the dominant flow, not a rigid semester sequence. In particular, programming (§0.13) can begin immediately, and graph theory (§0.11) does not require every analysis topic before it.

## Modules

| ID | Module | Status | Difficulty | Estimated effort |
|---|---|---|---:|---:|
| 0.01 | [Mathematical Notation and How to Read Mathematics](00.01-mathematical-notation/README.md) | Draft | 1/5 | 4-7 hours |
| 0.02 | [Algebra, Functions, and Precalculus Backfill](00.02-algebra-functions-precalculus/README.md) | Draft | 2/5 | 6-10 hours |
| 0.03 | [Exponents and Logarithms](00.03-exponents-logarithms/README.md) | Draft | 2/5 | 4-7 hours |
| 0.04 | [Sets, Relations, and Functions](00.04-sets-relations-functions/README.md) | Draft | 2/5 | 6-11 hours |
| 0.05 | [Logic and Quantifiers](00.05-logic-quantifiers/README.md) | Draft | 2/5 | 6-11 hours |
| 0.06 | [Proof Techniques](00.06-proof-techniques/README.md) | Draft | 3/5 | 6-11 hours |
| 0.07 | [Induction, Recursion, and Invariants](00.07-induction-recursion-invariants/README.md) | Draft | 3/5 | 8-13 hours |
| 0.08 | [Counting and Combinatorics](00.08-counting-combinatorics/README.md) | Draft | 3/5 | 8-13 hours |
| 0.09 | [Sums, Series, and Asymptotics](00.09-sums-series-asymptotics/README.md) | Draft | 3/5 | 10-15 hours |
| 0.10 | [Inequalities](00.10-inequalities/README.md) | Draft | 3/5 | 10-15 hours |
| 0.11 | [Graph Theory](00.11-graph-theory/README.md) | Draft | 3/5 | 10-15 hours |
| 0.12 | [Elementary Number Theory](00.12-elementary-number-theory/README.md) | Draft | 3/5 | 9-14 hours |
| 0.13 | [Programming and Scientific Computing](00.13-programming-scientific-computing/README.md) | Draft | 2/5 | 10-18 hours |
| 0.14 | [Algorithms and Data Structures](00.14-algorithms-data-structures/README.md) | Draft | 3/5 | 12-22 hours |
| 0.15 | [Computability and Complexity](00.15-computability-complexity/README.md) | Draft | 4/5 | 10-18 hours |

The estimates include a careful read and a representative selection of exercises. They are planning ranges, not deadlines.

## Suggested Routes

### Start Here

For most readers, begin with §0.01-§0.03. These modules establish the language used everywhere else and make later mathematical notation less expensive to parse.

### Mathematics-First Route

Prioritize §0.01-§0.10, then use graph theory, number theory, and computational foundations when downstream work requires them.

### Build-Things Route

Complete §0.01-§0.03 and §0.13-§0.14 early. Return to logic, proofs, counting, and inequalities as the algorithms and guarantees begin to need them.

### Classical AI and Computational Intelligence Route

Prioritize §0.04-§0.08 and §0.11-§0.15. Graphs, combinatorics, algorithms, and complexity carry much of the load in search, planning, evolutionary computation, and reinforcement learning.

## Section Learning Outcomes

After completing the modules relevant to your route, you should be able to:

- read dense mathematical notation without losing the underlying idea;
- move between prose, symbols, diagrams, and code;
- manipulate sums, products, functions, exponents, and logarithms reliably;
- translate English claims into logic and negate them correctly;
- construct and critique direct, indirect, and inductive proofs;
- count structured objects and connect counting to probability;
- use asymptotic notation and inequalities to reason about scale and bounds;
- model problems with graphs and relations;
- write, test, profile, and reproduce numerical code;
- choose data structures and analyze algorithms;
- explain what computability and complexity results do and do not imply.

## How to Use the Materials

Each published module contains a primary lesson, worked examples, exercises, solutions, and annotated resources. Supporting notes, notebooks, code, and visual assets appear only when they improve the lesson.

The file and content conventions live in the [style guide](../STYLE_GUIDE.md#module-file-structure). Mathematical conventions live in the [notation guide](../NOTATION.md). When those guides and a module disagree, the module should either be corrected or explain its local exception.

## Current Build Status

All fifteen modules, §0.01-§0.15, are published as complete draft learning
packages. The section now spans mathematical reading, proof, discrete structure,
scientific programming, algorithms, computability, and complexity.

This section will keep evolving as new modules test the structure. The point is not to freeze a perfect format before learning begins. The point is to build something worth learning from.
