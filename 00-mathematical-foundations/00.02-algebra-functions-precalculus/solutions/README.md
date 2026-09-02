# Solutions for §0.02 Algebra, Functions, and Precalculus Backfill

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Resources](../resources/README.md)

These are full worked solutions. A correct solution may choose different intermediate forms, but it must preserve domains, principal ranges, multiplicities, and numerical tolerances.

## E0.02.01 Change form without changing meaning

### Key idea

Expansion, factoring, and cancellation preserve values only where every original operation is defined.

### Reasoning

1. Distribute each term:
   $$
   (2x-5)(x+3)=2x^2+6x-5x-15=2x^2+x-15.
   $$
   The constant is $(-5)(3)=-15$, and the linear coefficient is $6-5=1$.

2. Split the middle term:
   $$
   6x^2-x-2=6x^2+3x-4x-2
   =3x(2x+1)-2(2x+1)
   =(3x-2)(2x+1).
   $$

3. Record denominator zeros first: $x^2-4=(x-2)(x+2)$ vanishes at $x=2,-2$. Then
   $$
   \frac{x^2-5x+6}{x^2-4}
   =\frac{(x-2)(x-3)}{(x-2)(x+2)}
   =\frac{x-3}{x+2},
   \qquad x\ne2,-2.
   $$

4. Factored form exposes roots and canceled factors. Expanded form exposes coefficients.

### Verification

Re-expanding $(3x-2)(2x+1)$ gives $6x^2-x-2$. At $x=0$, the original rational expression and simplified rule both equal $-3/2$. The simplified formula has a value at $x=2$, but the original does not, confirming why the restriction remains.

### Common wrong turn

Canceling the terms $x^2$ in a sum is invalid. Cancellation applies to common multiplicative factors after factoring.

## E0.02.02 Roots, holes, and asymptotes

### Key idea

Multiplicity describes local root behavior, the leading term describes polynomial ends, and factor cancellation classifies rational discontinuities.

### Reasoning

For $p(x)=-2(x+2)^2(x-1)^3$:

| Root | Multiplicity | Local behavior |
|---|---:|---|
| $-2$ | 2 | touches the axis |
| $1$ | 3 | crosses the axis |

The degree is $2+3=5$, and the leading coefficient is $-2$. Thus

$$
\lim_{x\to-\infty}p(x)=\infty,
\qquad
\lim_{x\to\infty}p(x)=-\infty.
$$

For

$$
r(x)=\frac{(x+2)(x-1)}{(x+2)(x-3)^2},
$$

the original domain is $\mathbb{R}\setminus\{-2,3\}$. On that domain,

$$
r(x)=\frac{x-1}{(x-3)^2}.
$$

The canceled factor creates a hole. Its missing output is

$$
\frac{-2-1}{(-2-3)^2}=-\frac{3}{25},
$$

so the hole is $(-2,-3/25)$. The factor $(x-3)^2$ remains, making $x=3$ a vertical asymptote. Since the numerator degree is less than the denominator degree, $y=0$ is the horizontal asymptote.

A graph should show a touch at $-2$ and a crossing at $1$ for $p$, plus the hole and asymptotes for $r$. A coarse plot may connect points across $x=3$ or fail to render the small hole marker.

### Verification

Near $x=3$, $(x-3)^2$ is positive and small while $x-1$ is positive, so $r(x)\to+\infty$ from both sides. For large $|x|$, $r(x)$ behaves like $x/x^2=1/x$, confirming the horizontal asymptote.

### Common wrong turn

Do not call both excluded inputs vertical asymptotes. Cancellation changes the local behavior at $x=-2$ but does not restore the original function's value there.

## E0.02.03 Complete the square and find the range

### Key idea

Vertex form exposes the range, and the discriminant independently checks the root count.

### Reasoning

Factor the leading coefficient from the first two terms:

$$
\begin{aligned}
f(x)
&=-3(x^2-4x)-7\\
&=-3[(x-2)^2-4]-7\\
&=-3(x-2)^2+5.
\end{aligned}
$$

The vertex is $(2,5)$, the axis is $x=2$, and the negative coefficient makes $5$ a maximum. Therefore the range is $(-\infty,5]$.

Set $f(x)=0$:

$$
-3(x-2)^2+5=0
\iff
(x-2)^2=\frac{5}{3}.
$$

Hence

$$
x=2\pm\sqrt{\frac{5}{3}}=2\pm\frac{\sqrt{15}}{3}.
$$

From the expanded form, $a=-3$, $b=12$, and $c=-7$, so

$$
\Delta=b^2-4ac=144-84=60>0.
$$

That agrees with two distinct real roots.

Replacing $-7$ by $-13$ gives

$$
-3x^2+12x-13=-3(x-2)^2-1.
$$

It is always negative, so there are no real roots. Over $\mathbb{C}$,

$$
(x-2)^2=-\frac{1}{3}
\quad\Longrightarrow\quad
x=2\pm\frac{\sqrt{3}}{3}i.
$$

### Verification

The two real roots of the original are symmetric around $x=2$. Substituting either makes $(x-2)^2=5/3$, so $f(x)=0$. For the modified quadratic, the discriminant is $144-156=-12$, and the quadratic formula gives the same conjugate pair.

### Common wrong turn

When factoring out $-3$, divide both the quadratic and linear coefficients by $-3$. Losing the sign changes the vertex and the range.

## E0.02.04 Transform a parent function

### Key idea

Map a parent point by solving the inside equation for the new input, then apply outside changes to its output.

### Reasoning

With $f(x)=|x|$,

$$
g(x)=-\frac{1}{2}f(2(x-3))+4.
$$

The graph shifts right $3$, is horizontally compressed by factor $1/2$, vertically scaled by $1/2$, reflected across the horizontal axis, and shifted up $4$. For this parent, the two scale factors cancel algebraically:

$$
g(x)=-\frac{1}{2}|2(x-3)|+4=-|x-3|+4.
$$

For a parent point $(u,f(u))$, solve $2(x-3)=u$, giving $x=u/2+3$, and transform the output to $-f(u)/2+4$.

| Parent point | New input | New output | Transformed point |
|---|---:|---:|---|
| $(-2,2)$ | $2$ | $3$ | $(2,3)$ |
| $(0,0)$ | $3$ | $4$ | $(3,4)$ |
| $(2,2)$ | $4$ | $3$ | $(4,3)$ |

The domain is $\mathbb{R}$ and the range is $(-\infty,4]$. The transformed graph is an upside-down V with vertex $(3,4)$.

The classmate's claim is reversed. The parent points at horizontal distance $2$ from the vertex become points at distance $1$, so the graph is compressed, not widened.

### Verification

Direct substitution gives $g(2)=3$, $g(3)=4$, and $g(4)=3$. These values match the landmark table and the simplified formula.

### Common wrong turn

Reading the inside factor as a vertical scale confuses inputs with outputs. Solve the inside equation instead of relying on a memorized phrase.

## E0.02.05 Compose, restrict, and invert

### Key idea

Composition domains come from the inner function plus the outer function's input constraint. An inverse branch is selected by a domain restriction.

### Reasoning

First,

$$
(f\circ g)(x)=(\sqrt{x+2}-1)^2.
$$

The square root requires $x+2\ge0$, so the domain is $[-2,\infty)$.

In the other order,

$$
(g\circ f)(x)=\sqrt{(x-1)^2+2}.
$$

The radicand is at least $2$, so the domain is all of $\mathbb{R}$. Thus $x=-3$ lies in the second domain but not the first. Every input in the first domain also lies in the second.

The function $f(x)=(x-1)^2$ is not one-to-one on $\mathbb{R}$ because, for example, $f(0)=f(2)=1$.

Restricting to the right branch gives

$$
f_+:[1,\infty)\to[0,\infty),
\qquad
f_+(x)=(x-1)^2.
$$

Solving $y=(x-1)^2$ with $x-1\ge0$ gives

$$
f_+^{-1}(y)=1+\sqrt{y}.
$$

On the left branch,

$$
f_-:(-\infty,1]\to[0,\infty)
$$

has inverse

$$
f_-^{-1}(y)=1-\sqrt{y}.
$$

### Verification

For $x\ge1$,

$$
f_+^{-1}(f_+(x))=1+\sqrt{(x-1)^2}=1+(x-1)=x.
$$

For $y\ge0$, $f_+(f_+^{-1}(y))=(\sqrt{y})^2=y$. On the left branch, $\sqrt{(x-1)^2}=|x-1|=1-x$, which similarly returns $x$ with the minus branch.

### Common wrong turn

Writing $1\pm\sqrt{y}$ as one inverse fails the function test. It gives two outputs for most positive $y$.

## E0.02.06 Decompose a rational function

### Key idea

A repeated denominator factor requires one term for each power through its multiplicity.

### Reasoning

Write

$$
\frac{2x^2+3x+5}{(x-1)^2(x+2)}
=
\frac{A}{x-1}+\frac{B}{(x-1)^2}+\frac{C}{x+2}.
$$

Clearing denominators gives

$$
2x^2+3x+5=A(x-1)(x+2)+B(x+2)+C(x-1)^2.
$$

Set $x=1$:

$$
10=3B\quad\Longrightarrow\quad B=\frac{10}{3}.
$$

Set $x=-2$:

$$
7=9C\quad\Longrightarrow\quad C=\frac{7}{9}.
$$

The $x^2$ coefficient is $A+C=2$, so $A=11/9$. Therefore

$$
\frac{2x^2+3x+5}{(x-1)^2(x+2)}
=
\frac{11}{9(x-1)}
+\frac{10}{3(x-1)^2}
+\frac{7}{9(x+2)}.
$$

The original domain excludes $x=1,-2$. Decomposition does not define either value because each remains a denominator zero. Integration becomes easier because the result separates into standard reciprocal and reciprocal-square forms.

### Verification

Recombining the numerators gives

$$
\frac{11}{9}(x^2+x-2)
+\frac{10}{3}(x+2)
+\frac{7}{9}(x^2-2x+1).
$$

Its coefficients are $2$ for $x^2$, $3$ for $x$, and $5$ for the constant, exactly matching the original numerator.

### Common wrong turn

Using only $A/(x-1)^2+C/(x+2)$ omits a necessary degree of freedom and generally cannot reproduce the numerator.

## E0.02.07 Radians and inverse trigonometry

### Key idea

Convert units first, then force inverse-trig outputs into their principal intervals.

### Reasoning

Using $180$ degrees $=\pi$ radians:

$$
150^\circ=\frac{5\pi}{6},
\qquad
-45^\circ=-\frac{\pi}{4},
\qquad
\frac{7\pi}{6}=210^\circ.
$$

The reference angle for $5\pi/6$ is $\pi/6$, and the point lies in quadrant II. Therefore

$$
\sin(5\pi/6)=\frac12,
\quad
\cos(5\pi/6)=-\frac{\sqrt3}{2},
\quad
\tan(5\pi/6)=-\frac{1}{\sqrt3}.
$$

Principal values give

$$
\arcsin(\sin(5\pi/6))=\frac{\pi}{6},
$$

$$
\arccos(\cos(5\pi/6))=\frac{5\pi}{6},
$$

$$
\arctan(\tan(5\pi/6))=-\frac{\pi}{6}.
$$

Arcsine returns a value in $[-\pi/2,\pi/2]$, arccosine in $[0,\pi]$, and arctangent in $(-\pi/2,\pi/2)$. Only the arccosine interval contains the original angle.

For an addition-identity check,

$$
\cos(\pi-\pi/6)
=\cos\pi\cos(\pi/6)+\sin\pi\sin(\pi/6)
=-\frac{\sqrt3}{2}.
$$

### Verification

Squaring and adding the sine and cosine values gives $1/4+3/4=1$. Dividing sine by cosine gives the stated tangent.

### Common wrong turn

An inverse trig function does not recover an arbitrary original angle. It returns the unique representative in its principal range.

## E0.02.08 Multiply in the complex plane

### Key idea

Rectangular form supports addition and conjugate division; polar form exposes scale and rotation.

### Reasoning

For $z=1+\sqrt3 i$,

$$
\overline{z}=1-\sqrt3 i,
\qquad
|z|=\sqrt{1+3}=2,
\qquad
z\overline{z}=4.
$$

The point $z$ has argument $\pi/3$, so $z=2e^{i\pi/3}$. The point $w=-1+i$ lies in quadrant II with modulus $\sqrt2$ and argument $3\pi/4$, so $w=\sqrt2e^{i3\pi/4}$.

Multiplication gives

$$
zw=2\sqrt2e^{i13\pi/12}=2\sqrt2e^{-i11\pi/12}.
$$

Direct rectangular multiplication gives

$$
zw=-(1+\sqrt3)+(1-\sqrt3)i.
$$

For division by conjugation,

$$
\frac{z}{w}
=\frac{(1+\sqrt3 i)(-1-i)}{(-1+i)(-1-i)}
=\frac{\sqrt3-1}{2}-\frac{1+\sqrt3}{2}i.
$$

Polar division gives

$$
\frac{z}{w}
=\sqrt2e^{i(\pi/3-3\pi/4)}
=\sqrt2e^{-i5\pi/12},
$$

which converts to the same rectangular components.

Multiplication by $z$ scales every modulus by $2$ and rotates every argument by $\pi/3$ modulo $2\pi$.

### Verification

The product modulus should be $2\sqrt2$. Squaring the rectangular components' magnitudes produces $8$. The quotient modulus should be $2/\sqrt2=\sqrt2$, which also follows from its rectangular components.

### Common wrong turn

Using $\arctan(b/a)$ without checking the quadrant gives the wrong argument for $w$ because its real part is negative.

## E0.02.09 Investigate roots of unity

### Key idea

All representations of $1$ have arguments $2\pi m$; dividing those arguments by six produces every sixth root.

### Reasoning

Write $z=re^{i\theta}$. From $z^6=1=e^{i2\pi m}$, we get $r^6=1$, so $r=1$, and

$$
6\theta=2\pi m
\quad\Longrightarrow\quad
\theta=\frac{2\pi m}{6}.
$$

Distinct values modulo $2\pi$ occur for $m=0,1,\ldots,5$:

$$
1,
e^{i\pi/3},
e^{i2\pi/3},
e^{i\pi},
e^{i4\pi/3},
e^{i5\pi/3}.
$$

In rectangular form they are

$$
1,
\frac12+\frac{\sqrt3}{2}i,
-\frac12+\frac{\sqrt3}{2}i,
-1,
-\frac12-\frac{\sqrt3}{2}i,
\frac12-\frac{\sqrt3}{2}i.
$$

Let $\omega=e^{i\pi/3}$. Then $\omega^6=e^{i2\pi}=1$. Multiplying $\omega^k$ by $\omega$ gives $\omega^{k+1}$, with exponents interpreted modulo $6$, so multiplication permutes the set.

For the sum,

$$
1+\omega+\cdots+\omega^5
=\frac{1-\omega^6}{1-\omega}=0.
$$

The denominator is nonzero because $\omega\ne1$.

A precise Fourier connection is: entries of the discrete Fourier transform matrix are integer powers of a primitive root of unity, so their algebra organizes sampled oscillations.

### Verification

Conjugate pairs in the rectangular list cancel their imaginary parts; opposite points cancel entirely. The explicit sum is therefore also zero geometrically.

### Common wrong turn

Taking only the principal argument of $1$ gives $\theta=0$ and misses five roots. Use all coterminal arguments $2\pi m$ before dividing.

## E0.02.10 Compare tanh and sigmoid

### Key idea

Positive exponentials establish the ranges, and direct algebra establishes the exact rescaling relation.

### Reasoning

Because $e^{-x}>0$, the sigmoid denominator is greater than $1$, so $0<s(x)<1$. For tanh, let $u=e^x>0$:

$$
h(x)=\frac{u-u^{-1}}{u+u^{-1}}=\frac{u^2-1}{u^2+1}.
$$

Since $|u^2-1|<u^2+1$, we have $-1<h(x)<1$.

Now

$$
\begin{aligned}
\frac{1+h(x/2)}{2}
&=\frac12\left(1+\frac{e^{x/2}-e^{-x/2}}{e^{x/2}+e^{-x/2}}\right)\\
&=\frac{e^{x/2}}{e^{x/2}+e^{-x/2}}\\
&=\frac{1}{1+e^{-x}}=s(x).
\end{aligned}
$$

The limits are

| Limit | $s(x)$ | $h(x)$ |
|---|---:|---:|
| $x\to\infty$ | $1$ | $1$ |
| $x\to-\infty$ | $0$ | $-1$ |

Also, $s(0)=1/2$ and $h(0)=0$, the centers of their respective ranges.

Solving $p=s(x)$ gives

$$
x=\log\frac{p}{1-p},
\qquad 0<p<1.
$$

A three-decimal table is

| $x$ | $s(x)$ | $h(x)$ |
|---:|---:|---:|
| $-4$ | 0.018 | -0.999 |
| $-2$ | 0.119 | -0.964 |
| $0$ | 0.500 | 0.000 |
| $2$ | 0.881 | 0.964 |
| $4$ | 0.982 | 0.999 |

Both flatten near their range boundaries. The algebraic rescaling identity is exact, but the raw outputs have different ranges and centers. In models, parameterization, downstream interpretation, and derivative scaling can therefore differ even when one function can be transformed into the other.

### Verification

Substituting $p=1/2$ into the logit gives $\log1=0$, which inverts $s(0)=1/2$. The table respects all proved ranges and the symmetry $h(-x)=-h(x)$.

### Common wrong turn

A limiting value is not necessarily attained. Neither function reaches its open range boundary at a finite real input.

## E0.02.11 Build a transformation laboratory

### Key idea

Turn each transformation claim into an assertion about hand-computed landmarks before interpreting a plot.

### Reasoning

This standard-library implementation evaluates the transformation and prints a sample table:

```python
from math import isclose, sin


def transform(function, x, *, a=1.0, b=1.0, h=0.0, k=0.0):
    return a * function(b * (x - h)) + k


def square(x):
    return x * x


assert isclose(transform(square, 0.0), 0.0)
assert isclose(transform(square, 2.0, h=2.0), 0.0)
assert isclose(transform(square, 3.0, a=-2.0, h=2.0, k=5.0), 3.0)

inputs = [-2.0, -1.0, 0.0, 1.0, 2.0]
cases = {
    "parent": {},
    "right 1": {"h": 1.0},
    "up 2": {"k": 2.0},
    "reflect": {"a": -1.0},
    "compress": {"b": 2.0},
}

for name, parameters in cases.items():
    outputs = [transform(square, x, **parameters) for x in inputs]
    print(name, list(zip(inputs, outputs)))

for x in inputs:
    parent_value = transform(square, x)
    assert isclose(transform(square, x, k=2.0), parent_value + 2.0)
    assert isclose(transform(square, x, a=-1.0), -parent_value)

assert isclose(transform(square, 1.5, b=2.0), square(3.0))
assert isclose(transform(sin, 0.0, h=2.0), sin(-2.0))
```

The square's vertex moves from $(0,0)$ to $(1,0)$ when $h=1$. The points where the parent reaches height $1$ are one unit from the vertex. With $b=2$, corresponding points are half a unit from the vertex, confirming horizontal compression.

For sine, shifting by a full period can make two sampled graphs coincide. Sparse samples can also miss peaks. For tanh, large inputs may all look nearly equal because the output is saturated. Those observations limit what a plot alone can establish.

### Verification

The first three assertions match hand calculations. The loop verifies the vertical shift and reflection at every sampled input. The landmark check for $b=2$ directly tests the inside-input rule.

### Common wrong turn

A visually similar plot is not a proof, especially with periodic functions or a poorly chosen window. Preserve parameters, landmark assertions, and sample values.

### Alternate route

A NumPy implementation can vectorize the same scalar formula, and a plotting library can draw solid, dashed, and dotted lines. The mathematical test should remain independent of pixel appearance.

## E0.02.12 Critique a chain of misconceptions

### Key idea

Separate algebraic facts, domain conditions, notation conventions, and historical claims before correcting them.

### Reasoning

| Claim | Diagnosis | Repair |
|---|---|---|
| The rational expressions have the same domain | cancellation hid $x=1$ | the original excludes $1$ and has a hole |
| Every cubic has three distinct real roots | FTA counts complex roots with multiplicity | a cubic has three complex roots counted with multiplicity |
| $f(x-2)$ shifts left | horizontal direction is reversed | it shifts recognizable features right by $2$ |
| squaring has an inverse on $\mathbb{R}$ | squaring is not one-to-one | restrict to a branch before inverting |
| $\sqrt{x^2}=x$ for all real $x$ | principal square root is nonnegative | $\sqrt{x^2}=\lvert x\rvert$ |
| angles have no units | numeric inputs require a convention | standard mathematical software uses radians unless documented otherwise |
| $\sin(90)=1$ in ordinary software | $90$ is read as radians | $\sin(\pi/2)=1$, or convert degrees explicitly |
| arcsine always undoes sine | arcsine returns a principal value | $\arcsin(\sin(3\pi/4))=\pi/4$ |
| hyperbolic functions describe circles | their core identity has a minus sign | $\cosh^2x-\sinh^2x=1$ describes a hyperbola branch |
| tanh reaches $1$ | $1$ is a limit, not a finite output | $\tanh x<1$ for finite real $x$ |
| Descartes invented $i$ | unsupported single-person attribution | use a sourced, distributed history of complex notation |
| every complex number has one argument | arguments repeat by full turns | if $\theta$ is an argument, so is $\theta+2\pi k$ |
| multiplying by $i$ is a reflection | multiplication adds $\pi/2$ | it rotates counterclockwise by a quarter-turn |

Counterexamples include:

- $(x^2-1)/(x-1)$ is undefined at $x=1$, while $x+1$ is defined there.
- $x^3+1=(x+1)(x^2-x+1)$ has only one real root.
- If $f(x)=x^2$, the vertex of $f(x-2)$ is at $x=2$.
- For $x=-3$, $\sqrt{x^2}=3\ne-3$.
- $3\pi/4$ lies outside arcsine's principal range.
- The complex number $1$ has arguments $2\pi k$ for every integer $k$.

A corrected paragraph under 180 words is:

> Canceling $(x-1)$ shows that $(x^2-1)/(x-1)$ agrees with $x+1$ only when $x\ne1$; the original has a hole. The fundamental theorem of algebra counts complex roots with multiplicity, so a cubic need not have three distinct real roots. The graph of $f(x-2)$ shifts right. Squaring becomes invertible only after a domain restriction, and $\sqrt{x^2}=|x|$. Trigonometric software normally expects radians, and inverse trig functions return principal values. Hyperbolic functions satisfy $\cosh^2x-\sinh^2x=1$, while $\tanh x$ approaches but never reaches $1$ at finite real inputs. Complex notation developed across many contributors, so a single-person invention claim needs strong historical evidence. A nonzero complex number has arguments differing by $2\pi k$, and multiplication by $i$ rotates the plane counterclockwise by $\pi/2$.

The domain, root, shift, square-root, inverse-trig, hyperbolic, and rotation corrections are mathematical facts. Radian input is a software convention that documentation must confirm. The invention claim is historical and requires a reliable source such as the module's [FTA history reference](../README.md#references).

### Verification

Every correction has either a counterexample, a declared range or domain, or a defining identity. The rewritten paragraph contains no unsupported priority claim.

### Common wrong turn

Correcting only the numerical examples leaves the structural errors intact. State the general domain, range, multiplicity, or convention that explains each example.

## Solution-set check

All exercise IDs and titles mirror the [exercise index](../exercises/README.md):

- E0.02.01 Change form without changing meaning
- E0.02.02 Roots, holes, and asymptotes
- E0.02.03 Complete the square and find the range
- E0.02.04 Transform a parent function
- E0.02.05 Compose, restrict, and invert
- E0.02.06 Decompose a rational function
- E0.02.07 Radians and inverse trigonometry
- E0.02.08 Multiply in the complex plane
- E0.02.09 Investigate roots of unity
- E0.02.10 Compare tanh and sigmoid
- E0.02.11 Build a transformation laboratory
- E0.02.12 Critique a chain of misconceptions

[Back to module](../README.md) | [Exercise set](../exercises/README.md)
