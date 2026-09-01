# Contributing to Intelligence, Assembled

## Welcome

**Intelligence, Assembled** is a personal learning project made public because good explanations improve when other people question, test, correct, and extend them.

Contributions are welcome when they make the curriculum more accurate, understandable, useful, or reproducible. This includes corrections, explanations, derivations, examples, exercises, solutions, code, notebooks, diagrams, historical context, and references.

Before contributing, read:

1. `README.md` for the project's purpose and voice;
2. `ROADMAP.md` for scope and module IDs;
3. `STYLE_GUIDE.md` for teaching and presentation standards;
4. `NOTATION.md` for mathematical conventions;
5. `SOURCES.md` for citation and licensing standards;
6. `ERRATA/README.md` for substantive corrections.

## Contribution Principles

- Explain theory in plain English without hiding the mathematics.
- Build intuition and rigor together.
- Derive before implementing when the derivation matters.
- Implement the central mechanism before hiding it behind a framework.
- Include history when it explains why an idea exists.
- Use visuals when they teach something meaningful.
- Design exercises that require thought and ship worked solutions.
- State assumptions, limitations, and uncertainty honestly.
- Prefer focused changes over broad rewrites.
- Preserve the project's direct, conversational voice.
- Do not use emdashes.

## What You Can Contribute

- **Corrections:** math, code, history, prerequisites, terminology, accessibility, and stale claims.
- **Explanations:** clearer intuition, missing derivation steps, counterexamples, or connections.
- **Examples:** small numerical cases, realistic applications, failure cases, and debugging scenarios.
- **Visuals:** diagrams, plots, animations, comparison tables, and historical images.
- **Exercises and solutions:** conceptual, mathematical, implementation, experimental, and applied work.
- **Code and tests:** first-principles implementations, numerical checks, and figure generators.
- **Notebooks:** reproducible investigations with interpretation and limitations.
- **Sources:** primary references and useful resources with an explanation of why they belong.

## Before You Start

### Find the Owning Module

Search `ROADMAP.md` for the concept and its aliases. Every concept should have one primary home. Later modules may revisit it in a new context, but they should link back rather than repeat the same treatment.

### Check Prerequisites

A contribution must not quietly depend on material taught later. Check the section graph and `PREREQUISITES.md`. If you add a prerequisite, identify the exact concept and whether it is required or merely recommended.

### Open an Issue First When Needed

Open an issue before working on:

- a new module or section;
- roadmap or prerequisite changes;
- a major rewrite;
- a new repository-wide convention;
- a large dependency or dataset;
- a hardware-intensive experiment;
- a disputed correction;
- anything affecting several modules.

A direct pull request is usually fine for:

- typos and grammar;
- broken links;
- small clarifications;
- missing citations;
- isolated test fixes;
- improved alt text;
- small examples that follow existing structure.

When uncertain, ask. A short conversation is cheaper than discarding a large contribution.

## Workflow

1. Create a focused branch.
2. Make the smallest coherent change.
3. Run the relevant tests and checks.
4. Inspect the rendered Markdown, equations, figures, and diff.
5. Open a pull request explaining purpose, scope, evidence, verification, and limitations.

Do not mix unrelated formatting or refactoring into the contribution.

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

## Module Template

Use the canonical [module file structure, metadata, and content layout](STYLE_GUIDE.md#module-file-structure). If a required layer does not apply, retain its heading and explain why briefly.

This contribution guide intentionally does not reproduce the template. Changes to module layout belong in `STYLE_GUIDE.md` so contributors always work from one current version.

## Exercises and Solutions

Each exercise should include:

- a stable ID such as `E05.06.1`;
- type and difficulty from 1 through 5;
- the learning objective it assesses;
- estimated time;
- allowed tools;
- assumptions and expected deliverables;
- progressive hints when useful.

Use a mix of conceptual, calculation, derivation, proof, implementation, experiment, applied, critique, and extension exercises.

Put full worked solutions in the sibling `solutions/` directory. A solution should identify the key idea, show the reasoning, verify the result, and discuss common wrong turns. Include alternatives only when they teach a genuinely different approach.

## Code and Notebook Standards

Code should be correct, readable, tested, and connected to the derivation.

Tests should cover:

- hand-computed examples;
- expected shapes and dtypes;
- boundary and failure cases;
- numerical agreement within justified tolerances;
- deterministic behavior where expected;
- comparison with a trusted implementation when useful.

Notebooks must:

- run top to bottom in a clean environment;
- use relative paths;
- state data provenance and licensing;
- record seeds or explain nondeterminism;
- report expected runtime and hardware;
- include interpretation between code sections;
- finish with conclusions and limitations;
- avoid private credentials and unnecessary committed output.

## Visual Standards

Every visual needs:

- a clear teaching purpose;
- descriptive alt text and a caption;
- readable labels, units, and legends;
- a source or `Original figure` attribution;
- non-color cues when color distinguishes meaning;
- generating code when produced computationally.

Before adapting an image, table, exercise, or diagram, verify its license and document the adaptation.

## Sources and Originality

Prefer:

1. primary papers;
2. authoritative textbooks;
3. official standards and documentation;
4. official university materials;
5. high-quality surveys;
6. secondary explanations with unusual pedagogical value.

Use numbered citations in order of first appearance. Open every submitted source and verify that it supports the nearby claim.

Do not submit copied textbook material, proprietary course solutions, paywalled figures without permission, incompatible code, or datasets without documented rights.

## Pull Request Checklist

```markdown
## Summary

What changed and why?

## Scope

- Module(s):
- Files changed:
- Out of scope:

## Learning objectives

Which objectives does this support?

## Evidence

Which sources support the contribution?

## Verification

- [ ] Markdown preview inspected
- [ ] Mathematics checked
- [ ] Tests passed
- [ ] Notebook runs top to bottom
- [ ] Figures regenerated and inspected
- [ ] Exercises and solutions agree
- [ ] Links and citations checked
- [ ] Accessibility checked
- [ ] No emdashes added

## AI assistance

- [ ] None
- [ ] Used and disclosed below

Tool/model:
Assisted portions:
Human verification:

## Limitations

What remains uncertain or incomplete?
```

## Definition of Done

A module may be marked `complete` when:

- [ ] metadata, objectives, prerequisites, and effort are accurate;
- [ ] intuition and formal theory are both developed;
- [ ] central derivations show load-bearing steps;
- [ ] history is useful and cited;
- [ ] examples include a small case and a failure case;
- [ ] implementation and experiments are present or marked not applicable;
- [ ] code and notebooks run successfully;
- [ ] visuals are meaningful and accessible;
- [ ] exercises cover several modes and have worked solutions;
- [ ] limitations and open questions are stated;
- [ ] notation and numbered citations follow project policy.

A module may be marked `reviewed` when another person has also checked technical correctness, sources, reproducibility, exercises, solutions, and accessibility, and `last_reviewed` records the date.

## Reporting Problems

Open an issue when you find an incorrect result, missing prerequisite, irreproducible experiment, accessibility barrier, stale claim, broken source, or overloaded term not handled by `GLOSSARY.md`.

For substantive corrections, follow `ERRATA/README.md`.
