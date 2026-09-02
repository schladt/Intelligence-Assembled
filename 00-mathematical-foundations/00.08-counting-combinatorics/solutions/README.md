# Solutions for §0.08 Counting and Combinatorics

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

These are full worked solutions. Equivalent models and proofs are valid when they preserve the declared outcomes, equality relation, and evidence boundary.

## E0.08.01 Specify the outcome before counting

### Key idea

Order and replacement define four different carriers.

### Reasoning

With three draws from five labels:

| Model | One outcome | Count |
|---|---|---:|
| ordered, replacement | tuple $(a_1,a_2,a_3)\in[5]^3$ | $5^3=125$ |
| ordered, no replacement | injective tuple | $(5)_3=60$ |
| unordered, replacement | multiplicities summing to three | $\binom73=35$ |
| unordered, no replacement | three-element subset | $\binom53=10$ |

`(A,C,E)` and `(E,C,A)` merge when order is forgotten. `(A,A,C)` disappears when repetition is forbidden.

If three physical balls carry label `A`, physical outcomes distinguish those balls unless the equality rule forgets identity. Visible-label outcomes merge them. The statement "drawing means choosing" is incomplete. It becomes correct only after adding "three distinct labels, without replacement, with order ignored."

### Verification

The four counts match the rows and columns of the sampling table.

### Common wrong turn

Do not use braces for an ordered sample. Set notation silently removes both order and duplicate occurrences.

## E0.08.02 Apply and audit the four counting rules

### Key idea

Every arithmetic operation must correspond to a partition, sequence of choices, bijection, or uniform fiber.

### Reasoning

Exactly one one gives $\binom51=5$ strings; exactly four ones gives $\binom54=5$. The Hamming-weight classes are disjoint, so the total is $10$.

For ternary strings, choose the first symbol in $3$ ways. Each later symbol has exactly $2$ choices different from its predecessor, giving

$$
3\cdot2^4=48.
$$

Map subset $S\subseteq[n]$ to indicator string $(b_1,\ldots,b_n)$ where $b_i=1$ iff $i\in S$. Reading the one positions is the inverse, so this is a bijection with $\{0,1\}^n$. Hence $|\mathcal P([n])|=2^n$.

The forget-order map sends an injective triple to its underlying set. Every three-subset has $3!=6$ orders, so

$$
|B|=\frac{(7)_3}{3!}=\frac{210}{6}=35.
$$

For a nonuniform example, map $f:\{1,2,3\}\to\{0,1\}$ by $f(1)=0$ and $f(2)=f(3)=1$. Fiber sizes are one and two, so no single divisor recovers $|\{0,1\}|$ from three.

### Verification

The binary-string cases total ten distinct strings, and $35=\binom73$.

### Common wrong turn

Surjectivity alone does not justify division. Uniform fiber size is essential.

## E0.08.03 Build the sampling model matrix

### Key idea

Ordered choices are tuples; unordered choices are subsets or multiplicity vectors.

### Reasoning

The formulas are $n^k$, $(n)_k$, $\binom{n+k-1}{k}$, and $\binom nk$ in the usual table. Zero draws have one empty outcome. From an empty population, every positive draw count is zero. Without replacement, $k>n$ gives zero.

For $n=4,k=2$, the counts are $16,12,10,6$. A direct audit is:

```python
from itertools import combinations, combinations_with_replacement, permutations, product

pool = "ABCD"
assert len(tuple(product(pool, repeat=2))) == 16
assert len(tuple(permutations(pool, 2))) == 12
assert len(tuple(combinations_with_replacement(pool, 2))) == 10
assert len(tuple(combinations(pool, 2))) == 6
assert list(combinations("AAB", 2)) == [("A", "A"), ("A", "B"), ("A", "B")]
```

The duplicate visible pair occurs because positions zero and one are distinct input elements. None of these counts supplies outcome weights, so none by itself defines a probability model.

### Verification

The iterators exhaust each fixed finite carrier and agree with the formulas.

### Common wrong turn

Do not interpret `itertools` value equality as its selection identity. The combinatoric iterators select positions.

## E0.08.04 Count permutations, combinations, and multisets

### Key idea

Factorial denominators remove labeled arrangements that collapse to one visible object.

### Reasoning

The requested counts are

$$
(9)_4=9\cdot8\cdot7\cdot6=3024,
$$

$$
\binom{14}{6}=3003,
$$

and

$$
\binom{9}{4,3,2}=\frac{9!}{4!3!2!}=1260.
$$

Labeling identical copies gives $9!$ orders. Every visible word has $4!3!2!$ labeled preimages. Alternatively choose four positions, then three of the remaining five; the last two are forced:

$$
\binom94\binom53\binom22=1260.
$$

For the identity, both sides count length-$n$ words over $m$ symbols. The right side chooses one of $m$ symbols at each position. The left partitions words by multiplicity vector.

```python
from itertools import product
from math import comb, factorial

assert factorial(9) // (factorial(4) * factorial(3) * factorial(2)) == 1260
for n in range(8):
    counts = {}
    for word in product(range(3), repeat=n):
        key = tuple(word.count(symbol) for symbol in range(3))
        counts[key] = counts.get(key, 0) + 1
    assert sum(counts.values()) == 3 ** n
```

### Verification

Both multinomial derivations agree, and finite word partitions sum to $3^n$.

### Common wrong turn

Divide only for copies that become indistinguishable under the declared visible-word equality.

## E0.08.05 Derive binomial and multinomial expansions

### Key idea

Exponents record how many labeled factors supplied each term.

### Reasoning

Choosing $k$ of $n$ factors to supply $b$ gives

$$
(a+b)^n=\sum_{k=0}^n\binom nka^{n-k}b^k.
$$

In $(2+x)^5$, the $x^3$ coefficient is $\binom{5}{3}2^{2}=10\cdot4=40$.

Setting $(a,b)=(1,1)$ gives $\sum_k\binom nk=2^n$, which also counts all subsets by size. Setting $(1,-1)$ gives zero for $n\ge1$.

Assigning each of $n$ factors to one of $m$ variables gives the multinomial theorem. For $x^2y^3z$ in degree six, the coefficient is

$$
\binom{6}{2,3,1}=\frac{6!}{2!3!}=60.
$$

Every factor contributes exactly one degree-one variable, so exponents must sum to six.

### Verification

Direct multiplication confirms the selected coefficient, while the factor-choice model proves the general statement.

### Common wrong turn

Do not multiply by variable values when the question asks only for a coefficient.

## E0.08.06 Prove Pascal and Vandermonde two ways

### Key idea

Partition one common set by a statistic, then count each class.

### Reasoning

For Pascal, the common set is all $k$-subsets of an $n$-set. Those containing a distinguished element correspond to $(k-1)$-subsets of the other $n-1$ elements; those omitting it are $k$-subsets of those elements. This proves

$$
\binom nk=\binom{n-1}{k-1}+\binom{n-1}k.
$$

At $k=0$ the first term is zero; at $k=n$ the second is zero. Complementation proves symmetry.

For Vandermonde, count $r$-subsets of disjoint $A\cup B$ by $k=|S\cap A|$. This gives

$$
\sum_k\binom mk\binom n{r-k}=\binom{m+n}r.
$$

Algebraically, compare $[x^r]$ in $(1+x)^m(1+x)^n=(1+x)^{m+n}$.

Thus

$$
\sum_k\binom7k\binom5{6-k}=\binom{12}{6}=924.
$$

### Verification

Each partition statistic has one value for every target subset, so the classes are disjoint and exhaustive.

### Common wrong turn

Do not state that both sides "choose things" without naming the same target set and the partition statistic.

## E0.08.07 Translate compositions with stars and bars

### Key idea

Stars record units and bars record labeled compartments; counting bar positions gives a bijection.

### Reasoning

The forward map writes $x_i$ stars in compartment $i$; the inverse counts stars between consecutive bars. Thus weak compositions of $r$ into $m$ parts are counted by $\binom{r+m-1}{m-1}$.

For total three and three parts, the ten strings are all placements of two bars among five positions, so the count is $\binom52=10$.

Positive parts use $y_i=x_i-1$, giving $\binom{r-1}{m-1}$ when $r\ge m$.

For the shifted problem, subtract lower bounds totaling seven. The remaining nonnegative total is thirteen across four variables:

$$
\binom{13+4-1}{3}=\binom{16}{3}=560.
$$

There is one zero-part composition of total zero and none of positive total. With positive parts, zero parts similarly represent only total zero. Plain bars impose no upper bounds because any compartment may contain all stars.

### Verification

Exhaustive tuples over `range(21)` produce 560 shifted solutions.

### Common wrong turn

Shift the total by the sum of lower bounds, not by the number of variables unless every lower bound is one.

## E0.08.08 Repair overcounting with inclusion-exclusion

### Key idea

An object in $t$ bad sets must receive total multiplicity one in a union and zero in a complement.

### Reasoning

For three sets, membership multiplicities become $1$, $2-1=1$, and $3-3+1=1$. In general an object in $t\ge1$ sets contributes $\sum_{j=1}^t(-1)^{j+1}\binom tj=1$.

For divisibility in $[120]$:

$$
60+40+24-20-12-8+4=88.
$$

For derangements of five:

$$
5!-\binom514!+\binom523!-\binom532!+\binom541!-\binom550!=44.
$$

For bounded solutions, unrestricted stars and bars gives $\binom{11}{2}=55$. Each event $x_i\ge5$ contributes $\binom62=15$ after shifting. Pair intersections are impossible because $10>9$. The result is

$$
55-3\cdot15=10.
$$

```python
from itertools import permutations, product

assert sum(any(value % divisor == 0 for divisor in (2, 3, 5)) for value in range(1, 121)) == 88
assert sum(all(index != value for index, value in enumerate(order)) for order in permutations(range(5))) == 44
assert sum(sum(values) == 9 and max(values) <= 4 for values in product(range(10), repeat=3)) == 10
```

### Verification

Direct finite enumeration agrees with all three inclusion-exclusion counts.

### Common wrong turn

Do not add pair intersections that are empty, but do state why they are empty.

## E0.08.09 Use pigeonhole and double counting

### Key idea

Count the domain and codomain for collisions; count incidences from each coordinate for identities.

### Reasoning

There are $2^{10}=1024$, not fewer than 101, binary strings of length ten, so item 1 as written does **not** force equality. A counterexample is any 101 distinct strings. The smallest repaired claim uses 1025 strings.

For jobs,

$$
\left\lceil\frac{73}{8}\right\rceil=10,
$$

so one queue has at least ten jobs.

For equal finite sizes, an injection has image of full size and is surjective; a surjection has fibers whose positive sizes sum to the domain size, so each fiber has size one and the map is injective.

Count pairs $(S,s)$ with $|S|=k$ and $s\in S$. Choosing $S$ then $s$ gives $k\binom nk$. Choosing $s$ then the other $k-1$ elements gives $n\binom{n-1}{k-1}$.

Summing over all subset sizes counts all incidences. For each of $n$ elements, exactly $2^{n-1}$ subsets contain it, so

$$
\sum_{k=0}^n k\binom nk=n2^{n-1}.
$$

Assume $n\ge1$ for the final exponent expression and eight positive queues for the ceiling bound.

### Verification

The first prompt is intentionally false; cardinality audit catches it before an invalid pigeonhole proof begins.

### Common wrong turn

Pigeonhole applies only when the domain is larger than the codomain. Similar-looking large numbers are not enough.

## E0.08.10 Extract coefficients from finite choices

### Key idea

Polynomial multiplication applies product counting to choice pairs and sum counting to equal total degrees.

### Reasoning

The product is

$$
(1+x+x^2)(1+x+\cdots+x^4)(1+x+\cdots+x^5).
$$

For each $x_1\in\{0,1,2\}$, count $x_2+x_3=8-x_1$ within bounds. The counts are $2,3,4$, so $[x^8]=9$.

```python
from itertools import product

def convolve(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a_i in enumerate(left):
        for j, b_j in enumerate(right):
            result[i + j] += a_i * b_j
    return result

coefficients = [1]
for maximum in (2, 4, 5):
    coefficients = convolve(coefficients, [1] * (maximum + 1))

assert coefficients[8] == 9
assert coefficients[8] == sum(sum(values) == 8 for values in product(range(3), range(5), range(6)))
assert sum(coefficients) == 3 * 5 * 6
```

Evaluating the product at $x=1$ proves the coefficient sum equals the total independent choices. Terms above degree eight cannot contribute back to degree eight under multiplication by nonnegative-degree polynomials, so truncation is safe for that target. Everything is finite coefficient algebra, so convergence is irrelevant.

### Verification

Convolution, direct enumeration, and the hand split all give nine.

### Common wrong turn

Do not discard high degrees before they have been formed if later factors could have negative degrees. This module uses ordinary nonnegative-degree polynomials.

## E0.08.11 Derive Fibonacci and Catalan counts

### Key idea

Both recurrences come from unique first or last decompositions.

### Reasoning

Tilings end uniquely in a square or domino, so $T_n=T_{n-1}+T_{n-2}$ with $T_0=T_1=1$. The same recurrence and bases as $F_{n+1}$ prove equality by induction.

For $F(x)=\sum_{n\ge0}F_nx^n$, coefficient shifts yield $F(x)=x+xF(x)+x^2F(x)$, hence $F(x)=x/(1-x-x^2)$ formally.

In a nonempty balanced word, match the first `(` with the first position where height returns to zero. The inside is uniquely $u$ and the remaining suffix is $v$. Splitting by the pair count of $u$ gives

$$
C_n=\sum_{i=0}^{n-1}C_iC_{n-1-i}.
$$

Among all paths with $n$ up and $n$ down steps, reflect the prefix through the first step below zero. This bijects invalid paths with paths having $n-1$ up and $n+1$ down steps. Therefore

$$
C_n=\binom{2n}{n}-\binom{2n}{n+1}=\frac1{n+1}\binom{2n}{n}.
$$

```python
from itertools import product
from math import comb

def balanced(word):
    height = 0
    for symbol in word:
        height += 1 if symbol == "(" else -1
        if height < 0:
            return False
    return height == 0

for n in range(6):
    observed = sum(balanced(word) for word in product("()", repeat=2 * n))
    assert observed == comb(2 * n, n) // (n + 1)
```

### Verification

Enumeration confirms fixed cases; unique decomposition and reflection prove the arbitrary-$n$ formulas.

### Common wrong turn

Equal initial values do not identify sequences unless the same recurrence is also proved.

## E0.08.12 Implement and audit a counting argument

### Key idea

Separate theorem, implementation, finite execution, API specification, probability assumption, and source license.

### Reasoning

The repository's [`test_counting.py`](../code/test_counting.py) supplies a compact valid implementation of items 1 through 8. Extend its ranges and deterministic families as requested. A passing report should include rows such as:

| Claim | Evidence | Limit |
|---|---|---|
| sampling helper matches model | exhaustive tuples for $n,k\le6$ | fixed finite parameter range |
| Vandermonde holds generally | common-set partition proof | assumes finite disjoint source groups |
| `itertools` selects positions | official Python documentation | current documented version |
| outcomes are equally likely | not established by counts | requires a probability model |
| coefficient identity is valid | finite/formal algebra | does not imply numerical convergence |

At least six flaws in the proposed claim are:

1. Python output is execution evidence, not a mathematical proof.
2. A library call may be used with the wrong outcome model.
3. Passing examples do not prove arbitrary parameters.
4. A count does not assign probability weights.
5. Physical mechanisms may make outcomes nonuniform.
6. Formal coefficient manipulation does not assert analytic convergence.
7. Numerical series evaluation would require a domain and convergence argument.
8. Correct API behavior does not verify source licensing or originality.

The source ledger should record MIT for curricular unit placement, Guichard for directly inspected counting and generating-function treatments, Levin for a second open undergraduate treatment, Python `math` for `comb` and `perm`, and Python `itertools` for iterator semantics. Record 2026-09-01 as the access date and state that all submitted examples and exercises are original.

### Verification

Run `python -m unittest -v` from `code/`; all tests must pass. Then inspect each source directly rather than relying on this summary.

### Common wrong turn

Do not merge "the program passed" and "the theorem is proved" into one evidence claim.

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Code](../code/README.md)