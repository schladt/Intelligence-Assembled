# Resources for §0.02 Algebra, Functions, and Precalculus Backfill

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)

This page is reading guidance, not a second formal bibliography. Numbered sources supporting claims remain in the module [reference list](../README.md#references).

## Core resources

### OpenStax Precalculus 2e

- **Resource:** Abramson and contributors, *Precalculus 2e*.
- **What it covers:** Functions, domain and range, composition, transformations, polynomial and rational functions, trigonometry, and later precalculus topics in a conventional full-course sequence.
- **Why it is included:** Use it when this module moves too quickly or when you need a larger bank of examples and exercises. Chapters 1 through 5 align most closely with this module.
- **Assumed level:** Introductory undergraduate or advanced secondary mathematics.
- **Access:** Free web text and downloadable PDF from OpenStax; print copies are commercial. The web version states a CC BY-NC-SA 4.0 license. https://openstax.org/details/books/precalculus-2e

### NIST Digital Library of Mathematical Functions, Chapter 4

- **Resource:** NIST DLMF, "Elementary Functions."
- **What it covers:** Authoritative definitions, identities, periodicity, branches, and references for exponential, logarithmic, trigonometric, inverse trigonometric, and hyperbolic functions over real and complex inputs.
- **Why it is included:** Use it to check a formula or domain convention after learning the idea from a more conversational source. Sections 4.14, 4.23, and 4.28 are especially relevant.
- **Assumed level:** Reference work; concise notation can feel advanced.
- **Access:** Free official NIST website, versioned and maintained. https://dlmf.nist.gov/4

### Project notation and style guides

- **Resource:** [Notation guide](../../../NOTATION.md) and [style guide](../../../STYLE_GUIDE.md).
- **What it covers:** Local conventions for functions, inverses, complex values, vectors, matrices, code, sources, and educational presentation.
- **Why it is included:** Keep the notation guide open while solving composition and inverse problems or translating code. The style guide explains what a complete derivation, visual, and experiment should report.
- **Assumed level:** Reference for all levels.
- **Access:** Free in this repository.

## Deep resources

### The fundamental theorem of algebra history

- **Resource:** O'Connor and Robertson, "The Fundamental Theorem of Algebra," MacTutor History of Mathematics Archive.
- **What it covers:** The long development from polynomial equations and complex arithmetic through attempts by d'Alembert, Euler, Lagrange, Laplace, Gauss, Argand, and others.
- **Why it is included:** It prevents the flattened story that one person stated and proved the modern theorem in one step. It also distinguishes a claimed proof from one that meets later standards.
- **Assumed level:** General mathematical history; some proof discussion is easier after calculus.
- **Access:** Free article from the University of St Andrews. https://mathshistory.st-andrews.ac.uk/HistTopics/Fund_theorem_of_algebra/

### MIT 18.01SC Single Variable Calculus

- **Resource:** MIT OpenCourseWare, *18.01SC Single Variable Calculus*.
- **What it covers:** Functions, graph behavior, trigonometry, differentiation, integration, techniques including algebraic preparation, and infinite series.
- **Why it is included:** Use it to see exactly where the algebra in this module becomes the working language of calculus. The self-study design includes notes, videos, problems, and solutions.
- **Assumed level:** Undergraduate calculus; this module is preparation.
- **Access:** Free MIT OpenCourseWare materials under the site terms and stated Creative Commons license. https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/

### MIT 18.06 Linear Algebra

- **Resource:** MIT OpenCourseWare, *18.06 Linear Algebra*, taught by Gilbert Strang.
- **What it covers:** Systems, vector spaces, determinants, eigenvalues, similarity, and positive definite matrices.
- **Why it is included:** Follow this after the complex-number and polynomial sections to see why real matrices can require complex eigenvalues. Rotation matrices provide the cleanest bridge.
- **Assumed level:** Undergraduate linear algebra.
- **Access:** Free lectures, problem sets, exams, and solutions through MIT OpenCourseWare. https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/

### Mathematics for Machine Learning

- **Resource:** Deisenroth, Faisal, and Ong, *Mathematics for Machine Learning*.
- **What it covers:** Linear algebra, analytic geometry, matrix decompositions, vector calculus, probability, optimization, and selected machine learning problems.
- **Why it is included:** It shows how function and algebra fluency supports later machine learning mathematics without claiming that every precalculus identity is itself an ML method.
- **Assumed level:** Undergraduate; basic algebra and programming help.
- **Access:** The authors provide a free, updated PDF; the Cambridge print edition is commercial. https://mml-book.github.io/

## Practice and implementation resources

### OpenStax chapter exercises

- **Resource:** Exercises embedded in *Precalculus 2e* chapters on functions, polynomial and rational functions, and trigonometry.
- **What it covers:** Short skill practice, mixed review, graph interpretation, and longer applications.
- **Why it is included:** The module's twelve exercises emphasize synthesis. Use OpenStax for additional repetitions of factoring, unit-circle values, transformations, and rational-function analysis.
- **Assumed level:** Introductory.
- **Access:** Free with the web textbook. Start at the chapter outline and select the relevant section. https://openstax.org/books/precalculus-2e/pages/1-introduction-to-functions

### Python cmath documentation

- **Resource:** Python Software Foundation, `cmath` documentation.
- **What it covers:** Rectangular complex representation, modulus, phase, polar conversion, rectangular conversion, elementary complex functions, branch cuts, and tolerant comparison.
- **Why it is included:** It is the source of truth for how Python represents and converts complex numbers. Read the branch-cut notes as a preview of issues deliberately outside this module.
- **Assumed level:** Basic Python.
- **Access:** Free official documentation. https://docs.python.org/3/library/cmath.html

### NumPy polynomial and tolerance documentation

- **Resource:** NumPy documentation for `numpy.roots`, the polynomial APIs, and `numpy.allclose`.
- **What it covers:** Coefficient ordering, computed polynomial roots, companion-matrix behavior, and elementwise tolerance checks.
- **Why it is included:** Use it to verify small hand-derived roots and to choose explicit tolerances. Note that `numpy.roots` is in the older polynomial API and is not a reason to skip residual checks.
- **Assumed level:** Basic NumPy arrays.
- **Access:** Free official NumPy documentation. https://numpy.org/doc/stable/reference/generated/numpy.roots.html and https://numpy.org/doc/stable/reference/generated/numpy.allclose.html

### Module transformation laboratory

- **Resource:** [E0.02.11 Build a transformation laboratory](../exercises/README.md#e00211-build-a-transformation-laboratory).
- **What it covers:** Function evaluation, landmark-based assertions, visual comparison, periodicity, saturation, and evidence limits.
- **Why it is included:** It turns transformation vocabulary into testable observations and requires you to separate a plotted pattern from a general proof.
- **Assumed level:** Basic Python or careful table construction.
- **Access:** Free in this repository; no data or external service is required.

## Suggested sequence

1. Read this module and use OpenStax only where a step needs more examples.
2. Check trig, inverse trig, hyperbolic, and complex identities against NIST DLMF.
3. Complete the module exercises before using the extra OpenStax practice sets.
4. Use Python `cmath` and NumPy documentation while verifying complex and polynomial calculations.
5. Continue to MIT 18.01SC for calculus or MIT 18.06 for eigenvalues and rotations.
6. Read the FTA history after the mathematics so you can distinguish theorem statements from proof-history claims.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)
