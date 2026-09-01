# Resources for §0.04 Sets, Relations, and Functions

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)

This page is reading and implementation guidance, not a second formal bibliography. Numbered sources supporting claims remain in the module [reference list](../README.md#references).

## Core resources

### Mathematics for Computer Science

- **Resource:** Lehman, Leighton, and Meyer, *Mathematics for Computer Science*, with the MIT 6.042J course materials.
- **What it covers:** Definitions, sets, functions, relations, proofs, partial orders, equivalence relations, and later discrete mathematics in a computer-science setting.
- **Why it is included:** This is the broadest course-aligned continuation of the module. Use it when you want more proof practice and connections to graphs, state machines, counting, and probability.
- **Assumed level:** Introductory undergraduate, proof-oriented.
- **Access:** Free MIT OpenCourseWare course page, open textbook, lectures, problems, and exams. MIT OCW states a CC BY-NC-SA 4.0 site license. https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/

### Open Logic Project: Sets, Functions, Relations

- **Resource:** Open Logic Project, *Sets, Functions, Relations*.
- **What it covers:** Set basics, subsets, products, Russell's paradox, relation properties, equivalence relations, orders, functions, inverses, composition, and set size.
- **Why it is included:** Its section structure closely matches this module, but it extends further into logic and foundations. Use the small component PDFs when one definition needs a second treatment.
- **Assumed level:** Undergraduate logic or discrete mathematics.
- **Access:** Free generated PDFs and source files. The inspected build index records revision `9620cc7` from 2026-07-12 and links the complete text plus component PDFs. https://builds.openlogicproject.org/

### Discrete Mathematics: An Open Introduction

- **Resource:** Oscar Levin, *Discrete Mathematics: An Open Introduction*, 3rd edition.
- **What it covers:** An introductory chapter on mathematical statements, sets, and functions, followed by counting, sequences, logic, graph theory, proof methods, and number theory.
- **Why it is included:** The book uses a friendly inquiry-based style and offers many exercises with hints or solutions. Use it for additional practice after the module's synthesis-heavy problems.
- **Assumed level:** First or second year undergraduate mathematics or computer science.
- **Access:** Free online and PDF editions. Licensed CC BY-SA 4.0. A fourth edition is available, while the stable third-edition page remains public. https://discrete.openmathbooks.org/dmoi3.html

### Mathematics in Lean, Chapter 4

- **Resource:** Jeremy Avigad and Patrick Massot, *Mathematics in Lean*, Chapter 4, "Sets and Functions."
- **What it covers:** Extensionality, set-builder notation, unions, intersections, differences, indexed families, images, preimages, injectivity, surjectivity, inverse construction, Cantor's theorem, and Schröder-Bernstein formalization.
- **Why it is included:** This is the best resource here for seeing exactly which assumptions each image or preimage law needs. The formal proofs expose witness handling that informal notation can hide.
- **Assumed level:** Undergraduate mathematics plus willingness to read Lean. Prior Lean experience helps but is not required for the prose.
- **Access:** Free web text and source. Text licensed CC BY 4.0. https://leanprover-community.github.io/mathematics_in_lean/C04_Sets_and_Functions.html

## History and foundations

### Russell's Paradox

- **Resource:** Deutsch, Marshall, and Irvine, "Russell's Paradox," *Stanford Encyclopedia of Philosophy*.
- **What it covers:** The unrestricted comprehension principle, the paradox, historical anticipations and attribution, Cantor diagonalization, Russell's work, Zermelo-style separation, type approaches, set-class approaches, and other responses.
- **Why it is included:** Use it to check any historical statement about discovery or any claim that one foundational response is uniquely forced. Sections 1, 2.1-2.2, and 4 are the most relevant to this module.
- **Assumed level:** General mathematical logic; later sections are philosophically and technically denser.
- **Access:** Free scholarly encyclopedia entry, substantively revised March 13, 2026. https://plato.stanford.edu/entries/russell-paradox/

### Set Theory

- **Resource:** Joan Bagaria, "Set Theory," *Stanford Encyclopedia of Philosophy*.
- **What it covers:** Cantor's cardinal comparison, early paradoxes, extensionality, power sets, products, separation, ZF and ZFC, alternatives, and the later theory of ordinals and cardinals.
- **Why it is included:** Read Sections 1 and 2 for a careful preview of why axioms are needed. Stop before the advanced cardinal and forcing material unless that is your independent goal.
- **Assumed level:** The opening is accessible after this module; later sections are advanced.
- **Access:** Free scholarly encyclopedia entry, substantive revision 2023. https://plato.stanford.edu/entries/set-theory/

### Set Theory: An Open Introduction

- **Resource:** Open Logic Project, *Set Theory: An Open Introduction*.
- **What it covers:** The motivation for set theory, reduction of mathematical objects to sets, the cumulative conception, and possible justification of ZFC axioms.
- **Why it is included:** This is the natural next source for readers who want the foundations that this module explicitly defers. It asks why axioms are adopted rather than presenting them as arbitrary rules.
- **Assumed level:** Intermediate undergraduate logic or philosophy of mathematics.
- **Access:** Free screen and print PDFs with source available. https://st.openlogicproject.org/

## Course and implementation resources

### Stanford CS103

- **Resource:** Stanford, *CS103 Mathematical Foundations of Computing*.
- **What it covers:** Mathematical logic, proof writing, sets, functions, graphs, computability, and complexity.
- **Why it is included:** Use the public schedule and handouts for another computer-science route from sets into proof and computation. The course is especially useful when §0.05 and §0.06 are published.
- **Assumed level:** Undergraduate computer science discrete mathematics.
- **Access:** Public course overview and selected materials; some systems require Stanford access. Current page checked for Summer 2026. https://web.stanford.edu/class/cs103/

### Python set, itertools, and fractions documentation

- **Resource:** Python Software Foundation documentation for `set`, `frozenset`, `itertools.product`, and `fractions.Fraction`.
- **What it covers:** Membership and mathematical set operations, hashability, Cartesian-product iteration, and normalized rational representations.
- **Why it is included:** These pages are the source of truth for the module's standard-library examples. Read them when container behavior, iteration order, or rational normalization affects an experiment.
- **Assumed level:** Basic Python.
- **Access:** Free official Python 3.14 documentation. https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset, https://docs.python.org/3/library/itertools.html#itertools.product, and https://docs.python.org/3/library/fractions.html

## Suggested sequence

1. Complete the module's notation and relation exercises before adding formal machinery.
2. Use MIT 6.042J or Levin for more discrete-mathematics practice.
3. Read *Mathematics in Lean* beside E0.04.07 and E0.04.11 to inspect exact assumptions.
4. Read the SEP Russell entry before making historical or foundational claims.
5. Continue to the Open Logic set theory text only if you want the axiomatic material deliberately deferred here.
6. Keep the Python documentation open during the relation and rational-enumeration experiments.

## Access notes

- Every cited landing or index URL above was opened and substantively inspected on 2026-09-01.
- Direct extraction of the MIT textbook resource was blocked by the client, and direct extraction of the Open Logic PDF returned no meaningful text. The inspected MIT course page and Open Logic build index expose the relevant coverage, so this module makes no page-specific claims from either PDF.
- The VCU *Book of Proof* landing page was considered but could not be meaningfully extracted during source verification, so it is not cited here.
- The MIT course page and Open Logic build index exposed their relevant contents; no unverified PDF page claims are made.
- Stanford course materials are copyrighted and are linked for reading only. No exercise or figure here is adapted from them.
- All prose, examples, exercises, solutions, Mermaid diagrams, and SVG figures in this module are original.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)
