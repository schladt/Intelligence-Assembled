# Contributing to Intelligence, Assembled

## Welcome

This is a personal learning project made public because explanations improve when people question, test, correct, and extend them. Focused contributions to accuracy, clarity, accessibility, and reproducibility are welcome: explanations, derivations, examples, practice and solutions, code, notebooks, visuals, historical context, and sources.

Read [README.md](README.md) for purpose and voice, [ROADMAP.md](ROADMAP.md) for topic ownership and readiness, and [NOTATION.md](NOTATION.md) for notation and terminology. This guide is the sole owner of authoring, source, and review conventions.

## Contents

- [Before you start](#before-you-start) and [workflow](#workflow)
- [Module file structure](#module-file-structure)
- [Teaching and presentation](#teaching-and-presentation)
- [Exercises and solutions](#exercises-and-solutions)
- [Code and notebook standards](#code-and-notebook-standards)
- [Citations and sources](#citations-and-sources)
- [AI-assisted contributions](#ai-assisted-contributions)
- [Review checklist](#review-checklist) and [reporting problems](#reporting-problems)

## Before You Start

### Find the Owning Module

Search the roadmap for the concept and its aliases. Each concept has one primary home; later lessons link back rather than duplicate its full treatment. Keep all existing module IDs and scope boundaries. Name exact required concepts and helpful background in reader prose, with links to the relevant modules. Do not quietly depend on material taught later or require an entire earlier section for two ideas. Use the roadmap's [readiness guidance](ROADMAP.md#readiness-and-learning-routes).

### Open an Issue First When Needed

Discuss new modules or sections, roadmap or prerequisite changes, major rewrites, repository-wide conventions, large dependencies or datasets, hardware-intensive experiments, disputed corrections, and changes affecting several modules before starting. A direct pull request is usually fine for typos, broken links, small clarifications, citations, isolated test fixes, alt text, and small examples. A short conversation is cheaper than discarding a large contribution.

## Workflow

1. Create a focused branch and make the smallest coherent change.
2. Run relevant checks and inspect the rendered Markdown, equations, and figures.
3. Open a pull request stating purpose, affected modules, evidence, verification performed, limitations, and any substantial AI assistance.

Do not mix unrelated formatting or refactoring into the contribution. Do not claim a check was performed when it was not.

## Module File Structure

One module has **one instructional Markdown file, `README.md`**. Keep its lesson, proofs, examples, implementation/run guidance, optional practice with worked solutions, and annotated references together. Do not split these into notes, exercise, solution, resource, or code README files.

### Section and Module Directories

Use two topic levels with lowercase kebab-case names and stable, zero-padded directory IDs:

```text
NN-section-name/
|-- README.md
`-- NN.MM-topic-name/
    |-- README.md
    |-- code/       (source and nearby tests, when needed)
    |-- notebooks/  (executable .ipynb investigations, when needed)
    `-- assets/     (figures, media, generation code, when needed)
```

IDs match the roadmap and are never reused or renumbered. Keep existing landing paths stable. Create a directory only for real material: an unauthored roadmap entry does not need a scaffold. Use descriptive artifact names; share code or assets only when several modules genuinely need the same artifact, not in anticipation of reuse.

### Section README

The section index owns its authored modules' status and reading order. Include purpose, outcomes, useful entry diagnostics, a link to the roadmap prerequisite graph and relevant routes, and a compact ID/title table. Add a status column when statuses differ; otherwise give one section-level availability notice. Link existing adjacent sections when helpful. Do not copy granular roadmap descriptions, lesson content, difficulty ratings, or effort tables.

### Module README

Begin with the ID/title, one concise scope-and-outcome summary, a short required/recommended background paragraph, and a compact local table of contents. Give useful readiness questions and targeted review links when they help the reader choose an entry point; do not force a fixed number of questions.

Use concept-specific headings and the order that best teaches the idea. Intuition, mathematics, derivation, implementation, experimentation, and practice are a teaching progression, not required boilerplate headings. Do not add empty or "not applicable" sections. Keep core explanations visible rather than hiding them in disclosures or notebooks. Place implementation and experiments before practice. Finish with relevant connections/navigation and a single references area, with clearly labeled further reading when useful. Preserve addressable headings that readers need.

### Module Metadata

YAML contains only the stable ID and title, preserving existing ID spelling:

```yaml
---
id: "0.01"
title: "Mathematical Notation and How to Read Mathematics"
---
```

Put background, outcomes, assumptions, and limitations in readable prose, not metadata. Status has one owner, the section index, not duplicate front matter or module property tables.

### Relative Links and Navigation

Use relative project links and meaningful link text, preferably including stable module IDs. Link existing previous and next modules and the section index when sequence is clear; use roadmap references for unauthored topics instead of nonexistent paths. Link a policy or derivation's owner instead of reproducing it. Link every useful code, notebook, and visual artifact from the lesson, and explain its role and execution context there.

### Source of Truth

- [ROADMAP.md](ROADMAP.md): all module IDs and granular scopes, section prerequisites, readiness routes, and starting sources.
- [NOTATION.md](NOTATION.md): notation, rendering contracts, and terminology.
- This guide: module layout, pedagogy, sources, contribution and review practice.
- Section indexes: authored module status and reading order.
- Module READMEs: the complete instructional path, including practice, answers, run instructions, and references.

### Module Lifecycle

Keep planned material in the roadmap. An authored lesson is `draft` while teaching or applicable verification is unfinished. It becomes `complete` when the applicable [review checklist](#review-checklist) is satisfied, including complete worked solutions for published exercises. `Reviewed` additionally means another person has checked correctness, sources, reproducibility, practice, and accessibility; record that review date alongside its status in the section index. Do not add mandatory history, experiments, or visuals when they would be filler.

## Teaching and Presentation

### Voice

Address the reader as **you**, use **we** during derivations and implementations, and reserve **I** for genuine author perspective. Use active voice, concrete language, natural contractions, and occasional useful humor. Do not use emdashes. Avoid "obviously," "clearly," "trivially," or "just" when they conceal a step. State assumptions and uncertainty honestly.

Prefer "We want to know how much the output changes when we nudge the input. The derivative gives us that local sensitivity" over impersonal abstractions that make the same idea harder to read.

### Learning Objectives

The opening summary should say what readers will be able to do: derive, prove, compute, implement, compare, diagnose, construct, interpret, explain why, or state the assumptions under which. Avoid uncheckable promises to "understand" or "be familiar with." Connect each outcome to an example, exercise, experiment, or self-check without objective-number bookkeeping.

### Explaining Theory

Answer what the idea is, why it exists, how it works, what it connects to, and why it matters. Teach important ideas in three passes: plain-English intuition; precise objects, assumptions, and results; then interpretation, application, and failure boundaries. Explain the consequence of important equations and show the load-bearing derivation steps, especially dimensions, transposes, inequalities, and approximations. Use a clearly labeled proof sketch only when a full proof needs out-of-scope material; say what is omitted.

### Historical Context

Include history when it explains the problem, earlier approaches and limitations, the sequence of ideas, hardware or data constraints, adjacent fields, disputes, rediscoveries, or parallel work. Avoid biography dumps and simplistic single-inventor stories; use the [historical evidence rules](#primary-sources-and-historical-claims).

### Examples

Usually include a smallest-possible hand-inspectable example, a realistic worked case, a counterexample or failure case, and a connection to later AI use. Increase complexity only when it teaches something new. Check numerical examples by an independent method when practical.

### Visual Standards

Use diagrams for structure and flow, plots for functions and tradeoffs, tables for comparisons, and animation only for genuinely dynamic behavior. Historical photographs belong only when the artifact or context matters. Prefer small focused Mermaid diagrams to one dense graph.

Every visual needs a teaching purpose, descriptive alt text and caption, readable labels/units/legends, source or `Original figure` attribution, and non-color cues. Keep generation code beside computationally generated figures when practical, and document how to run it in the lesson. Verify reuse rights before adapting any visual.

### Accessibility

Use logical headings, define symbols and abbreviations on first use, explain dense notation and important diagrams in prose, label axes and units, and use meaningful links. Do not encode meaning only through color. Provide transcripts or equivalent text for audio and video. Accessibility is part of correctness, not final polish.

### Maintaining Terminology

Add a concise entry to [Terminology](NOTATION.md#terminology) when fields use incompatible meanings, readers repeatedly confuse nearby concepts, or the project narrows common usage. Preserve overloads and common confusions, and point to the owning module for full instruction. If an entry becomes a lesson, put that explanation in its module and keep only the distinction in the reference.

## Exercises and Solutions

Practice is optional for a lesson whose purpose does not call for it, but every published exercise must have a complete worked solution. Use a meaningful progression across conceptual, calculation, derivation, proof, implementation, experiment, applied, critique, and extension work rather than imposing quotas or difficulty/time/type tables.

Keep existing exercise IDs and titles stable. New IDs use `E` plus the module ID and a zero-padded sequence number. State the full prompt, assumptions, deliverables, meaningful allowed-tool constraints, and evaluation criteria for open-ended work. Test reasoning rather than transcription, use only stated background, and offer progressive hints where useful.

Use `## Practice`, then a level-three exercise heading and an immediately paired disclosure:

```markdown
### E0.01.01 Exercise title

Full problem statement, constraints, and useful hints.

<details><summary>Worked solution</summary>

#### Solution E0.01.01

Complete reasoning and result, including verification and useful wrong turns.

</details>
```

Blank lines after the summary and before `</details>` are required for Markdown rendering. The solution heading provides a unique link, such as `#solution-e00101`; GitHub removes the dots. Use readable prose or bold labels for key ideas, reasoning, verification, and common mistakes rather than repeating boilerplate subheading trees. Include alternatives only when they teach a genuinely different approach. Disclosures hide answers, never core lesson content.

Keep display math, tables, lists, and code fences on their own lines, separated
from a preceding prose label by a blank line. Joining a label to a block opener
can turn a correct equation or table into ordinary text before rendering.

## Code and Notebook Standards

Derive the method when that is load-bearing, implement its central mechanism using basic operations, test hand-worked cases, and compare with a trusted library when useful. Explain what the library adds. Keep code readable and explicit about shapes, dtypes, numerical stability, and limitations. In Python use `@` for matrix multiplication and `*` for elementwise multiplication.

Keep reusable source and nearby tests in `code/`, non-Markdown media in `assets/`, and interactive investigations in `.ipynb` files only when execution adds value. The primary lesson owns their run instructions: state the working directory, portable commands, dependency and software versions, inputs/data provenance and license, expected runtime, hardware, seeds or nondeterminism, and expected outputs. Explain how code maps to the derivation. Avoid absolute workstation paths or a separate code README.

Tests should defend hand-computed behavior, shapes/dtypes where part of the contract, boundary and failure cases, numerical agreement with justified tolerances, expected determinism, and useful trusted-reference comparisons. A notebook is an executable argument, not a transcript: question, setup/hypothesis, method, results, interpretation, conclusions/limitations, and useful extensions. It must run top to bottom in a clean environment using relative paths. Record enough environment, code, data, and random-stream context to reconstruct a run; a seed alone is not reproducibility.

Never commit private credentials, confidential data, unauthorized restricted material, or unnecessary notebook output. Check data permissions before retrieval or redistribution. Describe results only at the scale and under the conditions actually tested.

## Citations and Sources

Lessons should stand on their own while claims remain traceable to evidence, historical context, and deeper treatment. Cite sources you actually inspected, and distinguish support for a claim from optional reading.

### Source Priorities

Prefer sources in this order when practical:

1. **Primary research:** original papers, technical reports, and standards.
2. **Authoritative texts:** established textbooks and monographs.
3. **Official documentation:** language, library, framework, and protocol documentation.
4. **Official university material:** syllabi, lecture notes, assignments, and open courseware.
5. **Surveys and reviews:** high-quality synthesis across primary work.
6. **Secondary explanations:** exceptional tutorials, visual explanations, and implementations.

The best source depends on the claim. Use the original paper for historical priority, a textbook for a standard proof, official documentation for current software behavior, and a survey for a broad research landscape.

### What Requires a Citation

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

### Numbered Citation Style

Use numbered references in square brackets:

```markdown
The original transformer replaced recurrence with self-attention [1].
```

Number references by first appearance within each module or standalone document. Reuse the same number for later references to the same source.

Do not use a number that does not appear in the reference list. Do not list sources that the document never cites unless they appear in a clearly labeled `Further reading` section.

### Reference Formats

Consistency and traceability matter more than perfect adherence to a publisher's house style.

#### Journal or Conference Paper

```text
[1] A. Author and B. Author, "Article title," Journal or Conference, vol. 1, no. 2, pp. 3-15, 2026. https://doi.org/...
```

#### Preprint

```text
[2] A. Author, "Preprint title," arXiv:2601.01234, version 2, 2026. https://arxiv.org/abs/2601.01234
```

Include the version when it matters. State `preprint` in nearby prose if publication status affects credibility.

#### Book

```text
[3] A. Author, Book Title, 2nd ed. Publisher, 2026, ch. 4.
```

Include chapter, section, or page numbers when citing a specific theorem, quotation, or argument.

#### University Course

```text
[4] Institution, "Course number: Course title," term and year, instructor. URL. Accessed 2026-09-01.
```

Course pages move. Record the offering and access date. Prefer stable open-courseware pages when available.

#### Official Documentation

```text
[5] Project or organization, "Page title," documentation version. URL. Accessed 2026-09-01.
```

Record the software version when behavior may differ across releases.

#### Dataset or Benchmark

```text
[6] A. Author et al., "Dataset or benchmark title," version, repository or archive, 2026. DOI or URL. License: CC BY 4.0.
```

Include version, license, and access method.

#### Software

```text
[7] Project name, version 1.2.3, source repository. URL. License: BSD-3-Clause.
```

Cite both the software artifact and its associated paper when both support the module.

#### Web Article or Tutorial

```text
[8] A. Author, "Page title," Site name, 2026. URL. Accessed 2026-09-01.
```

Use web articles for pedagogy or current practice, not as the sole evidence for a foundational theorem when a stronger source exists.

### Source Notes

A useful reference list can include one sentence explaining why a source matters:

```markdown
[3] G. Strang, *Introduction to Linear Algebra*, 6th ed. Wellesley-Cambridge Press, 2023.
    The primary geometric reference for the four fundamental subspaces and least squares.
```

Keep annotated sources in the lesson, merging equivalent bibliography records. For further reading, explain coverage, assumed level, teaching value, and free-access restrictions. Do not copy a numbered reference into a second bibliography merely to annotate it; avoid bare link collections.

### Verification Rules

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

### Primary Sources and Historical Claims

Historical claims require special care.

- Distinguish invention, independent discovery, first publication, popularization, and widespread adoption.
- Look for parallel work and earlier precursors.
- Prefer original publications plus a reliable historical treatment.
- Avoid assigning an entire field to one person when development was distributed.
- Do not infer priority from citation count or modern fame.
- Quote original language only when the wording matters.

### Figures, Tables, Exercises, and Adaptations

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

### Source Licensing

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

### Fast-Moving Material

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

### Adding a Source

Identify its claim or teaching purpose, choose the strongest practical source, inspect it directly, and supply a complete numbered reference with a stable DOI or URL. Record the relevant version, edition, term, or access date and any reuse rights. Annotate a non-obvious role and avoid equivalent duplicate records. The roadmap's [section starting sources](ROADMAP.md#canonical-starting-sources-by-section) are a starting point, not a substitute for inspecting the specific material cited.

### Broken or Removed Sources

Look for the DOI, official archive, author copy, or institutional archive. Update a moved URL without changing citation identity; describe a substantive source replacement in the pull request. If support disappears, revisit the claim rather than substituting a weak summary merely because it is accessible.

## AI-Assisted Contributions


AI assistance is allowed with disclosure and human verification.

Disclose tools that generated or substantially rewrote prose, equations, proofs, code, tests, exercises, solutions, citations, or diagrams. Routine completion of a few tokens does not need an inventory. When uncertain, disclose.

The pull request must state:

- the tool and model, when known;
- which files or sections it assisted;
- what kind of assistance it provided;
- how the contributor verified the output;
- whether every citation was opened and checked.

The contributor remains responsible for every claim and line of code. AI output is not evidence. Verification must come from sources, independent derivation, tests, reproducible experiments, or qualified human review.

Do not:

- submit unreviewed generated content;
- fabricate citations, quotations, experiments, or test results;
- claim a proof is verified because another model approved it;
- use AI to disguise copied work;
- upload confidential or restricted material without authorization;
- omit disclosure after substantial assistance.

## Review Checklist

Apply the checks relevant to the contribution, and state what was not checked rather than marking everything mechanically:

- Scope, outcomes, and required/recommended background are accurate; the lesson answers what, why, how, connections, and importance.
- Intuition accompanies formal theory; assumptions and limitations are explicit; derivations show load-bearing steps; useful history is cited.
- Examples move from inspectable cases to realistic use and failure boundaries.
- Every published exercise has its complete, correctly paired solution; hints, prompts, assumptions, and answers agree.
- Code and notebooks run in the documented context; tests or independent checks support the behavior claimed; generated figures are inspected.
- Sources were opened and support their claims; numbered citations and links resolve; versions, provenance, reuse licenses, and adaptation notices are present.
- Rendered Markdown, math, disclosures, figures, navigation, and accessibility have been inspected; no emdashes were added.
- Substantial AI assistance is disclosed with human verification and remaining uncertainty.

### Notation Review

- [ ] Important symbols are defined on first use.
- [ ] Object typography follows [NOTATION.md](NOTATION.md).
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

Check the [GitHub-sensitive syntax rules](NOTATION.md#general-rules), including protected inline math, set braces, superscript stars, table delimiters, and the different row-separator escaping required inside protected inline versus ordinary display math. The canonical conventions and local notation-table example remain in [NOTATION.md](NOTATION.md), not a second template here.

## Reporting Problems

[Open an ordinary GitHub issue](https://github.com/schladt/Intelligence-Assembled/issues) for an incorrect result, missing background, irreproducible experiment, accessibility barrier, stale claim, broken source, or ambiguous terminology. Focus on the affected material and evidence that helps improve it.
