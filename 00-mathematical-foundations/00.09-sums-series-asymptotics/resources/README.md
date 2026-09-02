# Resources for §0.09 Sums, Series, and Asymptotics

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)

This page is annotated reading guidance and a provenance record, not a second formal bibliography. Numbered sources supporting lesson claims remain in the module [reference list](../README.md#references).

## Core route

### OpenStax Calculus Volume 2, Chapter 5

- **Resource:** Gilbert Strang and Edwin "Jed" Herman, *Calculus Volume 2*, Chapter 5, §§5.1-5.6.
- **What was directly inspected:** The book details page and all six HTML chapter sections. The inspected theorem statements cover the epsilon definition for sequences; bounded and monotone convergence; partial sums; geometric and telescoping series; nth-term divergence; integral and remainder tests; direct and limit comparison; alternating convergence and its next-term error; absolute and conditional convergence; rearrangement; and ratio and root tests.
- **Why it is included:** This is the primary inspectable undergraduate source for the complete convergence-test route. Keep its hypotheses visible while doing E0.09.03 through E0.09.08.
- **Assumed level:** Second-semester undergraduate calculus. The integral sections assume improper integrals.
- **Access:** Free HTML and PDF. Published 2016; web version updated 2026-07-15. License: CC BY-NC-SA 4.0. https://openstax.org/books/calculus-volume-2/pages/5-introduction

The site HTML exposed theorem text and mathematical expressions directly on 2026-09-01. Page extraction included many exercises and site controls, so inspection was filtered by theorem names and hypotheses. No OpenStax exercise, solution, prose, table, or figure was adapted.

### MIT 18.01SC Exploring the Infinite

- **Resource:** MIT OpenCourseWare, *18.01SC Single Variable Calculus*, Fall 2010, Prof. David Jerison, Unit 5.
- **What was directly inspected:** The Unit 5 index plus Session 92 "Integral Comparison," Session 94 "Infinite Series," and Session 95 "Series Comparison." Session 94's overview explicitly connects infinite regions, Riemann sums, infinite sums, and the geometric series. Session 95 lists comparison tests, ratio testing, the integral test, and integral estimation.
- **Why it is included:** Use it as a university-course second route for the geometric and area-comparison intuition.
- **Assumed level:** Undergraduate single-variable calculus.
- **Access:** Free course pages, videos, notes, problems, and solutions. MIT OpenCourseWare license: CC BY-NC-SA 4.0. https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-5-exploring-the-infinite/

The session HTML overviews and resource titles were inspectable on 2026-09-01. Linked PDF text and video transcripts were not extracted, so no exact theorem wording in the module is attributed to those artifacts. An initially guessed Session 77 URL returned 404 and was excluded.

## Precise asymptotic formulas

### NIST Digital Library of Mathematical Functions

- **Resource:** NIST DLMF, Version 1.2.7, §§2.1, 5.4, 5.5, and 5.11.
- **What was directly inspected:** Equations 2.1.1-2.1.3 for $\sim$, $o$, and $O$; the finite-limit and infinite-limit framing; equation 5.4.14 relating harmonic numbers to the psi function; equation 5.5.2 for the psi recurrence; equations 5.11.1-5.11.4 for log-gamma and Stirling expansions; and §5.11(ii)'s real-positive first-neglected-term remainder rule.
- **Why it is included:** This is the authoritative source for the harmonic expansion, Stirling coefficients, and finite remainder discipline. Read the expansion and error-bound subsections together.
- **Assumed level:** Advanced undergraduate analysis. Complex-sector details can be skipped for this real-positive module.
- **Access:** Free HTML with numbered equations. Version 1.2.7 released 2026-06-15. https://dlmf.nist.gov/2.1 and https://dlmf.nist.gov/5.11

The HTML and equation text were directly inspectable on 2026-09-01. The module specializes the source's complex statements to positive integers and derives the displayed harmonic and factorial forms. It does not claim a full derivation of the DLMF expansions.

### Reading the finite remainder correctly

DLMF's statement that a real-positive truncated log-gamma or psi expansion has a remainder with the sign and magnitude of the first neglected term supports two different module bounds:

1. the harmonic correction after $-1/(12n^2)$ is positive and smaller than $1/(120n^4)$;
2. the log-factorial correction lies between $1/(12n)-1/(360n^3)$ and $1/(12n)$.

These are finite inequalities. The infinite displayed asymptotic series is not treated as a convergent numerical series.

## Algorithm-analysis route

### Princeton Algorithms, §1.4

- **Resource:** Robert Sedgewick and Kevin Wayne, "1.4 Analysis of Algorithms," companion site for *Algorithms*, 4th edition.
- **What was directly inspected:** The HTML sections on scientific method, timing observations, doubling tests, mathematical models, tilde approximations, order-of-growth classifications, cost models, input dependence, worst-case guarantees, and amortized analysis.
- **Why it is included:** It connects asymptotic mathematics to an explicit basic-operation model and keeps reproducible timing evidence separate from a proved cost count.
- **Assumed level:** Introductory undergraduate algorithms and basic programming.
- **Access:** Free inspectable HTML. Last modified 2020-03-18. Copyright retained by the authors. https://algs4.cs.princeton.edu/14analysis/

The page directly defines tilde approximation by a ratio tending to one and shows how empirical doubling informs a model. It does not supply the module's full formal $O/\Omega/\Theta/o/\omega$ definition set, so those definitions are grounded in DLMF and independently stated. No code, exercise, or figure was reused.

### MIT 6.006 extraction limit

MIT 6.006 Lecture 2 was considered for a directly inspectable algorithms source. The course resource page was blocked by the inspection client, and the linked PDF did not yield meaningful text. It is therefore not a numbered source and supports no module claim. This is an extraction limit, not evidence that the course lacks the material.

## Python implementation reference

### Python `math`

- **Resource:** Python Software Foundation, Python 3.14 `math` documentation.
- **What was directly inspected:** `factorial`, `fsum`, `lgamma`, `isclose`, `log`, and floating-point behavior notes. `fsum` tracks multiple intermediate partial sums, and `lgamma(x)` returns the natural logarithm of the absolute gamma function.
- **Why it is included:** This is the software source of truth for the module's exact factorial reference and floating log/summation tools.
- **Assumed level:** Basic Python and floating-point awareness.
- **Access:** Free official documentation under PSF License Version 2. Documentation examples are additionally 0BSD. https://docs.python.org/3/library/math.html

The API text was directly inspected on 2026-09-01. Python results are implementation evidence for finite inputs. They do not establish a convergence theorem or a source license for surrounding curriculum material.

## Suggested sequence

1. Read the module through partial sums and complete E0.09.01-E0.09.03.
2. Keep OpenStax §§5.3-5.6 beside the convergence-test exercises.
3. Use MIT Sessions 92, 94, and 95 when rectangle or geometric intuition needs another presentation.
4. Read DLMF §2.1 beside E0.09.11.
5. Read DLMF §5.11(i) and §5.11(ii) together beside E0.09.09-E0.09.10.
6. Use Princeton §1.4 before interpreting benchmarks as asymptotic evidence.
7. Keep Python's `math` page open while extending the tests.
8. Stop before power-series convergence, Taylor series, or Fourier series.

## Provenance and originality ledger

| Source | Accessed | Exact support used | Extraction limit | Reuse boundary |
|---|---|---|---|---|
| OpenStax Chapter 5 HTML | 2026-09-01 | sequence and series definitions; every listed convergence test; remainder and rearrangement statements | long pages required targeted theorem extraction | cited and checked; no content adapted |
| MIT 18.01SC Unit 5 and Sessions 92, 94, 95 | 2026-09-01 | course placement, page overviews, and named resource coverage | linked PDF and video content not extracted | page facts only; no problem or media reused |
| NIST DLMF §§2.1, 5.4, 5.5, 5.11 | 2026-09-01 | ratio definitions, harmonic identities, Stirling expansion, and real-positive remainder rule | specialized from complex notation to positive integers | equations cited; derivations and examples independently written |
| Princeton Algorithms §1.4 | 2026-09-01 | tilde meaning, cost models, reproducible observation, and model limits | not used for the full formal notation family | no code, exercise, or figure reused |
| Python 3.14 `math` | 2026-09-01 | `fsum`, `factorial`, and `lgamma` behavior | platform rounding remains implementation-dependent where documented | API semantics only; helpers and tests original |
| MIT 6.006 Lecture 2 candidate | 2026-09-01 | none | page blocked and PDF text extraction failed | excluded from references |

Wikipedia and MathWorld were not used as numbered references. AI-generated summaries were not treated as evidence. All lesson prose, worked examples, exercises, solutions, code, tests, Mermaid diagrams, and SVG figures in this module are original.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)