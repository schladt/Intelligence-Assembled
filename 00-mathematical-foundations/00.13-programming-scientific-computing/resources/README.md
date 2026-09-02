# Resources for §0.13 Programming and Scientific Computing

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)

This page is annotated reading guidance and a provenance record. Numbered
evidence remains in the module [reference list](../README.md#references).

## Core route

### Python 3.14 tutorial and library reference

- **Directly inspected:** function definitions and annotations; modules and
  import behavior; aliasing and classes; iterator protocol, generators, and
  `StopIteration`; exception types, propagation, chaining, and cleanup; standard
  library quality-control and performance sections.
- **Why included:** These pages define the working language mechanisms without
  turning the module into a syntax survey.
- **Level:** Readers with basic programming exposure.
- **Access and rights:** Public official documentation under the PSF License
  Version 2; documentation examples additionally use 0BSD. No prose or example
  was adapted.

Use the tutorial as a reference when a Python mechanism blocks the computation.
Do not read it as a prerequisite cover to cover.

### NumPy 2.5 manual

- **Directly inspected:** array creation; `shape`, `size`, `ndim`, `itemsize`,
  and byte `strides`; fixed-width dtypes, overflow, and precision; basic and
  advanced indexing; copies and views; trailing-axis broadcasting; ufuncs;
  elementwise `multiply`; `matmul` and `@`.
- **Why included:** This is the authoritative behavioral contract for the
  module's central array distinctions.
- **Level:** Basic Python plus the shape notation introduced in the lesson.
- **Access and rights:** Free official documentation. No text, figure, or code
  was adapted.

The stable docs reported NumPy v2.5 during inspection. Exact local validation
used NumPy `2.5.2`.

### Matplotlib 3.11.1 documentation

- **Directly inspected:** backend definition and selection, Agg as a
  noninteractive file-writing backend, `subplots`, and `Figure.savefig`.
- **Why included:** It supports deterministic file-based plot tests while
  keeping plotting subordinate to evidence and units.
- **Level:** Basic array manipulation.
- **Access and rights:** Free official documentation. The module plot and SVGs
  are original.

## Trust and diagnosis route

### unittest

- **Directly inspected:** `TestCase`, discovery naming, fixtures, subtests,
  specific assertions, exception assertions, command-line execution, and test
  independence.
- **Why included:** It is sufficient for the module tests and avoids adding a
  testing dependency.
- **Boundary:** The lesson discusses property-based testing as an evidence
  strategy but does not add a third-party generation framework.

### Tracebacks and pdb

- **Directly inspected:** traceback role; `breakpoint()`; command-line and
  post-mortem debugging; breakpoints; stack movement; `next`, `step`, expression
  inspection, and continuation.
- **Why included:** These tools connect a failing contract to inspectable runtime
  state.
- **Boundary:** No IDE-specific debugging workflow is taught.

### timeit, cProfile, and tracemalloc

- **Directly inspected:** setup exclusion; repeats; default garbage-collection
  handling; external process interference; cProfile call, internal, and
  cumulative time; the explicit distinction between profiling and benchmarking;
  Python memory-block tracing, snapshots, domains, and overhead.
- **Why included:** They establish measurement limits before optimization claims.
- **Boundary:** `tracemalloc` is not presented as complete native-memory or
  resident-set measurement. No timing observation is treated as universal proof.

## Reproducibility route

### Python Packaging User Guide

- **Directly inspected:** isolated `venv` environments; activation and
  interpreter checks; requirements files; `pip freeze`; `pyproject.toml`
  dependency fields and build-system ownership.
- **Why included:** It separates environment capture from full package
  distribution.
- **Boundary:** The repository has no dependency-file convention, so §0.13
  documents local requirements and does not create packaging architecture.

### Official Git documentation and Pro Git

- **Directly inspected:** version control as recorded file history; `git status`
  worktree and index distinctions; `git diff` endpoint comparisons; `git log`
  commit history.
- **Why included:** A source commit is a necessary part of run provenance.
- **Boundary:** Git does not capture uncommitted content, external data,
  environment, hardware, or random state unless the run record does.

### NumPy Generator, SeedSequence, and parallel random generation

- **Directly inspected:** `default_rng`; separate `Generator` and `BitGenerator`
  state; no `Generator` cross-version compatibility guarantee;
  `SeedSequence.entropy`; `spawn`; child-tree position mixing; warnings against
  ad hoc neighboring worker seeds.
- **Why included:** It supports independent reproducible streams without global
  call-order coupling.
- **Boundary:** Statistical quality and cryptographic randomness are not taught
  here. "Very probably independent" is retained rather than upgraded to proof.

## Suggested sequence

1. Read the Python tutorial sections only as each language contract appears.
2. Keep NumPy array attributes, indexing, copies, and broadcasting pages open
   while doing E0.13.03 through E0.13.06.
3. Read `unittest` before E0.13.07 and `pdb` before E0.13.08.
4. Read all three measurement pages before E0.13.10.
5. Read PyPA, Git, and NumPy random sources together before E0.13.11-12.

## Provenance and originality ledger

| Source | Accessed | Exact support used | Inspection limit | Reuse boundary |
|---|---|---|---|---|
| Python 3.14 docs | 2026-09-01 | functions, classes, iterators, exceptions, modules, stdlib, tests, debugger, profilers | documentation behavior only | no adaptation |
| NumPy 2.5 docs | 2026-09-01 | arrays, dtype, shape, strides, indexing, views/copies, broadcasting, operations, RNG | no performance generalization | no adaptation |
| Matplotlib 3.11.1 docs | 2026-09-01 | backends, figure creation, file output | no GUI workflow | original plot code |
| PyPA guide | 2026-09-01 | venv, dependency declaration and capture | no tool mandated for this repo | no copied configuration |
| Git docs and Pro Git | 2026-09-01 | status, diff, log, history purpose | Git is only one provenance layer | no adaptation |

No Wikipedia, MathWorld, generated summary, uninspected search result, or raw
notebook transcript is evidence. All prose, exercises, solutions, Python code,
tests, Mermaid diagrams, and four SVG figures are original.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)