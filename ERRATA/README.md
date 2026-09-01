# Errata

## Purpose

This directory records substantive corrections to published curriculum material. The goal is not to preserve every typo. It is to make meaningful mistakes visible, explain their impact, and show how they were corrected.

A correction belongs here when the original could change a reader's understanding, derivation, implementation, experiment, or answer.

## What Belongs Here

Record:

- incorrect equations, proofs, or theorem conditions;
- incorrect code or expected output;
- misleading historical attribution;
- a figure, table, or label that changes interpretation;
- an exercise with no valid solution as written;
- a solution that teaches an invalid method;
- an experiment that cannot support its stated conclusion;
- a missing prerequisite that materially blocks the module;
- a citation that does not support the claim;
- a privacy, security, or safety error in instructional material.

Correct without an erratum entry:

- spelling, punctuation, and formatting;
- broken links replaced with the same source;
- wording changes that do not alter meaning;
- purely stylistic code cleanup;
- minor accessibility improvements that do not change interpretation.

When uncertain, record the correction. A short transparent entry costs little.

## Statuses

- `reported`: submitted but not yet verified;
- `confirmed`: verified and awaiting a correction;
- `corrected`: fixed in the curriculum;
- `disputed`: evidence or interpretation remains unresolved;
- `superseded`: replaced by a later erratum covering the same issue.

## Erratum IDs and Files

Use IDs in the form:

```text
IA-YYYY-NNN
```

Example:

```text
IA-2026-001
```

Create one Markdown file per substantive correction:

```text
ERRATA/IA-2026-001.md
```

Do not reuse IDs. Keep corrected entries rather than deleting them.

## Erratum Template

```markdown
# IA-YYYY-NNN: Short title

- **Status:** reported | confirmed | corrected | disputed | superseded
- **Reported:** YYYY-MM-DD
- **Confirmed:** YYYY-MM-DD or N/A
- **Corrected:** YYYY-MM-DD or N/A
- **Affected module:** §NN.MM
- **Affected files:** paths
- **Reported by:** name or `anonymous`
- **Fix:** commit or pull request link

## Original

Quote or summarize the incorrect statement, equation, code behavior, exercise, or result.

## Correction

State the corrected material precisely.

## Why It Was Wrong

Explain the error, including the missing assumption or failed reasoning.

## Impact

Identify affected examples, exercises, solutions, code, notebooks, figures, or downstream modules.

## Verification

Describe how the correction was checked: derivation, primary source, test, reproduced experiment, or independent review.

## References

[1] Numbered reference supporting the correction.
```

## Workflow

1. Open an issue describing the suspected error and evidence.
2. Assign the next erratum ID if the issue is substantive.
3. Verify the report independently.
4. Mark it `confirmed`, `disputed`, or close it as non-substantive.
5. Correct every affected artifact, including exercises and solutions.
6. Add tests or checks that would catch the error again when practical.
7. Link the fixing pull request or commit.
8. Mark the erratum `corrected` and update the index below.
9. Credit the reporter with permission.

Do not delay a clear correction merely to complete a perfect historical investigation. Fix the teaching material, record what is known, and update the entry if stronger evidence appears.

## Review Standard

A correction should be verified using at least one of:

- an independent derivation;
- an authoritative textbook or primary paper;
- a failing and then passing test;
- a reproduced experiment;
- inspection by a qualified reviewer.

AI agreement is not independent verification.

## Index

| ID | Status | Module | Summary | Corrected |
|---|---|---|---|---|
| None | N/A | N/A | No substantive errata recorded yet | N/A |

Replace the placeholder row when the first erratum is added.

## Disputed Corrections

A disputed entry should present:

- the exact point of disagreement;
- evidence for each serious interpretation;
- what remains unresolved;
- the temporary wording used in the curriculum;
- what evidence would settle the issue.

Do not use `disputed` to avoid correcting a demonstrable error.

## Relationship to Git History

Git records what changed. Errata explains why the original was materially wrong and what readers should now believe. Both are useful, and neither replaces the other.
