# Style Guide

## Purpose

This guide defines how **Intelligence, Assembled** should teach. Modules should be rigorous without sounding sterile, approachable without hiding the mathematics, and thorough without becoming encyclopedic.

Related guides:

- `NOTATION.md` defines mathematical and computational notation.
- `PREREQUISITES.md` explains readiness and learning routes.
- `SOURCES.md` defines citation and evidence standards.
- `CONTRIBUTING.md` defines the contribution workflow.

## Voice

Use a direct, conversational teaching voice.

- Address the reader as **you**.
- Use **we** while working through a derivation or implementation.
- Use **I** only for genuine author perspective or experience.
- Prefer active voice and concrete language.
- Use contractions when they sound natural.
- Keep humor occasional and useful.
- Do not use emdashes.

Prefer:

> We want to know how much the output changes when we nudge the input. The derivative gives us that local sensitivity.

Avoid:

> The derivative may be understood as a local sensitivity operator by which output variation is induced.

Avoid words such as `obviously`, `clearly`, `trivially`, and `just` when they hide a real step. Qualify claims with their assumptions. Say when evidence is mixed or a mechanism remains unsettled.

## What Every Module Should Do

A module should answer:

1. What is this?
2. Why does it exist?
3. How does it work?
4. What does it connect to?
5. Why does it matter?

Use the six-layer progression:

**Intuition -> Mathematics -> Derivation -> Implementation -> Experimentation -> Exercises**

Keep these headings so modules remain predictable. If a layer does not apply, say so briefly instead of adding filler.

## Module File Structure

This section is the single source of truth for module layout. `README.md` and `ROADMAP.md` should link here rather than reproduce the structure.

### Section and Module Directories

Use zero-padded section directories and stable module IDs:

```text
NN-section-name/
|-- README.md
`-- NN.MM-topic-name/
    |-- README.md
    |-- notes/
    |-- exercises/
    |-- solutions/
    |-- notebooks/
    |-- code/
    |-- assets/
    `-- resources/
```

Example:

```text
05-optimization/
|-- README.md
|-- 05.01-the-optimization-problem/
`-- 05.06-unconstrained-first-order-methods/
```

Rules:

- Directory names use lowercase kebab case after the stable ID.
- Module IDs match `ROADMAP.md` and are never reused.
- Renaming a title may change the descriptive slug, but not the ID.
- Use two directory levels: section, then module. Organize depth inside the module by content type rather than adding another topic hierarchy.
- Do not create empty directories merely to satisfy the template. Add a directory when it contains useful material.
- Keep the main learning path visible from the module `README.md`; readers should not need to inspect the filesystem to discover the lesson order.

### Section README

The section `README.md` is a landing page, not a duplicate of every module.

It should contain:

- the section's purpose and connection to the larger curriculum;
- section-level prerequisites and a readiness check;
- the prerequisite graph from `ROADMAP.md` or a link to it;
- an ordered module table with ID, title, status, difficulty, and estimated effort;
- section-level learning outcomes;
- one or two suggested routes when not every module is required;
- links to the previous and next sections.

Module descriptions, derivations, and exercises belong in module directories.

### Module README

The module `README.md` is the primary lesson and navigation hub. It owns the module's scope, learning objectives, teaching sequence, and links to supporting material.

Use this content layout:

```markdown
# NN.MM Module title

## Why this matters
## Learning objectives
## Prerequisite check
## Historical context
## Intuition
## Mathematics
## Derivation
## Implementation
## Experimentation
## Worked examples
## Common mistakes
## Exercises
## What you should now be able to do
## Where this leads
## References
```

Modules may add subheadings as needed. Keep these major headings predictable. If a layer does not apply, retain the heading and explain why in one sentence rather than adding filler.

The module README should link directly to every supporting note, exercise set, solution set, notebook, implementation, and resource needed for the main path. Supporting files deepen the lesson; they do not replace a coherent module README.

### Module Metadata

Place YAML front matter at the top of each module README:

```yaml
---
id: "05.06"
title: "Unconstrained First-Order Methods"
prerequisites: ["01.09", "02.08", "05.03"]
recommended: ["02.10", "02.12"]
difficulty: 3
level: advanced-undergraduate
estimated_hours:
  reading: [3, 5]
  exercises: [3, 7]
status: stub
last_reviewed: null
---
```

Metadata rules:

- `prerequisites` lists material required before starting.
- `recommended` lists useful but non-blocking preparation.
- `difficulty` uses the 1 through 5 scale.
- Time estimates are honest ranges for reading and doing.
- `status` is `stub`, `draft`, `complete`, or `reviewed`.
- `last_reviewed` is required when a module reaches `reviewed`.

### Notes

Use `notes/` for substantial treatments that would interrupt the main lesson, such as a long proof, alternate derivation, historical deep dive, or technical appendix.

```text
notes/
|-- convergence-proof.md
|-- geometric-interpretation.md
`-- historical-notes.md
```

Each note should:

- have a descriptive filename and title;
- state why it exists and where it fits;
- link back to the module README;
- follow project notation and citation rules;
- avoid repeating content already owned by the main lesson.

A short explanation belongs in the module README. Create a separate note only when the material has independent value or significant depth.

### Exercises and Solutions

Exercise and solution files mirror one another so readers can move between them predictably:

```text
exercises/
|-- README.md
|-- E05.06.01-gradient-descent.md
`-- E05.06.02-conditioning-experiment.md

solutions/
|-- README.md
|-- E05.06.01-gradient-descent.md
`-- E05.06.02-conditioning-experiment.md
```

Use one exercise file for a substantial problem and a grouped `README.md` for short related questions. Keep the same ID, title, notation, and assumptions in the exercise and solution.

Exercise IDs use `ENN.MM.XX`, where `NN.MM` is the module ID and `XX` is a zero-padded sequence number. Solutions are committed from the start unless the module is explicitly marked `draft` and the missing solution is tracked.

The exercise index should show type, difficulty, learning objective, and estimated time without revealing the solution.

### Notebooks

Use `notebooks/` for interactive derivations, visualizations, and experiments that benefit from executable narrative.

```text
notebooks/
|-- 01-gradient-descent-geometry.ipynb
`-- 02-conditioning-experiment.ipynb
```

Number notebooks when order matters. Each notebook should be linked from the module README and should state its question, expected runtime, hardware, dependencies, data source, and seed policy.

Do not move the only explanation of a core concept into a notebook. The README should still explain the idea for readers who cannot execute it.

### Code and Tests

Use `code/` for reusable implementations that are clearer as source files than notebook cells:

```text
code/
|-- gradient_descent.py
|-- test_gradient_descent.py
`-- README.md
```

The code README should explain how the implementation maps to the derivation and how to run its tests or examples. Keep tests near module code until shared project tooling establishes another convention.

Promote code to a shared package only when multiple modules genuinely depend on it. Do not create a general utility layer preemptively.

### Assets

Use `assets/` for module-owned visual and media files:

```text
assets/
|-- gradient-field.png
|-- newton-vs-gradient-descent.svg
`-- generate-gradient-field.py
```

Prefer descriptive filenames. Commit generation code beside generated assets when practical. Every visual must be linked from instructional content with alt text, a caption, and source attribution.

Use a repository-level shared asset only when the exact same artifact serves several modules. Avoid copying one image into multiple module directories.

### Resources

Use `resources/` for annotated reading and source guidance, not a link dump.

```text
resources/
`-- README.md
```

For each resource, state what it covers, assumed level, why it is included, and whether it is freely accessible. Formal references used to support module claims still belong in the module's numbered reference list.

### Relative Links and Navigation

- Use relative links for project files.
- Link from the module README to supporting files and back again.
- Add previous-module, section-index, and next-module links where the module sequence is clear.
- Prefer stable module IDs in link text so renamed slugs remain understandable.
- Do not duplicate a derivation or policy to avoid a link. Link to its owning document.

### Source of Truth

Each kind of information has one owner:

- `ROADMAP.md`: curriculum scope, module IDs, and section prerequisites;
- `STYLE_GUIDE.md`: module filesystem and content layout;
- `NOTATION.md`: notation conventions;
- `PREREQUISITES.md`: route and readiness guidance;
- `SOURCES.md`: source and citation policy;
- module `README.md`: module scope, objectives, and primary lesson;
- `exercises/`: problem statements and hints;
- `solutions/`: worked answers;
- `ERRATA/`: material corrections to published content.

Other documents should link to the owner instead of maintaining a second version.

### Module Lifecycle

- **Stub:** Create the module directory and README with metadata, scope, objectives, and planned supporting artifacts. Do not create empty subdirectories.
- **Draft:** Add the primary lesson and whichever supporting directories contain real work. Track missing solutions or validation explicitly.
- **Complete:** The lesson, examples, relevant implementations, exercises, solutions, references, and accessibility checks are present.
- **Reviewed:** Another person has checked correctness, sources, reproducibility, exercises, solutions, and accessibility; record `last_reviewed`.

### Learning Objectives

Use two to six measurable objectives. Prefer verbs such as:

- derive;
- prove;
- compute;
- implement;
- compare;
- diagnose;
- construct;
- interpret;
- explain why;
- state the assumptions under which.

Avoid `understand`, `know`, `appreciate`, and `be familiar with`. Every objective should map to an example, exercise, experiment, or self-check.

### Prerequisite Check

List the required module IDs, then give three to six quick questions that help the reader decide whether they are ready. Point directly to the material they should review if they are not.

## Explaining Theory

Teach important ideas in three passes:

1. **Intuition:** State the problem and central idea in plain English.
2. **Formal development:** Define the objects, assumptions, and result precisely.
3. **Interpretation:** Explain what the result means, where it applies, and where it can fail.

Before a theorem or guarantee, state its assumptions. After an important equation, explain its consequence. Show the load-bearing steps in a derivation, especially when dimensions, transposes, inequalities, or approximations matter.

Use a proof sketch only when the full proof requires material outside the module. Label it clearly and state what was omitted.

## Historical Context

History belongs when it helps explain the idea.

Include:

- the problem people were trying to solve;
- earlier approaches and their limitations;
- the sequence of ideas that led to the modern method;
- the role of hardware, data, or adjacent fields;
- important disputes, rediscoveries, or parallel work.

Use dates and priority claims carefully. Cite primary or scholarly sources. Avoid biography dumps and simplified `one person invented it` stories.

## Examples

A complete module should usually include:

- one smallest-possible example;
- one realistic worked example;
- one counterexample, edge case, or failure case;
- one connection to a later AI application.

Start with numbers small enough to inspect by hand. Increase complexity only when it reveals something new. Verify numerical examples by a second method when practical.

## Visuals

Use visuals when they teach something better than prose alone.

- Use diagrams for structure, flow, architecture, and causality.
- Use plots for functions, distributions, convergence, and tradeoffs.
- Use tables for compact comparison.
- Use animations for genuinely dynamic behavior.
- Use photographs or historical images only when the physical artifact or context matters.

Every visual needs:

- a teaching purpose in nearby prose;
- a descriptive caption and alt text;
- readable labels, units, and legends;
- a source or `Original figure` attribution;
- non-color cues when color distinguishes categories;
- generating code when the visual is produced computationally.

Keep Mermaid diagrams small. Prefer multiple focused diagrams over one dense graph.

## Code and Notebooks

When implementation helps understanding:

1. derive the method;
2. implement the central mechanism from basic operations;
3. test it on hand-worked examples;
4. compare it with a trusted library;
5. explain what the library adds.

Code should be readable, tested, and explicit about shapes and numerical stability. Use `@` for matrix multiplication and `*` for elementwise multiplication in Python.

A notebook should be an executable argument, not a raw transcript. It should contain:

1. question or claim;
2. setup and hypothesis;
3. method;
4. results;
5. interpretation;
6. limitations;
7. exercises or extensions.

Notebooks must run top to bottom, use relative paths, state data provenance, record seeds, avoid private credentials, and report expected runtime and hardware.

## Exercises and Solutions

Use a meaningful mix of:

- `conceptual`;
- `calculation`;
- `derivation`;
- `proof`;
- `implementation`;
- `experiment`;
- `applied`;
- `critique`;
- `extension`.

Difficulty uses the roadmap's 1 through 5 scale:

1. Direct application
2. Guided combination
3. Independent synthesis
4. Advanced transfer
5. Open investigation

Every exercise should:

- map to a learning objective;
- use only stated prerequisites;
- state assumptions and deliverables;
- test reasoning rather than transcription;
- identify allowed tools;
- include evaluation criteria when open-ended.

Provide progressive hints for difficult exercises. Put full worked solutions in the sibling `solutions/` directory.

A solution should explain the key idea, show the reasoning, verify the result, and discuss likely wrong turns. Include an alternative solution only when it teaches a genuinely different method.

## Citations

Use numbered citations in square brackets: `[1]`, `[2]`, and so on. Number them by first appearance within each module.

Cite:

- nontrivial factual and historical claims;
- theorem statements when attribution or precise conditions matter;
- empirical results;
- datasets and software behavior;
- quotations and close paraphrases;
- adapted exercises, figures, and tables;
- contested interpretations.

Prefer primary papers, authoritative texts, official documentation, and official course materials. See `SOURCES.md` for formats and source policy.

## Accessibility

- Use a logical heading hierarchy.
- Define symbols and abbreviations on first use.
- Provide alt text and captions.
- Do not encode meaning by color alone.
- Label axes and units.
- Summarize important diagrams in prose.
- Avoid dense, uninterrupted notation.
- Use meaningful link text.
- Provide transcripts or equivalent text for audio and video.

Accessibility is part of correctness, not a final polish step.

## Review Checklist

- [ ] The module explains what, why, how, connections, and importance.
- [ ] Learning objectives are measurable and assessed.
- [ ] Prerequisites and effort are realistic.
- [ ] Important terms and assumptions are explicit.
- [ ] Intuition accompanies formal theory.
- [ ] Derivations show the steps where the idea lives.
- [ ] Historical claims are useful and cited.
- [ ] Examples progress from small to realistic and include failure cases.
- [ ] Visuals are meaningful, sourced, and accessible.
- [ ] Code and notebooks are reproducible and tested.
- [ ] Exercises vary in type and difficulty.
- [ ] Every published exercise has a worked solution.
- [ ] Limitations and unsettled claims are represented honestly.
- [ ] Notation follows `NOTATION.md`.
- [ ] Numbered citations follow `SOURCES.md`.
- [ ] No emdashes are present.
