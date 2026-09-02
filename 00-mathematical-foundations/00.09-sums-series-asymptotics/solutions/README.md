# Solutions for §0.09 Sums, Series, and Asymptotics

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

These are full worked solutions. Equivalent bounds, comparison series, or implementations are valid when they preserve every hypothesis and state the same evidence limits.

Python excerpts that import `series_tools` run from the module's `code/` directory.

## E0.09.01 Derive three finite sums

### Key idea

Prove cancellation or pairing inside a finite partial sum. Only then take a limit when one is requested.

### Reasoning

For an arithmetic sequence,

$$
S_N=a+(a+d)+\cdots+(a+(N-1)d).
$$

Adding the reversed expression gives

$$
2S_N=N(2a+(N-1)d),
$$

so

$$
S_N=\frac N2(2a+(N-1)d).
$$

For the sequence from $7$ to $202$ with difference $5$,

$$
202=7+39\cdot5,
$$

so there are $40$ terms and

$$
S_{40}=\frac{40}{2}(7+202)=4180.
$$

For a geometric sum with $r\ne1$,

$$
S_N=a+ar+\cdots+ar^{N-1}
$$

and

$$
S_N-rS_N=a-ar^N.
$$

Therefore

$$
S_N=a\frac{1-r^N}{1-r}.
$$

When $r=1$, subtraction would divide by zero, while direct addition gives $S_N=Na$.

Thus

$$
\sum_{k=0}^{9}3\left(\frac23\right)^k
=9\left(1-\left(\frac23\right)^{10}\right)
=\frac{58025}{6561}.
$$

Partial fractions give

$$
\frac{2}{n(n+2)}=\frac1n-\frac1{n+2}.
$$

Hence

$$
\sum_{n=1}^{N}\frac{2}{n(n+2)}
=1+\frac12-\frac1{N+1}-\frac1{N+2}.
$$

Taking $N\to\infty$ gives $3/2$.

```python
from fractions import Fraction

from series_tools import arithmetic_sum, geometric_sum

assert arithmetic_sum(7, 5, 40) == 4180
assert geometric_sum(3, Fraction(2, 3), 10) == Fraction(58025, 6561)
for count in range(1, 101):
    direct = sum(Fraction(2, n * (n + 2)) for n in range(1, count + 1))
    closed = Fraction(3, 2) - Fraction(1, count + 1) - Fraction(1, count + 2)
    assert direct == closed
```

### Verification

Every identity is exact for finite $N$. The only infinite step is the final limit of the two boundary terms.

### Common wrong turn

Do not drop $1/(N+1)$ and $1/(N+2)$ before the finite cancellation is complete.

## E0.09.02 Prove convergence from monotone bounds

### Key idea

Invariant bounds and monotonicity establish existence. The recurrence identifies the limit only afterward.

### Reasoning

At $n=1$, $1\le a_1<2$. If $1\le a_n<2$, then

$$
\sqrt3\le a_{n+1}=\sqrt{2+a_n}<\sqrt4=2,
$$

so the interval is invariant.

All terms are positive. To prove increase, square both sides:

$$
a_{n+1}>a_n
\iff
2+a_n>a_n^2.
$$

The difference factors as

$$
2+a_n-a_n^2=(2-a_n)(a_n+1)>0
$$

because $1\le a_n<2$. Thus the sequence is increasing and bounded above by $2$. The monotone convergence theorem gives a finite limit $L$.

Continuity of the square root gives

$$
L=\sqrt{2+L}.
$$

Squaring yields $(L-2)(L+1)=0$. The established interval excludes $-1$, so $L=2$.

Solving a fixed-point equation first only lists possible limits. It does not show that the sequence has a limit.

The bounded sequence $(-1)^n$ is not monotone and diverges. The monotone sequence $a_n=n$ is not bounded above and diverges.

### Verification

The proof supplies induction, monotonicity, an upper bound, convergence, and then unique limit identification in that order.

### Common wrong turn

A fixed point of the update map need not attract the initial value. Never replace a convergence proof with a fixed-point calculation.

## E0.09.03 Build partial sums and use the nth-term test

### Key idea

The nth-term test asks about $a_n$. Convergence asks about the different sequence $S_N$.

### Reasoning

| Series | First four $a_n$ | First four $S_N$ | Nth-term conclusion |
|---|---|---|---|
| $\sum n/(n+1)$ | $1/2,2/3,3/4,4/5$ | $1/2,7/6,23/12,163/60$ | diverges since $a_n\to1$ |
| $\sum1/n$ | $1,1/2,1/3,1/4$ | $1,3/2,11/6,25/12$ | inconclusive since $a_n\to0$ |
| $\sum1/n^2$ | $1,1/4,1/9,1/16$ | $1,5/4,49/36,205/144$ | inconclusive since $a_n\to0$ |
| $\sum(-1)^n$ | $-1,1,-1,1$ | $-1,0,-1,0$ | diverges since $a_n$ has no limit |
| $\sum(-1)^{n-1}/n$ | $1,-1/2,1/3,-1/4$ | $1,1/2,5/6,7/12$ | inconclusive since $a_n\to0$ |

The convergent example $\sum1/n^2$ and divergent example $\sum1/n$ both have terms approaching zero.

If $S_N\to S$, then $S_{N-1}\to S$ and

$$
a_N=S_N-S_{N-1}\to0.
$$

A tiny millionth term reports one local magnitude. It does not bound the infinite tail or the partial sums. Changing finitely many initial terms adds one finite constant to all later partial sums, so convergence is unchanged while the sum shifts by that constant.

### Verification

Only the first and fourth rows fail the necessary term-limit condition. The other rows need different tests.

### Common wrong turn

"Inconclusive" is not a weaker spelling of "convergent."

## E0.09.04 Apply direct and limit comparison

### Key idea

For nonnegative terms, convergence moves downward from a convergent majorant and divergence moves upward from a divergent minorant.

### Reasoning

1. Since $0\le1/(n^2+7)\le1/n^2$, the series converges.
2. Compare with $1/n$:
   $$
   \frac{(4n+1)/(n^2+3)}{1/n}
   =\frac{4n^2+n}{n^2+3}\to4.
   $$
   It diverges with the harmonic series.
3. Since $2^n+n\ge2^n$,
   $$
   0\le\frac1{2^n+n}\le\frac1{2^n},
   $$
   so it converges.
4. Compare with $1/n^2$:
   $$
   \frac{n/(n^3+1)}{1/n^2}=\frac{n^3}{n^3+1}\to1,
   $$
   so it converges.
5. Compare with $1/n$:
   $$
   \frac{(n^2+1)/(n^3+2)}{1/n}=\frac{n^3+n}{n^3+2}\to1,
   $$
   so it diverges.

Arguments 6 and 7 use the two unlicensed direct-comparison directions. A smaller series may converge while a larger one diverges. They should be replaced by the known $p$-series classification.

For $L=0$ with divergent $b_n=1/n$:

$$
a_n=\frac1{n^2}
$$

converges, while

$$
a_n=\frac1{n\ln n},\quad n\ge2,
$$

diverges. Both satisfy $a_n/b_n\to0$.

For $L=\infty$ with convergent $b_n=1/n^2$, the choice $a_n=1/n^{3/2}$ converges and $a_n=1/n$ diverges. Both ratios tend to infinity.

If the ratio limit does not exist, this version of limit comparison gives no conclusion.

### Verification

Every accepted comparison includes eventual positivity, a known reference series, and the correct direction.

### Common wrong turn

The size relation alone is not enough. The known behavior must point in the useful direction.

## E0.09.05 Use integrals to bound sums and tails

### Key idea

A positive decreasing function traps unit-width rectangles between neighboring integrals.

### Reasoning

For decreasing $1/x$,

$$
\frac1{k+1}\le\int_k^{k+1}\frac{dx}{x}\le\frac1k.
$$

Summing gives

$$
\ln(n+1)\le H_n\le1+\ln n.
$$

The lower bound tends to infinity, so the harmonic partial sums are unbounded. Dividing by $\ln n$ gives

$$
\frac{\ln(n+1)}{\ln n}\le\frac{H_n}{\ln n}\le1+\frac1{\ln n}.
$$

Both outer expressions tend to one, so $H_n\sim\ln n$. The same bounds give $H_n=\Theta(\ln n)$.

For $n\ge2$, $f(x)=1/[x(\ln x)^2]$ is continuous, positive, and decreasing. With $u=\ln x$,

$$
\int_2^\infty\frac{dx}{x(\ln x)^2}
=\int_{\ln2}^\infty u^{-2}\,du<\infty.
$$

The series converges. Replacing $(\ln x)^2$ by $\ln x$ produces $\int du/u$, which diverges, so $\sum1/(n\ln n)$ diverges.

For $p>1$,

$$
\frac{(N+1)^{1-p}}{p-1}
\le R_N\le
\frac{N^{1-p}}{p-1}.
$$

For $p=3$, require

$$
\frac1{2N^2}<10^{-4}.
$$

This is $N^2>5000$, so the smallest integer is $N=71$.

The integral and series share convergence behavior under the theorem, not value. For an unavailable example, $a_n=2+(-1)^n$ has positive terms but the natural extension $f(x)=2+\cos(\pi x)$ is not decreasing. The nth-term test settles divergence anyway.

### Verification

$70^2=4900$ fails the requested bound and $71^2=5041$ passes.

### Common wrong turn

Do not quote an integral remainder estimate before proving that the series converges and that the extension is eventually positive, continuous, and decreasing.

## E0.09.06 Apply and refuse ratio and root tests

### Key idea

Limits below one create geometric domination. One is the exact boundary where that proof stops.

### Reasoning

1. For $a_n=5^n/n!$,
   $$
   \left|\frac{a_{n+1}}{a_n}\right|=\frac5{n+1}\to0,
   $$
   so the series converges absolutely.
2. For $a_n=n!/4^n$, the ratio is $(n+1)/4\to\infty$, so the series diverges.
3. The root limit is
   $$
   \frac{2n+1}{5n+3}\to\frac25<1,
   $$
   so the series converges absolutely.
4. The root is $(1+1/n)^{-n}\to e^{-1}<1$, so the series converges.
5. For $1/n^3$, both ratio and root limits equal one. Both tests are inconclusive, although the $p$-series converges.
6. For $(-1)^n/n$, the absolute ratio tends to one. Ratio is inconclusive; the alternating test gives conditional convergence.

The convergent $p$-series $\sum1/n^2$ and divergent harmonic series both have ratio limit one.

For a convergent series with no root limit, define

$$
a_n=
\begin{cases}
2^{-n},&n\text{ even},\\
3^{-n},&n\text{ odd}.
\end{cases}
$$

Its root diagnostic alternates between $1/2$ and $1/3$, but comparison with $2^{-n}$ proves absolute convergence.

If $L>1$, then $|a_n|$ eventually fails to approach zero because successive magnitudes grow by a factor bounded above one. The nth-term condition therefore proves ordinary divergence.

### Verification

Every conclusion below one is absolute. Every case at one or without a limit uses another theorem or remains unresolved by the named test.

### Common wrong turn

The test does not say "converges for $L\le1$." The strict inequality is load-bearing.

## E0.09.07 Classify alternating and signed series

### Key idea

Test ordinary convergence and absolute convergence as separate questions.

### Reasoning

1. $\sum(-1)^{n-1}/n$ converges by the alternating test, while its absolute series is harmonic. It is conditional.
2. $\sum(-1)^{n-1}/n^2$ converges absolutely by the $p$-series test.
3. The magnitude $n/(n+1)\to1$, so the terms do not approach zero. It diverges.
4. Magnitudes $1/\sqrt n$ decrease to zero, so the series converges. Its absolute $p$-series has $p=1/2$ and diverges, so convergence is conditional.
5. The absolute series $\sum(n+2)/2^n$ converges by the ratio test with limit $1/2$. It is absolute.
6. The magnitudes are not eventually decreasing because each even term jumps above the preceding odd term. More strongly, positive odd terms $1/n^2$ have a finite sum while negative even magnitudes contain one half of the harmonic series, so partial sums diverge to $-\infty$.

For item 1, the alternating error satisfies

$$
|R_N|\le\frac1{N+1}.
$$

The smallest $N$ guaranteeing at most $10^{-3}$ is $N=999$.

The next-term bound comes from the bracketing of monotone alternating partial sums. Without decreasing magnitudes and a zero limit, that geometry need not hold.

For absolute convergence, write

$$
0\le |a_n|+a_n\le2|a_n|.
$$

Comparison shows $\sum(|a_n|+a_n)$ converges. Subtracting the convergent $\sum|a_n|$ gives convergence of $\sum a_n$.

### Verification

The six classifications are conditional, absolute, divergent, conditional, absolute, and divergent.

### Common wrong turn

Alternating signs do not rescue terms whose magnitudes fail to approach zero.

## E0.09.08 Rearrange a conditional series carefully

### Key idea

Both sign pools are unbounded in total magnitude, while individual terms shrink. Those facts let partial sums cross any finite target with shrinking overshoot.

### Reasoning

The positive odd subseries satisfies

$$
\sum_{k=1}^{m}\frac1{2k-1}
\ge\frac12H_m,
$$

so it diverges. The negative magnitudes satisfy

$$
\sum_{k=1}^{m}\frac1{2k}=\frac12H_m,
$$

so they also diverge.

Therefore a positive phase always crosses $T=1$, and a negative phase always crosses back. At an upward crossing, the overshoot is no larger than the last added positive term. At a downward crossing, the undershoot is no larger than the last negative magnitude. Those terms approach zero, so both crossing subsequences approach one.

No term is skipped forever. If a positive term were the first never selected, later positive phases could not proceed past it. The same argument holds for negative terms. Thus the construction is a permutation of all original terms, not a selected subseries.

```python
target = 1.0
total = 0.0
positive_index = 1
negative_index = 1
crossings = []

while positive_index + negative_index <= 10_000:
    while total <= target:
        total += 1 / (2 * positive_index - 1)
        positive_index += 1
    crossings.append(("above", total))
    while total >= target:
        total -= 1 / (2 * negative_index)
        negative_index += 1
    crossings.append(("below", total))

assert all(side == "above" and value > target or side == "below" and value < target
           for side, value in crossings)
assert max(abs(value - target) for _, value in crossings[-20:]) < 0.001
```

An absolutely convergent series has a finite total absolute tail, so every permutation has the same limit. Conditional convergence lacks that protection.

### Verification

The proof uses divergence of both sign pools, shrinking terms, and exhaustion of every term. The code illustrates only a finite prefix.

### Common wrong turn

Crossing the target many times does not alone prove convergence. The overshoot must shrink, and the construction must use every original term exactly once.

## E0.09.09 Certify harmonic approximations

### Key idea

The approximation is useful at a finite $n$ because the omitted remainder is bounded, not because the displayed decimals look stable.

### Reasoning

The coarse bounds and Euler bound follow directly from the module. For the sharp approximation,

$$
0<H_n-A_n<\frac1{120n^4}.
$$

To make the right side smaller than $10^{-12}$, require

$$
n^4>\frac{10^{12}}{120}=8{,}333{,}333{,}333.\overline3.
$$

Since

$$
302^4=8{,}318{,}169{,}616
$$

and

$$
303^4=8{,}428{,}892{,}481,
$$

the smallest integer is $n=303$.

```python
from math import fsum, log

gamma = 0.5772156649015328606
for number in (1, 10, 100, 1000, 10_000):
    harmonic = fsum(1 / index for index in range(1, number + 1))
    coarse_lower = log(number + 1)
    coarse_upper = 1 + log(number)
    approximation = log(number) + gamma + 1 / (2 * number) - 1 / (12 * number**2)
    assert coarse_lower <= harmonic <= coarse_upper
    assert 0 < harmonic - log(number) - gamma <= 1 / number
    assert harmonic - approximation < 1 / (120 * number**4) + 2e-15

assert 1 / (120 * 302**4) > 1e-12
assert 1 / (120 * 303**4) < 1e-12
```

The small tolerance in the binary64 assertion belongs to rounding, not to the analytic theorem. A high-precision check should remove that representational ambiguity.

The coarse squeeze proof divides $\ln(n+1)\le H_n\le1+\ln n$ by $\ln n$ and takes limits. Decimal data is unnecessary.

### Verification

The integral and squeeze arguments are proofs, the sharp remainder is a directly inspected DLMF consequence, and the table is finite computational evidence.

### Common wrong turn

Observed error can be smaller than the certified bound. That does not improve the theorem for untested inputs.

## E0.09.10 Use Stirling with finite error discipline

### Key idea

Stirling describes the scale of the permutation count. The remainder interval controls a chosen finite input.

### Reasoning

$n!$ counts linear orders of $n$ distinct objects. The relation

$$
n!\sim e^{L_n}
$$

means $n!/e^{L_n}\to1$. It does not mean equality after a threshold or supply a requested finite tolerance.

The certified log interval is

$$
L_n+\frac1{12n}-\frac1{360n^3}<\ln(n!)<L_n+\frac1{12n}.
$$

Exponentiation preserves order and gives

$$
e^{L_n}e^{1/(12n)-1/(360n^3)}<n!<e^{L_n}e^{1/(12n)}.
$$

The log-width is exactly

$$
\frac1{12n}-\left(\frac1{12n}-\frac1{360n^3}\right)
=\frac1{360n^3}.
$$

For width below $10^{-12}$, require $n^3>10^{12}/360$. Since

$$
1405^3=2{,}773{,}505{,}125
$$

and

$$
1406^3=2{,}779{,}431{,}416,
$$

the smallest integer is $1406$.

The repository test uses `Decimal(factorial(n)).ln()` at 70-digit precision to validate selected correction intervals independently of `lgamma`. It also retains the correction endpoints as exact `Fraction` values.

Binary64 spacing grows with magnitude. Once the correction width is smaller than one representable gap near $\ln(n!)$, two distinct mathematical endpoints can round to the same float. "Exact for large $n$" is false. The relative error tends to zero but is generally nonzero at every finite $n$.

### Verification

Run `python -m unittest -v` in `code/`. The high-precision test checks $n=1,2,10,100,1000$ and the exact width identity is symbolic.

### Common wrong turn

More correct decimal digits do not turn an asymptotic equivalence into an equality.

## E0.09.11 Prove asymptotic relations and separations

### Key idea

Use constants for big notation and ratios for little notation or equivalence. Always name the limit direction.

### Reasoning

For $n\ge1$,

$$
5n^3\le7n^3-2n+4\le11n^3.
$$

Thus $f(n)=\Theta(n^3)$ with $c=5$, $C=11$, and $N=1$. Also,

$$
\frac{7n^3-2n+4}{7n^3}
=1-\frac{2}{7n^2}+\frac{4}{7n^3}\to1,
$$

so $f\sim7n^3$. Its ratio to $n^3$ tends to $7$, so $f\not\sim n^3$.

Write $t=\sqrt n$. Then

$$
\frac{\ln n}{\sqrt n}=\frac{2\ln t}{t}\to0,
$$

using logarithmic growth from §0.03. Hence $\ln n=o(\sqrt n)$.

For $b_n=n^5/2^n$,

$$
\frac{b_{n+1}}{b_n}=\frac{(1+1/n)^5}{2}\to\frac12<1.
$$

Therefore $b_n\to0$, which is $n^5=o(2^n)$.

If $f/g\to0$, then eventually $|f/g|\le1$, so $|f|\le|g|$ eventually. Thus $f=o(g)$ implies $f=O(g)$. The converse fails for $f=g=n$.

If $f/g\to1$, then eventually $1/2\le|f/g|\le3/2$, so $f=\Theta(g)$. The converse fails for $f=3g$ with positive $g$.

As $h\to0$,

$$
\frac{h^3}{h^2}=h\to0,
$$

so $h^3=o(h^2)$ and therefore $h^3=O(h^2)$. The direction changed, but the distinction did not: bounded ratio is still big-O, while zero ratio is still little-o.

Finally:

- $n^2=O(n^3)$ is true;
- $n^2=\Omega(n)$ is true;
- $n^2=\omega(n)$ is true because the ratio is $n\to\infty$;
- $3n^2\sim n^2$ is false because the ratio tends to three.

### Verification

Every relation has a direction, and each failed converse has an explicit counterexample.

### Common wrong turn

Theta ignores a positive constant factor. Asymptotic equivalence does not.

## E0.09.12 Implement and audit an asymptotic claim

### Key idea

Different evidence answers different questions. The report should never let one passing loop stand in for theorem hypotheses, source inspection, or a universal proof.

### Reasoning

A complete report can extend [`test_series_tools.py`](../code/test_series_tools.py). Its evidence table should distinguish:

| Claim | Evidence | Limit |
|---|---|---|
| finite sum helper matches direct sum | exact `Fraction` checks | tested finite parameter grid |
| harmonic series diverges | integral lower-bound proof | universal positive integers |
| sharp harmonic interval | DLMF expansion and remainder rule | stated positive-real conditions |
| Stirling implementation matches selected values | 70-digit decimal checks | selected finite inputs |
| ratio test at $L=1$ is inconclusive | theorem plus convergent and divergent $p$-series | requires ratio limit |
| timing or ratio trend | reproducible experiment | observed machine and input range |

At least eight defects in the proposed claim are:

1. A ratio that merely looks near one does not establish a limit.
2. A ratio limit of one makes the ratio test inconclusive.
3. The series may converge or diverge at that boundary.
4. Big-O means eventual bounded relative magnitude, not ratio zero.
5. Little-o is the ratio-zero statement.
6. Every asymptotic statement needs a limit direction.
7. Stirling's leading expression is generally not exactly $n!$ at any finite threshold.
8. An asymptotic equivalence alone gives no requested finite error.
9. Ten thousand cases remain finite and cannot prove an all-input claim.
10. Tests can share an implementation or transcription error with the code under test.
11. Floating-point agreement includes rounding behavior and is not exact arithmetic.
12. Source authority and reuse permission require direct inspection, not execution.

The source ledger should record that OpenStax HTML exposed theorem statements and exercises directly; MIT's Unit 5 index exposed session placement but the guessed session URL and some linked artifact extraction failed; DLMF exposed numbered equations and remainder conditions; Princeton exposed tilde models, cost models, and empirical-method limits; and Python exposed current API semantics. No source material should be copied into the report.

### Verification

Run the unit tests, all Python fences, high-precision recomputation, link and citation checks, then remove `__pycache__`. Record actual output and finite ranges.

### Common wrong turn

Do not label a source "verified" when only a search result, generated summary, or inaccessible PDF was seen.

## Solution-set check

All exercise IDs and titles mirror the [exercise index](../exercises/README.md):

- E0.09.01 Derive three finite sums
- E0.09.02 Prove convergence from monotone bounds
- E0.09.03 Build partial sums and use the nth-term test
- E0.09.04 Apply direct and limit comparison
- E0.09.05 Use integrals to bound sums and tails
- E0.09.06 Apply and refuse ratio and root tests
- E0.09.07 Classify alternating and signed series
- E0.09.08 Rearrange a conditional series carefully
- E0.09.09 Certify harmonic approximations
- E0.09.10 Use Stirling with finite error discipline
- E0.09.11 Prove asymptotic relations and separations
- E0.09.12 Implement and audit an asymptotic claim

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md)