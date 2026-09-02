# Resources for §0.11 Graph Theory

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)

This page is annotated reading guidance and a provenance record, not a second
bibliography. Numbered evidence remains in the module [reference list](../README.md#references).

## Core route

### Levin, Discrete Mathematics: An Open Introduction

- **What was directly inspected:** The complete HTML graph chapter, especially
  definitions and representations, handshake lemma, trees and spanning trees,
  connected planar Euler formula, Euler versus Hamilton paths, vertex coloring,
  bipartite matching, augmenting paths, and Hall's theorem.
- **Why it is included:** It is the most accessible single route through the
  simple undirected core and exposes theorem statements and assumptions in HTML.
- **Assumed level:** Introductory undergraduate discrete mathematics.
- **Access and rights:** Free HTML and PDF, CC BY-NC-SA 4.0. No prose, exercise,
  solution, or figure was adapted.

The source mainly uses "graph" for a simple undirected graph. This module marks
every extension to digraphs and multigraphs explicitly. The disconnected planar
formula is developed as an exercise in the source and independently derived in
the lesson.

### MIT Mathematics for Computer Science

- **What was directly inspected:** The official Spring 2015 reading index,
  course metadata, instructor names, textbook link, chapter sequence, and OCW
  license. The downloadable textbook endpoint was verified, but neither the web
  extractor nor local PDF tools exposed reliable text in this environment.
- **Why it is included:** Use it as a second broad discrete-mathematics route,
  especially for proof practice and structures.
- **Assumed level:** Undergraduate computer science mathematics.
- **Access and rights:** MIT OpenCourseWare, CC BY-NC-SA 4.0.

Because theorem-bearing PDF text was not directly extractable here, MIT 6.042J
is annotated guidance but is not a numbered source for a claim unique to it.

## Algorithms route

### Sedgewick and Wayne, MST

- **What was directly inspected:** The official Princeton HTML page's MST
  definition, connectedness assumption, arbitrary and possibly negative
  weights, tie behavior, cut property, Kruskal description, and treatment of
  parallel edges and loops.
- **Why it is included:** It makes the MST input contract unusually explicit.
- **Assumed level:** Undergraduate algorithms.
- **Access and rights:** Freely readable author booksite; copyright retained. No
  code, exercise, solution, or figure was reused.

### Erickson, Algorithms

- **What was directly inspected:** The official Illinois book page, chapter
  inventory for basic graphs, DFS, MST, maximum flow/minimum cut, and flow
  applications; publication metadata; prerequisite warning; and license.
- **Why it is included:** Chapters 5-7 and 10-11 are the deeper path after this
  module. Their algorithm analysis belongs mainly to §0.14.
- **Assumed level:** Advanced undergraduate algorithms with prior data structures.
- **Access and rights:** Free first-edition PDF, CC BY 4.0.

### Sedgewick and Wayne, maximum flow

- **What was directly inspected:** The official Princeton HTML page identifying
  maximum flow, minimum $s$-$t$ cut, Edmonds-Karp shortest augmenting paths, and
  bipartite-matching applications.
- **Why it is included:** It supports the named implementation family and its
  returned cut certificate.
- **Assumed level:** Undergraduate algorithms.
- **Access and rights:** Freely readable author booksite; copyright retained.

The page labels itself under major construction, so Erickson is the preferred
deeper theorem treatment. Princeton is used for the exact implementation name.

## Matching route

### Gale and Shapley, 1962

- **What was directly inspected:** Crossref's DOI metadata for title, authors,
  journal, year, volume, issue, and pages. The publisher landing page presented
  a CAPTCHA, so no inaccessible text was treated as inspected evidence.
- **Why it is included:** It is the primary historical record for deferred
  acceptance and stable two-sided allocation.
- **Assumed level:** Undergraduate discrete mathematics or market design.
- **Access and rights:** Publisher-controlled article; no text, example, or
  notation was copied.

### Roughgarden, Stanford CS364A Lecture 10

- **What was directly inspected:** The official course page, instructor and term,
  Lecture 10's "Kidney Exchange, Stable Matching" title, linked notes/video, and
  assigned readings.
- **Why it is included:** It shows where stable matching leads in market design
  after the finite deferred-acceptance foundation.
- **Assumed level:** Advanced algorithms and basic game theory.
- **Access and rights:** Public Stanford course material. No note text or
  exercises were adapted.

## Matrix and autodiff route

### MIT 18.06 Lecture 12

- **What was directly inspected:** The official page title, instructor, course
  term, lecture-recording note, and description connecting graphs, electrical
  networks, the Internet, and incidence matrices.
- **Why it is included:** This is the roadmap's requested bridge from graph
  structure to later linear algebra.
- **Assumed level:** Introductory linear algebra.
- **Access and rights:** MIT OpenCourseWare, CC BY-NC-SA 4.0.

### JAX Autodidax

- **What was directly inspected:** The official executable tutorial's primitive
  tracing, Jaxpr representation, partial-evaluation tracer-recipe bipartite DAG,
  topological sort, and reverse interpreter.
- **Why it is included:** It gives a concrete official example of DAG order
  inside an automatic-differentiation system.
- **Assumed level:** Strong Python and introductory autodiff.
- **Access and rights:** JAX project documentation and source, Apache 2.0. No
  tutorial code was copied.

## Implementation reference

### Python 3.14 documentation

- **What was directly inspected:** `collections.deque` endpoint operations and
  guarantees, dictionary insertion ordering, and `heapq` tie-handling guidance.
- **Why it is included:** These are the software contracts behind deterministic
  queue and ordering choices in the module code.
- **Assumed level:** Basic Python.
- **Access and rights:** PSF License Version 2; documentation examples also 0BSD.

## Suggested sequence

1. Read Levin §§2.1-2.2 beside models, traversal, and trees.
2. Read Princeton 4.3 beside the Kruskal implementation.
3. Read Levin §2.7 and the stable-matching section as two distinct allocation
   questions.
4. Read Levin §§2.3-2.5 beside planarity, tours, and coloring.
5. Watch MIT 18.06 Lecture 12 after the incidence derivation.
6. Read the selected JAX Autodidax passages before §2.13.
7. Use Erickson for the deeper algorithms route, especially flow and cut.
8. Stop before spectral methods, shortest paths, advanced planarity, and full
   algorithm analysis.

## Provenance and originality ledger

| Source | Accessed | Exact support used | Inspection limit | Reuse boundary |
|---|---|---|---|---|
| Levin Chapter 2 HTML | 2026-09-01 | simple graph core, trees, Hall, tours, coloring, planar Euler | broad page required targeted theorem inspection | no prose, exercise, solution, or figure adapted |
| MIT 6.042J readings | 2026-09-01 | course metadata and open-text route | PDF text extraction unavailable | not numbered for unique theorem claims |
| Princeton MST | 2026-09-01 | MST assumptions, ties, cut property, Kruskal | author page retains copyright | no code or visual reused |
| Gale-Shapley DOI record | 2026-09-01 | primary paper metadata and historical scope | publisher CAPTCHA blocked article text | no article text reused |
| Stanford CS364A | 2026-09-01 | stable-matching course placement and further route | linked PDF not extracted | no note content reused |
| MIT 18.06 Lecture 12 | 2026-09-01 | incidence-matrix bridge | page summarizes rather than transcribes lecture | derivations are original |
| JAX Autodidax | 2026-09-01 | tracer-recipe DAG, topological sort, reverse pass | work-in-progress tutorial | no source code copied |
| Erickson Algorithms | 2026-09-01 | graph and flow chapter route, license | PDF text not extracted | no exercise or figure reused |
| Princeton maximum flow | 2026-09-01 | Edmonds-Karp and min-cut output | page marked under construction | implementation independently written |
| Python 3.14 docs | 2026-09-01 | deque and ordering semantics | platform performance remains implementation-dependent | API semantics only |

The lesson's examples, proofs, exercise set, solutions, Python code, tests,
Mermaid diagrams, and four SVG figures are original. No generated summary,
Wikipedia page, or MathWorld page was used as numbered evidence.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)