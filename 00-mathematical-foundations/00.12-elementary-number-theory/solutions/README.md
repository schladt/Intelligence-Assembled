# Solutions for §0.12 Elementary Number Theory

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

These are full worked solutions. Equivalent arguments are valid when they state
the same domains, normalizations, theorem conditions, and evidence limits. Run
Python excerpts from the module's `code/` directory.

## E0.12.01 Audit divisibility, signs, and zero

### Key idea

Use the integer multiplier definition before relying on intuition about division.

### Reasoning

$6\mid-42$ because $-42=6(-7)$, and $-6\mid42$ because $42=(-6)(-7)$.
$7\mid0$ because $0=7(0)$. Also $0\mid0$ because $0=0k$ for every integer
$k$. But $0\nmid7$ because $0k$ is never $7$. Finally $1\mid n$ because
$n=1\cdot n$.

If $b=ak$, then $b=(-a)(-k)$, so $a\mid b$ implies $-a\mid b$. Applying the
same argument to $-a$ proves the reverse direction.

For division, $-37=(-5)8+3$, and $0\le3<8$. Uniqueness follows from the
division algorithm. Divisor zero cannot give a bounded remainder interval
$0\le r<0$, and $a=0q+r$ cannot determine a unique quotient.

The audited claim is false when $b=0$: $7\mid0$ but $7\nleq0$. A repair is:
if $a\mid b$ and $b\ne0$, then $a\ne0$ and $|a|\le|b|$.

### Verification

Each true divisibility statement has an explicit integer witness; each false
one shows why no witness exists.

### Common wrong turn

Do not declare $0\nmid0$ by importing a rule against division by zero. The
divisibility relation is defined by multiplication.

## E0.12.02 Recover arithmetic from prime exponents

### Key idea

Gcd takes minimum exponents, lcm takes maximum exponents, and sign is separate.

### Reasoning

$$
\gcd(a,b)=2^2 3^2=36,
$$

$$
\operatorname{lcm}(a,b)=2^4 3^5 5\cdot7=136080.
$$

Their product is $36\cdot136080=4,898,880=|ab|$. The positive divisor count
of $|a|=2^4 3^2 7$ is $(4+1)(2+1)(1+1)=30$.

The fundamental theorem states that every integer $n\ge2$ is a product of
primes, uniquely up to factor order. A negative integer is $-1$ times the prime
factorization of its absolute value. Zero cannot be a finite prime product
because every such product is nonzero.

For Euclid's lemma on $a_1\cdots a_k$, use induction. The case $k=2$ is the
lemma. If $p\mid(a_1\cdots a_{k-1})a_k$, then either $p\mid a_k$ or
$p\mid a_1\cdots a_{k-1}$; apply the inductive hypothesis in the latter case.

### Verification

Minimum plus maximum equals the sum of the two exponents prime by prime, which
proves the product identity in this example and generally for nonzero inputs.

### Common wrong turn

Do not put $-1$ or $1$ into the list of primes.

## E0.12.03 Trace Euclid's invariant

### Key idea

Each division preserves the complete set of common divisors and decreases the
remainder.

### Reasoning

$$
1071=2(462)+147,
$$

$$
462=3(147)+21,
$$

$$
147=7(21)+0.
$$

Thus the gcd is $21$. If $d\mid a$ and $d\mid b$, then
$d\mid(a-bq)=r$. Conversely, if $d\mid b$ and $d\mid r$, then
$d\mid(bq+r)=a$. The common-divisor sets are equal.

Every nonterminal remainder satisfies $0\le r<b$. Positive divisors therefore
form a strictly decreasing sequence of nonnegative integers, which must reach
zero.

```python
import math
from number_theory import gcd, gcd_trace

common, steps = gcd_trace(1071, 462)
assert common == 21
assert steps == ((1071, 462, 2, 147), (462, 147, 3, 21), (147, 21, 7, 0))

for left, right in ((1071, 462), (-1071, 462), (1071, -462),
                    (-1071, -462), (0, 0), (19, 0), (0, -19)):
    assert gcd(left, right) == math.gcd(left, right)
```

### Verification

Every row satisfies dividend = quotient times divisor + remainder and the
remainder bound. `math.gcd` independently confirms the normalized final value.

### Common wrong turn

Comparing with `math.gcd` tests results; it does not prove the invariant or
termination.

## E0.12.04 Produce Bézout coefficients and inverses

### Key idea

Back-substitution turns the final gcd into a linear combination, and gcd one
turns that combination into an inverse.

### Reasoning

From the trace,

$$
21=462-3(147)=462-3(1071-2(462))=7(462)-3(1071).
$$

Thus $(x,y)=(-3,7)$. For $17$ and $43$,

$$
43=2(17)+9,
\quad17=1(9)+8,
\quad9=1(8)+1,
$$

so $1=2(43)-5(17)$. Therefore $17^{-1}\equiv-5\equiv38\pmod{43}$.

If $\gcd(a,n)=1$, Bézout gives $ax+ny=1$, so $ax\equiv1\pmod n$.
If $ax\equiv1\pmod n$, then $ax-kn=1$ for some $k$, so every common divisor
of $a,n$ divides $1$ and the gcd is $1$. If $(x_0,y_0)$ is one coefficient
pair, adding $(kn/g,-ka/g)$ gives infinitely many others.

$14$ has no inverse modulo $35$ because $\gcd(14,35)=7\ne1$.

```python
from number_theory import extended_gcd, modular_inverse

assert extended_gcd(1071, 462) == (21, -3, 7)
assert modular_inverse(17, 43) == 38 == pow(17, -1, 43)
```

### Verification

$17\cdot38=646=15(43)+1$.

### Common wrong turn

Do not reduce a Bézout coefficient modulo the wrong modulus.

## E0.12.05 Reason with classes and legal cancellation

### Key idea

Congruence is equality of classes, and cancellation requires an invertible
factor or a weakened modulus.

### Reasoning

Reflexivity follows from $n\mid a-a=0$. Symmetry follows because
$n\mid(a-b)$ implies $n\mid-(a-b)=b-a$. Transitivity follows by adding
multiples: if $n\mid(a-b)$ and $n\mid(b-c)$, then $n\mid(a-c)$.

$$
[3]_5=\{3+5k:k\in\mathbb{Z}\},
$$

with representatives $-7,-2,3,8,13$. If $a\equiv a'$ and $b\equiv b'$,
then $n$ divides $(a+b)-(a'+b')$. It also divides
$ab-a'b'=a(b-b')+b'(a-a')$. Therefore class addition and multiplication do
not depend on representatives.

$7^{-1}\equiv13\pmod{15}$, so $x\equiv13(4)\equiv7\pmod{15}$.
For $6x\equiv9\pmod{15}$, divide coefficient, right side, and modulus by
$3$: $2x\equiv3\pmod5$, hence $x\equiv4\pmod5$. The classes modulo $15$
are $x\equiv4,9,14$.

Unrestricted cancellation fails because $2(1)\equiv2(4)\pmod6$ but
$1\not\equiv4\pmod6$. The remainder statement is safe when the modulus is
positive and canonical remainders are fixed. The definition
$n\mid(a-b)$ is convention-independent.

### Verification

Substitution gives $7(7)=49\equiv4\pmod{15}$ and
$6(4),6(9),6(14)\equiv9\pmod{15}$.

### Common wrong turn

Do not divide a congruence as if every nonzero class were a unit.

## E0.12.06 Construct a coprime CRT solution

### Key idea

Build selectors that are one in one modulus and zero in the others.

### Reasoning

$N=4\cdot5\cdot7=140$. The partial products are $35,28,20$. Their required
inverses are

$$
35^{-1}\equiv3\pmod4,
\quad28^{-1}\equiv2\pmod5,
\quad20^{-1}\equiv6\pmod7.
$$

Thus

$$
x\equiv1(35)(3)+4(28)(2)+6(20)(6)=1049\equiv69\pmod{140}.
$$

Indeed $69\bmod4=1$, $69\bmod5=4$, and $69\bmod7=6$.
If $x,y$ satisfy all three congruences, each pairwise-coprime modulus divides
$x-y$, so their product $140$ divides $x-y$. This proves uniqueness modulo
$140$.

```python
from number_theory import chinese_remainder

assert chinese_remainder(((1, 4), (4, 5), (6, 7))) == (69, 140)
```

Having overall gcd one is weaker than pairwise coprimality: $6,10,15$ have
collective gcd one, but every pair shares a factor.

### Verification

Both the selector sum and direct substitution produce the same normalized class.

### Common wrong turn

Do not replace pairwise coprimality with $\gcd(n_1,n_2,n_3)=1$.

## E0.12.07 Diagnose general CRT compatibility

### Key idea

The shared gcd is exactly the overlap on which two residue views must agree.

### Reasoning

If $x=a+um=b+vn$, then $b-a=um-vn$, so $g=\gcd(m,n)$ divides $b-a$.
Conversely, if $g\mid(b-a)$, divide
$mk\equiv b-a\pmod n$ by $g$. Since $m/g$ and $n/g$ are coprime,
$m/g$ has an inverse modulo $n/g$, which gives $k$ and hence $x=a+mk$.

For $x\equiv4\pmod6$ and $x\equiv10\pmod{15}$, the residues agree modulo
$3$. Values $4,10,16,22,28,34$ modulo $6$ show $x=10$ works, so
$x\equiv10\pmod{30}$. The system $3\pmod6$ and $4\pmod{15}$ is impossible
because $3\not\equiv4\pmod3$.

Adding $x\equiv1\pmod7$, merge $x=10+30k$. Then
$10+30k\equiv3+2k\equiv1\pmod7$, so $2k\equiv5$, $k\equiv6$, and
$x\equiv190\pmod{210}$.

```python
from number_theory import chinese_remainder

assert chinese_remainder(((4, 6), (10, 15))) == (10, 30)
assert chinese_remainder(((4, 6), (10, 15), (1, 7))) == (190, 210)
try:
    chinese_remainder(((3, 6), (4, 15)))
except ValueError:
    pass
else:
    raise AssertionError("incompatible system must be refused")
```

### Verification

$190$ has residues $4,10,1$ in moduli $6,15,7$.

### Common wrong turn

Noncoprime does not mean impossible. It means compatibility must be checked.

## E0.12.08 Distinguish rings, units, and prime fields

### Key idea

Units are exactly coprime classes. Prime moduli make every nonzero class a unit.

### Reasoning

The units modulo $12$ are $1,5,7,11$, and each is self-inverse. The nonzero
multiplication table modulo $5$ is

| $\times$ | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| 1 | 1 | 2 | 3 | 4 |
| 2 | 2 | 4 | 1 | 3 |
| 3 | 3 | 1 | 4 | 2 |
| 4 | 4 | 3 | 2 | 1 |

If $p$ is prime and $[a]_p\ne[0]_p$, then $p\nmid a$, so
$\gcd(a,p)=1$ and Bézout supplies an inverse. If $n=ab$ is composite with
$1<a,b<n$, then $[a]_n,[b]_n$ are nonzero but their product is zero. A field
cannot contain nonzero zero divisors. Therefore the quotient is a field exactly
for prime modulus.

In $\mathbb{F}_7$, $3^{-1}=5$, so $4/3=4(5)=20\equiv6$.

```python
from number_theory import fp_divide, fp_inverse

assert fp_divide(4, 3, 7) == 6
for value, modulus in ((0, 7), (3, 8)):
    try:
        fp_inverse(value, modulus)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid field division must be refused")
```

### Verification

Every nonzero row of the $\mathbb{F}_5$ table contains $1$ exactly once.

### Common wrong turn

Do not call $\mathbb{Z}/n\mathbb{Z}$ a field merely because addition and
multiplication are defined.

## E0.12.09 Count units and apply Euler's theorem

### Key idea

Phi counts classes not divisible by any prime factor, and Euler reduces powers
only for units.

### Reasoning

Among $0,\ldots,p^e-1$, exactly the $p^{e-1}$ multiples of $p$ are nonunits.
Thus $\varphi(p^e)=p^e-p^{e-1}$. For coprime $m,n$, CRT bijects classes
modulo $mn$ with pairs modulo $m,n$, and a class is a unit exactly when both
coordinates are units. Counting gives multiplicativity.

$360=2^3 3^2 5$, so

$$
\varphi(360)=360(1-1/2)(1-1/3)(1-1/5)=96.
$$

$\varphi(40)=16$ and $222\equiv14\pmod{16}$, so

$$
7^{222}\equiv7^{14}\equiv9\pmod{40}.
$$

Euler cannot be invoked for base $10$ because $\gcd(10,40)=10$. Directly,
$10^2=100\equiv20\pmod{40}$ and multiplying by $10$ preserves residue $0$
for exponents at least $3$, so $10^{222}\equiv0$.

```python
from number_theory import modular_power, phi

assert phi(360) == 96
assert modular_power(7, 222, 40) == 9
assert modular_power(10, 222, 40) == 0
```

### Verification

Built-in `pow(7, 222, 40)` and `pow(10, 222, 40)` return $9$ and $0$.

### Common wrong turn

Do not reduce exponents modulo $\varphi(n)$ when the base is not a unit.

## E0.12.10 Separate Fermat evidence from primality proof

### Key idea

Fermat gives a necessary property of primes, not a sufficient test result for
one or many bases.

### Reasoning

If $p$ is prime and $p\nmid a$, then $a^{p-1}\equiv1\pmod p$. For every
integer $a$, $a^p\equiv a\pmod p$. The second includes $p\mid a$, where both
sides are zero; otherwise it follows by multiplying the first by $a$.

Multiplication by nonzero $a$ permutes $1,\ldots,p-1$. Their products satisfy

$$
a^{p-1}(p-1)!\equiv(p-1)!\pmod p.
$$

The factorial is nonzero modulo $p$ and can be cancelled, proving the theorem.

For $n=15$, base $2$ exposes compositeness because $2^{14}\equiv4\not\equiv1$.
Yet

```python
from number_theory import modular_power

assert modular_power(2, 14, 15) == 4
assert modular_power(2, 560, 561) == 1
assert modular_power(3, 560, 561) != 1
```

$561$ is composite, so the base-$2$ pass proves no converse. Base $3$ shares a
factor with $561$, so the unit-form theorem does not apply and the result need
not be one.

### Verification

$561=3\cdot11\cdot17$ is an explicit nontrivial factorization.

### Common wrong turn

Do not call a probable-prime check a proof without a theorem that supplies a
valid converse under stated conditions.

## E0.12.11 Audit the implementation contracts

### Key idea

Exhaustive bounded comparisons are strong implementation evidence with an
explicit finite boundary.

### Reasoning

One compact test is:

```python
import math

from number_theory import chinese_remainder, extended_gcd, gcd
from number_theory import modular_inverse, modular_power

for a in range(-30, 31):
    for b in range(-30, 31):
        result = extended_gcd(a, b)
        assert gcd(a, b) == math.gcd(a, b) == result.gcd
        assert a * result.x + b * result.y == result.gcd

for base in range(-10, 11):
    for exponent in range(13):
        for modulus in range(2, 21):
            assert modular_power(base, exponent, modulus) == pow(base, exponent, modulus)

for modulus in range(2, 26):
    for value in range(modulus):
        if math.gcd(value, modulus) == 1:
            assert modular_inverse(value, modulus) == pow(value, -1, modulus)
        else:
            try:
                modular_inverse(value, modulus)
            except ValueError:
                pass
            else:
                raise AssertionError("nonunit accepted")

for left_modulus in range(2, 11):
    for right_modulus in range(2, 11):
        period = math.lcm(left_modulus, right_modulus)
        for left in range(left_modulus):
            for right in range(right_modulus):
                brute = [x for x in range(period)
                         if x % left_modulus == left and x % right_modulus == right]
                try:
                    result = chinese_remainder(((left, left_modulus),
                                                (right, right_modulus)))
                except ValueError:
                    assert not brute
                else:
                    assert brute == [result.residue]
                    assert result.modulus == period
```

### Verification

The ranges are finite and complete as stated. Reference functions are used only
after the from-scratch implementations exist.

### Common wrong turn

Even millions of finite cases do not quantify over all integers. Proof supplies
the universal conclusion.

## E0.12.12 Prove and delimit textbook RSA

### Key idea

Correctness is prime-by-prime arithmetic plus CRT. Security is a separate
scheme-level claim that the toy code does not make.

### Reasoning

$n=11\cdot17=187$ and $\varphi(n)=10\cdot16=160$. Extended Euclid gives
$7^{-1}\equiv23\pmod{160}$, so $d=23$ and $ed=161=1+160$.

The teaching key requires distinct primes $p,q$, $n=pq$,
$1<e<\varphi(n)$, $\gcd(e,\varphi(n))=1$, and
$ed\equiv1\pmod{\varphi(n)}$. Representatives satisfy $0\le m<n$.

For $m=42$, $c=42^7\bmod187=15$ and $15^{23}\bmod187=42$. The same process
returns $0,11,17,22$ for those four messages. The latter three are not all
units modulo $187$.

For any $m$, modulo $p$ there are two cases. If $p\mid m$, then
$m^{ed}\equiv0\equiv m$. Otherwise, since $ed=1+k_p(p-1)$,

$$
m^{ed}=m(m^{p-1})^{k_p}\equiv m.
$$

Repeat modulo $q$. Therefore $m^{ed}$ and $m$ agree modulo both coprime primes,
so CRT uniqueness gives agreement modulo $pq$. Euler modulo $n$ alone covers
only $\gcd(m,n)=1$ and misses nonzero multiples of $p$ or $q$.

```python
from number_theory import make_toy_rsa_key, toy_rsa_decrypt, toy_rsa_encrypt

key = make_toy_rsa_key(11, 17, 7)
assert (key.n, key.phi, key.d) == (187, 160, 23)
assert toy_rsa_encrypt(42, key) == 15
for message in range(key.n):
    assert toy_rsa_decrypt(toy_rsa_encrypt(message, key), key) == message
```

Absent security responsibilities include secure prime generation and testing,
approved key sizes, entropy handling, OAEP or PSS encoding, message-to-integer
conversion, private-key storage, key validation, constant-time operations,
blinding, fault resistance, protocol binding, and uniform error handling.

Raw RSA exponentiation is a deterministic mathematical primitive.
RSAES-OAEP combines the encryption/decryption primitive with randomized
encoding for an encryption scheme. RSASSA-PSS combines signing/verification
primitives with probabilistic encoding for a signature scheme. The toy code
implements none of those secure schemes.

### Verification

Exhaustive testing covers all $187$ representatives for this one tiny key. The
symbolic two-case proof covers every valid two-prime teaching key.

### Common wrong turn

Do not report round-trip correctness, large integers, or a public/private
exponent pair as evidence that raw RSA is secure.

[Back to module](../README.md) | [Exercise set](../exercises/README.md)