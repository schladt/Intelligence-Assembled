# Solutions for §0.07 Induction, Recursion, and Invariants

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Resources](../resources/README.md)

These are full worked solutions. Different predicates, witnesses, measures, or code organization can be valid, but every solution must preserve the declared domain and all proof obligations.

Python excerpts reuse definitions from the module's [Implementation](../README.md#implementation) section. Run those five lesson fences in order before running the solution excerpts in order.

## E0.07.01 Plan an induction and align its base

### Key idea

An induction plan is a dependency graph. The base enters the graph, and the step edges must reach every index or constructor claimed by the conclusion.

### Reasoning

A compact ledger is:

| Item | Predicate and domain | Base obligation | Hypothesis and step target |
|---:|---|---|---|
| 1 | $P(n):\sum_{i=0}^{n}(2i+1)=(n+1)^2$, $n\ge0$ | $P(0)$ | arbitrary $k\ge0$; assume $P(k)$; prove $P(k+1)$ |
| 2 | $P(n):2^n>n$, $n\ge3$ | $P(3)$ | arbitrary $k\ge3$; assume $P(k)$; prove $P(k+1)$ |
| 3 | $P(n):8\mid(3^n-1)$, even $n\ge0$ | $P(0)$ | arbitrary even $k$; assume $P(k)$; prove $P(k+2)$ |
| 4 | $P(n):a_n\le3^n$, $n\ge0$ | $P(0),P(1)$ | assume $P(k),P(k+1)$; prove $P(k+2)$ |
| 5 | $P(t):L(t)=N(t)+1$, all full binary trees | prove for a leaf | one IH per child; prove for `Node(left,right)` |

The conclusions retain those domains: all naturals from zero in item 1, all naturals from three in item 2, only even naturals in item 3, all sequence indices in item 4, and all constructor-generated trees in item 5.

The audits are:

- Item 2 cannot connect $P(0)$ to a step whose premise is available only from $k\ge3$. Use base $P(3)$.
- Item 3's one base and step of two are correct only because the theorem is restricted to even indices. Claiming all naturals would require another base for odd indices and a true odd-index statement, which does not exist here because $3^1-1=2$.
- Item 4 needs both $P(k)$ and $P(k+1)$ because the recurrence uses both terms. It also needs bases $0$ and $1$.
- Item 5 needs two child hypotheses because node size combines two independently constructed trees. Structural induction is the direct principle; a size induction needs a separate all-smaller-object formulation.

Assuming $P(k)$ in the step proves the conditional $P(k)\implies P(k+1)$. The base and earlier applications later discharge that assumption. Assuming the final universal theorem would put the target among its own premises and create circularity.

### Verification

Each plan starts at the first claimed object and supplies exactly the hypotheses consumed by one recursive step or constructor.

### Common wrong turn

Do not choose bases by counting how many formulas appear in the statement. Choose them by the predecessor dependencies and reachable residue classes.

## E0.07.02 Prove identities by weak induction

### Key idea

Separate the last summand or factor, then replace only the established prefix by the inductive hypothesis.

### Reasoning

**1. Odd-number sum.** Let

$$
P(n):\quad\sum_{i=0}^{n}(2i+1)=(n+1)^2.
$$

At $n=0$, both sides equal $1$. Let $k\ge0$ and assume $P(k)$. Then

$$
\begin{aligned}
\sum_{i=0}^{k+1}(2i+1)
&=\sum_{i=0}^{k}(2i+1)+(2(k+1)+1)\\\\
&=(k+1)^2+2k+3\\\\
&=(k+2)^2.
\end{aligned}
$$

The second line uses the hypothesis, and the final expression is $P(k+1)$.

**2. Geometric sum.** Let

$$
P(n):\quad\sum_{i=0}^{n}3^i=\frac{3^{n+1}-1}{2}
$$

for $n\ge1$. At $n=1$, $1+3=4=(3^2-1)/2$. Assume $P(k)$ for $k\ge1$. Then

$$
\begin{aligned}
\sum_{i=0}^{k+1}3^i
&=\frac{3^{k+1}-1}{2}+3^{k+1}\\\\
&=\frac{3^{k+1}-1+2\cdot3^{k+1}}{2}\\\\
&=\frac{3^{k+2}-1}{2}.
\end{aligned}
$$

**3. Divisibility.** At $n=1$, $6^1-1=5$. Assume $6^k-1=5q$. Then

$$
6^{k+1}-1=6(6^k-1)+5=5(6q+1),
$$

so $5\mid(6^{k+1}-1)$.

A finite audit is:

```python
for n in range(21):
    assert sum(2 * i + 1 for i in range(n + 1)) == (n + 1) ** 2
for n in range(1, 21):
    assert sum(3 ** i for i in range(n + 1)) == (3 ** (n + 1) - 1) // 2
    assert (6 ** n - 1) % 5 == 0

assert next(
    n for n in range(21)
    if sum(2 * i + 1 for i in range(n + 1)) != n ** 2
) == 0
```

The last assertion mutates $(n+1)^2$ to $n^2$ and finds failure at the base.

### Verification

Every proof uses the hypothesis exactly when replacing the current prefix. Exact integer checks confirm cases through the declared finite limits.

### Common wrong turn

Finite checks support debugging. They do not create the universal implication that advances from arbitrary $k$.

## E0.07.03 Cover multiple bases and step sizes

### Key idea

A $+4$ step preserves residue modulo four, so four consecutive starting cases cover all later integers.

### Reasoning

The bases are

$$
18=4+2\cdot7,
\quad19=3\cdot4+7,
\quad20=5\cdot4,
\quad21=3\cdot7.
$$

Assume arbitrary $k\ge18$ is representable as $k=4a+7b$. Then

$$
k+4=4(a+1)+7b,
$$

so representability advances by four. The bases $18,19,20,21$ occupy residues $2,3,0,1$ modulo four, respectively. Every $n\ge18$ has one of those residues and is reached by repeatedly adding four.

Bases $18$ and $19$ reach only residues $2$ and $3$. Values $20$ and $21$ would remain unsupported even though they happen to be representable.

For a theorem only about $n\equiv2\pmod4$, base $P(18)$ and step $P(k)\implies P(k+4)$ are enough for every such $n\ge18$.

For the recurrence, $a_0=1<3$ and $a_1=2<9$. Assume

$$
a_k<3^{k+1},
\qquad
a_{k+1}<3^{k+2}.
$$

Then

$$
\begin{aligned}
a_{k+2}
&=2a_{k+1}+a_k\\\\
&<2\cdot3^{k+2}+3^{k+1}\\\\
&=7\cdot3^{k+1}\\\\
&<9\cdot3^{k+1}=3^{k+3}.
\end{aligned}
$$

This is the required bound at $k+2$.

A third-order recurrence generally needs three aligned bases because its step consumes three preceding terms. Two bases leave the first recursive computation unsupported.

```python
def reached_by_step(bases, step, upper):
    reached = set(bases)
    changed = True
    while changed:
        changed = False
        for value in tuple(reached):
            if value + step <= upper and value + step not in reached:
                reached.add(value + step)
                changed = True
    return reached

assert reached_by_step((18, 19), 4, 50) == {
    n for n in range(18, 51) if n % 4 in (2, 3)
}
assert reached_by_step((18, 19, 20, 21), 4, 50) == set(range(18, 51))
```

### Verification

The four bases cover every residue, and the step preserves representation. The recurrence algebra uses both hypotheses.

### Common wrong turn

Showing that the next four values are true is not a replacement for showing how every later value reaches one of them.

## E0.07.04 Use strong induction on smaller parts

### Key idea

Strong induction matches decompositions whose pieces are merely smaller, not necessarily one smaller.

### Reasoning

For prime products, assume every $j$ with $2\le j<n$ is a product of primes. If $n$ is prime, the one-factor product works. Otherwise $n=ab$ with $2\le a,b<n$. The hypothesis gives prime-product expressions for both $a$ and $b$, and multiplying those products gives one for $n$.

For $q(n)$, proceed by strong induction on $n\ge1$. At $n=1$, zero moves work. For $n>1$, subtraction by one produces $n-1$, a smaller positive integer. By induction, a finite path from $n-1$ to $1$ exists; prepend the subtraction move. Hence $q(n)$ exists. This construction also gives

$$
q(n)\le1+q(n-1)\le1+(n-2)=n-1.
$$

When $n$ is even, a potentially shorter path can use $n/2<n$. That call needs the all-smaller hypothesis because $n/2$ is generally not $n-1$.

For weak induction, define

$$
Q(n):\quad\text{every }j\text{ with }2\le j\le n\text{ is a prime product}.
$$

At $n=2$, the claim follows because $2$ is prime. Assume $Q(k)$. To establish $Q(k+1)$, retain all old cases and prove the new case. If $k+1$ is composite, both nontrivial factors lie between $2$ and $k$, so $Q(k)$ covers them.

In strong induction stated as one step, the first value has an empty smaller-case range. The proof must still handle it without drawing information from that empty hypothesis.

An invalid hypothesis would be

$$
\forall j\le n,\ P(j)
$$

while proving $P(n)$. It includes the current target and is circular. The strict inequality $j<n$ is essential.

### Verification

Every recursive part is positive and strictly smaller. The cumulative weak predicate reproduces the information of strong induction.

### Common wrong turn

Do not claim a composite factor is smaller without excluding the factors $1$ and $n$.

## E0.07.05 Build a least-counterexample proof

### Key idea

Nonemptiness comes from negating the theorem. Minimality then turns every smaller eligible value into an established case.

### Reasoning

Suppose the claim is false and define

$$
C=\{n\in\mathbb{N}:n\ge24\text{ and no }a,b\in\mathbb{N}
\text{ satisfy }n=5a+7b\}.
$$

The negation of the universal claim makes $C$ nonempty. By well-ordering, let $m=\min C$.

The five consecutive amounts are

$$
24=2\cdot5+2\cdot7,
\quad25=5\cdot5,
\quad26=5+3\cdot7,
$$

$$
27=4\cdot5+7,
\quad28=4\cdot7.
$$

Thus $m\ge29$. Then $m-5\ge24$ and $m-5<m$. Since $m$ is the least counterexample, $m-5$ is representable:

$$
m-5=5a+7b.
$$

Therefore

$$
m=5(a+1)+7b,
$$

contradicting $m\in C$.

The strong-induction version assumes every value from $24$ through $n-1$ is representable. It proves five base cases, then for $n\ge29$ applies the hypothesis to $n-5$. The arithmetic content is the same; least-counterexample language packages it as contradiction.

For well-ordering to induction, suppose base and step hold but some case fails. The nonempty counterexample set has a least member. It is not the base, and its predecessor is not a counterexample, so the step contradicts its failure.

For induction to well-ordering, suppose nonempty $S\subseteq\mathbb{N}$ has no least element. Inductively show no member of $S$ is at most $n$. At zero, membership would make zero least. If there is no member at most $n$, then membership of $n+1$ would make it least. The resulting emptiness contradicts the premise.

"Choose the least counterexample; if none exist, we are done" invokes a minimum before the proof has entered the branch where counterexamples exist. Assume failure and establish nonemptiness first.

Natural-number well-ordering does not apply to arbitrary nonempty real sets. The set $(0,1)$ has no least positive real: if $x$ lies in it, then $x/2$ is smaller and still lies in it.

### Verification

The counterexample set is explicitly a nonempty subset of $\mathbb{N}$ before its minimum is selected. The five bases align with subtraction by five.

### Common wrong turn

Do not infer that $m-5$ is representable merely because it is smaller. It must also remain inside the theorem's eligible range.

## E0.07.06 Follow constructors with structural induction

### Key idea

Recursive definitions and structural proofs use the same constructor boundaries. A changed syntax requires changed claims.

### Reasoning

Use

$$
[]\mathbin{+\!+}ys=ys,
$$

$$
cons(x,xs)\mathbin{+\!+}ys=cons(x,xs\mathbin{+\!+}ys),
$$

$$
reverse([])=[],
$$

$$
reverse(cons(x,xs))=reverse(xs)\mathbin{+\!+}[x].
$$

Fix `ys` and induct on `xs`. For the empty list,

$$
reverse([]\mathbin{+\!+}ys)=reverse(ys)
=reverse(ys)\mathbin{+\!+}[].
$$

For `cons(x,xs)`, assume

$$
reverse(xs\mathbin{+\!+}ys)=reverse(ys)\mathbin{+\!+}reverse(xs).
$$

Then

$$
\begin{aligned}
reverse(cons(x,xs)\mathbin{+\!+}ys)
&=reverse(cons(x,xs\mathbin{+\!+}ys))\\\\
&=reverse(xs\mathbin{+\!+}ys)\mathbin{+\!+}[x]\\\\
&=(reverse(ys)\mathbin{+\!+}reverse(xs))\mathbin{+\!+}[x]\\\\
&=reverse(ys)\mathbin{+\!+}reverse(cons(x,xs)).
\end{aligned}
$$

The final reassociation uses associativity of append, which itself needs a prior proof.

For odd node count, a `Number` has size one. An `Add` or `Multiply` has

$$
1+odd+odd=odd.
$$

Both child hypotheses are required. Combining $L=N+1$ with $size=L+N$ gives

$$
size=2L-1.
$$

Alternatively, prove it directly: a leaf has $1=2\cdot1-1$, and a binary node adds one to two child sizes.

Adding `Negate(child)` breaks odd size because `Negate(Number(1))` has size two. A repaired parity statement is

$$
size(t)\equiv1+U(t)\pmod2,
$$

where $U(t)$ counts unary nodes. A `Number` has $(size,U)=(1,0)$. Binary constructors add one and two child pairs; unary negation adds one to both size and unary count. Each constructor preserves the congruence.

```python
@dataclass(frozen=True)
class Negate:
    child: object


def counts_with_unary(expression):
    if isinstance(expression, Number):
        return (1, 0)
    if isinstance(expression, Negate):
        size, unary = counts_with_unary(expression.child)
        return (size + 1, unary + 1)
    if isinstance(expression, (Add, Multiply)):
        left_size, left_unary = counts_with_unary(expression.left)
        right_size, right_unary = counts_with_unary(expression.right)
        return (1 + left_size + right_size, left_unary + right_unary)
    raise TypeError(type(expression).__name__)

unary_examples = (
    Number(1),
    Negate(Number(1)),
    Add(Negate(Number(0)), Number(2)),
    Multiply(Negate(Number(1)), Negate(Number(2))),
)
for expression in unary_examples:
    size, unary = counts_with_unary(expression)
    assert size % 2 == (1 + unary) % 2
assert counts_with_unary(Negate(Number(1)))[0] == 2
```

Structural induction follows immediate children. Strong induction on size would assume the claim for every smaller tree and then observe that each child is smaller. It is valid but gives more hypotheses than needed.

### Verification

Every constructor, including the added unary one, has a case. The repaired parity invariant survives all constructor equations.

### Common wrong turn

Do not retain a theorem after extending the datatype unless the new constructor preserves it.

## E0.07.07 Audit recursive definitions and termination

### Key idea

A decreasing call is not enough if clauses conflict or omit inputs. Audit meaning and progress separately.

### Reasoning

| Item | Coverage and overlap | Decrease | Verdict and repair |
|---:|---|---|---|
| 1 | covers every $n\ge0$ disjointly | $n-1<n$ for $n\ge1$ | valid |
| 2 | covers all $n\ge0$ | calls larger $n+1$ | not well-founded; add a base and recurse downward |
| 3 | zero matches both base and even clause | even clause at zero calls $h(0)$ | ambiguous/circular; restrict recursive clauses to positive inputs |
| 4 | clause $n\ge1$ overlaps base $n=1$ and asks for $r(-1)$ | invalid at first overlap | change recurrence domain to $n\ge2$ |
| 5 | covers $b=0$ and $b>0$ | remainder is in $[0,b)$ | valid on stated nonnegative domain |

A repaired item 3 is

$$
h(0)=0,
$$

$$
h(2n)=h(n)+1\quad(n\ge1),
$$

$$
h(2n+1)=h(n)+1\quad(n\ge0).
$$

Use the input itself as measure. In the positive even branch, $n<2n$; in the odd branch, $n<2n+1$.

A repaired item 2 could be

$$
g(0)=0,
\qquad g(n)=g(n-1)+1\quad(n\ge1).
$$

```python
from math import gcd as library_gcd


def recursive_gcd(left, right):
    if left < 0 or right < 0:
        raise ValueError("nonnegative inputs required")
    if right == 0:
        return left
    remainder = left % right
    assert 0 <= remainder < right
    return recursive_gcd(right, remainder)

for left in range(40):
    for right in range(40):
        assert recursive_gcd(left, right) == library_gcd(left, right)

for number in range(50):
    calls = [0]
    assert factorial_recursive(number, calls) == factorial_iterative(number)
```

Euclid's correctness invariant is

$$
\gcd(a,b)=\gcd(b,a\bmod b).
$$

Its termination measure is the second argument $b$. Equality of gcd values does not prove decrease, and decrease does not prove the returned value is the gcd.

Python's recursion limit is an interpreter-stack guard. A mathematically terminating call chain can exceed it; an invalid upward recursion can fail much sooner or consume resources indefinitely in another runtime.

### Verification

Every repaired definition covers its stated domain without inconsistent overlap, and every recursive call decreases a natural-valued measure.

### Common wrong turn

Do not rely on source-code pattern order to repair an ambiguous mathematical definition. State disjoint clause domains.

## E0.07.08 Prove a state-machine invariant

### Key idea

Both transitions add three to the coordinate sum. Reachability stays inside the resulting congruence class, but that class includes unreachable states.

### Reasoning

At the start, $x+y=0$, divisible by three. Transition $A$ changes the sum by $2+1=3$, and transition $B$ changes it by $1+2=3$. Therefore divisibility by three is initialized and preserved.

Both coordinates start nonnegative. Each transition adds positive integers, so nonnegativity is preserved.

If $x+y=10$, then the sum is not divisible by three. This contradicts the invariant, so every reachable state satisfies safety property $x+y\ne10$.

The state $(3,0)$ satisfies nonnegativity and has sum divisible by three, but is unreachable. After $a$ uses of $A$ and $b$ uses of $B$,

$$
(x,y)=(2a+b,a+2b).
$$

Solving $(2a+b,a+2b)=(3,0)$ over nonnegative integers would force $a=b=0$ from the second coordinate and then $x=0$. Thus invariant satisfaction is not reachability.

$x-y$ is even at the start. Transition $A$ changes it by $1$, so preservation fails immediately at $(2,1)$.

With terminal condition $x+y\ge12$, define

$$
\mu(x,y)=\max(0,12-(x+y)).
$$

At every nonterminal state, the sum is below twelve and each transition raises it by three, so $\mu$ decreases by three until zero. It remains a nonnegative integer, proving termination.

```python
def exercise_successors(state):
    left, right = state
    if left + right >= 12:
        return ()
    return ((left + 2, right + 1), (left + 1, right + 2))

exercise_reached = reachable_states((0, 0), exercise_successors)
assert all((x + y) % 3 == 0 for x, y in exercise_reached)
assert all(x >= 0 and y >= 0 for x, y in exercise_reached)
assert all(x + y != 10 for x, y in exercise_reached)
assert (3, 0) not in exercise_reached
assert next(
    state for state in sorted(exercise_reached)
    if (state[0] - state[1]) % 2 != 0
) == (1, 2)


def mutated_successors(state):
    left, right = state
    if left + right >= 12:
        return ()
    return ((left + 2, right + 1), (left + 1, right + 1))

mutated_reached = reachable_states((0, 0), mutated_successors)
assert (1, 1) in mutated_reached
assert (1 + 1) % 3 != 0
```

The mutation changes the sum by two, so divisibility preservation fails.

### Verification

Initialization and both original transitions were checked symbolically. The bounded graph is finite because transitions stop at the threshold.

### Common wrong turn

Do not prove safety from nonnegativity alone. The load-bearing invariant for excluding ten is divisibility by three.

## E0.07.09 Design loop invariants and prove correctness

### Key idea

Name the processed prefix exactly. The exit condition then turns a prefix fact into the promised whole-input fact.

### Reasoning

For the odd sum, initialize `index = total = 0`. The invariant $total=index^2$ holds. If it holds before an iteration, then

$$
total'=index^2+(2index+1)=(index+1)^2.
$$

Incrementing the index restores the invariant. At exit, `index == length`, so `total == length ** 2`, which equals the required odd-number sum. Variant `length - index` starts nonnegative and decreases by one.

For first minimum after processing nonempty prefix `values[:index]`, use:

- $1\le index\le len(values)$;
- $0\le best<index$;
- `values[best] == min(values[:index])`;
- no earlier index with the minimum value precedes `best`.

Initialization with `index = 1` and `best = 0` satisfies the invariant. When the next value is strictly smaller, assigning its index makes it the unique earliest location of the new minimum. Otherwise the old earliest minimum remains valid. At exit the prefix is the full list.

```python
def odd_sum(length):
    if length < 0:
        raise ValueError("length must be nonnegative")
    index = 0
    total = 0
    while index < length:
        assert total == index * index
        total += 2 * index + 1
        index += 1
    assert total == length * length
    return total


def first_minimum_index(values):
    if not values:
        raise ValueError("values must be nonempty")
    best = 0
    index = 1
    while index < len(values):
        assert values[best] == min(values[:index])
        assert best == values[:index].index(values[best])
        if values[index] < values[best]:
            best = index
        index += 1
    assert best == values.index(min(values))
    return best

for length in range(101):
    assert odd_sum(length) == sum(2 * i + 1 for i in range(length))
assert first_minimum_index((3, -1, -1, 2)) == 1
assert first_minimum_index((0,)) == 0
assert first_minimum_index((4, 3, 2, 1)) == 3
```

Changing `<` to `<=` updates `best` on ties, so the loop returns the last minimum rather than the first. A valid invariant must change its tie-breaking clause.

The loop

```python
safe_value = 0
while False:
    safe_value += 1
assert safe_value == 0
```

terminates, so it is not the requested counterexample. A genuine safe nonterminating specification is `while True: assert safe_value == 0` with no mutation. Its safety invariant is maintained, but it has no decreasing variant and no exit.

### Verification

Both terminating loops have initialization, maintenance, postcondition, and decreasing variants. Tests include empty-length arithmetic, singleton search, duplicates, and negative values.

### Common wrong turn

Do not execute the nonterminating example. Its source-level reasoning is enough to show that safety does not imply progress.

## E0.07.10 Solve linear recurrences by characteristic roots

### Key idea

Multiplicity controls the solution family. Initial conditions then determine its free constants.

### Reasoning

**1.** The polynomial is

$$
r^2-4r+3=(r-1)(r-3).
$$

Thus $a_n=A+B3^n$. From $A+B=2$ and $A+3B=4$, we get $A=B=1$:

$$
a_n=1+3^n.
$$

**2.** The polynomial is

$$
r^2-8r+16=(r-4)^2.
$$

Thus $b_n=(A+Bn)4^n$. Initial values give $A=1$ and $4(1+B)=8$, so $B=1$:

$$
b_n=(n+1)4^n.
$$

**3.** The polynomial is

$$
r^2-2r-3=(r-3)(r+1).
$$

Thus $c_n=A3^n+B(-1)^n$. From $A+B=0$ and $3A-B=4$, we get $A=1,B=-1$:

$$
c_n=3^n-(-1)^n.
$$

**4.** Fibonacci has roots $\varphi=(1+\sqrt5)/2$ and $\psi=(1-\sqrt5)/2$. From $A+B=0$ and $A\varphi+B\psi=1$, obtain $A=1/\sqrt5$ and $B=-1/\sqrt5$:

$$
F_n=\frac{\varphi^n-\psi^n}{\sqrt5}.
$$

Item 2 needs $n4^n$ because a repeated root contributes only one ordinary exponential mode. Without one initial condition, each second-order family retains one free parameter.

```python
solution_a = generate_second_order(2, 4, 4, -3, 41)
solution_b = generate_second_order(1, 8, 8, -16, 41)
solution_c = generate_second_order(0, 4, 2, 3, 41)

assert solution_a == [1 + 3 ** n for n in range(41)]
assert solution_b == [(n + 1) * 4 ** n for n in range(41)]
assert solution_c == [3 ** n - (-1) ** n for n in range(41)]
assert recurrence_residuals(solution_a, 4, -3) == (0,) * 39
assert recurrence_residuals(solution_b, 8, -16) == (0,) * 39
assert recurrence_residuals(solution_c, 2, 3) == (0,) * 39

fib_exact = generate_second_order(0, 1, 1, 1, 41)
phi = (1 + sqrt(5)) / 2
psi = (1 - sqrt(5)) / 2
assert all(
    isclose((phi ** n - psi ** n) / sqrt(5), exact,
            rel_tol=1e-9, abs_tol=1e-9)
    for n, exact in enumerate(fib_exact)
)
```

Writing $r^2-2r+3$ for item 3 changes the recurrence sign. Since the original has $+3c_{n-2}$ on the right, moving it left gives $-3r^{n-2}$ and therefore constant term $-3$.

### Verification

Every formula satisfies both initial values and has zero exact recurrence residual through index forty.

### Common wrong turn

Residual checks without initial-value checks can verify a different member of the same solution family.

## E0.07.11 Apply and refuse the Master Theorem

### Key idea

Name a case only after matching the exact balanced form and checking polynomial separation and any regularity requirement.

### Reasoning

| Item | $a,b,p$ | Comparison and condition | Result or refusal |
|---:|---|---|---|
| 1 | $9,3,2$ | $n=O(n^{2-1})$ | case 1, $\Theta(n^2)$ |
| 2 | $3,3,1$ | $f(n)=\Theta(n)$ | case 2, $\Theta(n\log n)$ |
| 3 | $3,3,1$ | $n^2=\Omega(n^{1+1})$; regularity | case 3, $\Theta(n^2)$ |
| 4 | $1,4,0$ | $n^{1/2}=\Omega(n^{0+1/2})$; regularity | case 3, $\Theta(\sqrt n)$ |
| 5 | none | unequal subproblem sizes | not applicable |
| 6 | $a=n$ | subproblem count is not constant | not applicable |
| 7 | $2,2,1$ | logarithmic, not polynomial, gap below $n$ | no basic case applies |
| 8 | $2,2,1$ | negative $f$ violates cost assumptions | not applicable |
| 9 | $2,2,1$ | polynomial gap but regularity fails | case 3 unavailable |

For item 3,

$$
3f(n/3)=3(n/3)^2=\frac13n^2,
$$

so choose $c=1/3$.
For item 4,

$$
f(n/4)=\sqrt{n/4}=\frac12\sqrt n,
$$

so $c=1/2$.

```python
master_1 = recursion_tree_levels(3 ** 6, 9, 3, lambda n: n)
master_2 = recursion_tree_levels(3 ** 6, 3, 3, lambda n: n)
master_3 = recursion_tree_levels(3 ** 6, 3, 3, lambda n: n ** 2)
master_4 = recursion_tree_levels(4 ** 5, 1, 4, lambda n: int(sqrt(n)))

assert [row[3] for row in master_1[:3]] == [3 ** 6, 3 ** 7, 3 ** 8]
assert len({row[3] for row in master_2}) == 1
assert [row[3] for row in master_3[:3]] == [3 ** 12, 3 ** 11, 3 ** 10]
assert [row[3] for row in master_4[:3]] == [2 ** 5, 2 ** 4, 2 ** 3]
```

The final integer square-root work values are exact on the selected powers of four. They decrease by one half per level.

A recursion tree exposes node counts, sizes, and level work. Ellipses and finite tables do not bound every omitted level or every sufficiently large input. The theorem supplies those bounds under its hypotheses.

This solution restricts $n$ to exact powers of $b$. An algorithm on arbitrary integer sizes must analyze floor and ceiling subproblem sizes or invoke a theorem version that includes them.

### Verification

Every accepted recurrence has constant $a$, constant $b>1$, equal-size subproblems, nonnegative work, a fixed base case, and the required gap. Both case-three applications include explicit $c<1$.

### Common wrong turn

Do not label item 7 case 1 merely because $n/\log n<n$. Case 1 demands a polynomial gap $n^\varepsilon$.

## E0.07.12 Implement, experiment, and audit sources

### Key idea

Each evidence type answers a different question. Exact tests audit implementations; induction proves universal mathematical claims; documentation specifies APIs; source inspection supports attribution and reuse boundaries.

### Reasoning

One integrated audit is:

```python
import sys
from math import gcd as math_gcd

for number in range(101):
    calls = [0]
    assert factorial_recursive(number, calls) == factorial_iterative(number)

naive_counts = {}
cache_rows = {}
for number in range(31):
    naive_fibonacci_calls = 0
    assert fibonacci_naive(number) == fibonacci_iterative(number)
    naive_counts[number] = naive_fibonacci_calls

    fibonacci_cached.cache_clear()
    memoized_fibonacci_misses = 0
    assert fibonacci_cached(number) == fibonacci_iterative(number)
    info = fibonacci_cached.cache_info()
    cache_rows[number] = (info.hits, info.misses, info.currsize)
    expected_misses = 1 if number < 2 else number + 1
    assert info.misses == expected_misses
    assert memoized_fibonacci_misses == info.misses

assert naive_counts[10] == 177
assert naive_counts[20] == 21891
assert cache_rows[30][1:] == (31, 31)

for left in range(75):
    for right in range(75):
        value, trace = gcd_with_trace(left, right)
        assert value == math_gcd(left, right)
        assert all(remainder < divisor for _, divisor, remainder in trace)

for expression in expressions(2):
    leaves, internal, size = tree_counts(expression)
    assert leaves == internal + 1
    assert size == leaves + internal
    evaluate(expression)

reached, failures = check_invariant(
    (0, 0), bounded_parity_successors,
    lambda state: (state[0] + state[1]) % 2 == 0,
)
assert not failures
invalid_failure = next(
    state for state in sorted(reached) if state[0] != state[1]
)
assert invalid_failure in reached

assert sys.getrecursionlimit() > 100
assert sum_prefix(0) == 0
assert first_index((2, 2, 3), 2) == 0
assert recurrence_residuals(distinct, 5, -6) == (0,) * 10
assert recursion_tree_levels(64, 2, 2, lambda n: n)[0][3] == 64
```

Cached body counts equal misses because a hit returns from the wrapper's dictionary without entering the wrapped function body. The cache does not make every recursion polynomial. It helps only when repeated subproblems have reusable results, arguments are cacheable, and the number and cost of distinct states are controlled.

A six-part claim audit is:

| Claim fragment | Diagnosis | Repair |
|---|---|---|
| memoization makes every recursion polynomial | false | bound distinct states and per-state work |
| every function may be cached safely | false | purity, hashability, memory, and concurrency matter |
| bounded invariant checks cover all executions | false | they cover only reached states inside the bound |
| no found counterexample proves preservation | false | prove the transition implication symbolically |
| matching ratios prove $\Theta$ | false | finite ratios do not establish eventual upper and lower bounds |
| Master applies from a visual trend | false | verify recurrence form, gap, regularity, and base conditions |
| recursion error means nontermination | false | it may mean a finite call chain exceeded a runtime limit |
| termination proves correctness | false | value preservation and postconditions remain separate |

A source ledger is:

| Source | Accessed | Supported claim | Reuse boundary |
|---|---|---|---|
| Python `functools` docs | 2026-09-01 | `cache` equals unbounded `lru_cache`; cache statistics and retained entries | PSF docs; examples here original |
| Python `sys` docs | 2026-09-01 | recursion limit protects interpreter stack | PSF docs; no copied recipe |
| Cornell CS3110 Lecture 20 | 2026-09-01 | recursion-tree formula, three Master cases, regularity, non-applicability | course notes cited; examples here independently selected |
| MIT 6.042J readings | 2026-09-01 | course units and chapter map for proofs and structures | CC BY-NC-SA 4.0; no adapted exercise |
| *Mathematics in Lean* Chapter 5 | 2026-09-01 | inductive types, recursion, weak/strong induction, decreasing well-founded calls | CC BY 4.0; no copied formal proof |

A safe recursion-limit demonstration does not need to hit the limit. Compare the known depth $n+1$ of recursive factorial with `sys.getrecursionlimit()` and decline calls whose predicted depth approaches it. This demonstrates the engineering constraint without changing global state or risking interpreter failure.

### Verification

The audit compares independent implementations, checks exact recurrences, records finite domains, and ties every external claim to a directly inspected source.

### Common wrong turn

Do not let one successful run serve simultaneously as a proof, performance benchmark, API specification, and license check.

## Solution-set check

All exercise IDs and titles mirror the [exercise index](../exercises/README.md):

- E0.07.01 Plan an induction and align its base
- E0.07.02 Prove identities by weak induction
- E0.07.03 Cover multiple bases and step sizes
- E0.07.04 Use strong induction on smaller parts
- E0.07.05 Build a least-counterexample proof
- E0.07.06 Follow constructors with structural induction
- E0.07.07 Audit recursive definitions and termination
- E0.07.08 Prove a state-machine invariant
- E0.07.09 Design loop invariants and prove correctness
- E0.07.10 Solve linear recurrences by characteristic roots
- E0.07.11 Apply and refuse the Master Theorem
- E0.07.12 Implement, experiment, and audit sources

[Back to module](../README.md) | [Exercise set](../exercises/README.md)
