# Resources for §0.03 Exponentials and Logarithms

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)

This page is reading and implementation guidance, not a second formal bibliography. Numbered sources supporting claims remain in the module [reference list](../README.md#references).

## Core resources

### NIST Digital Library of Mathematical Functions, Chapter 4

- **Resource:** NIST DLMF, "Elementary Functions."
- **What it covers:** Definitions, identities, limits, inequalities, computation, and references for powers, exponentials, logarithms, trigonometric functions, and hyperbolic functions.
- **Why it is included:** Use it as the authoritative formula and convention reference after the module's conversational explanation. Sections 4.2 through 4.8 are the most relevant here.
- **Assumed level:** Undergraduate reference; terse notation can feel more advanced than the underlying facts.
- **Access:** Free official NIST site, versioned and maintained. https://dlmf.nist.gov/4

### OpenStax Precalculus 2e

- **Resource:** Abramson and contributors, *Precalculus 2e*.
- **What it covers:** Exponential functions, logarithmic functions, equations, applications, and a large bank of worked examples and exercises in a full precalculus sequence.
- **Why it is included:** Use it when you need more repetition with laws, graphs, change of base, or equation solving than this focused module provides. It is also a useful bridge for readers backfilling a conventional course.
- **Assumed level:** Introductory undergraduate or advanced secondary mathematics.
- **Access:** Free web text and downloadable PDF from OpenStax; print copies are commercial. Use the verified book landing page rather than an unverified section URL. https://openstax.org/details/books/precalculus-2e

### Project notation and prerequisite guides

- **Resource:** [Notation guide](../../../NOTATION.md) and [prerequisite guide](../../../PREREQUISITES.md).
- **What it covers:** The local natural-log convention, likelihood notation, logits, losses, vectors, and the route from this module into calculus, probability, and information theory.
- **Why it is included:** Keep the notation guide open when translating sources that use `log` differently. Use the prerequisite guide to decide whether to continue into §1, §3, or §6 next.
- **Assumed level:** Reference for all levels.
- **Access:** Free in this repository.

## Historical resources

### John Napier biography

- **Resource:** O'Connor and Robertson, "John Napier," MacTutor History of Mathematics Archive.
- **What it covers:** Napier's 1614 publication, computational motivation, moving-point construction, scale choices, and interactions with Briggs.
- **Why it is included:** It prevents the common error of describing Napier's original logarithms as though they were exactly modern natural logs. It also connects products-to-sums with the calculation problem the method was designed to solve.
- **Assumed level:** General mathematical history.
- **Access:** Free public article from the University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Napier/

### Henry Briggs biography

- **Resource:** O'Connor and Robertson, "Henry Briggs," MacTutor History of Mathematics Archive.
- **What it covers:** Briggs's reaction to Napier's work, correspondence and visits, discussions about more convenient logarithms, and construction and publication of tables.
- **Why it is included:** Read it alongside the Napier biography to distinguish publication, collaboration, convention changes, table construction, and popularization. The pair resists a simplistic single-inventor narrative.
- **Assumed level:** General mathematical history.
- **Access:** Free public article from the University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Briggs/

## Deeper mathematical and machine-learning resources

### Deep Learning, Chapter 4

- **Resource:** Goodfellow, Bengio, and Courville, *Deep Learning*, Chapter 4, "Numerical Computation."
- **What it covers:** Underflow, overflow, conditioning, stability, gradient-based optimization context, and numerical issues that arise in machine learning.
- **Why it is included:** Use it after the module to place log-space calculations inside a broader numerical-computation discipline. It explains why evaluating a mathematically valid expression can still be a computational problem.
- **Assumed level:** Intermediate undergraduate to graduate; calculus and linear algebra help.
- **Access:** Free author-hosted web version; print edition is commercial. https://www.deeplearningbook.org/contents/numerical.html

### Accurately computing log-sum-exp and softmax

- **Resource:** Blanchard, D. J. Higham, and N. J. Higham, "Accurately computing the log-sum-exp and softmax functions."
- **What it covers:** Conditioning, rounding-error analysis, basic and shifted algorithms, overflow, harmful and harmless underflow, and experiments across low-precision formats.
- **Why it is included:** This is the deepest source behind the module's stability treatment. Read the introduction and shifted-algorithm section first. Continue into the error bounds when you have calculus and numerical-analysis background.
- **Assumed level:** Advanced undergraduate or graduate numerical analysis.
- **Access:** Open-access journal article under CC BY 4.0. The DOI is stable. https://doi.org/10.1093/imanum/draa038

### PyTorch CrossEntropyLoss documentation

- **Resource:** PyTorch Contributors, `torch.nn.CrossEntropyLoss`.
- **What it covers:** Accepted logit and target shapes, class-index and class-probability targets, reductions, weighting, label smoothing, and the class-index equivalence to LogSoftmax followed by NLLLoss.
- **Why it is included:** Use it to check how the derived class loss maps to a real framework API without turning this module into a training tutorial. Pay attention to zero-based class indices and to features deliberately omitted from the lesson.
- **Assumed level:** Basic array programming and introductory machine learning.
- **Access:** Free official documentation for a versioned API. https://docs.pytorch.org/docs/2.13/generated/torch.nn.CrossEntropyLoss.html

## Computational resources

### Python math documentation

- **Resource:** Python Software Foundation, `math` module documentation.
- **What it covers:** `exp`, `expm1`, `log`, `log1p`, `log2`, `log10`, `prod`, `fsum`, exception behavior, and floating-point constants.
- **Why it is included:** This is the source of truth for standard-library naming and behavior. Use it to verify that `math.log` is natural log, understand why `log1p` and `expm1` exist, and check whether an invalid input raises an exception.
- **Assumed level:** Basic Python.
- **Access:** Free official documentation. The `/3/` URL tracks the current Python 3 documentation; record your interpreter version in experiments. https://docs.python.org/3/library/math.html

### Python floating-point tutorial

- **Resource:** Python Software Foundation, "Floating-Point Arithmetic: Issues and Limitations."
- **What it covers:** Binary fractions, representation error, precision, display, exact stored values, tolerant comparison, and more accurate summation.
- **Why it is included:** Read it before interpreting an experiment as a failure of algebra. It explains why decimal input is usually represented approximately and why printed output can hide the stored value.
- **Assumed level:** Basic Python and arithmetic.
- **Access:** Free official tutorial. https://docs.python.org/3/tutorial/floatingpoint.html

### NumPy floating-point limits

- **Resource:** NumPy Developers, `numpy.finfo`.
- **What it covers:** Maximum finite values, epsilon, smallest normal values, smallest subnormal values, precision, and dtype-specific limits.
- **Why it is included:** Use it in the numerical range laboratory instead of hard-coding folklore thresholds. The distinction between `smallest_normal` and `smallest_subnormal` is essential when classifying underflow.
- **Assumed level:** Basic NumPy arrays and dtypes.
- **Access:** Free official NumPy v2.5 documentation. https://numpy.org/doc/stable/reference/generated/numpy.finfo.html

### NumPy log-domain addition

- **Resource:** NumPy Developers, `numpy.logaddexp`.
- **What it covers:** Stable evaluation of $\log(e^a+e^b)$ for arrays, broadcasting, and a probability-in-log-space example.
- **Why it is included:** Use it to verify a two-term implementation and to add probabilities represented by their logs. It is not a replacement for understanding reduction axes or general LSE.
- **Assumed level:** Basic NumPy.
- **Access:** Free official documentation. https://numpy.org/doc/stable/reference/generated/numpy.logaddexp.html

### NumPy near-zero functions

- **Resource:** NumPy Developers, `numpy.log1p` and `numpy.expm1`.
- **What it covers:** Elementwise stable evaluation of $\log(1+x)$ and $e^x-1$, broadcasting, real and complex behavior, and examples showing precision near zero.
- **Why it is included:** Use these pages while completing E0.03.09. They show concrete cases where the naive composite expression loses information even though the specialized operation retains it.
- **Assumed level:** Basic NumPy and floating-point awareness.
- **Access:** Free official documentation. https://numpy.org/doc/stable/reference/generated/numpy.log1p.html and https://numpy.org/doc/stable/reference/generated/numpy.expm1.html

### SciPy logsumexp documentation

- **Resource:** SciPy Community, `scipy.special.logsumexp`.
- **What it covers:** Stable LSE reduction across axes, optional weights, retained dimensions, sign return, backend notes, and comparison with NumPy's two-argument operations.
- **Why it is included:** Use it as an optional trusted comparison after implementing LSE from first principles. The module has no SciPy dependency and does not require installation.
- **Assumed level:** Intermediate NumPy.
- **Access:** Free official SciPy documentation. https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.logsumexp.html

## Practice and experiments

### Module numerical range laboratory

- **Resource:** [E0.03.06 Find floating-point range failures](../exercises/README.md#e00306-find-floating-point-range-failures).
- **What it covers:** `float32` versus `float64`, normal and subnormal values, product underflow, exponential overflow, and shifted LSE.
- **Why it is included:** It turns numerical-stability vocabulary into measurements on your actual interpreter and hardware. The deliverable requires environment records and distinguishes harmful from harmless underflow.
- **Assumed level:** Basic Python and NumPy.
- **Access:** Free in this repository; no external data or service required.

### Module log-domain toolkit

- **Resource:** [E0.03.10 Implement a log-domain toolkit](../exercises/README.md#e00310-implement-a-log-domain-toolkit).
- **What it covers:** Stable product representation, pairwise log addition, LSE, log-softmax, class-index NLL, axes, shapes, invariance, and invalid inputs.
- **Why it is included:** It consolidates the computational spine into a small API whose tests directly mirror the derivations. Complete it before relying on a framework loss function.
- **Assumed level:** Comfortable Python functions and NumPy arrays.
- **Access:** Free in this repository; SciPy comparison is optional.

### Module growth crossover investigation

- **Resource:** [E0.03.11 Investigate growth crossovers visually](../exercises/README.md#e00311-investigate-growth-crossovers-visually).
- **What it covers:** Log-domain comparisons, multiple crossings, plotting windows, controlled parameter changes, and evidence limits.
- **Why it is included:** It trains the habit of separating a finite computational observation from an asymptotic theorem. This distinction matters later in algorithm analysis and scaling arguments.
- **Assumed level:** Basic loops and plotting or table construction.
- **Access:** Free in this repository; a plotting library is optional.

## Suggested sequence

1. Use OpenStax for extra algebra practice while reading the main lesson.
2. Check definitions and identities against NIST DLMF.
3. Read the Napier and Briggs biographies together, not as competing single-person stories.
4. Complete the equation, compounding, and growth exercises.
5. Read Python's floating-point tutorial before the numerical range laboratory.
6. Keep the NumPy API pages open while implementing the log-domain toolkit.
7. Read Blanchard, Higham, and Higham after deriving max shifting yourself.
8. Check the PyTorch documentation only after deriving the class-index NLL formula.
9. Use Goodfellow, Bengio, and Courville to continue into broader numerical computation.

## Access notes

- All web resources above were directly checked on 2026-09-01.
- OpenStax section-level URLs previously attempted during source research returned errors, so this guide uses the verified book landing page.
- The Oxford article is open access and has a stable DOI; publication metadata distinguish online publication in 2020 from the 2021 journal issue.
- Python, NumPy, SciPy, and PyTorch documentation changes over time. Record versions when reproducing API behavior.
- No source here is evidence that Stanford CS109 explicitly teaches underflow. This module makes no such claim.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)
