# Solutions for §0.03 Exponentials and Logarithms

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Resources](../resources/README.md)

These are full worked solutions. Numerical thresholds can vary with platform and dtype implementation, so experimental answers must report their environment and distinguish observations from mathematical conclusions.

## E0.03.01 Audit exponent laws and domains

### Key idea

An exponent law is usable only when every intermediate expression is defined in the stated number system.

### Reasoning

| Claim | Diagnosis | Repair |
|---|---|---|
| $(-16)^{3/4}=-8$ | invalid over the reals; the reduced denominator is even | no real value exists |
| $(-8)^{2/6}=2$ | invalid result; $2/6=1/3$ before interpretation | $(-8)^{1/3}=-2$ |
| $0^{-2}=0$ | invalid; negative power requires a reciprocal | $a^{-2}=1/a^2$ for $a\ne0$ |
| $x^{1/2}x^{3/2}=x^2$ for every real $x$ | left side is real only for $x\ge0$ | state $x\ge0$, or use positive bases as a general default |
| $(a^x)^y=a^{xy}$ for all real values | invalid through undefined or branch-sensitive intermediates | it is safe for arbitrary real $x,y$ when $a>0$ |

For the first claim, $(-16)^3$ is real and negative, but its fourth root is not real. The proposed value $-8$ also fails the simplest check because $(-8)^4$ is positive and far larger than $(-16)^3$ in magnitude.

For the exact evaluations,

$$
27^{-2/3} =
\frac{1}{27^{2/3}} =
\frac{1}{(\sqrt[3]{27})^2} =
\frac{1}{9}.
$$

The odd root permits the negative-base case:

$$
(-27)^{-2/3} =
\frac{1}{(-27)^{2/3}} =
\frac{1}{(\sqrt[3]{-27})^2} =
\frac{1}{(-3)^2} =
\frac{1}{9}.
$$

For $a>0$, $\log a$ is real, so $\exp(x\log a)$ defines a positive real value for every real $x$. If $a<0$, real $\log a$ does not exist. Some rational exponents of negative bases remain real, but the logarithmic formula cannot represent them within real arithmetic.

### Verification

Cubing $-2$ returns $-8$. Raising either evaluated negative power to the reciprocal operation gives the expected base relation. The expression $x^{1/2}x^{3/2}$ at $x=-1$ is not real, while the claimed right side equals $1$, which disproves the unrestricted identity.

### Common wrong turn

Do not choose a root from the numerator and denominator of an unreduced rational exponent independently. Reduce the fraction first, then inspect denominator parity.

### Alternate route

For rational powers of a negative base, write the exponent in lowest terms $m/n$. A real value can exist when $n$ is odd, with reciprocal restrictions added when $m<0$.

## E0.03.02 Solve exponential and logarithmic equations

### Key idea

Use one-to-one exponential or logarithmic behavior only on valid domains, and treat algebraic roots from log equations as candidates.

### Reasoning

1. Since $4=2^2$ and $32=2^5$,

   $$
   4^{2x-1}=2^{4x-2}=2^5
   \iff
   4x-2=5
   \iff
   x=\frac{7}{4}.
   $$

2. Both sides are positive:

   $$
   7e^{0.3t}=19
   \iff
   0.3t=\ln(19/7)
   \iff
   t=\frac{\ln(19/7)}{0.3}\approx3.32843.
   $$

3. The domain is $x>2$. Exponential form gives

   $$
   x-2=3^4=81,
   $$

   so $x=83$, which satisfies the domain.

4. The log arguments require $x>5$. Then

   $$
   \log_2((x-1)(x-5))=4
   $$

   gives

   $$
   (x-1)(x-5)=16
   \iff
   x^2-6x-11=0.
   $$

   The candidates are

   $$
   x=3\pm2\sqrt5.
   $$

   Only $x=3+2\sqrt5$ exceeds $5$. The other root is rejected.

5. The domain is $x>1$. Combine logs:

   $$
   \log\left(\frac{x+1}{x-1}\right)=\log3.
   $$

   Since log is one-to-one,

   $$
   \frac{x+1}{x-1}=3
   \iff
   x+1=3x-3
   \iff
   x=2.
   $$

6. Change of base gives

   $$
   \log_7 50=\frac{\ln50}{\ln7}\approx2.01038.
   $$

### Verification

Substituting $x=7/4$ gives exponent $2x-1=5/2$, and $4^{5/2}=32$. For part 4, the valid root makes $(x-1)(x-5)=16$, so the two base-2 logs sum to $4$. In part 5, $(2+1)/(2-1)=3$. Finally, $7^{2.01038}$ is approximately $50$.

### Common wrong turn

Combining logs before writing the domain makes it easy to accept a quadratic root whose original log argument is nonpositive.

## E0.03.03 Move from compound to continuous growth

### Key idea

Count periods and use the per-period multiplier first. The continuous formula is a limit of that stated model, not a separate magic rule.

### Reasoning

With $n$ compounds per year, each period has rate $r/n$ and there are $nt$ periods. Therefore

$$
A_n(t)=P\left(1+\frac{r}{n}\right)^{nt}.
$$

For $P=2500$, $r=0.048$, and $t=12$:

| Compounding | Formula | Amount, approximately |
|---|---|---:|
| annual | $2500(1.048)^{12}$ | $4388.09$ |
| monthly | $2500(1+0.048/12)^{144}$ | $4442.16$ |
| daily | $2500(1+0.048/365)^{4380}$ | $4447.10$ |
| continuous | $2500e^{0.576}$ | $4447.27$ |

To expose the defining limit, set $m=n/r$ when considering positive $r$ along a compatible sequence. Then $r/n=1/m$ and $nt=mrt$, so

$$
\left(1+\frac{r}{n}\right)^{nt} =
\left[\left(1+\frac{1}{m}\right)^m\right]^{rt}
\longrightarrow e^{rt}.
$$

Thus $A(t)=Pe^{rt}$.

The doubling time satisfies $2=e^{rT_2}$, so

$$
T_2=\frac{\ln2}{0.048}\approx14.4406\text{ years}.
$$

For $Q(t)=600e^{-0.18t}$,

$$
\frac12=e^{-0.18T_{1/2}}
\quad\Longrightarrow\quad
T_{1/2}=\frac{\ln2}{0.18}\approx3.8508
$$

in the time unit used by $t$.

The algebra does not establish that a real account holds a constant nominal rate, that deposits and fees are absent, or that a physical decay law remains valid forever.

The products $rt$, $rT_2$, and $0.18T_{1/2}$ are dimensionless. Therefore $r$ and $0.18$ carry inverse-time units.

### Verification

Substituting $T_2$ gives $e^{rT_2}=e^{\ln2}=2$. Substituting the half-life gives $e^{-0.18T_{1/2}}=e^{-\ln2}=1/2$. The finite amounts approach the continuous amount as compounding frequency increases.

### Common wrong turn

Do not use $n$ both for compounds per year and total periods. The exponent is $nt$, not merely $n$.

### Alternate route

Take logs of $A_n/P$ and use the later calculus fact $\log(1+u)/u\to1$ as $u\to0$. That route is shorter after limits are developed in §1.

## E0.03.04 Compare finite and eventual growth

### Key idea

Log values support safe finite comparison, while little-$o$ states a limit beyond every fixed finite window.

### Reasoning

Compare natural logs of the positive values:

| $n$ | $\log f(n)$ | $\log g(n)$ | $\log h(n)$ | Finite ordering |
|---:|---:|---:|---:|---|
| $10$ | $7.7418$ | $13.8155$ | $1.8232$ | $g>f>h$ |
| $100$ | $8.4349$ | $27.6310$ | $18.2322$ | $g>h>f$ |
| $1000$ | $8.8407$ | $41.4465$ | $182.3216$ | $h>g>f$ |

The eventual ordering is

$$
1000\log n=o(n^6),
\qquad
n^6=o(1.2^n).
$$

Three points cannot prove a limit. They leave infinitely many untested inputs and cannot rule out a later crossing.

For polynomial versus exponential,

$$
n^6<1.2^n
\iff
6\log n<n\log1.2,
$$

because log is increasing. This comparison avoids forming either large value.

For a finite search $1\le n\le N$:

- A **first-win crossover** is the smallest $n$ at which the chosen winner first exceeds the other function.
- A **sustained-through-$N$ crossover** is the smallest $n$ after which it wins at every tested integer through $N$.

A plot ending at $n=100$ suggests that $n^6$ dominates $1.2^n$. Extending to $n=1000$ reverses that finite conclusion and aligns with the eventual order.

A repaired algorithm statement is: "For fixed coefficients, degree, and exponential base greater than one, exponential growth eventually exceeds polynomial growth, but runtime on practical inputs also depends on constants, implementation, hardware, and the input range reached."

### Verification

The log comparisons preserve each ordering because natural log is strictly increasing. At $n=1000$, the gap $n\log1.2-6\log n$ is strongly positive, confirming the table without overflow.

### Common wrong turn

Do not replace "eventually" with "always." Even $2^n$ and $n^2$ exchange order on small positive integers.

## E0.03.05 Turn a product into a log-likelihood

### Key idea

Strict monotonicity preserves ranking, while log space changes numerical scale and optimization geometry.

### Reasoning

The products are

$$
\mathcal{L}_A=0.8\cdot0.7\cdot0.4\cdot0.9\cdot0.6=0.12096,
$$

$$
\mathcal{L}_B=0.75\cdot0.75\cdot0.5\cdot0.8\cdot0.65=0.14625.
$$

Their log-likelihoods are

$$
\ell_A=\sum_i\log p_i^{(A)}=\log(0.12096)\approx-2.11230,
$$

$$
\ell_B=\sum_i\log p_i^{(B)}=\log(0.14625)\approx-1.92244.
$$

Both representations rank $B$ above $A$. The NLL values are approximately $2.11230$ and $1.92244$, so minimizing NLL also selects $B$.

For any positive likelihood values $u$ and $v$, $u>v$ if and only if $\log u>\log v$ because log is strictly increasing. Thus every maximizer of the positive likelihood is a maximizer of log-likelihood and conversely, including ties.

The transformed objective does not have the same differences, slopes, or curvature. For differentiable positive $\mathcal{L}$,

$$
\nabla\log\mathcal{L}=\frac{\nabla\mathcal{L}}{\mathcal{L}},
$$

so an iterative optimizer can take different steps even though the final argmax set agrees.

Repeating each five-factor block 400 times gives product likelihoods $\mathcal{L}_A^{400}$ and $\mathcal{L}_B^{400}$, which underflow to zero in ordinary binary64 arithmetic. Their log-likelihoods remain finite at approximately $-844.92$ and $-768.98$.

### Verification

Since $0.14625>0.12096$, $B$ wins directly. Since $-1.92244>-2.11230$, it also wins after logging. Negation reverses the inequality, making $B$ the NLL minimizer.

### Common wrong turn

Do not say the optimization problems are identical. Their optimizer sets agree under the positivity condition, but their objective surfaces are differently scaled.

## E0.03.06 Find floating-point range failures

### Key idea

Measure each dtype's limits directly, then separate catastrophic loss of every term from loss of a negligible shifted tail.

### Reasoning

A suitable reference implementation is:

```python
import platform
import sys

import numpy as np


def shifted_lse(values, dtype):
    array = np.asarray(values, dtype=dtype)
    maximum = np.max(array)
    return maximum + np.log(np.sum(np.exp(array - maximum), dtype=dtype))


print(sys.version)
print(platform.platform())
print(np.__version__)

for dtype in (np.float32, np.float64):
    info = np.finfo(dtype)
    print(dtype.__name__, info.max, info.smallest_normal, info.smallest_subnormal)
    print(np.log(info.max), np.log(info.smallest_subnormal))

    with np.errstate(over="ignore", under="ignore", divide="ignore"):
        positive = np.arange(0, 1000, dtype=dtype)
        positive_exp = np.exp(positive)
        finite_indices = np.flatnonzero(np.isfinite(positive_exp))
        first_overflow = int(finite_indices[-1]) + 1

        negative = -np.arange(0, 1200, dtype=dtype)
        negative_exp = np.exp(negative)
        zero_indices = np.flatnonzero(negative_exp == 0)
        first_zero = int(-negative[zero_indices[0]])

    print("first_overflow", first_overflow, "first_zero_magnitude", first_zero)
```

On a typical NumPy IEEE implementation, the first positive integer overflow is near $89$ for `float32` and $710$ for `float64`. Exponentials become zero near magnitudes $104$ and $746$, respectively. Exact transition details should come from the submitted run, not from these representative values.

For products, loop over lengths and record the first exact zero for each factor and dtype. Preserve the operation dtype explicitly. A product may become stuck at a positive subnormal before becoming zero because repeated rounding can change the expected mathematical descent.

Test LSE as follows:

```python
cases = [
    [100.0, 99.0, 98.0],
    [1000.0, 999.0, 998.0],
    [-100.0, -101.0],
    [-1000.0, -1001.0],
    [0.0, -1000.0],
]

for values in cases:
    reference = shifted_lse(values, np.float64)
    for dtype in (np.float32, np.float64):
        stable = shifted_lse(values, dtype)
        assert np.isfinite(stable)
        assert np.isclose(stable, reference, rtol=1e-6, atol=1e-6)
```

For `[0.0, -1000.0]`, the shifted tail exponential can be zero while the maximum term remains $1$. The exact result is $\log(1+e^{-1000})$, indistinguishable from zero at binary64 precision. Losing that tail is harmless at the requested accuracy. In naive LSE for `[-1000, -1001]`, both terms become zero, so `log(0)` loses the finite scale near $-1000$. That is harmful.

### Verification

A valid report checks thresholds against `log(finfo.max)` and `log(finfo.smallest_subnormal)`. Stable LSE must satisfy the mathematical bounds for every finite test vector. At least one shifted exponential must equal one.

### Common wrong turn

Do not describe every underflow flag as equally damaging. The effect depends on whether the lost term could materially change the final rounded result.

### Alternate route

Use binary search around thresholds after a coarse integer scan. Report both the method and whether the threshold is for integer test inputs or arbitrary floating-point inputs.

## E0.03.07 Derive stable log-sum-exp

### Key idea

Bounding by the maximum produces both the core inequality and the numerically stable factorization.

### Reasoning

Since some $x_k=m$,

$$
\sum_i e^{x_i}\ge e^m.
$$

Taking logs gives $\mathrm{LSE}(\boldsymbol{x})\ge m$. Also, every $e^{x_i}\le e^m$, so

$$
\sum_i e^{x_i}\le ne^m,
$$

and therefore

$$
\mathrm{LSE}(\boldsymbol{x})\le\log(ne^m)=m+\log n.
$$

Factor the maximum:

$$
\mathrm{LSE}(\boldsymbol{x})
=\log\left(e^m\sum_i e^{x_i-m}\right)
=m+\log\sum_i e^{x_i-m}.
$$

Every shifted argument is nonpositive, so no shifted exponential exceeds one. At least one shifted argument is zero, so at least one exponential equals one. This prevents both exponential overflow and all-term underflow.

For two values, let $m=\max(a,b)$. The other value is $m-|a-b|$, hence

$$
\log(e^a+e^b)
=m+\log(1+e^{-|a-b|}).
$$

A stable implementation uses

$$
m+\mathrm{log1p}(e^{-|a-b|}),
$$

especially when the second term is tiny.

For $(1000,999,998)$,

$$
1000+\log(1+e^{-1}+e^{-2})\approx1000.4076.
$$

It satisfies $1000\le\mathrm{LSE}\le1000+\log3$.

For $(-1000,-1001)$,

$$
-1000+\log(1+e^{-1})\approx-999.6867.
$$

The result exceeds $-1000$ because adding a second positive exponential makes the sum larger than $e^{-1000}$ before taking the log.

If all $x_i=x$, then

$$
\mathrm{LSE}(\boldsymbol{x})=\log(ne^x)=x+\log n,
$$

so the upper bound is attained.

### Verification

The stable formulas use exponentials only at $0$, $-1$, and $-2$ in the examples. Direct high-precision evaluation or a trusted library gives the same rounded values.

### Common wrong turn

Subtracting the maximum without adding it back changes LSE by $m$. Softmax cancels a common shift, but LSE itself shifts by that constant.

## E0.03.08 Derive log-softmax and class NLL

### Key idea

Keep normalization in log space and let a one-hot target select exactly one class log-probability.

### Reasoning

Define

$$
p_c=\frac{e^{z_c}}{\sum_{j=1}^{C}e^{z_j}}.
$$

Each numerator is positive and the denominator is a sum of positive terms, so $p_c>0$. Summing gives

$$
\sum_c p_c
=\frac{\sum_c e^{z_c}}{\sum_j e^{z_j}}=1.
$$

Taking logs,

$$
\log p_c
=z_c-\log\sum_j e^{z_j}
=z_c-\mathrm{LSE}(\boldsymbol{z}).
$$

For a one-hot target,

$$
-\sum_c[c=y]\log p_c=-\log p_y.
$$

Substituting log-softmax yields

$$
-\log p_y=-z_y+\mathrm{LSE}(\boldsymbol{z}).
$$

For shift invariance, replace every logit by $z_c+k$:

$$
\frac{e^{z_c+k}}{\sum_j e^{z_j+k}} =
\frac{e^ke^{z_c}}{e^k\sum_j e^{z_j}}
=p_c.
$$

Also $\mathrm{LSE}(\boldsymbol{z}+k\boldsymbol{1})=k+\mathrm{LSE}(\boldsymbol{z})$, so the $k$ terms cancel in the class loss.

For $\boldsymbol{z}=(1000,999,998)$,

$$
\mathrm{LSE}(\boldsymbol{z})\approx1000.407606.
$$

Thus log-softmax is approximately

$$
(-0.407606,-1.407606,-2.407606),
$$

and target class $1$ has loss $0.407606$.

In Python, mathematical class $1$ is target index `0`. For batch logits with shape `(B, C)`, targets have shape `(B,)`, log-softmax has shape `(B, C)`, and unreduced class NLL has shape `(B,)`.

This is a cross-entropy identity for a one-hot or class-index target. It does not yet develop entropy, expected code length, distributional targets, or divergence.

### Verification

Exponentiating the three log-probabilities gives values summing to one. Adding any constant, such as $-1000$, produces logits $(0,-1,-2)$ and the same probabilities and loss.

### Common wrong turn

Do not exponentiate logits first and then take a log of the selected probability. The stable formula combines those operations before large intermediate values are formed.

## E0.03.09 Preserve small changes with log1p and expm1

### Key idea

The elementary function may be accurate while the surrounding addition or subtraction destroys the small quantity.

### Reasoning

One suitable experiment is:

```python
from math import exp, expm1, log, log1p

values = [1e-4, 1e-8, 1e-12, 1e-16, -1e-12]

for value in values:
    naive_log = log(1.0 + value)
    stable_log = log1p(value)
    naive_exp = exp(value) - 1.0
    stable_exp = expm1(value)
    print(
        f"{value:.1e}",
        f"log error={naive_log - stable_log:.3e}",
        f"exp error={naive_exp - stable_exp:.3e}",
        f"1+x==1: {1.0 + value == 1.0}",
    )
```

Representative binary64 behavior is:

| $x$ | `log(1+x)` behavior | `log1p(x)` behavior | `exp(x)-1` versus `expm1(x)` |
|---:|---|---|---|
| $10^{-4}$ | close | close | both close |
| $10^{-8}$ | visible relative error | accurate | naive loses digits |
| $10^{-12}$ | visible relative error | accurate | naive loses more digits |
| $10^{-16}$ | returns $0$ | retains about $10^{-16}$ | naive may retain a rounded ulp or zero |
| $-10^{-12}$ | visible relative error | accurate | naive loses digits |

At $x=10^{-16}$ on standard binary64, `1.0 + x == 1.0`, so the naive log receives exactly one and returns zero. In `exp(x) - 1`, two nearly equal numbers are subtracted, causing cancellation. `expm1` evaluates the combined expression without first rounding away the small difference.

The approximations

$$
\log(1+x)\approx x,
\qquad
e^x-1\approx x
$$

hold for small $|x|$; higher-order terms explain the remaining difference. They are not exact except at $x=0$ in the limiting sense.

The real domain of $\log(1+x)$ is $x>-1$. Python's `math.log1p(-1.0)` raises `ValueError`; NumPy typically returns `-inf` with a divide warning. The report must name which API was tested.

### Verification

A high-precision `decimal` calculation or a sufficiently long series confirms the stable values. The sign and leading magnitude should agree with $x$ for all listed small inputs.

### Common wrong turn

Comparing two floating-point methods to each other does not identify which is accurate. Include an independent high-precision or analytic reference.

## E0.03.10 Implement a log-domain toolkit

### Key idea

Build every operation around a max shift, preserve reduction axes, and test mathematical invariants rather than only example outputs.

### Reasoning

A complete NumPy implementation is:

```python
from math import fsum, log, log1p

import numpy as np


def log_product(values):
    values = list(values)
    if not values:
        raise ValueError("values must be nonempty")
    if any(value <= 0 for value in values):
        raise ValueError("all factors must be positive")
    return fsum(log(value) for value in values)


def logaddexp_pair(a, b):
    maximum = max(a, b)
    return maximum + log1p(np.exp(-abs(a - b)))


def logsumexp(values, axis=None, keepdims=False):
    array = np.asarray(values)
    if array.size == 0:
        raise ValueError("values must be nonempty")
    maximum = np.max(array, axis=axis, keepdims=True)
    shifted_sum = np.sum(np.exp(array - maximum), axis=axis, keepdims=True)
    result = maximum + np.log(shifted_sum)
    if keepdims:
        return result
    if axis is None:
        return np.squeeze(result)
    return np.squeeze(result, axis=axis)


def log_softmax(logits, axis=-1):
    array = np.asarray(logits)
    return array - logsumexp(array, axis=axis, keepdims=True)


def class_nll(logits, targets):
    array = np.asarray(logits)
    target_array = np.asarray(targets)
    if array.ndim != 2:
        raise ValueError("logits must have shape (batch, classes)")
    if target_array.shape != (array.shape[0],):
        raise ValueError("targets must have shape (batch,)")
    if np.any((target_array < 0) | (target_array >= array.shape[1])):
        raise ValueError("target index out of range")
    rows = np.arange(array.shape[0])
    return -log_softmax(array, axis=1)[rows, target_array]
```

Representative tests are:

```python
assert np.isclose(log_product([0.5, 0.2]), log(0.1))

for a, b in [(0.0, 0.0), (1000.0, 999.0), (-1000.0, -1001.0)]:
    assert np.isclose(logaddexp_pair(a, b), np.logaddexp(a, b))

vectors = [
    np.array([1.0, 2.0, 3.0]),
    np.array([1000.0, 999.0]),
    np.array([-1000.0, -1001.0]),
]
for vector in vectors:
    result = logsumexp(vector)
    maximum = vector.max()
    assert maximum <= result <= maximum + np.log(vector.size)

logits = np.array([[1000.0, 999.0, 998.0], [-1000.0, -999.0, -998.0]])
targets = np.array([0, 2])
logs = log_softmax(logits)
losses = class_nll(logits, targets)

assert logs.shape == logits.shape
assert losses.shape == (2,)
assert np.allclose(np.exp(logs).sum(axis=1), 1.0)
assert np.allclose(log_softmax(logits + 5000.0), logs)

try:
    log_product([0.5, 0.0])
    raise AssertionError("expected ValueError")
except ValueError:
    pass

try:
    class_nll(logits, np.array([0, 3]))
    raise AssertionError("expected ValueError")
except ValueError:
    pass
```

The pair implementation uses `np.exp` for one scalar. A pure standard-library version can use `math.exp` instead.

### Verification

The tests cover hand values, extreme finite logits, mathematical LSE bounds, shift invariance, shape, normalization, agreement with `numpy.logaddexp`, and two invalid-input paths. A SciPy comparison is optional and should be skipped explicitly if unavailable.

### Common wrong turn

Computing a maximum without `keepdims=True` can break broadcasting or shift along the wrong axis. State shapes before reduction.

### Alternate route

For production code, prefer a trusted library implementation that handles special values, multiple axes, weights, and backend details. The first-principles version exists to make the algebra and tests inspectable.

## E0.03.11 Investigate growth crossovers visually

### Key idea

Search on log values, record all sign changes, and label the boundary between observed behavior and asymptotic theorem.

### Reasoning

A reusable search core is:

```python
from math import log


def log_difference(n, *, coefficient, power, base):
    return n * log(base) - (log(coefficient) + power * log(n))


def crossings(*, coefficient, power, base, limit):
    found = []
    previous_sign = None
    for n in range(1, limit + 1):
        difference = log_difference(
            n, coefficient=coefficient, power=power, base=base
        )
        sign = difference > 0
        if previous_sign is not None and sign != previous_sign:
            found.append(n)
        previous_sign = sign
    return found
```

A sound investigation predicts that $(10,2)$ crosses later than $(2,2)$ because the higher polynomial degree raises the polynomial log value $k\log n$. A base near $1$, such as $1.1$, can delay exponential dominance much further because $n\log a$ grows with a small coefficient.

A complete result table should include:

| Coefficient | $k$ | $a$ | Search limit | Crossings | Winner at limit |
|---:|---:|---:|---:|---|---|
| chosen | $2$ | $2$ | stated | measured | measured |
| chosen | $10$ | $2$ | stated | measured | measured |
| chosen | chosen | $1.1$ | stated | measured | measured |

A visual should plot either raw values within range or the clearly labeled log values

$$
\log(cn^k)=\log c+k\log n,
\qquad
\log(a^n)=n\log a.
$$

Use a vertical marker at each measured crossing and another at the search limit. For $(10,2)$, one narrow early window can show polynomial dominance, while a sufficiently extended window reveals the exponential's later sustained lead.

A strong conclusion has this form:

**Observation.** Within the stated ranges, increasing $k$, decreasing $a$ toward one, or increasing $c$ delayed the final observed exponential crossover.

**Asymptotic result.** For every fixed $c>0$, $k>0$, and $a>1$, $cn^k=o(a^n)$ as $n\to\infty$.

**Limitation.** The finite search illustrates crossings but does not prove there are no later crossings. The theorem supplies the eventual claim.

### Verification

At every reported crossing, inspect the log difference on both sides. The visual and table must be generated from the same parameters and ranges. Increasing the search limit without changing parameters should preserve earlier reported sign changes.

### Common wrong turn

A chart with an unlabeled logarithmic vertical axis can visually misrepresent distance. Name the transformation and interpret ordering, not apparent slope alone.

### Alternate route

Instead of plotting, provide a dense table of log differences and an accessible text description of every sign change. This still satisfies the mathematical investigation when plotting software is unavailable.

## E0.03.12 Critique logarithm claims and sources

### Key idea

Separate historical priority, mathematical identity, asymptotic qualification, optimizer equivalence, floating-point implementation, and naming convention before assigning evidence.

### Reasoning

At least twelve repairs are available:

| Claim | Diagnosis | Repair | Evidence type |
|---|---|---|---|
| Napier invented modern natural logs | conflates a historical construction with modern $\ln$ | Napier published a logarithm construction in 1614 that was not simply modern natural log | historical source |
| Napier worked entirely alone | ignores later collaboration in conventions and tables | distinguish Napier's publication from discussions with Briggs | historical source |
| Briggs changed to base 10 without Napier | contradicts documented discussions | base-10-style tables and $\log1=0$ emerged through their exchanges, with Briggs constructing tables | historical source |
| logs turn every operation into addition | overgeneralization | logs turn products into sums and quotients into differences | algebra |
| $\log(x+y)=\log x+\log y$ | false law | no such distribution; use LSE for sums of exponentials | counterexample |
| taking logs leaves optimization unchanged | too broad | positive likelihood and log-likelihood have the same argmax, but different values and geometry | monotonicity and calculus preview |
| $2^n$ is always larger than $n^{10}$ | false finite claim | $2^n$ eventually dominates, but $n^{10}$ is larger for many finite $n$ | calculation and asymptotics |
| a finite plot proves eventual growth | evidence mismatch | a finite plot illustrates only the inspected range | logic |
| Python `log` is base 10 | false API claim | `math.log(x)` is natural log | official docs |
| calculators all use one convention | unsupported generalization | inspect each interface; many calculators label base 10 as `log` | device docs |
| machine learning uses base 10 by default | conflicts with common notation | natural logs and nats are the project default; state alternatives explicitly | notation contract and texts |
| softmax overflow is unavoidable | ignores algebraic reformulation | subtract the maximum before exponentiating | derivation and numerical analysis |
| max shifting is exact on a computer | confuses exact algebra with floating point | formulas are algebraically equal; rounding still occurs | numerical analysis |
| any shifted underflow invalidates LSE | ignores relative significance | a negligible nonmaximum tail may vanish harmlessly while a maximum term remains one | error analysis |
| cross-entropy is always different from NLL | false for class-index targets | one-hot or class-index cross-entropy reduces to target-class NLL | algebra and framework docs |

The Napier biography supports the 1614 publication, dynamical construction, and warning that a modern base description is potentially misleading. The Briggs biography supports his response to the 1614 text, meetings with Napier, their discussion of $\log1=0$ and base-10-style tables, and Briggs's table construction. These biographies do not turn seventeenth-century terminology into modern formal base definitions.

Official Python documentation supports the natural-log behavior of `math.log` and the special near-zero functions. NumPy documentation supports `logaddexp`, `log1p`, `expm1`, and `finfo`. PyTorch documentation supports the class-index CrossEntropyLoss equivalence to LogSoftmax plus NLLLoss.

In exact real arithmetic,

$$
\log\sum_i e^{x_i}
=m+\log\sum_i e^{x_i-m}.
$$

In floating-point arithmetic, subtraction, exponentiation, summation, and log each round. The reformulation controls range and usually improves reliability, but "exact on a computer" is not a defensible blanket claim.

A corrected paragraph under 220 words is:

> Napier published his logarithm construction in 1614 to simplify difficult calculations. His logarithms were not simply modern natural logs. After reading the work, Briggs corresponded and met with Napier; their discussions shaped more convenient base-10-style tables with $\log1=0$, and Briggs carried out major table construction. Modern logs turn products into sums, not arbitrary operations, so $\log(x+y)$ does not split. For a positive likelihood, taking logs preserves the argmax because log is increasing, but it changes objective scale and curvature. An exponential with base greater than one eventually exceeds any fixed polynomial, although finite inputs and plots can show the opposite ordering. Log notation depends on context: Python's `math.log` and this curriculum use natural log, while some calculators use `log` for base 10. Stable softmax and LSE subtract the largest logit before exponentiating. This identity is exact algebraically, while its computer evaluation still rounds. A tiny shifted tail may underflow harmlessly because a maximum term remains one. For a one-hot or class-index target, cross-entropy reduces to the negative log-likelihood of the target class.

A source ledger should include at least:

| URL | Supported sentence |
|---|---|
| Napier MacTutor biography | 1614 publication, construction, nonmodern base caveat |
| Briggs MacTutor biography | collaboration, visits, and table construction |
| Python `math` docs | `log`, `log1p`, and `expm1` behavior |
| NumPy API docs | `finfo` and log-domain operations |
| Blanchard et al. DOI or publisher page | shifted LSE and softmax numerical analysis |
| PyTorch CrossEntropyLoss docs | class-index LogSoftmax plus NLLLoss equivalence |

### Verification

Every row identifies whether its support is algebraic, computational, historical, or documentary. The corrected paragraph avoids a single-inventor story, false log laws, universal base claims, and an overstatement about floating-point exactness.

### Common wrong turn

A source that mentions a person or API is not automatically evidence for every nearby claim. Record the exact sentence or behavior each source supports.

### Alternate route

Use Napier's translated preface as a primary source for his computational motivation, then retain a scholarly history for interpreting how his construction differs from modern logarithms.

## Solution-set check

All exercise IDs and titles mirror the [exercise index](../exercises/README.md):

- E0.03.01 Audit exponent laws and domains
- E0.03.02 Solve exponential and logarithmic equations
- E0.03.03 Move from compound to continuous growth
- E0.03.04 Compare finite and eventual growth
- E0.03.05 Turn a product into a log-likelihood
- E0.03.06 Find floating-point range failures
- E0.03.07 Derive stable log-sum-exp
- E0.03.08 Derive log-softmax and class NLL
- E0.03.09 Preserve small changes with log1p and expm1
- E0.03.10 Implement a log-domain toolkit
- E0.03.11 Investigate growth crossovers visually
- E0.03.12 Critique logarithm claims and sources

[Back to module](../README.md) | [Exercise set](../exercises/README.md)
