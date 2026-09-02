# Solutions for §0.10 Inequalities

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

These are full worked solutions. Equivalent arguments are valid when they state
the same assumptions, direction, equality conditions, and evidence limits.
Python excerpts importing `inequality_tools` run from the module's `code/`
directory.

## E0.10.01 Audit order-preserving operations

### Key idea

An operation's monotonicity and the operands' domains determine direction.

### Reasoning

From $a\le b$ we always obtain $a+c\le b+c$. Multiplication gives

$$
ac\le bc\quad(c>0),\qquad ac=bc\quad(c=0),\qquad ac\ge bc\quad(c<0).
$$

If $0<a\le b$, then $ab>0$. Multiplying $a\le b$ by $1/(ab)>0$ gives
$1/b\le1/a$.

Squaring needs nonnegative operands. The counterexample $-3<-2$ but $9>4$
shows that squaring is not increasing on all reals. A sufficient condition is
$0\le a\le b$, which gives $a^2\le ab\le b^2$.

The function $x^2$ increases on $[0,\infty)$ and decreases on
$(-\infty,0]$. The reciprocal decreases on $(0,\infty)$ and also on
$(-\infty,0)$, but an interval cannot cross zero. The logarithm increases on
$(0,\infty)$.

The multiplication claim needs $z\ge0$ for the displayed direction, with
equality collapse at $z=0$; it reverses for $z<0$. The square-root claim becomes
valid as $|x|\le|y|$ from $x^2\le y^2$. It gives $x\le y$ only with additional
conditions such as $0\le x,y$.

### Verification

Each repaired statement names the multiplier sign or function domain before the
direction.

### Common wrong turn

Do not infer monotonicity from familiar notation. State the interval on which
the function is monotone.

## E0.10.02 Prove triangle and reverse triangle bounds

### Key idea

Trap a scalar between its positive and negative magnitudes, then apply triangle
in both directions.

### Reasoning

Since $-|a|\le a\le|a|$ and $-|b|\le b\le|b|$, addition gives

$$
-(|a|+|b|)\le a+b\le|a|+|b|.
$$

Therefore $|a+b|\le|a|+|b|$. Also,

$$
|a|=|(a-b)+b|\le|a-b|+|b|,
$$

so $|a|-|b|\le|a-b|$. Swapping $a,b$ proves
$||a|-|b||\le|a-b|$.

For any norm,

$$
\lVert\boldsymbol{x}\rVert
\le\lVert\boldsymbol{x}-\boldsymbol{y}\rVert+
\lVert\boldsymbol{y}\rVert.
$$

Subtract and swap the vectors to obtain

$$
|\lVert\boldsymbol{x}\rVert-\lVert\boldsymbol{y}\rVert|
\le\lVert\boldsymbol{x}-\boldsymbol{y}\rVert.
$$

Hence the approximation's norm error is at most $0.01$.

Scalar equality occurs exactly when $ab\ge0$. For example, $|2+3|=2+3$;
$|2-3|<2+3$. Euclidean equality examples are $(1,2)+(2,4)$, whose vectors
align positively, and the strict example $(1,0)+(0,1)$.

### Verification

The reverse bound follows from the norm axioms alone and therefore applies to
every norm, not only $\ell^2$.

### Common wrong turn

Opposite proportional vectors do not give equality in the norm of a sum unless
one is zero; they create cancellation.

## E0.10.03 Optimize with AM-GM and audit equality

### Key idea

Convert a fixed sum or product into the side controlled by AM-GM, then solve the
equality requirements together with the constraint.

### Reasoning

For $a,b\ge0$,

$$
0\le(\sqrt a-\sqrt b)^2=a+b-2\sqrt{ab},
$$

so $\sqrt{ab}\le(a+b)/2$, with equality exactly at $a=b$.

If $x+y=18$, then $\sqrt{xy}\le9$, so $xy\le81$. Equality requires and is
attained by $x=y=9$.

If $abc=64$ and all values are positive,

$$
4=(abc)^{1/3}\le\frac{a+b+c}{3}.
$$

Thus $a+b+c\ge12$, attained exactly at $a=b=c=4$.

For the weighted example,

$$
1^{1/3}9^{2/3}=\sqrt[3]{81}
\le\frac13+\frac23(9)=\frac{19}{3}.
$$

The inequality is strict because both weights are positive and $1\ne9$.

A zero value with positive weight makes the weighted geometric product zero. A
zero-weight coordinate is omitted, including from the equality audit. Negative
inputs break this real AM-GM contract; for example, the real square root in the
geometric mean of $-1$ and $2$ is not defined.

Weighted two-value AM-GM is exactly

$$
u^\theta v^{1-\theta}\le\theta u+(1-\theta)v
$$

for $u,v>0$ and $\theta\in[0,1]$.

```python
from inequality_tools import weighted_am_gm_sides

for first in range(1, 11):
    for second in range(1, 11):
        geometric, arithmetic = weighted_am_gm_sides(
            (first, second), (0.25, 0.75)
        )
        assert geometric <= arithmetic + 1e-12

for values, weights in [((-1, 2), (0.5, 0.5)), ((1, 2), (0.4, 0.4)), ((1,), (-1,))]:
    try:
        weighted_am_gm_sides(values, weights)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid contract was accepted")
```

### Verification

The code checks 100 valid pairs and three invalid inputs. The square and Jensen
arguments prove the stated forms.

### Common wrong turn

Finding the equality candidate is not enough. Verify that it satisfies the
original sum or product constraint.

## E0.10.04 Derive Cauchy-Schwarz from a quadratic

### Key idea

The squared distance from one vector to the line through another cannot be
negative.

### Reasoning

If $\boldsymbol{y}=\mathbf0$, both sides are zero. Otherwise,

$$
0\le\lVert\boldsymbol{x}-t\boldsymbol{y}\rVert_2^2
=\lVert\boldsymbol{x}\rVert_2^2
-2t\langle\boldsymbol{x},\boldsymbol{y}\rangle
+t^2\lVert\boldsymbol{y}\rVert_2^2.
$$

At

$$
t=\frac{\langle\boldsymbol{x},\boldsymbol{y}\rangle}
{\lVert\boldsymbol{y}\rVert_2^2},
$$

nonnegativity rearranges to

$$
|\langle\boldsymbol{x},\boldsymbol{y}\rangle|^2
\le\lVert\boldsymbol{x}\rVert_2^2\lVert\boldsymbol{y}\rVert_2^2.
$$

Taking nonnegative square roots proves the theorem. Equality occurs exactly when
the minimized squared norm is zero, meaning
$\boldsymbol{x}=t\boldsymbol{y}$. Together with the zero case, this is linear
dependence.

Pairing $\boldsymbol{x}$ with $\boldsymbol{1}_n$ gives

$$
\left(\sum_i x_i\right)^2\le n\sum_i x_i^2,
$$

with equality exactly when all $x_i$ are equal. Pairing with $(2,-1,3)$ gives

$$
|2x_1-x_2+3x_3|\le\sqrt{14}\lVert\boldsymbol{x}\rVert_2.
$$

For $(1,2,3)$ and $(4,-5,6)$, the left side is $|4-10+18|=12$ and the right
side is $\sqrt{14}\sqrt{77}=\sqrt{1078}$. A negative-proportional equality
example is $(1,2)$ and $(-3,-6)$.

### Verification

$144\le1078$. Cauchy-Schwarz is the $p=q=2$ case; other exponent pairs require
Hölder's conjugacy contract.

### Common wrong turn

The equality constant can be negative because the theorem bounds the magnitude
of the inner product.

## E0.10.05 Match conjugate exponents in Hölder

### Key idea

Normalize each vector in its own norm, then use Young's inequality coordinate by
coordinate.

### Reasoning

For $p=3$, conjugacy gives $1/q=2/3$, hence $q=3/2$. Weighted AM-GM with
weights $1/p,1/q$ applied to $u^p,v^q$ gives

$$
uv\le\frac{u^p}{p}+\frac{v^q}{q}.
$$

For nonzero vectors, set

$$
u_i=\frac{|x_i|}{\lVert\boldsymbol{x}\rVert_p},\qquad
v_i=\frac{|y_i|}{\lVert\boldsymbol{y}\rVert_q}.
$$

Summing Young gives $\sum_i u_iv_i\le1$, which proves Hölder after multiplying
by the norm product. A zero vector makes both sides zero.

For finite exponents and nonzero vectors, equality requires
$|x_i|^p=c|y_i|^q$ for one $c>0$ and every $i$.

In the numerical example,

$$
\sum_i|x_i y_i|=3+10+8=21
$$

and

$$
21\le73^{1/3}
\left(3^{3/2}+5^{3/2}+2^{3/2}\right)^{2/3}.
$$

For equality with $p=3,q=3/2$, take
$\boldsymbol{x}=(1,2,3)$ and $\boldsymbol{y}=(1,4,9)$ because
$|x_i|^3=|y_i|^{3/2}$.

At the endpoint,

$$
\sum_i|x_i y_i|\le\sum_i|x_i|\lVert\boldsymbol{y}\rVert_\infty
=\lVert\boldsymbol{x}\rVert_1\lVert\boldsymbol{y}\rVert_\infty.
$$

The proposal $p=q=3$ fails conjugacy because $1/3+1/3\ne1$. For
$|\sum_i x_iy_i|$, equality also requires all nonzero products to have one sign,
so the absolute-value triangle step is exact.

### Verification

Every exponent pair is conjugate and every zero case is handled before division
by a norm.

### Common wrong turn

Do not choose the second exponent by symmetry unless the first exponent is two.

## E0.10.06 Derive Minkowski and break the p contract

### Key idea

Use scalar triangle first and Hölder on the resulting product sums.

### Reasoning

For $z_i=|x_i+y_i|$,

$$
z_i^p\le(|x_i|+|y_i|)z_i^{p-1}.
$$

Summing and applying Hölder with $q=p/(p-1)$ gives

$$
\sum_i z_i^p
\le(\lVert\boldsymbol{x}\rVert_p+\lVert\boldsymbol{y}\rVert_p)
(\sum_i z_i^{(p-1)q})^{1/q}.
$$

Since $(p-1)q=p$, the last factor is
$\lVert\boldsymbol{x}+\boldsymbol{y}\rVert_p^{p-1}$. If that norm is zero,
Minkowski is immediate. Otherwise divide to obtain the theorem.

For $p=1$, sum the coordinatewise scalar triangle inequalities. For
$p=\infty$,

$$
\max_i|x_i+y_i|\le\max_i(|x_i|+|y_i|)
\le\max_i|x_i|+\max_i|y_i|.
$$

For $1<p<\infty$, equality means zero or positive proportionality. For $p=1$,
each coordinate must avoid cancellation: $x_iy_i\ge0$. For $p=\infty$, one
coordinate must attain both sup norms with matching sign.

When $p=1/2$,

$$
\lVert(1,1)\rVert_{1/2}=(1+1)^2=4,
$$

but

$$
\lVert(1,0)\rVert_{1/2}+\lVert(0,1)\rVert_{1/2}=1+1=2.
$$

Thus $4\le2$ is false. One counterexample refutes a universal claim, while any
finite collection of passing cases leaves untested inputs.

```python
from math import inf

from inequality_tools import minkowski_sides

for exponent in (1, 1.5, 2, 4, inf):
    left, right = minkowski_sides((1, -2, 3), (-4, 5, 1), exponent)
    assert left <= right + 1e-12
```

### Verification

The loop checks one vector pair at five valid exponents. The proof covers all
finite real vector pairs under the theorem's exponent contract.

### Common wrong turn

Calling the $p<1$ formula a norm quietly assumes the property the counterexample
disproves.

## E0.10.07 Choose Jensen's direction and domain

### Key idea

Convexity determines direction only after the inputs and normalized weights form
a valid convex combination inside the function's domain.

### Reasoning

For $f(x)=x^2$ on $\mathbb{R}$, the weighted input is
$(-2)/4+1/2+4/4=1$. Jensen gives

$$
1=f(1)\le\frac14f(-2)+\frac12f(1)+\frac14f(4)=\frac{11}{2}.
$$

Strictness follows because positive-weight inputs differ.

For concave $\log$ on $(0,\infty)$,

$$
\log(5/2)\ge\frac12\log1+\frac12\log4=\log2.
$$

For affine $f(x)=3x-7$, Jensen is equality for every valid input and weight set.
Logarithm is undefined at zero. Weights $2,1$ do not sum to one; normalizing
produces $2/3,1/3$ and changes $2x_1+x_2$ into $(2x_1+x_2)/3$.

For the induction proof, group the first $n-1$ weights into total $s$, normalize
inside that group, apply two-point convexity to the group mean and final point,
then apply the induction hypothesis inside the group. Zero-total endpoint groups
reduce to fewer points.

Strict convexity gives equality only when all positive-weight inputs coincide.
A merely convex function can be affine on their convex hull and also give
equality. For a domain example, $f(x)=1/x$ is convex on $(0,\infty)$ but not on
a domain crossing zero, where it is not even defined.

```python
from math import log

from inequality_tools import jensen_gap

assert jensen_gap((1, 3), (0.5, 0.5), lambda value: value**2) > 0
assert abs(jensen_gap((1, 3), (0.5, 0.5), lambda value: 3 * value + 1)) < 1e-12
assert jensen_gap((1, 4), (0.5, 0.5), log) < 0
```

### Verification

The helper evaluates selected points. It does not inspect every point on a domain
and therefore cannot prove convexity or concavity.

### Common wrong turn

Weights summing to one is not a formatting convention. It keeps the weighted
input inside the convex hull.

## E0.10.08 Build a finite log-Jensen lower bound

### Key idea

Log is concave, so Jensen reverses the convex direction.

### Reasoning

For $r_i>0$, $w_i\ge0$, and $\sum_iw_i=1$,

$$
\log\left(\sum_iw_ir_i\right)\ge\sum_iw_i\log r_i.
$$

Every positive-weight $r_i$ must be positive so its logarithm exists. Strict
concavity gives equality exactly when all positive-weight $r_i$ are equal.

For the stated values,

$$
\sum_iw_ir_i=\frac12+1+4=\frac{11}{2},
$$

while

$$
\sum_iw_i\log r_i=\frac14\log4+\frac14\log16
=\frac32\log2.
$$

Thus $\log(11/2)\ge(3/2)\log2$. Exponentiation is increasing on
$\mathbb{R}$, so

$$
\sum_iw_ir_i\ge\prod_i r_i^{w_i},
$$

which is weighted AM-GM.

If $q_i>0$, $a_i>0$, and $\sum_iq_i=1$, set $r_i=a_i/q_i$. Then

$$
\log\left(\sum_i a_i\right)
=\log\left(\sum_iq_i\frac{a_i}{q_i}\right)
\ge\sum_iq_i\log\frac{a_i}{q_i}.
$$

The substitution requires finite indexing, positive $q_i$ and $a_i$, and
normalized $q_i$. Later derivations choose adjustable weights to make a difficult
logarithm lower-bounded by a weighted sum of simpler logs. Their probabilistic
meaning and optimization belong in later modules.

The audit claim is too broad. The repaired statement is: concave Jensen moves
log across a finite convex combination of positive inputs and gives the displayed
lower bound.

### Verification

All logarithm inputs are positive and exponentiation preserves direction.

### Common wrong turn

Do not write $a_i/q_i$ when a weight can be zero. A separate limiting argument
would be required.

## E0.10.09 Measure union-bound overlap

### Key idea

The union indicator records at least one occurrence, while the sum of indicators
counts occurrences and therefore overcounts overlaps.

### Reasoning

The events are

$$
A=\{2,4,6,8,10,12\},\quad
B=\{3,6,9,12\},\quad
C=\{10,11,12\}.
$$

Their union is $\{2,3,4,6,8,9,10,11,12\}$, so its probability is $9/12=3/4$.
The marginal sum is $(6+4+3)/12=13/12$ and the capped bound is $1$.

The overlaps are $A\cap B=\{6,12\}$, $A\cap C=\{10,12\}$,
$B\cap C=\{12\}$, with triple overlap $\{12\}$. For equality, choose
$\{1\},\{2,3\},\{4,5,6\}$. If all three events are $\{1,2\}$, the true union
probability is $1/6$ while the sum is $1/2$.

Pointwise,

$$
\mathbf1_{A\cup B\cup C}\le\mathbf1_A+\mathbf1_B+\mathbf1_C.
$$

Averaging over the 12 equally weighted outcomes proves the bound. No step uses
independence.

```python
outcomes = set(range(1, 13))
events = (
    {value for value in outcomes if value % 2 == 0},
    {value for value in outcomes if value % 3 == 0},
    {value for value in outcomes if value >= 10},
)
actual = len(set().union(*events)) / len(outcomes)
bound = min(1, sum(len(event) / len(outcomes) for event in events))
assert actual == 3 / 4
assert actual <= bound == 1
```

### Verification

Marginal probabilities do not encode overlap, so `union_bound` cannot recover
the actual union probability.

### Common wrong turn

The cap at one improves reporting but does not use overlap information.

## E0.10.10 Prove Bernoulli and locate equality

### Key idea

The induction multiplies by the nonnegative quantity $1+x$ and leaves a
nonnegative remainder $nx^2$.

### Reasoning

At $n=0$, both sides equal one. Assume $(1+x)^n\ge1+nx$. Since $x\ge-1$,
$1+x\ge0$, so multiplication preserves direction:

$$
(1+x)^{n+1}\ge(1+nx)(1+x)
=1+(n+1)x+nx^2\ge1+(n+1)x.
$$

The condition $n\ge0$ makes $nx^2\ge0$ and defines the induction sequence. The
condition $x\ge-1$ licenses multiplication by $1+x$.

For $n=0$ or $n=1$, equality holds for every allowed $x$. For any $n$, $x=0$
gives equality. For $n\ge2$ and nonzero allowed $x$, the induction or factorized
difference is strict, so these are all equality cases.

Numerically,

$$
1.1^{10}=2.5937424601\ge2
$$

and

$$
(1-0.5)^4=0.0625\ge-1.
$$

Dropping the domain gives the counterexample $x=-4,n=3$:
$(-3)^3=-27<-11=1+3(-4)$. Noninteger powers need separately stated domains and
convexity directions.

The approximation claim has no error bound. Bernoulli supplies a lower bound,
not a guarantee that the linear term is close.

```python
from inequality_tools import bernoulli_sides

for exponent in range(21):
    for increment in (-1, -0.75, -0.1, 0, 0.1, 1, 5):
        left, right = bernoulli_sides(increment, exponent)
        assert left + 1e-12 >= right

for increment, exponent in [(-1.1, 2), (0.2, -1), (0.2, True)]:
    try:
        bernoulli_sides(increment, exponent)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid contract was accepted")
```

### Verification

The loop checks 147 valid pairs and three invalid inputs. Induction proves every
pair in the stated infinite domain.

### Common wrong turn

A lower bound can be numerically far from the powered expression.

## E0.10.11 Prove finite rearrangement by swaps

### Key idea

Removing an inversion changes the product sum by a product of two nonnegative
differences.

### Reasoning

For $a_i\le a_j$ and $b_r\le b_s$,

$$
(a_ib_r+a_jb_s)-(a_ib_s+a_jb_r)
=(a_j-a_i)(b_s-b_r)\ge0.
$$

Thus replacing a crossed pair with an aligned pair never decreases the sum.
Repeated adjacent inversion removal reaches sorted order, proving the maximum.
Applying the maximum result after reversing one sequence proves the minimum.

If both sequences are strictly increasing, every nontrivial inversion removal is
strict, so the extrema are unique. A tied difference makes the swap cost zero.

For $a=(-2,1,1,5)$ and $b=(-3,0,4,7)$, the maximum is

$$
(-2)(-3)+1(0)+1(4)+5(7)=45,
$$

and the minimum is

$$
(-2)(7)+1(4)+1(0)+5(-3)=-25.
$$

Swapping the $b$ values paired with the two equal entries of $a$ gives another
maximizing permutation.

```python
import itertools
from math import fsum

from inequality_tools import rearrangement_extremes

left = (-2, 1, 1, 5)
right = (-3, 0, 4, 7)
minimum, maximum = rearrangement_extremes(left, right)
products = [
    fsum(a * b for a, b in zip(left, permutation))
    for permutation in itertools.permutations(right)
]
assert (minimum, maximum) == (-25, 45)
assert minimum == min(products)
assert maximum == max(products)
```

| Feature | Finite rearrangement here | Series rearrangement in §0.09 |
|---|---|---|
| Object | two finite sequences and pairings | one infinite series and term order |
| Question | extrema of a finite product sum | convergence and value of partial sums |
| Main condition | sorted order | absolute versus conditional convergence |
| Proof mechanism | adjacent swaps | tail control or positive/negative term pools |

### Verification

Enumeration proves the extrema for these 24 indexed permutations. The swap proof
covers arbitrary finite real sequences of equal length.

### Common wrong turn

Nonnegativity is not required. Sorted order, equal finite length, and a product
sum are the controlling structure.

## E0.10.12 Select, implement, and audit an inequality

### Key idea

Select from structure only after recording the target, contract, direction, and
equality geometry. Keep proof, source evidence, and finite execution separate.

### Reasoning

A valid classification ledger can use these rows as templates:

| Target structure | Contract cue | Candidate | Equality cue |
|---|---|---|---|
| magnitude of sum | absolute value or norm | triangle | no cancellation or aligned vectors |
| product under fixed sum | nonnegative values | AM-GM | equal values |
| Euclidean inner product | two-norms | Cauchy-Schwarz | linear dependence |
| product sum with different norms | conjugate exponents | Hölder | proportional powers |
| norm of vector sum | $p\ge1$ | Minkowski | aligned vectors, endpoint details |
| function of weighted mean | convex domain and weights | Jensen | equal inputs or affine region |
| any of finitely many events | probabilities already defined | union bound | no positive-mass overlap |
| integer power of $1+x$ | $x\ge-1$, $n\ge0$ | Bernoulli | $n\in\{0,1\}$ or $x=0$ |
| extrema over finite pairings | sorted equal-length sequences | rearrangement | ties or sorted extrema |

Refusal examples include negative AM-GM inputs, $p<1$ for Minkowski, weights
not summing to one for Jensen, nonconjugate Hölder exponents, a noninteger
Bernoulli exponent, and an infinite sequence passed to finite rearrangement.

At least eight defects in the proposed audit claim are:

1. Passing tests quantify only over tested inputs.
2. Floating-point comparisons include representation error.
3. Tests can repeat the implementation's own mistake.
4. Equality conditions reveal tightness and cannot be discarded.
5. Jensen requires a convex domain containing all inputs and their mean.
6. Jensen requires nonnegative weights summing to one.
7. Jensen's direction depends on convexity versus concavity.
8. The union bound does not require independence.
9. Marginal event probabilities do not reveal overlap.
10. A theorem can be correctly implemented but selected for the wrong target
    direction.
11. Source metadata does not itself verify a theorem passage.
12. A source license and a citation answer different reuse questions.

The source report should match the module's provenance ledger: Stanford book
pages were inspected and linked PDFs were locally extracted with PDF.js after the
web extractor failed; OpenStax exposed direct HTML; MIT's resource endpoint was
blocked but its official PDF downloaded and extracted; Levin supplied induction
structure but not Bernoulli's inequality; Python docs supplied API behavior.

An evidence table should distinguish:

| Evidence | What it supports | What it does not support |
|---|---|---|
| symbolic derivation | all inputs under stated hypotheses | source priority or software behavior |
| one counterexample | falsity of one universal claim | behavior of unrelated inputs |
| finite test grid | selected implementation behavior | universal theorem |
| directly inspected theorem text | exact sourced statement | independent proof or reuse permission |
| license statement | reuse boundary | mathematical correctness |

Run the repository suite with:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v
```

Then run every added deterministic case under the same environment and remove
any cache directory created by another command.

### Verification

A complete report contains at least 20 prompt classifications, 18 accepted uses,
9 theorem refusals, 200 valid checks, 20 invalid checks, the two required
counterexamples, five evidence categories, six directly inspected source groups,
and explicit no-copy confirmation.

### Common wrong turn

Do not choose a theorem because its formula resembles the target. Choose it
because every assumption is available and its direction advances the proof.

## Solution-set check

All exercise IDs and titles mirror the [exercise index](../exercises/README.md):

- E0.10.01 Audit order-preserving operations
- E0.10.02 Prove triangle and reverse triangle bounds
- E0.10.03 Optimize with AM-GM and audit equality
- E0.10.04 Derive Cauchy-Schwarz from a quadratic
- E0.10.05 Match conjugate exponents in Hölder
- E0.10.06 Derive Minkowski and break the p contract
- E0.10.07 Choose Jensen's direction and domain
- E0.10.08 Build a finite log-Jensen lower bound
- E0.10.09 Measure union-bound overlap
- E0.10.10 Prove Bernoulli and locate equality
- E0.10.11 Prove finite rearrangement by swaps
- E0.10.12 Select, implement, and audit an inequality

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md)