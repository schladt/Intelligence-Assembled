# Resources for §0.06 Proof Techniques

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)

This page is reading and implementation guidance, not a second formal bibliography. Numbered sources supporting claims remain in the module [reference list](../README.md#references).

## Core resources

### Stanford CS103 Proofwriting Checklist

- **Resource:** Stanford University, "Proofwriting Checklist," *CS103: Mathematical Foundations of Computing*, Summer 2026.
- **What it covers:** Explicit assumptions and targets, load-bearing sentences, variable provenance and scope, specific claims, using definitions, complete prose, symbolic-density guidance, and contradiction sandwiches.
- **Why it is included:** This is the closest source to the module's proof-audit emphasis. Read it after writing a proof draft, then inspect whether every variable has a source and every sentence advances the argument.
- **Assumed level:** Introductory undergraduate discrete mathematics.
- **Access:** Public web page. The course page was last updated June 22, 2026, and the checklist April 1, 2026. All course materials state copyright Stanford University 2025. Link for study only. https://web.stanford.edu/class/archive/cs/cs103/cs103.1268/proofwriting_checklist

No exercise, solution, example, table, diagram, or figure in this module is adapted from the Stanford material.

### Mathematics for Computer Science

- **Resource:** Eric Lehman, F. Thomson Leighton, and Albert R. Meyer, *Mathematics for Computer Science*, with MIT 6.042J OpenCourseWare.
- **What it covers:** Definitions, proofs, sets, functions, relations, graphs, state machines, counting, and probability for computer science. The inspected reading map assigns Chapters 1 through 7 to Unit 1: Proofs and Chapters 13 through 14 to Unit 3: Counting.
- **Why it is included:** Use it for a broad computer-science continuation, especially proof methods, invariants, graph arguments, and counting. It connects this module to §§0.07, 0.08, 0.11, and 0.15.
- **Assumed level:** Introductory undergraduate, proof-oriented.
- **Access:** Free course page, readings, open textbook, lectures, problem sets, and exams. MIT OpenCourseWare states a CC BY-NC-SA 4.0 site license. https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/

The reading page and course landing page were inspectable. The direct textbook resource was blocked by the client, so this module makes no page-specific claim from the textbook PDF.

### Discrete Mathematics: An Open Introduction

- **Resource:** Oscar Levin, *Discrete Mathematics: An Open Introduction*, 3rd edition.
- **What it covers:** Mathematical statements, sets, functions, logic, proof methods, counting, sequences, graph theory, number theory, induction, and combinatorial proofs.
- **Why it is included:** This is the most approachable source for additional hand practice. Its inquiry-based style is useful when proof discovery feels less natural than proof checking.
- **Assumed level:** First or second year undergraduate mathematics or computer science.
- **Access:** Free online and PDF editions. Licensed CC BY-SA 4.0. The third-edition landing page remains available, while a fourth edition is now offered. https://discrete.openmathbooks.org/dmoi3.html

The landing page identifies proof by contradiction, induction, and combinatorial proof among the text's methods. The module's prose and exercises are original rather than adapted.

### Book of Proof

- **Resource:** Richard Hammack, *Book of Proof*, third edition, revision 3.4.
- **What it covers:** Direct proof, contrapositive proof, contradiction, nonconditional statements, set proofs, disproof, induction, relations, functions, and cardinality.
- **Why it is included:** Use Parts II and III for a sustained second treatment of conditional proof methods, equality, and disproof. Its chapter separation makes it easy to revisit one route at a time.
- **Assumed level:** Introductory undergraduate proof course.
- **Access:** Free PDF and print editions. The inspected landing page records the edition 3.4 correction release on February 5, 2025. Licensed CC BY-NC-ND 4.0. https://richardhammack.github.io/BookOfProof/

The no-derivatives license permits sharing under its terms but not adapting the content for redistribution. This module links to the book and does not adapt its prose, examples, or exercises.

## Formalization and logic

### Mathematics in Lean, Chapter 5

- **Resource:** Jeremy Avigad and Patrick Massot, *Mathematics in Lean*, Chapter 5, "Elementary Number Theory."
- **What it covers:** Formalized irrational-root arguments, coprimality, divisibility, prime-factor reasoning, nonzero side conditions, induction, recursion, finite sets, and infinitely many primes.
- **Why it is included:** Formalization exposes assumptions informal proofs often suppress. Compare its coprimality and nonzero hypotheses with the irrationality and cancellation audits in this module.
- **Assumed level:** Undergraduate mathematics plus willingness to read Lean syntax.
- **Access:** Free web text and source. Text licensed CC BY 4.0. https://leanprover-community.github.io/mathematics_in_lean/C05_Elementary_Number_Theory.html

### Open Logic Project Methods: Proofs

- **Resource:** Open Logic Project generated build index and the "Methods: Proofs" component.
- **What it covers:** Starting proofs, using definitions, inference patterns, proof by contradiction, reading proofs, and proof limitations. The index also separates methods of proof from induction.
- **Why it is included:** The component map reinforces this module's boundary: ordinary proof construction here, induction next. Use the index to select a narrow component rather than opening the complete text.
- **Assumed level:** Introductory undergraduate logic.
- **Access:** Free generated PDFs and source. The inspected build index records Git revision `9620cc7` from July 12, 2026. https://builds.openlogicproject.org/ and https://builds.openlogicproject.org/content/methods/proofs/proofs.pdf

The build index and its component labels were inspectable. PDF text extraction failed, so this module makes no page-specific claim from the methods PDF.

### Classical Logic

- **Resource:** Stewart Shapiro and Teresa Kouri Kissel, "Classical Logic," *Stanford Encyclopedia of Philosophy*.
- **What it covers:** Formal language, a deductive system, model-theoretic semantics, validity, satisfiability, soundness, completeness, quantifier rules, and alternatives to classical logic.
- **Why it is included:** Use Sections 3 through 5 when proof, derivation, semantic consequence, validity, and soundness begin to blur. The quantifier-rule side conditions are especially useful for witness-scope audits.
- **Assumed level:** The opening sections are accessible after §§0.05-0.06; the metatheory is more advanced.
- **Access:** Free scholarly encyclopedia entry, substantively revised June 17, 2026. https://plato.stanford.edu/entries/logic-classical/

## Counting and diagonalization

### Set Theory

- **Resource:** Joan Bagaria, "Set Theory," *Stanford Encyclopedia of Philosophy*.
- **What it covers:** Cantor's cardinal comparison, uncountability, power sets, early paradoxes, and the axioms and later development of set theory.
- **Why it is included:** Use the opening sections for historical and mathematical context around Cantor's diagonal method. Return to §0.04 for this curriculum's complete elementary power-set proof.
- **Assumed level:** Introductory sections are accessible after §0.04; later sections are advanced.
- **Access:** Free scholarly encyclopedia entry, substantively revised January 31, 2023. https://plato.stanford.edu/entries/set-theory/

For pigeonhole, double counting, and combinatorial proof, use the MIT and Levin resources above. This module intentionally stops before §0.08's full counting scope.

## Implementation resources

### Python `itertools` and `math`

- **Resource:** Python Software Foundation documentation for `itertools.product` and `math.ceil`.
- **What it covers:** Finite Cartesian-product iteration, repeated factors, deterministic iteration order, and the ceiling function.
- **Why it is included:** The module uses these operations to exhaust finite assignments and compute the generalized pigeonhole lower bound. Official documentation is the source of truth for software behavior.
- **Assumed level:** Basic Python.
- **Access:** Free Python 3.14 documentation under the PSF License Version 2. https://docs.python.org/3/library/itertools.html and https://docs.python.org/3/library/math.html#math.ceil

`itertools.product` consumes its input pools and is appropriate here only because every experiment declares finite inputs. The code examples remain responsible for their own mathematical interpretation.

## Suggested sequence

1. Read the module and complete E0.06.01 before writing a long proof.
2. Use the Stanford checklist to audit assumptions, targets, variables, and prose.
3. Use Levin or Hammack for more direct, contrapositive, contradiction, and disproof practice.
4. Compare the irrationality example with *Mathematics in Lean* to see hidden hypotheses become explicit.
5. Use MIT 6.042J for the broader route into induction, invariants, graphs, and counting.
6. Use the SEP logic entry when semantic consequence and derivability need to be separated.
7. Return to §0.04 and the SEP set-theory entry for Cantor's theorem rather than duplicating it here.
8. Keep the Python pages open while implementing E0.06.07, E0.06.09, and E0.06.10.

## Access and originality notes

- Every landing page and documentation URL above was opened and substantively inspected on 2026-09-01.
- Stanford course materials are copyrighted and linked for study only. No material was adapted.
- Levin's text is CC BY-SA 4.0, but this module's prose, examples, exercises, solutions, Mermaid diagrams, and SVG figures are original.
- Hammack's book is CC BY-NC-ND 4.0 and was used only as a linked structural reference. No derivative material was created.
- MIT OpenCourseWare states a CC BY-NC-SA 4.0 site license. The inspected reading map supports the unit and chapter-range claims; the blocked textbook file supports no page-specific claim here.
- *Mathematics in Lean* is CC BY 4.0. Its formalization was inspected for assumptions, not copied.
- The Open Logic build index records revision `9620cc7`; the methods PDF exists, but extraction failed, so only index-visible labels are reported.
- SEP entries were cited for scholarly definitions and context, not adapted.
- Python documentation was inspected for exact library behavior. Passing code remains evidence only for declared finite inputs.
- All module prose, formulas selected as examples, exercises, solutions, diagrams, and figures are original.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)
