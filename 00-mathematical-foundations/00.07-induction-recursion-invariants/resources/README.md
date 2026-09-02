# Resources for §0.07 Induction, Recursion, and Invariants

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)

This page is annotated reading guidance, not a second bibliography. Numbered sources supporting lesson claims remain in the module [reference list](../README.md#references).

## Core proof resources

### Mathematics for Computer Science

- **Resource:** Eric Lehman, F. Thomson Leighton, and Albert R. Meyer, *Mathematics for Computer Science*, with MIT 6.042J OpenCourseWare.
- **What it covers:** The inspected reading index separates Unit 1: Proofs, Unit 2: Structures, Unit 3: Counting, and Unit 4: Probability. The course materials connect induction and state machines to broader discrete mathematics.
- **Why it is included:** Use this for the most direct computer-science continuation from induction to invariants, graphs, counting, and probability.
- **Assumed level:** Introductory undergraduate, proof-oriented.
- **Access:** Free MIT OpenCourseWare page, readings, textbook links, lectures, problems, and exams. Site license: CC BY-NC-SA 4.0. https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/

The reading index was directly inspected. The textbook PDF was not extracted for this module, so no page-specific claim is made from it.

### Mathematics in Lean, Chapter 5

- **Resource:** Jeremy Avigad and Patrick Massot, *Mathematics in Lean*, Chapter 5, "Elementary Number Theory."
- **What it covers:** Inductive natural numbers, factorial by recursion, ordinary induction, finite sums and products, strong induction on smaller factors, multiple-base Fibonacci recursion, finite-set induction, and well-founded recursive calls.
- **Why it is included:** This is the clearest source here for seeing one inductive datatype supply both a recursion principle and an induction principle. Formal code also exposes strict-decrease and domain obligations.
- **Assumed level:** Undergraduate mathematics plus willingness to read Lean syntax.
- **Access:** Free web text and source. Text licensed CC BY 4.0. https://leanprover-community.github.io/mathematics_in_lean/C05_Elementary_Number_Theory.html

### Open Logic Project: Methods, Induction

- **Resource:** Open Logic Project generated build index and "Methods: Induction" component.
- **What it covers:** The inspected index lists induction on natural numbers, strong induction, inductive definitions, structural induction, and induction on relations as separate components.
- **Why it is included:** Use the index to choose a narrow second treatment and to keep ordinary proof methods separate from induction-specific principles.
- **Assumed level:** Introductory undergraduate logic or discrete mathematics.
- **Access:** Free generated PDFs and source. The inspected build records Git revision `9620cc7` from 2026-07-12. https://builds.openlogicproject.org/ and https://builds.openlogicproject.org/content/methods/induction/induction.pdf

The build index was inspectable. Direct PDF extraction was not reliable, so the lesson makes no page-specific PDF claim.

### Discrete Mathematics: An Open Introduction

- **Resource:** Oscar Levin, *Discrete Mathematics: An Open Introduction*, 3rd edition.
- **What it covers:** Sequences, recurrence relations, mathematical induction, counting, logic, graph theory, and proof methods in an inquiry-based undergraduate text.
- **Why it is included:** Use it for additional hand practice after the module, especially when recurrence generation and induction planning need a friendlier second pass.
- **Assumed level:** First or second year undergraduate mathematics or computer science.
- **Access:** Free online and PDF editions. Licensed CC BY-SA 4.0. https://discrete.openmathbooks.org/dmoi3.html

The landing page, scope, edition, and license were inspected. This module does not adapt its examples or exercises.

## Recurrences and algorithm analysis

### Cornell CS3110: Recursion Trees and the Master Method

- **Resource:** Cornell University, "Lecture 20: Recursion Trees and the Master Method," Spring 2012.
- **What it covers:** Recursion-tree node counts and level work, the balanced recurrence $T(n)=aT(n/b)+f(n)$, the three polynomial-gap cases, the case-three regularity condition, valid examples, and unequal-subproblem non-applicability.
- **Why it is included:** This is the directly inspectable authoritative source for the exact basic Master-Theorem statement used in the lesson. Compare every exercise classification with its hypotheses.
- **Assumed level:** Undergraduate data structures and functional programming.
- **Access:** Free university course note. https://www.cs.cornell.edu/courses/cs3110/2012sp/lectures/lec20-master/lec20.html

### MIT 6.046J Divide and Conquer

- **Resource:** MIT OpenCourseWare, *6.046J Design and Analysis of Algorithms*, Lecture 2, Spring 2015.
- **What it covers:** The official course index identifies Lecture 2 as divide and conquer with convex hull and median finding.
- **Why it is included:** Use it for broader divide-and-conquer context after the small recurrence-analysis slice here.
- **Assumed level:** Undergraduate algorithms after data structures and asymptotic analysis.
- **Access:** Free MIT OpenCourseWare resource. Site license: CC BY-NC-SA 4.0. https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/resources/lecture-2-notes/

The resource page and attached PDF URL were verified. The client blocked the resource page and no local PDF text extractor was available, so this module does not attribute exact theorem wording to it.

### MIT 6.006 lecture-note index

- **Resource:** MIT OpenCourseWare, *6.006 Introduction to Algorithms*, Fall 2011 lecture notes.
- **What it covers:** The inspected index includes sorting, trees, graphs, shortest paths, a four-lecture dynamic-programming unit, and computational complexity.
- **Why it is included:** Follow this route for Fibonacci memoization and dynamic programming after learning the proof and recurrence foundations here.
- **Assumed level:** Introductory undergraduate algorithms.
- **Access:** Free course index and notes. Site license: CC BY-NC-SA 4.0. https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/lecture-notes/

The index does not directly expose a Master-Theorem note, so it is not cited for that theorem.

## Python implementation resources

### Python `functools.cache` and `lru_cache`

- **Resource:** Python Software Foundation, `functools` documentation for Python 3.14.
- **What it covers:** `cache` as a lightweight unbounded cache equivalent to `lru_cache(maxsize=None)`, hashable arguments, cache statistics, retained references, concurrency notes, and Fibonacci memoization.
- **Why it is included:** This is the source of truth for memoization semantics used by the call-count experiment. Read it before interpreting body entries as total wrapper calls.
- **Assumed level:** Basic Python functions and decorators.
- **Access:** Free official documentation under the PSF License Version 2. https://docs.python.org/3/library/functools.html#functools.cache

### Python recursion-limit documentation

- **Resource:** Python Software Foundation, `sys.getrecursionlimit` and `sys.setrecursionlimit`, Python 3.14.
- **What it covers:** The interpreter-stack depth guard, its role in protecting the C stack, platform dependence, and the risk of setting the limit too high.
- **Why it is included:** It keeps practical stack failure separate from mathematical nontermination. The lesson reads the limit but does not change it.
- **Assumed level:** Basic Python runtime behavior.
- **Access:** Free official documentation under the PSF License Version 2. https://docs.python.org/3/library/sys.html#sys.getrecursionlimit

## Suggested sequence

1. Read the module and complete E0.07.01 before attempting longer induction proofs.
2. Use Levin for more ordinary induction and recurrence practice.
3. Compare recursive definitions with *Mathematics in Lean* Chapter 5.
4. Use the Open Logic index when structural and strong induction need separate treatments.
5. Read the Cornell note beside E0.07.11 and check every Master hypothesis.
6. Continue to MIT 6.006 for memoization and dynamic programming.
7. Use MIT 6.046J only after §0.09 supplies fuller asymptotic tools.
8. Keep the Python documentation open during E0.07.12.

## Access and originality notes

- Every landing page, index, HTML note, and Python documentation URL above was directly inspected on 2026-09-01.
- The MIT 6.046J PDF URL was verified, but no theorem text was extracted from it; exact Master conditions come from the inspected Cornell HTML note.
- MIT OpenCourseWare pages state a CC BY-NC-SA 4.0 site license.
- *Mathematics in Lean* is CC BY 4.0, and Levin's text is CC BY-SA 4.0.
- Open licenses permit reuse under their terms, but this module's prose, examples, exercises, solutions, diagrams, and SVG figures are original rather than adaptations.
- Python documentation defines API behavior. Passing assertions remain evidence only for their declared inputs.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)
