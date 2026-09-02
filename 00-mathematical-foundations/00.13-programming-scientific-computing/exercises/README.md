# Exercises for §0.13 Programming and Scientific Computing

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solutions. Difficulty follows the
project's 1 through 5 scale. Run programming work from the module's `code/`
directory with the repository `.venv/bin/python` interpreter.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.13.01 | Write an executable function contract | conceptual and implementation | 2 | design explicit function and exception contracts | 40 min |
| E0.13.02 | Audit a one-shot iterator and state invariant | implementation and critique | 3 | distinguish lists, iterables, iterators, and state | 45 min |
| E0.13.03 | Separate shape, size, ndim, and dtype | calculation and experiment | 3 | predict structural metadata and numeric limits | 50 min |
| E0.13.04 | Trace strides, views, and copies | calculation and implementation | 3 | reason about byte offsets and aliasing | 55 min |
| E0.13.05 | Derive broadcasting and multiplication contracts | derivation and calculation | 3 | predict trailing-axis and operation semantics | 55 min |
| E0.13.06 | Stabilize and compare two computations | derivation and implementation | 4 | implement stable array semantics without speed folklore | 60 min |
| E0.13.07 | Build an evidence ladder before trust | testing and critique | 4 | combine examples, properties, invariants, and references | 70 min |
| E0.13.08 | Localize a failure with a minimal reproduction | debugging and explanation | 4 | use traceback and breakpoint evidence | 55 min |
| E0.13.09 | Make an exploratory plot reproducible | implementation and experiment | 3 | preserve units, provenance, and temporary output | 55 min |
| E0.13.10 | Profile time and memory within their limits | experiment and critique | 4 | record benchmark and allocation evidence honestly | 75 min |
| E0.13.11 | Design a reproducible run record | applied and implementation | 4 | capture process, environment, Git, data, and evidence | 70 min |
| E0.13.12 | Construct independent random streams | implementation and critique | 5 | use Generator and SeedSequence.spawn reproducibly | 85 min |

## E0.13.01 Write an executable function contract

- **Type:** conceptual and implementation
- **Difficulty:** 2
- **Objective:** Design explicit function and exception contracts.
- **Estimated time:** 40 minutes
- **Allowed tools:** Python standard library and NumPy.

### Problem

Design `normalize_rows(matrix)` for a finite floating array of shape
`(rows, features)`. Each row must have a nonzero Euclidean norm. It returns a
new `float64` array of the same shape whose row norms are one.

1. State contracts for values, type, shape, dtype, units, mutation, and output.
2. Implement the function without a Python loop over rows.
3. Raise `ContractError` for wrong rank, nonfloating dtype, nonfinite values, or
   a zero row.
4. Explain why an annotation alone does not enforce the contract.
5. Give one hand-computed example and one failure case.

**Deliverable:** Contract ledger, implementation, and two tests.

## E0.13.02 Audit a one-shot iterator and state invariant

- **Type:** implementation and critique
- **Difficulty:** 3
- **Objective:** Distinguish lists, iterables, iterators, and state.
- **Estimated time:** 45 minutes
- **Allowed tools:** Standard library and module code.

### Problem

1. Create a list `[2.0, 4.0, 9.0]` and a generator over the same values.
2. Demonstrate two traversals of each.
3. Pass the generator to `RunningMean.update`, then prove by inspection that it
   is exhausted.
4. State and verify the `RunningMean` invariant after two separate updates.
5. Diagnose a function that computes `sum(values) / len(list(values))` for an
   arbitrary iterable.
6. Repair it while stating the memory tradeoff.

**Deliverable:** Executable audit, invariant, diagnosis, and repair.

## E0.13.03 Separate shape, size, ndim, and dtype

- **Type:** calculation and experiment
- **Difficulty:** 3
- **Objective:** Predict structural metadata and numeric limits.
- **Estimated time:** 50 minutes
- **Allowed tools:** NumPy and hand calculation.

### Problem

For `a = np.arange(24, dtype=np.int16).reshape(2, 3, 4)`:

1. Predict `shape`, `size`, `ndim`, `itemsize`, `nbytes`, and C-order strides.
2. Verify each prediction.
3. Predict the shape and dtype of `a.sum(axis=1)`.
4. Construct an `int8` overflow example and explain why Python `int` differs.
5. Construct a `float32` precision example where adding one changes nothing.
6. Explain why correct shape is insufficient evidence of a correct result.

**Deliverable:** Metadata table, two failure demonstrations, and interpretation.

## E0.13.04 Trace strides, views, and copies

- **Type:** calculation and implementation
- **Difficulty:** 3
- **Objective:** Reason about byte offsets and aliasing.
- **Estimated time:** 55 minutes
- **Allowed tools:** NumPy and module code.

### Problem

Let `source = np.arange(20, dtype=np.float64).reshape(4, 5)`.

1. Compute the byte offset of `source[2, 3]` from strides.
2. Predict shape and strides for `source.T` and `source[:, ::2]`.
3. Compare `source[1:3, 1:4]` and `source[[1, 2], 1:4]`.
4. Use `memory_relation` and a mutation test to classify each result.
5. Explain why `.base is source` is not a complete immediate-parent test.
6. State when an explicit copy of a small slice can reduce retained memory.

**Deliverable:** Offset derivation, metadata, and aliasing experiment.

## E0.13.05 Derive broadcasting and multiplication contracts

- **Type:** derivation and calculation
- **Difficulty:** 3
- **Objective:** Predict trailing-axis and operation semantics.
- **Estimated time:** 55 minutes
- **Allowed tools:** Hand shape analysis and NumPy.

### Problem

1. Determine the result shape, or exact incompatibility, for `(7, 1, 5)` with
   `(3, 5)`, `(4, 3, 1)` with `(3, 6)`, `()` with `(2, 4)`, and `(2, 3)` with
   `(2,)`.
2. Verify with `broadcast_result_shape`.
3. For two explicit $2\times2$ arrays, compute `A * B` and `A @ B` by hand.
4. Derive the shapes in `features @ weights.T + bias` for `(8, 3)`, `(5, 3)`,
   and `(5,)`.
5. Give one same-shaped pair for which `*` and `@` both run but differ.

**Deliverable:** Four broadcast audits and two operation derivations.

## E0.13.06 Stabilize and compare two computations

- **Type:** derivation and implementation
- **Difficulty:** 4
- **Objective:** Implement stable array semantics without speed folklore.
- **Estimated time:** 60 minutes
- **Allowed tools:** NumPy and module code.

### Problem

1. Derive maximum-shift log-sum-exp.
2. Show that direct evaluation overflows for `[1000, 1001, 999]`.
3. Compare `stable_logsumexp` with a `longdouble` reference.
4. Implement the same stable formula with an outer Python loop over rows.
5. Test equality of semantics with justified tolerances.
6. Explain why the array expression is vectorized but not guaranteed faster.

**Deliverable:** Derivation, two implementations, comparison, and limitation.

## E0.13.07 Build an evidence ladder before trust

- **Type:** testing and critique
- **Difficulty:** 4
- **Objective:** Combine examples, properties, invariants, and references.
- **Estimated time:** 70 minutes
- **Allowed tools:** `unittest`, NumPy, and module code.

### Problem

Write tests for `affine_batch` and `stable_logsumexp` that include:

1. one hand-computed result each;
2. shape, dtype, empty, nonfinite, and mismatch failures;
3. the property $\mathrm{LSE}(\boldsymbol{x}+c)=
   \mathrm{LSE}(\boldsymbol{x})+c$ over 100 generated finite cases;
4. a reference comparison for affine output using explicit scalar loops;
5. a stated random-stream construction and tolerance policy;
6. an explanation of what the finite test domain does not prove.

**Deliverable:** Passing tests and an evidence-boundary paragraph.

## E0.13.08 Localize a failure with a minimal reproduction

- **Type:** debugging and explanation
- **Difficulty:** 4
- **Objective:** Use traceback and breakpoint evidence.
- **Estimated time:** 55 minutes
- **Allowed tools:** Python traceback, `breakpoint()`, and NumPy.

### Problem

Given a pipeline whose final line fails inside `affine_batch`:

1. read the traceback from exception to callers;
2. reduce the original dataset to the smallest arrays preserving the failure;
3. record values, types, shapes, dtypes, finiteness, and mutation state;
4. use a breakpoint immediately before the call to inspect those facts;
5. state one falsifiable hypothesis;
6. add a regression test before repairing the input transformation;
7. explain why swallowing the exception would make diagnosis worse.

Use a mismatch where features have shape `(2, 3)` and weights have shape
`(4, 2)`.

**Deliverable:** Minimal reproduction, debugger checklist, test, and repair.

## E0.13.09 Make an exploratory plot reproducible

- **Type:** implementation and experiment
- **Difficulty:** 3
- **Objective:** Preserve units, provenance, and temporary output.
- **Estimated time:** 55 minutes
- **Allowed tools:** NumPy, Matplotlib Agg, temporary files, and module code.

### Problem

1. Generate $x=0,1,\ldots,10$ seconds and $y=x^2$ meters.
2. Save a plot using `save_exploration_plot` inside `TemporaryDirectory`.
3. Verify the PNG signature, nonzero size, labels, units, and cleanup.
4. State the synthetic-data provenance and transformation.
5. Explain what the plot suggests and what it cannot prove.
6. Refuse mismatched vector lengths and a non-PNG output path.

**Deliverable:** Temporary plot test and evidence statement.

## E0.13.10 Profile time and memory within their limits

- **Type:** experiment and critique
- **Difficulty:** 4
- **Objective:** Record benchmark and allocation evidence honestly.
- **Estimated time:** 75 minutes
- **Allowed tools:** `benchmark`, `timeit`, `cProfile`, `tracemalloc`, NumPy.

### Problem

Compare a scalar Python square loop with `array * array` on one stated input.

1. Keep data creation outside timed functions.
2. Use explicit warmup, calls per repeat, and at least five repeats.
3. Record all observations and environment metadata.
4. Use `cProfile` to identify call locations, not to rank Python versus C time.
5. Use `tracemalloc` on a Python-list workload and explain why its result does
   not measure every native NumPy allocation.
6. Make no fragile threshold assertion or universal speed claim.

**Deliverable:** Timing records, profile interpretation, memory limitation.

## E0.13.11 Design a reproducible run record

- **Type:** applied and implementation
- **Difficulty:** 4
- **Objective:** Capture process, environment, Git, data, and evidence.
- **Estimated time:** 70 minutes
- **Allowed tools:** Standard library, Git, NumPy, and module code.

### Problem

Design a JSON run record for a synthetic array experiment. Include:

1. command, working directory, timestamp with timezone, and process ID;
2. Git commit and dirty status;
3. Python executable, implementation, package versions, platform, and machine;
4. data origin, license, shape, dtype, units, transformation, and checksum;
5. configuration, root entropy, stream role, and generator identity;
6. tests run, output paths or checksums, hardware limitations, and known gaps.

Explain why `pip freeze`, a Git commit, or a seed alone is insufficient.

**Deliverable:** JSON-compatible schema, sample record, and three limitations.

## E0.13.12 Construct independent random streams

- **Type:** implementation and critique
- **Difficulty:** 5
- **Objective:** Use Generator and SeedSequence.spawn reproducibly.
- **Estimated time:** 85 minutes
- **Allowed tools:** NumPy random Generator, SeedSequence, and module code.

### Problem

For one experiment needing data generation, parameter initialization, and
resampling:

1. create three child generators from one recorded root entropy;
2. rerun construction and verify stream-by-position reproduction;
3. show that child outputs are not identical on a finite sample without claiming
   this proves independence;
4. demonstrate how sharing one global generator couples output to call order;
5. explain why `root_seed + worker_id` is an unsafe general stream policy;
6. record NumPy version, BitGenerator class, child role, and spawn identity;
7. state the no-cross-version-bitstream guarantee;
8. list process, environment, code, data, hardware, and evidence needed beyond
   `seed(0)`.

**Deliverable:** Stream factory, reproducibility tests, coupling demonstration,
and complete audit.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)