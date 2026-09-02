# Resources for §0.10 Inequalities

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)

This page is annotated reading guidance and a provenance record, not a second
formal bibliography. Numbered sources supporting lesson claims remain in the
module [reference list](../README.md#references).

## Core route

### Boyd and Vandenberghe, Convex Optimization

- **Resource:** Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*,
  especially §§2.2, 3.1.8, and Appendix A.
- **What was directly inspected:** The official Stanford book page, the
  author-hosted PDF downloaded from that page, and PDF.js text extracted locally.
  The inspected text states finite Jensen for points in a convex-function domain
  and nonnegative weights summing to one; gives expectation and integral
  extensions with existence conditions; states the arithmetic-geometric mean
  inequality on nonnegative vectors; and gives the finite dual-norm product
  bound and conjugate $\ell^p/\ell^q$ relation.
- **Why it is included:** This is the primary source for convex-combination
  contracts, Jensen, AM-GM context, and the norm-family connection.
- **Assumed level:** Advanced undergraduate mathematics. Read only the cited
  sections here; optimization models and duality belong later.
- **Access and rights:** Free author-hosted PDF. Cambridge University Press
  retains copyright and permits the web download. No book prose, exercise,
  solution, table, code, or figure was adapted.

The official HTML page was inspectable on 2026-09-01. Its linked PDF did not
yield meaningful text through the web-page extractor, so the file was downloaded
to a temporary directory and read with Mozilla PDF.js. The PDF's broader
probability and infinite-dimensional extensions are outside this module.

### Boyd and Vandenberghe, Introduction to Applied Linear Algebra

- **Resource:** Stephen Boyd and Lieven Vandenberghe, *Introduction to Applied
  Linear Algebra: Vectors, Matrices, and Least Squares*, Chapter 3.
- **What was directly inspected:** The official book page and locally extracted
  author-hosted PDF. Chapter 3 states Euclidean norm properties, including
  homogeneity, triangle inequality, nonnegativity, and definiteness, and derives
  the triangle inequality from the inner-product bound.
- **Why it is included:** It gives a concise finite-dimensional route from dot
  products to Cauchy-Schwarz and triangle geometry.
- **Assumed level:** Introductory undergraduate linear algebra.
- **Access and rights:** Free author-hosted PDF. Cambridge University Press
  retains copyright. The posted slides request acknowledgment if used; no slides,
  examples, exercises, or figures were reused here.

### OpenStax Calculus Volume 3, §2.3

- **Resource:** Gilbert Strang and Edwin "Jed" Herman, *Calculus Volume 3*, §2.3.
- **What was directly inspected:** The HTML definition of the dot product, its
  algebraic and norm properties, the angle formula, orthogonality theorem,
  projections, examples, and licensing footer.
- **Why it is included:** Use this as the gentler route into inner products and
  the geometric meaning behind Cauchy-Schwarz equality.
- **Assumed level:** Undergraduate precalculus and vectors.
- **Access and rights:** Free HTML and PDF under CC BY-NC-SA 4.0.

The HTML page exposed substantial theorem, example, exercise, and site text.
Inspection was limited to definitions and theorem-bearing passages. No OpenStax
exercise, solution, prose, or figure was adapted.

## Discrete route

### MIT Mathematics for Computer Science

- **Resource:** Albert R. Meyer and Adam Chlipala, *Mathematics for Computer
  Science*, §16.5.
- **What was directly inspected:** The MIT OpenCourseWare reading index, the
  linked full textbook downloaded from the course, and locally extracted text
  around Rule 16.5.4. The text derives Boole's inequality from finite
  inclusion-exclusion and nonnegative probabilities, then states the finite union
  bound and a component-failure example.
- **Why it is included:** It supports the exact finite union-bound contract and
  confirms that independence is not required.
- **Assumed level:** Undergraduate discrete mathematics. Probability spaces are
  supplied by Section 3 in this curriculum.
- **Access and rights:** Free MIT OpenCourseWare material under CC BY-NC-SA 4.0.

The OpenCourseWare textbook resource endpoint was blocked in the web inspector,
while direct official download succeeded. PDF.js extraction was used only for
inspection. The countably infinite extension visible nearby was deliberately not
included in this module.

### Levin, proof by induction

- **Resource:** Oscar Levin, *Discrete Mathematics: An Open Introduction*, 4th
  ed., §4.5.
- **What was directly inspected:** The complete interactive HTML section,
  including its induction objectives, recursive motivation, base and inductive
  cases, examples, warnings, exercises, book metadata, and license.
- **Why it is included:** It is a directly inspectable refresher for the proof
  structure used to derive Bernoulli's inequality. It is not cited as a source of
  Bernoulli's theorem itself.
- **Assumed level:** First-year undergraduate discrete mathematics.
- **Access and rights:** Free interactive text and PDF under CC BY-NC-SA 4.0.

The page did not contain Bernoulli's inequality. The module's Bernoulli proof,
examples, and exercises are independently written from the theorem statement.

## Implementation reference

### Python `math` and `fractions`

- **Resource:** Python Software Foundation, Python 3.14 documentation.
- **What was directly inspected:** `math.fsum`, `math.prod`, `math.hypot`,
  `math.sumprod`, `math.isclose`, floating-point limitations, and exact rational
  construction with `fractions.Fraction`.
- **Why it is included:** This is the software source of truth for the module's
  standard-library accumulation, products, norms, tolerances, and rational-value
  behavior.
- **Assumed level:** Basic Python and floating-point awareness.
- **Access and rights:** Free official documentation under PSF License Version 2;
  code examples are additionally 0BSD.

The API text was directly inspected on 2026-09-01. Documentation links to
Wikipedia for some background topics were not used as evidence. The module code
is original and does not copy documentation examples.

## Suggested sequence

1. Read the module through Cauchy-Schwarz and complete E0.10.01-E0.10.04.
2. Use Boyd and Vandenberghe's Appendix A beside Hölder and Minkowski.
3. Read *Convex Optimization* §3.1.8 beside Jensen and weighted AM-GM.
4. Use OpenStax when the dot-product geometry needs another presentation.
5. Read MIT §16.5 only after events and finite probability tables are meaningful.
6. Review Levin §4.5 before writing the Bernoulli induction proof.
7. Keep Python's `math` page open during the implementation audit.
8. Stop before expectation Jensen, measure theory, convex optimization, or
   concentration bounds.

## Provenance and originality ledger

| Source | Accessed | Exact support used | Extraction limit | Reuse boundary |
|---|---|---|---|---|
| Boyd and Vandenberghe, *Convex Optimization* | 2026-09-01 | finite Jensen contract; AM-GM statement; dual and conjugate norm relations | web extractor could not parse PDF; temporary PDF.js extraction succeeded | cited and checked; no content adapted |
| Boyd and Vandenberghe, *Introduction to Applied Linear Algebra* | 2026-09-01 | norm axioms; Euclidean triangle route | same PDF extraction limit and fallback | no examples, exercises, slides, or figures reused |
| OpenStax §2.3 HTML | 2026-09-01 | dot product, norm relation, angle, orthogonality | long page required targeted theorem inspection | cited and checked; no content adapted |
| MIT 6.042J text §16.5 | 2026-09-01 | finite union bound, derivation, no independence premise | resource endpoint blocked; official download and local extraction succeeded | no problem, prose, table, or figure reused |
| Levin §4.5 HTML | 2026-09-01 | induction proof structure only | does not contain Bernoulli's inequality | no exercise or wording reused |
| Python 3.14 documentation | 2026-09-01 | summation, products, norms, closeness, rational construction | platform floating behavior remains as documented | API semantics only; code and tests original |

The finite rearrangement theorem, Bernoulli derivation, equality audits, worked
examples, exercises, solutions, code, tests, Mermaid diagrams, and SVG figures
were independently written for this module. No generated summary, Wikipedia, or
MathWorld page was used as numbered evidence.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)