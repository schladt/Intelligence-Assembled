# Sources and Citation Guide

## Purpose

This document defines how **Intelligence, Assembled** selects, verifies, cites, and maintains sources.

The curriculum should be understandable on its own, but its claims must remain traceable. Sources provide evidence, historical context, deeper treatment, and a way for readers to check our work.

## Source Priorities

Prefer sources in this order when practical:

1. **Primary research:** original papers, technical reports, and standards.
2. **Authoritative texts:** established textbooks and monographs.
3. **Official documentation:** language, library, framework, and protocol documentation.
4. **Official university material:** syllabi, lecture notes, assignments, and open courseware.
5. **Surveys and reviews:** high-quality synthesis across primary work.
6. **Secondary explanations:** exceptional tutorials, visual explanations, and implementations.

The best source depends on the claim. Use the original paper for historical priority, a textbook for a standard proof, official documentation for current software behavior, and a survey for a broad research landscape.

## What Requires a Citation

Cite:

- historical dates, attribution, and priority claims;
- theorem statements when attribution or precise conditions matter;
- empirical results and performance claims;
- datasets, benchmarks, and evaluation protocols;
- software behavior that may change;
- quotations and close paraphrases;
- adapted figures, tables, exercises, and examples;
- contested interpretations;
- claims about current best practice;
- non-obvious factual claims.

Common mathematical manipulations do not need a citation at every step. The module should still identify the principal references from which its treatment was developed.

## Numbered Citation Style

Use numbered references in square brackets:

```markdown
The original transformer replaced recurrence with self-attention [1].
```

Number references by first appearance within each module or standalone document. Reuse the same number for later references to the same source.

Do not use a number that does not appear in the reference list. Do not list sources that the document never cites unless they appear in a clearly labeled `Further reading` section.

## Reference Formats

Consistency and traceability matter more than perfect adherence to a publisher's house style.

### Journal or Conference Paper

```text
[1] A. Author and B. Author, "Article title," Journal or Conference, vol. 1, no. 2, pp. 3-15, 2026. https://doi.org/...
```

### Preprint

```text
[2] A. Author, "Preprint title," arXiv:2601.01234, version 2, 2026. https://arxiv.org/abs/2601.01234
```

Include the version when it matters. State `preprint` in nearby prose if publication status affects credibility.

### Book

```text
[3] A. Author, Book Title, 2nd ed. Publisher, 2026, ch. 4.
```

Include chapter, section, or page numbers when citing a specific theorem, quotation, or argument.

### University Course

```text
[4] Institution, "Course number: Course title," term and year, instructor. URL. Accessed 2026-09-01.
```

Course pages move. Record the offering and access date. Prefer stable open-courseware pages when available.

### Official Documentation

```text
[5] Project or organization, "Page title," documentation version. URL. Accessed 2026-09-01.
```

Record the software version when behavior may differ across releases.

### Dataset or Benchmark

```text
[6] A. Author et al., "Dataset or benchmark title," version, repository or archive, 2026. DOI or URL. License: CC BY 4.0.
```

Include version, license, and access method.

### Software

```text
[7] Project name, version 1.2.3, source repository. URL. License: BSD-3-Clause.
```

Cite both the software artifact and its associated paper when both support the module.

### Web Article or Tutorial

```text
[8] A. Author, "Page title," Site name, 2026. URL. Accessed 2026-09-01.
```

Use web articles for pedagogy or current practice, not as the sole evidence for a foundational theorem when a stronger source exists.

## Source Notes

A useful reference list can include one sentence explaining why a source matters:

```markdown
[3] G. Strang, *Introduction to Linear Algebra*, 6th ed. Wellesley-Cambridge Press, 2023.
    The primary geometric reference for the four fundamental subspaces and least squares.
```

Annotated references are especially useful in module `resources/` directories. Avoid bare link collections.

## Verification Rules

Before citing a source:

- open and inspect it;
- confirm that it supports the nearby claim;
- verify authors, title, date, venue, edition, and URL or DOI;
- check theorem assumptions and experimental conditions;
- distinguish what the source demonstrates from what the module infers;
- verify that quotations are exact;
- record access dates for pages likely to change;
- prefer a stable DOI, archive, or official repository over a search-result URL.

A citation discovered through an AI tool, summary, or secondary source must still be opened and checked directly.

## Primary Sources and Historical Claims

Historical claims require special care.

- Distinguish invention, independent discovery, first publication, popularization, and widespread adoption.
- Look for parallel work and earlier precursors.
- Prefer original publications plus a reliable historical treatment.
- Avoid assigning an entire field to one person when development was distributed.
- Do not infer priority from citation count or modern fame.
- Quote original language only when the wording matters.

## Figures, Tables, Exercises, and Adaptations

A public source is not automatically reusable.

Before reusing or adapting material:

1. verify the license or obtain permission;
2. confirm that derivative work is allowed;
3. cite the source;
4. label the material as adapted;
5. state meaningful modifications;
6. preserve required attribution and license notices.

Use an adaptation note:

```markdown
> **Adapted from [4].** Notation was changed to match `NOTATION.md`; the example and implementation are original additions. Source licensed CC BY 4.0.
```

Do not copy proprietary textbook exercises or publish proprietary course solutions without permission.

## Source Licensing

Record licenses for:

- datasets;
- figures and images;
- code;
- notebooks;
- adapted exercises;
- substantial excerpts;
- open textbooks and course material.

Citation and permission are separate questions. A citation gives credit. A license or permission establishes whether reuse is allowed.

When the license is unclear, link to the source and create original material instead of copying it.

## Fast-Moving Material

Modules on deep learning systems, transformers, LLMs, agents, interpretability, and safety should include a review note:

```markdown
> **Review note:** Last reviewed YYYY-MM-DD. This is a rapidly changing area. Verify implementation details and benchmark status against the cited sources.
```

For these modules:

- cite versions and dates;
- distinguish peer-reviewed work from preprints;
- avoid `state of the art` without a date, benchmark, and evaluation condition;
- preserve superseded material when it remains historically useful;
- update claims when benchmarks are contaminated, retired, or materially changed.

## Canonical Starting Sources by Section

This is a starter registry, not an exhaustive bibliography. Individual modules should cite the specific chapters, lectures, and papers they use.

| Section | Starting sources |
|---|---|
| §0 Mathematical Foundations | MIT 6.042J Mathematics for Computer Science; Stanford CS103; Sedgewick and Wayne, *Algorithms*; Sipser, *Introduction to the Theory of Computation* |
| §1 Calculus | MIT 18.01 and 18.02 OpenCourseWare; CMU 21-266; Spivak, *Calculus* |
| §2 Linear Algebra | MIT 18.06; MIT 18.S096 Matrix Calculus; Strang, *Introduction to Linear Algebra*; Trefethen and Bau, *Numerical Linear Algebra* |
| §3 Probability | Harvard STAT 110; MIT 6.041 and 18.600; Blitzstein and Hwang, *Introduction to Probability* |
| §4 Statistics | MIT 18.650; Stanford STATS 200; Wasserman, *All of Statistics*; Gelman et al., *Bayesian Data Analysis* |
| §5 Optimization | Stanford EE364A/B; CMU 10-725; Boyd and Vandenberghe, *Convex Optimization*; Nocedal and Wright, *Numerical Optimization* |
| §6 Information Theory | MIT 6.441; Stanford EE376A; Cover and Thomas, *Elements of Information Theory*; MacKay, *Information Theory, Inference, and Learning Algorithms* |
| §7 Data Analysis | Berkeley Data 100 and STAT 153; Stanford CS246; Tukey, *Exploratory Data Analysis*; Hyndman and Athanasopoulos, *Forecasting: Principles and Practice* |
| §8 Machine Learning | Stanford CS229; CMU 10-701/10-715; Berkeley CS189; Hastie et al., *The Elements of Statistical Learning*; Murphy, *Probabilistic Machine Learning* |
| §9 Evolutionary Computation | Eiben and Smith, *Introduction to Evolutionary Computing*; Poli et al., *A Field Guide to Genetic Programming*; Deb, *Multi-Objective Optimization Using Evolutionary Algorithms* |
| §10 Neural Networks | Stanford CS231n; CMU 11-785; Goodfellow et al., *Deep Learning*; Karpathy, *Neural Networks: Zero to Hero* |
| §11 Deep Learning | MIT 6.7960; Berkeley CS182; Prince, *Understanding Deep Learning*; *Dive into Deep Learning* |
| §12 Transformers | Stanford CS224N and CS336; Vaswani et al., "Attention Is All You Need"; *The Annotated Transformer* |
| §13 Large Language Models | Stanford CS336 and CS324; Princeton COS 597R; Jurafsky and Martin, *Speech and Language Processing*; Raschka, *Build a Large Language Model (From Scratch)* |
| §14 Beyond | Russell and Norvig, *Artificial Intelligence: A Modern Approach*; Sutton and Barto, *Reinforcement Learning*; Koller and Friedman, *Probabilistic Graphical Models*; Pearl, *Causality* |

## Adding a Source

When adding a source:

- [ ] identify the claim or teaching purpose it supports;
- [ ] choose the strongest available source type;
- [ ] verify the source directly;
- [ ] add a complete numbered reference;
- [ ] include a stable URL or DOI when available;
- [ ] record version, edition, term, or access date as needed;
- [ ] verify reuse rights for adapted material;
- [ ] annotate the source when its role is not obvious;
- [ ] avoid duplicating an equivalent source without a reason.

## Broken or Removed Sources

When a link breaks:

1. look for the DOI, official archive, author copy, or institutional archive;
2. update the URL without changing the citation's identity;
3. record a substantive source replacement in the pull request;
4. use `ERRATA/` if the unavailable source undermines a published claim;
5. do not replace an authoritative source with a weak summary merely because it is accessible.
