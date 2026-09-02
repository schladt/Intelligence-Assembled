# Resources for §0.08 Counting and Combinatorics

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)

This page is annotated reading guidance and a provenance record, not a second formal bibliography. Numbered sources supporting lesson claims remain in the module [reference list](../README.md#references).

## Core route

### MIT 6.042J Mathematics for Computer Science

- **Resource:** Eric Lehman, F. Thomson Leighton, and Albert R. Meyer, *Mathematics for Computer Science*, with MIT 6.042J OpenCourseWare, Spring 2015.
- **What was inspected:** The official reading index identifies Unit 3 as Counting, with sessions 23 through 27 assigned to Chapters 13 and 14, followed by Unit 4 Probability.
- **Why it is included:** It supports the module's placement of finite counting before probability and provides the broad computer-science continuation.
- **Assumed level:** Introductory undergraduate, proof-oriented.
- **Access:** Free course page, readings, textbook resource, lectures, problems, and exams. MIT OpenCourseWare site license: CC BY-NC-SA 4.0. https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/

The reading index was directly inspectable on 2026-09-01. The textbook resource itself was blocked by the client, so this module makes no page-specific theorem claim from the PDF.

### Combinatorics and Graph Theory

- **Resource:** David Guichard, *Combinatorics and Graph Theory*, Whitman College.
- **What was inspected:** HTML sections 1.2, 1.3, 1.5, 2.1, 3.4, and 3.5. They visibly cover sum and product principles, permutations and combinations, Pascal and binomial identities, sampling with and without replacement, multisets, multinomials, stars and bars, inclusion-exclusion, generating functions for recurrences, Fibonacci, and Catalan numbers.
- **Why it is included:** This is the strongest directly inspectable source for the module's complete mathematical route. Its formulas were checked against independent derivations and exact code.
- **Assumed level:** Undergraduate combinatorics after basic proof methods.
- **Access:** Free HTML and PDF. License: CC BY-NC-SA 3.0. https://www.whitman.edu/mathematics/cgt_online/book/

The source's exercises, solutions, prose, examples, tables, and figures were not adapted. The module's treatment and artifacts are original.

### Discrete Mathematics: An Open Introduction

- **Resource:** Oscar Levin, *Discrete Mathematics: An Open Introduction*, 3rd edition, 2023.
- **What was inspected:** The landing page, license, book scope, and HTML Section 1.3 on combinations and permutations. The text covers counting, sequences, logic, graph theory, combinatorial proof, and generating functions.
- **Why it is included:** Use this as a friendlier second explanation and for additional independent practice. Its function-counting examples connect well to §0.04.
- **Assumed level:** First or second year undergraduate mathematics or computer science.
- **Access:** Free HTML, PDF, and source. License: CC BY-SA 4.0. https://discrete.openmathbooks.org/dmoi3.html

## Focused routes

### For sampling models and multisets

Read Guichard §1.5 after the module's sampling table. It explicitly distinguishes ordered and unordered selections with and without replacement, then derives multiset permutations and nonnegative integer solutions.

Keep the model boundary visible: type-level replacement is not always the same physical experiment as drawing from several identical-looking copies without replacement.

### For binomial identities

Read Guichard §§1.2-1.3 or Levin §1.3. For each identity, name the common finite set before reading the algebraic proof. Compare Pascal's identity with a distinguished-element split and Vandermonde with a two-group split.

### For inclusion-exclusion

Read Guichard §2.1. Track one object through the alternating sum before applying the formula to bounded integer solutions or derangements. This prevents memorized signs from hiding an omitted intersection depth.

### For generating functions

Read Guichard Chapter 3 only after finite generating polynomials feel natural. Sections 3.4 and 3.5 move from recurrence coefficients to Fibonacci and Catalan examples. This module uses formal coefficient identities only. Defer convergence and infinite-series analysis to §0.09.

## Python implementation resources

### Python `math`

- **Resource:** Python Software Foundation, Python 3.14 `math` documentation.
- **What was inspected:** `math.comb` counts unordered selections without repetition; `math.perm` counts ordered selections without repetition. Both return zero when $k>n$ and reject negative arguments.
- **Why it is included:** It is the software source of truth for the exact reference operations used in tests.
- **Access:** Free official documentation under PSF License Version 2. https://docs.python.org/3/library/math.html#math.comb

### Python `itertools`

- **Resource:** Python Software Foundation, Python 3.14 `itertools` documentation.
- **What was inspected:** `product`, `permutations`, `combinations`, and `combinations_with_replacement`; output ordering; positional identity; finite-input consumption for `product`; and the formulas for iterator lengths.
- **Why it is included:** These iterators exhaust small finite model instances independently of the module's formula helpers.
- **Access:** Free official documentation under PSF License Version 2. Documentation examples and recipes are additionally 0BSD. https://docs.python.org/3/library/itertools.html#itertools.product

## Suggested sequence

1. Complete E0.08.01 before opening a formula reference.
2. Use Levin §1.3 for a second pass on permutations and combinations.
3. Read Guichard §1.5 beside E0.08.03 and E0.08.07.
4. Read Guichard §2.1 beside E0.08.08.
5. Use MIT's Unit 3 for broader proof-oriented practice.
6. Read Guichard Chapter 3 beside E0.08.10 and E0.08.11.
7. Keep official Python pages open while extending the module tests.
8. Stop before analytic convergence or asymptotic coefficient estimates and continue there only after §0.09 is published.

## Provenance and originality ledger

| Source | Accessed | Exact support used | Reuse boundary |
|---|---|---|---|
| MIT 6.042J readings | 2026-09-01 | dedicated counting unit precedes probability | index facts only; blocked textbook supports no page-level claim |
| Guichard HTML text | 2026-09-01 | formulas and topic sequence listed above | cited and checked; no exercise, prose, code, or visual adapted |
| Levin landing and §1.3 | 2026-09-01 | edition, license, scope, permutation and combination treatment | linked as second treatment; no material adapted |
| Python `math` | 2026-09-01 | `comb` and `perm` behavior | API semantics only; module helpers and tests original |
| Python `itertools` | 2026-09-01 | iterator carriers, lengths, and positional identity | API semantics only; examples in this module independently written |

One candidate open-combinatorics URL served a default nginx page during research and was excluded. Wilf's *generatingfunctionology* PDF URL was reachable but not text-extractable through the inspection client, so no claim here relies on its contents.

Every source above was opened directly. AI-generated summaries were not treated as evidence. All lesson prose, selected examples, exercises, worked solutions, Python implementation, tests, Mermaid diagrams, and SVG figures in this module are original.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)