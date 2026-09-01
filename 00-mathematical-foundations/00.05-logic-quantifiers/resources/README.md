# Resources for §0.05 Logic and Quantifiers

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)

This page is reading and implementation guidance, not a second formal bibliography. Numbered sources supporting claims remain in the module [reference list](../README.md#references).

## Core resources

### Classical Logic

- **Resource:** Stewart Shapiro and Teresa Kouri Kissel, "Classical Logic," *Stanford Encyclopedia of Philosophy*.
- **What it covers:** Formal language, first-order syntax, a deductive system, model-theoretic semantics, semantic validity, satisfiability, soundness, completeness, and alternatives to classical logic.
- **Why it is included:** This is the strongest single source for the module's organizing distinction among syntax, deduction, semantics, and metatheory. Use Sections 2 through 5 when the words `valid`, `derivable`, `sound`, or `complete` begin to blur together.
- **Assumed level:** The opening sections are accessible after this module. The metatheory is more advanced.
- **Access:** Free scholarly encyclopedia entry, substantively revised June 17, 2026. https://plato.stanford.edu/entries/logic-classical/

### Mathematics in Lean, Chapter 3

- **Resource:** Jeremy Avigad and Patrick Massot, *Mathematics in Lean*, Chapter 3, "Logic."
- **What it covers:** Implication, universal and existential quantifiers, negation, conjunction, biconditionals, disjunction, and mathematical examples written as checked Lean proofs.
- **Why it is included:** Formal proof makes side conditions and evidence requirements concrete. The chapter is especially useful for seeing why a universal proof introduces an arbitrary object, why an existential proof supplies a witness, and how negation moves across quantifiers.
- **Assumed level:** Undergraduate mathematics plus willingness to read a small amount of Lean syntax.
- **Access:** Free web text and source. Text licensed CC BY 4.0. https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html

### Discrete Mathematics: An Open Introduction, Section 3.1

- **Resource:** Oscar Levin, *Discrete Mathematics: An Open Introduction*, 3rd edition, Section 3.1, "Propositional Logic."
- **What it covers:** Propositions, exact connective truth tables, tautologies, logical equivalence, De Morgan's laws, implication elimination, deduction rules, quantifier negation, and quantifier order.
- **Why it is included:** This is the most approachable second treatment for hand practice. It connects truth tables to argument validity before previewing predicates and quantifiers.
- **Assumed level:** Introductory undergraduate discrete mathematics.
- **Access:** Free web and PDF editions. Licensed CC BY-SA 4.0. https://discrete.openmathbooks.org/dmoi3/sec_propositional.html

### Mathematics for Computer Science

- **Resource:** Lehman, Leighton, and Meyer, *Mathematics for Computer Science*, with MIT 6.042J course materials.
- **What it covers:** Definitions, proofs, sets, functions, relations, graphs, state machines, counting, probability, and mathematical reasoning for computing.
- **Why it is included:** Use this as the broader continuation from logic into proof techniques, induction, combinatorics, and discrete structures. It aligns the formal material with later computer-science applications.
- **Assumed level:** Introductory undergraduate, proof-oriented.
- **Access:** Free MIT OpenCourseWare course page, open textbook, lectures, problems, and exams. MIT OCW states a CC BY-NC-SA 4.0 site license. https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/

## Formal logic depth

### Open Logic Project builds

- **Resource:** Open Logic Project, generated build index.
- **What it covers:** Separate components for propositional syntax and semantics; valuations and satisfiability; first-order terms, formulas, free variables, structures, assignments, and satisfaction; natural deduction, sequent calculus, tableaux, soundness, and completeness.
- **Why it is included:** The component index is useful when you need one narrowly focused topic rather than a full book. It also makes the separation between semantic and proof-theoretic material visible in the table of contents.
- **Assumed level:** Undergraduate logic for the introductory components; advanced undergraduate or graduate level for metatheory.
- **Access:** Free generated PDFs and source files. The inspected index records Git revision `9620cc7` from 2026-07-12. https://builds.openlogicproject.org/

The component PDFs are linked and available from the index, but direct extraction did not yield meaningful text during this audit. The module therefore cites the inspected index and its content labels without making page-specific claims from those PDFs.

## Course and practice resources

### Stanford CS103

- **Resource:** Stanford, *CS103 Mathematical Foundations of Computing*, Summer 2026.
- **What it covers:** Mathematical logic, proof writing, sets, functions, graphs, computability, and complexity.
- **Why it is included:** This course shows the route from formal logic into the theoretical foundations of computing. Use its public schedule and selected handouts when moving into §§0.06 and 0.15.
- **Assumed level:** Undergraduate computer science discrete mathematics.
- **Access:** Public course overview and selected materials; some systems require Stanford access. The inspected page was last updated June 22, 2026. https://web.stanford.edu/class/cs103/

Stanford course materials are copyrighted. They are linked for study only. No exercise, solution, example, table, or figure in this module is adapted from them.

### Stanford CS103 Truth Table Generator

- **Resource:** Stanford CS103, "Truth Table Generator."
- **What it covers:** Interactive propositional truth tables with several accepted text forms for negation, conjunction, disjunction, implication, and truth constants.
- **Why it is included:** Use it as an independent check after computing a truth table by hand. It is not evidence for first-order validity, historical claims, or the behavior of a proof system.
- **Assumed level:** Introductory.
- **Access:** Free web tool. https://web.stanford.edu/class/cs103/tools/truth-table-tool/

## Implementation resources

### Python `itertools.product`

- **Resource:** Python Software Foundation documentation for `itertools.product`.
- **What it covers:** Cartesian-product iteration, repeated factors, deterministic odometer order, and the finite-input requirement.
- **Why it is included:** The module evaluator uses `product((False, True), repeat=n)` to enumerate the valuation space $\{F,T\}^n$ exactly.
- **Assumed level:** Basic Python.
- **Access:** Free official Python 3.14 documentation. https://docs.python.org/3/library/itertools.html#itertools.product

### Python Boolean operations

- **Resource:** Python Language Reference, "Boolean operations."
- **What it covers:** Truth testing, short-circuit behavior, evaluation order, and the rule that `and` and `or` return the last evaluated operand rather than always returning a Boolean.
- **Why it is included:** This is the source of truth for the warning that Python syntax is not automatically a formal two-valued semantics over arbitrary objects. An evaluator should explicitly return Booleans.
- **Assumed level:** Basic Python.
- **Access:** Free official Python 3.14 language reference. https://docs.python.org/3/reference/expressions.html#boolean-operations

## Suggested sequence

1. Read the module and compute E0.05.02 by hand.
2. Check only the final propositional columns with Stanford's tool.
3. Use Levin for more truth-table and equivalence practice.
4. Read the SEP Sections 2 through 5 beside E0.05.05 and E0.05.12.
5. Use *Mathematics in Lean* when quantifier inference and negation need a formal second view.
6. Use the Open Logic index to choose one narrow syntax, semantics, or proof-system component.
7. Continue into MIT 6.042J and Stanford CS103 for proof and computation.
8. Keep the Python pages open while implementing E0.05.09 and E0.05.11.

## Access and originality notes

- Every landing page and documentation URL above was opened and substantively inspected on 2026-09-01.
- The SEP entry is cited for its formal distinctions and 2026 revision, not copied for prose or examples.
- *Mathematics in Lean* and Levin's text have open licenses, but this module's exposition, examples, and exercises are original rather than adaptations.
- The Open Logic build index was inspectable and records revision `9620cc7`; no page-specific PDF claim is made because extraction failed.
- Stanford's course and tool were inspected for course scope and tool behavior only. No proprietary exercise was reused.
- Python documentation was inspected for `itertools.product` and Boolean operand-return behavior.
- All prose, formulas selected as teaching examples, exercises, solutions, Mermaid diagrams, and SVG figures in this module are original.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)
