# Solutions for §0.05 Logic and Quantifiers

[Back to module](../README.md) | [Exercise set](../exercises/README.md) | [Resources](../resources/README.md)

These are full worked solutions. A correct solution may choose different separating models or normal forms, but it must preserve the same parse, truth conditions, domains, side conditions, and evidence boundaries.

## E0.05.01 Parse formulas and mark scope

### Key idea

The main operator is the final construction at the root of the parse tree. A quantifier binds matching variable occurrences only inside its scope.

### Reasoning

Using the local precedence convention:

1. $P\lor Q\land\neg R$ parses as
   $$
   P\lor(Q\land(\neg R)).
   $$
   The main operator is $\lor$. Its right child has main operator $\land$, whose right child is $\neg R$. The atoms are $P,Q,R$.

2. $(P\lor Q)\implies(\neg R\land S)$ already exposes its parse. The main operator is $\implies$. Its left child is $P\lor Q$ and its right child is $(\neg R)\land S$. The atoms are $P,Q,R,S$.

3. $\neg P\implies Q\iff R$ parses as
   $$
   ((\neg P)\implies Q)\iff R.
   $$
   The main operator is $\iff$. Its left child is an implication and its right child is $R$.

4. The fourth expression parses as
   $$
   (\forall x\,(A(x)\implies\exists y\,R(x,y)))\land B(y).
   $$
   The main operator is $\land$. The $x$ occurrences in $A(x)$ and $R(x,y)$ are bound by $\forall x$. The $y$ in $R(x,y)$ is bound by $\exists y$. The $y$ in $B(y)$ is free because it lies outside the existential scope.

5. In
   $$
   \forall x\,(P(x)\lor\exists x\,(Q(x)\land R(x,z))),
   $$
   the first $x$ in $P(x)$ is bound by the outer universal. The $x$ occurrences in $Q(x)$ and $R(x,z)$ are bound by the inner existential, which shadows the outer binder. The $z$ is free.

Two separating valuations are:

| $P$ | $Q$ | $R$ | $P\lor(Q\land R)$ | $(P\lor Q)\land R$ |
|---:|---:|---:|---:|---:|
| T | F | F | T | F |
| T | T | F | T | F |

A safe renaming is

$$
\forall x\,(P(x)\lor\exists y\,(Q(y)\land R(y,z))).
$$

### Verification

Every connective has the required number of children, and every renamed occurrence preserves its original binder. Direct evaluation separates the two parses.

### Common wrong turn

Do not let a quantifier bind a matching variable that lies outside its syntactic scope. Reusing the same letter does not create one global variable.

## E0.05.02 Build a truth table and classify

### Key idea

Evaluate each column recursively from its immediate subformulas. Classification quantifies over the entire final column.

### Reasoning

One complete table is:

| $P$ | $Q$ | $R$ | $P\lor Q$ | $P\oplus Q$ | $P\implies Q$ | $(P\oplus Q)\implies R$ | contrapositive biconditional | $(P\land\neg P)\lor R$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T | T | T | T | F | T | T | T | T |
| T | T | F | T | F | T | T | T | F |
| T | F | T | T | T | F | T | T | T |
| T | F | F | T | T | F | F | T | F |
| F | T | T | T | T | T | T | T | T |
| F | T | F | T | T | T | F | T | F |
| F | F | T | F | F | T | T | T | T |
| F | F | F | F | F | T | T | T | F |

Here "contrapositive biconditional" abbreviates

$$
(P\implies Q)\iff(\neg Q\implies\neg P).
$$

Classifications:

| Formula | Satisfiable? | Class | Satisfying rows |
|---|---:|---|---|
| $P\lor Q$ | yes | contingent | all except $P=F,Q=F$ |
| $P\oplus Q$ | yes | contingent | exactly one of $P,Q$ true |
| $P\implies Q$ | yes | contingent | all except $P=T,Q=F$ |
| $(P\oplus Q)\implies R$ | yes | contingent | all except rows 4 and 6 above |
| contrapositive biconditional | yes | tautology | all rows |
| $(P\land\neg P)\lor R$ | yes | contingent | exactly rows with $R=T$ |

When $P=Q=T$, inclusive OR is true and XOR false. Satisfiability needs one true row; tautology needs every row true.

### Verification

The implication column is false only at $T,F$. The biconditional column contains eight true values. The final formula simplifies to $R$ because $P\land\neg P$ is always false.

### Common wrong turn

Do not classify a formula after finding its first satisfying row. Continue through every valuation before deciding tautology or contingency.

## E0.05.03 Translate implication language

### Key idea

"Only if" points toward a necessary condition; "if" points away from a sufficient condition.

### Reasoning

The translations are:

1. $G\implies A$.
2. $A\implies G$.
3. $(G\implies A)\land\neg(A\implies G)$.
4. $(A\land Z)\implies G$.
5. $G\iff(A\land Z)$.
6. Reading "$P$ unless $Q$" as "$P$ if not $Q$," the sentence becomes $\neg A\implies\neg G$, equivalent to $G\implies A$.
7. $G\implies Z$.

For $G\implies A$:

| Name | Formula | English |
|---|---|---|
| original | $G\implies A$ | access only if authenticated |
| converse | $A\implies G$ | authenticated implies access |
| inverse | $\neg G\implies\neg A$ | no access implies not authenticated |
| contrapositive | $\neg A\implies\neg G$ | not authenticated implies no access |

The original and contrapositive are equivalent. The converse and inverse are equivalent to each other.

For a counterinterpretation, take an authenticated but unauthorized user. Let $A=T$, $Z=F$, and $G=F$. Then $G\implies A$ is true, while $A\implies G$ is false.

Material implication gives a truth condition only. It does not by itself state that authentication causes access, happens earlier, or is implemented by a particular mechanism.

### Verification

The counterinterpretation evaluates the original as $F\to T$, which is true, and the converse as $T\to F$, which is false.

### Common wrong turn

Do not translate "authentication is necessary" as $A\implies G$. Necessary conditions appear on the consequent side.

## E0.05.04 Transform equivalences into CNF and DNF

### Key idea

First remove implication and biconditional, then push negations inward. Distribution or truth rows finish the normal forms.

### Reasoning

For

$$
\varphi_1=\neg(P\implies(Q\lor R)),
$$

we obtain

$$
\begin{aligned}
\varphi_1
&\equiv\neg(\neg P\lor Q\lor R)\\
&\equiv P\land\neg Q\land\neg R.
\end{aligned}
$$

This is already one DNF term and a CNF of three unit clauses.

For

$$
\varphi_2=P\iff(Q\land R),
$$

biconditional expansion gives a compact CNF:

$$
(\neg P\lor Q)\land(\neg P\lor R)\land(P\lor\neg Q\lor\neg R).
$$

The first two clauses encode $P\implies Q\land R$. The third encodes $(Q\land R)\implies P$.

The true rows are $(F,F,F)$, $(F,F,T)$, $(F,T,F)$, and $(T,T,T)$, so canonical DNF is

$$
(\neg P\land\neg Q\land\neg R)
\lor(\neg P\land\neg Q\land R)
\lor(\neg P\land Q\land\neg R)
\lor(P\land Q\land R).
$$

It simplifies to

$$
(\neg P\land(\neg Q\lor\neg R))\lor(P\land Q\land R).
$$

For

$$
\varphi_3=(P\oplus Q)\implies R,
$$

XOR is true on exactly one of $P,Q$, so one DNF is

$$
(P\land Q)
\lor(\neg P\land\neg Q)
\lor R.
$$

A CNF, derived from the two false rows $(T,F,F)$ and $(F,T,F)$, is

$$
(\neg P\lor Q\lor R)
\land(P\lor\neg Q\lor R).
$$

Atoms and negated atoms are literals. Each parenthesized disjunction in the CNFs is a clause. Each parenthesized conjunction in the DNFs is a term.

Canonical forms include one row-selecting or row-excluding component per relevant row. A shortest form may combine several rows and be much smaller. Distribution can multiply component counts, which is why normal-form expansion may grow rapidly.

### Verification

Evaluating each original and each displayed form on all eight valuations gives identical columns. For $\varphi_3$, only $(T,F,F)$ and $(F,T,F)$ are false, exactly as its two CNF clauses encode.

### Common wrong turn

Do not negate implication as $\neg P\implies\neg Q$. The correct first step for $\neg(P\implies Q)$ is $P\land\neg Q$.

## E0.05.05 Test validity and expose fallacies

### Key idea

An argument is invalid only when one shared valuation makes all premises true and the conclusion false.

### Reasoning

| Item | Classification | Rule or countervaluation |
|---:|---|---|
| 1 | valid | modus ponens |
| 2 | valid | modus tollens |
| 3 | invalid | $P=F,Q=T$ |
| 4 | invalid | $P=F,Q=T$ |
| 5 | valid | disjunctive syllogism |
| 6 | valid | hypothetical syllogism |
| 7 | valid | $Q\lor\neg Q$ is a tautology |
| 8 | invalid | $P=F,Q=F,R=T$ |

A valid argument with false premises and false conclusion is:

1. If $10$ is prime, then $10$ is odd.
2. $10$ is prime.
3. Therefore $10$ is odd.

Its form is modus ponens. Both premises and the conclusion are false.

An invalid argument with actually true statements is:

1. Paris is in France.
2. Therefore Rome is in Italy.

Treating the claims as independent atoms, a valuation can keep the premise true and set the conclusion atom false, so the form is invalid despite the actual truths.

A sound ordinary argument is:

1. If an integer is divisible by $4$, it is even.
2. $12$ is divisible by $4$.
3. Therefore $12$ is even.

Validity depends on the impossibility of true premises and false conclusion, not on actual premise truth. Ordinary soundness adds actual true premises. Deductive-system soundness instead states that every formally derivable consequence in the system is semantically valid.

### Verification

Each invalid row makes every listed premise true and the conclusion false. The valid rows correspond to truth-preserving forms or a tautological conclusion.

### Common wrong turn

Do not reject item 7 because the premise is irrelevant. Any tautology follows semantically from any premise set in classical logic.

## E0.05.06 Audit predicates, domains, and variables

### Key idea

Syntax determines open versus closed form. An interpretation supplies predicate meanings; an assignment supplies values for free variables.

### Reasoning

| Formula | Atomic? | Open or sentence | Free variables | Bound variables |
|---|---:|---|---|---|
| $E(x)$ | yes | open | $x$ | none |
| $E(4)$ | yes | sentence | none | none |
| $\forall x\,E(x)$ | no | sentence | none | $x$ |
| $\exists y\,L(x,y)$ | no | open | $x$ | $y$ |
| $\forall x\exists y\,L(x,y)$ | no | sentence | none | $x,y$ |
| shadowed formula | no | open | $z$ | both scopes named $x$ |

Over $D=\{0,1,2\}$ with ordinary evenness and order:

- $E(x)$ is true for assignments $x=0,2$ and false for $x=1$.
- $E(4)$ requires a language whose numeral $4$ denotes an object. If constants must denote inside $D$, this interpretation must either include $4$ or explicitly interpret the symbol `4` as a member of $D$. Under ordinary arithmetic, enlarge the domain. This catches an important interpretation mismatch.
- $\forall x\,E(x)$ is false because $1$ is odd.
- $\exists y\,L(x,y)$ is true for $x=0,1$ and false for $x=2$.
- $\forall x\exists y\,L(x,y)$ is false because no domain member exceeds $2$.

$\exists x(x^2=2)$ is false over $\mathbb{Q}$ and true over $\mathbb{R}$, witnessed by $\sqrt2$ or $-\sqrt2$.

$E(x)$ lacks standalone truth because changing the assignment to $x$ changes its satisfaction. The shadowed formula safely becomes

$$
\forall x\,(E(x)\lor\exists y\,L(y,z)).
$$

If empty domains were allowed, every universal sentence over the empty domain would be vacuously true and every existential sentence false. This module uses nonempty first-order domains.

One explicit interpretation is:

$$
D=\{a,b,c\},
\quad
c^{\mathcal M}=b,
\quad
P^{\mathcal M}=\{a,c\},
\quad
R^{\mathcal M}=\{(a,b),(b,c)\}.
$$

### Verification

Each sentence has no free-variable dependence. Every predicate extension has the right arity: $P^{\mathcal M}\subseteq D$ and $R^{\mathcal M}\subseteq D^2$.

### Common wrong turn

Do not evaluate a numeral under an "ordinary arithmetic" interpretation whose domain omits that numeral. Domains and symbol denotations must be coherent.

## E0.05.07 Translate restricted English

### Key idea

Universal restrictions exclude counterexamples with implication. Existential restrictions demand one object satisfying both type and property with conjunction.

### Reasoning

The translations are:

1. $\forall x\,(S(x)\implies P(x))$.
2. $\exists x\,(S(x)\land P(x))$.
3. $\forall x\,(S(x)\implies\neg P(x))$, equivalently $\neg\exists x\,(S(x)\land P(x))$.
4. $\exists x\,(S(x)\land\neg P(x))$.
5. $\forall x\,(R(x)\implies\exists y\,(S(y)\land M(x,y)))$.
6. $\exists y\,(S(y)\land\forall x\,(R(x)\implies M(x,y)))$.
7. $\neg\exists x\,(R(x)\land\forall y\,(S(y)\implies M(x,y)))$.
8. $\exists!x\,(R(x)\land M(x,a))$.
9. $\forall x\,((S(x)\land R(x))\implies M(x,x))$.
10. $\forall x\forall y\,((M(x,y)\land R(y))\implies P(x))$.

For a countermodel to $\forall x(S(x)\land P(x))$ as a translation of item 1, include one programmer who is not a student. The intended universal remains true if every student is a programmer, but the mistranslation is false because not everyone is a student.

For a countermodel to $\exists x(S(x)\implies P(x))$ as item 2, use a domain with one nonstudent and no student programmers. The nonstudent vacuously satisfies the implication, making the mistranslation true while the intended existential is false.

If the domain is already all students, items 1 through 4 become

$$
\forall x\,P(x),
\quad
\exists x\,P(x),
\quad
\forall x\,\neg P(x),
\quad
\exists x\,\neg P(x).
$$

Item 6 could be read as one shared student or, in looser English, a possibly different student per researcher. We chose one shared student. Item 8 takes "exactly one" to modify researcher, not mentoring event. Item 10 takes "only programmers" to restrict mentors of researchers.

### Verification

Each universal type restriction appears as an antecedent. Each existential type restriction is conjoined with its target property. Formula 7 rules out any researcher who mentors all students.

### Common wrong turn

Do not write item 5 as $\exists y\forall x$ unless one student must be mentored by every researcher. That changes witness dependency.

## E0.05.08 Negate nested quantifiers mechanically

### Key idea

Cross one operator per line. Flip quantifiers, apply De Morgan, and replace negated implication with antecedent plus negated consequent.

### Reasoning

First:

$$
\begin{aligned}
\neg\forall x(A(x)\implies B(x))
&\equiv\exists x\neg(A(x)\implies B(x))\\
&\equiv\exists x(A(x)\land\neg B(x)).
\end{aligned}
$$

There is an $A$ that is not a $B$.

Second:

$$
\begin{aligned}
\neg\exists x(A(x)\land\forall yR(x,y))
&\equiv\forall x\neg(A(x)\land\forall yR(x,y))\\
&\equiv\forall x(\neg A(x)\lor\neg\forall yR(x,y))\\
&\equiv\forall x(\neg A(x)\lor\exists y\neg R(x,y)).
\end{aligned}
$$

Every object is not an $A$, or it fails to relate to some $y$.

Third:

$$
\begin{aligned}
\neg\forall x\exists y(P(x,y)\implies Q(y))
&\equiv\exists x\forall y\neg(P(x,y)\implies Q(y))\\
&\equiv\exists x\forall y(P(x,y)\land\neg Q(y)).
\end{aligned}
$$

Fourth already begins with negation:

$$
\begin{aligned}
\neg\exists x\forall y(P(x)\lor\neg R(x,y))
&\equiv\forall x\exists y\neg(P(x)\lor\neg R(x,y))\\
&\equiv\forall x\exists y(\neg P(x)\land R(x,y)).
\end{aligned}
$$

Fifth:

$$
\begin{aligned}
\neg((\exists xP(x))\implies(\forall yQ(y)))
&\equiv(\exists xP(x))\land\neg\forall yQ(y)\\
&\equiv(\exists xP(x))\land(\exists y\neg Q(y)).
\end{aligned}
$$

For unique existence, expand first:

$$
\exists x(P(x)\land\forall y(P(y)\implies y=x)).
$$

Its negation is

$$
\forall x(\neg P(x)\lor\exists y(P(y)\land y\ne x)).
$$

Equivalently, unique existence fails because no $P$ exists or because two distinct $P$ objects exist:

$$
(\forall x\neg P(x))
\lor
\exists y\exists z(P(y)\land P(z)\land y\ne z).
$$

### Verification

In each derivation, the number and order of quantifiers remain visible, every crossed quantifier flips, and final negations apply only to atoms.

### Common wrong turn

Do not swap variable names while negating. Quantifier type flips, but order and binding structure remain until a justified renaming.

## E0.05.09 Compare quantifier orders and witnesses

### Key idea

Enumerate each finite relation exactly once. The shared-witness statement is stronger than the dependent-witness statement.

### Reasoning

A standard-library implementation is:

```python
from itertools import product


def forall(domain, predicate):
    return all(predicate(value) for value in domain)


def exists(domain, predicate):
    return any(predicate(value) for value in domain)


left = (0, 1, 2)
right = ("a", "b")
edges = tuple(product(left, right))


def relation_from_bits(bits):
    return {
        edge for edge, included in zip(edges, bits) if included
    }


def dependent_witness(relation):
    return forall(
        left,
        lambda x: exists(right, lambda y: (x, y) in relation),
    )


def shared_witness(relation):
    return exists(
        right,
        lambda y: forall(left, lambda x: (x, y) in relation),
    )


counts = {(False, False): 0, (False, True): 0,
          (True, False): 0, (True, True): 0}
relations = []
for bits in product((False, True), repeat=len(edges)):
    relation = relation_from_bits(bits)
    result = (dependent_witness(relation), shared_witness(relation))
    counts[result] += 1
    relations.append(relation)
    assert not result[1] or result[0]

assert counts == {
    (False, False): 37,
    (False, True): 0,
    (True, False): 12,
    (True, True): 15,
}

separating = sorted(
    (
        relation for relation in relations
        if dependent_witness(relation) and not shared_witness(relation)
    ),
    key=lambda relation: (len(relation), sorted(relation)),
)[0]

assert separating == {(0, "a"), (1, "a"), (2, "b")}
witnesses = {
    x: next(y for y in right if (x, y) in separating)
    for x in left
}
assert witnesses == {0: "a", 1: "a", 2: "b"}

predicate = lambda x, y: x <= y
assert forall(left, lambda x: forall(left, lambda y: predicate(x, y))) == (
    forall(left, lambda y: forall(left, lambda x: predicate(x, y)))
)
assert exists(left, lambda x: exists(left, lambda y: predicate(x, y))) == (
    exists(left, lambda y: exists(left, lambda x: predicate(x, y)))
)

empty_right = ()
assert not forall(
    left,
    lambda x: exists(empty_right, lambda y: True),
)
assert not exists(
    empty_right,
    lambda y: forall(left, lambda x: True),
)
```

The smallest separating relations have three edges because each of three left objects needs an outgoing edge. The deterministic one shown uses `a` for $0$ and $1$, then `b` for $2$. Neither `a` nor `b` reaches all three left objects.

The exhaustive run proves the counts and implication for every relation on these exact domains. One separating relation disproves the proposed logical equivalence in general. The empty-right experiment is valid Python behavior but not a standard first-order model under this module's nonempty-domain convention.

### Verification

The four counts sum to $64=2^6$. The impossible category `(False, True)` has count zero, confirming that a shared witness always supplies each dependent witness.

### Common wrong turn

Do not call the two formulas equivalent because both are true for the universal relation. Equivalence requires agreement in every interpretation.

## E0.05.10 Express unique existence

### Key idea

Exactly one means at least one plus at most one. The two standard expansions package those requirements differently.

### Reasoning

Assume

$$
\exists x(P(x)\land\forall y(P(y)\implies y=x)).
$$

Choose its witness $a$. Then $P(a)$, establishing existence. If $P(y)$ and $P(z)$, the uniqueness clause gives $y=a$ and $z=a$, hence $y=z$. This proves the second formulation.

Conversely, assume

$$
(\exists xP(x))\land
\forall y\forall z((P(y)\land P(z))\implies y=z).
$$

Choose an existence witness $a$. For any $y$ with $P(y)$, at-most-one gives $y=a$. Therefore

$$
P(a)\land\forall y(P(y)\implies y=a),
$$

which supplies the first expansion.

The at-most-one clause alone is vacuously true when no object satisfies $P$, so it cannot establish existence.

For a binary operation $\circ$, exactly one identity is:

$$
\exists!e\,\forall x\,((e\circ x=x)\land(x\circ e=x)).
$$

Every account has exactly one primary owner:

$$
\forall a\,(Account(a)\implies\exists!o\,(Person(o)\land PrimaryOwner(o,a))).
$$

This differs from

$$
\exists!o\,(Person(o)\land\forall a(Account(a)\implies PrimaryOwner(o,a))),
$$

which requires one unique person to own every account.

A separating model has accounts $a_1,a_2$, owners $o_1,o_2$, and relation

$$
\{(o_1,a_1),(o_2,a_2)\}.
$$

Each account has a unique owner, but no one owner has both accounts.

Negating the first account formula yields a counterexample account with either no primary owner or at least two distinct primary owners.

### Verification

The equivalence proof establishes both directions. The finite model has one relation pair per account and no owner related to every account.

### Common wrong turn

Do not move $\exists!o$ in front of $\forall a$. That changes per-account uniqueness into one global owner.

## E0.05.11 Implement an evaluator and countermodel finder

### Key idea

Keep the AST, valuation generation, and semantic evaluation as separate functions. Validity is exhaustive absence of a countervaluation.

### Reasoning

One complete implementation is:

```python
from itertools import product


def Not(value): return ("not", value)
def And(left, right): return ("and", left, right)
def Or(left, right): return ("or", left, right)
def Xor(left, right): return ("xor", left, right)
def Implies(left, right): return ("implies", left, right)
def Iff(left, right): return ("iff", left, right)


def atoms(formula):
    if isinstance(formula, str):
        return {formula}
    if formula[0] == "not":
        return atoms(formula[1])
    return atoms(formula[1]) | atoms(formula[2])


def evaluate(formula, valuation):
    if isinstance(formula, str):
        return bool(valuation[formula])
    operator = formula[0]
    if operator == "not":
        return not evaluate(formula[1], valuation)
    left = evaluate(formula[1], valuation)
    right = evaluate(formula[2], valuation)
    if operator == "and": return left and right
    if operator == "or": return left or right
    if operator == "xor": return left != right
    if operator == "implies": return (not left) or right
    if operator == "iff": return left == right
    raise ValueError(f"unknown operator: {operator}")


def valuations(formulas):
    names = sorted(set().union(*(atoms(formula) for formula in formulas)))
    for values in product((False, True), repeat=len(names)):
        yield dict(zip(names, values))


def truth_rows(formula):
    return [(v, evaluate(formula, v)) for v in valuations([formula])]


def classify(formula):
    column = [result for _, result in truth_rows(formula)]
    if all(column): return "tautology"
    if not any(column): return "contradiction"
    return "contingent"


def satisfiable(formulas):
    return next((
        v for v in valuations(formulas)
        if all(evaluate(formula, v) for formula in formulas)
    ), None)


def equivalent(left, right):
    return all(
        evaluate(left, v) == evaluate(right, v)
        for v in valuations([left, right])
    )


def countermodel(premises, conclusion):
    return next((
        v for v in valuations([*premises, conclusion])
        if all(evaluate(premise, v) for premise in premises)
        and not evaluate(conclusion, v)
    ), None)


def valid(premises, conclusion):
    return countermodel(premises, conclusion) is None


def canonical_cnf(formula):
    names = sorted(atoms(formula))
    false_rows = [
        valuation for valuation in valuations([formula])
        if not evaluate(formula, valuation)
    ]
    if not false_rows:
        return Or(names[0], Not(names[0]))
    clauses = []
    for valuation in false_rows:
        literals = [
            Not(name) if valuation[name] else name for name in names
        ]
        clause = literals[0]
        for literal in literals[1:]:
            clause = Or(clause, literal)
        clauses.append(clause)
    result = clauses[0]
    for clause in clauses[1:]:
        result = And(result, clause)
    return result


P, Q, R = "P", "Q", "R"
connectives = [And, Or, Xor, Implies, Iff]
expected = {
    "and": [False, False, False, True],
    "or": [False, True, True, True],
    "xor": [False, True, True, False],
    "implies": [True, True, False, True],
    "iff": [True, False, False, True],
}
for constructor in connectives:
    formula = constructor(P, Q)
    column = [value for _, value in truth_rows(formula)]
    assert column == expected[formula[0]]

assert classify(Or(P, Not(P))) == "tautology"
assert classify(And(P, Not(P))) == "contradiction"
assert classify(Implies(P, Q)) == "contingent"
assert equivalent(Implies(P, Q), Or(Not(P), Q))
assert equivalent(Implies(P, Q), Implies(Not(Q), Not(P)))
assert equivalent(Not(Implies(P, Q)), And(P, Not(Q)))
assert satisfiable([P, Not(P)]) is None
assert valid([Implies(P, Q), P], Q)
assert valid([Implies(P, Q), Not(Q)], Not(P))
assert valid([Implies(P, Q), Implies(Q, R)], Implies(P, R))
assert valid([Or(P, Q), Not(P)], Q)
assert countermodel([Implies(P, Q), Q], P) == {"P": False, "Q": True}
assert countermodel([Implies(P, Q), Not(P)], Not(Q)) == {
    "P": False, "Q": True
}
assert not valid([P], Q)

try:
    evaluate(("mystery", P, Q), {"P": True, "Q": True})
    raise AssertionError("unknown operator was accepted")
except ValueError:
    pass

formulas = [
    P, Not(P), And(P, Q), Or(P, Q), Xor(P, Q), Implies(P, Q),
    Iff(P, Q), And(Implies(P, Q), R), Or(Xor(P, Q), R),
    Implies(Xor(P, Q), R),
]
for formula in formulas:
    assert equivalent(formula, canonical_cnf(formula))
```

For $n$ distinct atoms, exhaustive valuation checks use $2^n$ rows. Evaluation cost also depends on AST size, so a direct bound is $O(2^n m)$ for a formula of $m$ nodes. Canonical CNF may contain one $n$-literal clause per false row.

The implementation decides semantic questions exactly for its finite propositional input. It does not parse arbitrary text, decide unrestricted first-order validity, implement SAT search optimizations, or establish facts about intended real-world meanings.

### Verification

All required connectives receive exact four-row columns. Every validity check shares one valuation across premises and conclusion. CNF equivalence is exhaustively asserted for ten formulas.

### Common wrong turn

Do not return `False` as the only invalidity result. A concrete deterministic countervaluation is the evidence that diagnoses the failed inference.

## E0.05.12 Critique logic, AI, and source claims

### Key idea

The paragraph collapses syntax, semantics, consequence, deduction, metatheory, software behavior, and empirical claims. Repair each in its own layer with appropriate evidence.

### Reasoning

A diagnosis table includes:

| Claim | Layer | Diagnosis | Repair | Evidence |
|---|---|---|---|---|
| logic proves statements true | semantics/deduction | overbroad | a system derives formulas; interpretations assign truth | SEP |
| true conclusion makes validity | consequence | false | validity forbids true premises with false conclusion | SEP |
| valid arguments have true premises | consequence | false | validity is conditional on premise-satisfying cases | counterexample |
| satisfiable means tautology | semantics | false | some model versus every model | truth table |
| all $A$ uses conjunction | translation | false | use $\forall x(A\implies B)$ | derivation |
| some $A$ uses implication | translation | false | use $\exists x(A\land B)$ | countermodel |
| mixed quantifiers commute | semantics | false | witnesses may depend on earlier variables | finite relation |
| negated implication is implication | semantics | false | $\neg(P\implies Q)\equiv P\land\neg Q$ | truth table |
| one example permits UG | deduction | side condition violated | object must be arbitrary | SEP |
| existential name is permanent | deduction | side condition violated | use fresh local witness | SEP |
| Python operators always return bool | software | false | `and`/`or` return operands | Python behavior |
| SAT decides all FOL validity | computation | false | propositional SAT and FOL validity differ | scope statement |
| neural output proves theorem-prover internals | empirical AI | unsupported | behavioral output does not identify mechanism | empirical evidence needed |
| both soundness senses identical | terminology | equivocation | distinguish argument and system soundness | SEP plus definitions |
| completeness covers true English | metatheory | false | it relates semantic validity to derivability for a formal language/system | SEP |
| two sources prove every claim | evidence | unsupported | each source supports specific nearby claims | source ledger |

Counterexamples include:

- True conclusion but invalid: $P\therefore Q$ with actual true sentences, while valuation $P=T,Q=F$ defeats the form.
- Valid with false premise: $P,P\implies Q\therefore Q$ remains valid when intended $P,Q$ are false.
- Satisfiable but not tautological: $P$.
- Wrong existential restriction: with one non-$A$ object, $A(x)\implies B(x)$ is true although no $A\land B$ witness exists.
- Mixed quantifiers: over integers, $\forall x\exists y(y>x)$ is true and $\exists y\forall x(y>x)$ false.
- Negated implication: $P=T,Q=F$ makes $\neg(P\implies Q)$ true, while common proposed implication negations fail on other rows.
- Bad universal generalization: $2$ is even and has an even square, but not every integer has an even square.

Python directly demonstrates operand return:

```python
assert ("left" and "right") == "right"
assert ("left" or "right") == "left"
assert ([] or [1, 2]) == [1, 2]
assert not isinstance("left" and "right", bool)
```

A corrected paragraph under 220 words is:

> Formal logic separates well-formed formulas, truth under interpretations, semantic consequence, and derivation under stated rules. A conclusion can be actually true while the argument for it is invalid, and a valid argument can have false premises. An ordinary argument is sound when it is valid and its premises are actually true. A deductive system is sound when every derivable consequence is semantically valid. Satisfiable means true in at least one model; tautological or logically valid means true in every relevant model. With a broad domain, "all A are B" is $\forall x(A(x)\implies B(x))$, while "some A are B" is $\exists x(A(x)\land B(x))$. Mixed quantifiers generally do not commute because later witnesses may depend on earlier variables. Negating implication yields $P\land\neg Q$. Universal generalization requires an arbitrary object, and existential elimination uses a fresh local witness. Python's `and` and `or` short-circuit and return operands, so a formal evaluator should produce explicit Booleans. Propositional SAT and bounded model checks do not decide general first-order validity. Neural-network behavior alone does not establish that its internal mechanism is classical deduction. Soundness and completeness are precise claims about a chosen formal system and semantics, not about every true English sentence.

A source ledger can record:

| URL | Supported claim |
|---|---|
| `https://plato.stanford.edu/entries/logic-classical/` | language, deduction, semantics, validity, soundness, completeness, alternatives |
| `https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html` | quantifier use, negation, connectives, classical steps |
| `https://web.stanford.edu/class/cs103/` | course scope only |
| `https://web.stanford.edu/class/cs103/tools/truth-table-tool/` | propositional truth-table generation only |
| `https://docs.python.org/3/reference/expressions.html#boolean-operations` | short-circuit operand-return behavior |

A claim about neural internals requires experiments or mechanistic evidence that discriminates classical deduction from pattern completion, retrieval, tool use, or other processes. Similar outputs do not establish identical mechanisms.

All exercises, examples, tables, diagrams, and figures in this module are original. Stanford materials are linked for study and were not copied.

### Verification

The corrected paragraph preserves each distinction and makes no claim broader than its evidence. Every mathematical repair has a counterexample, truth condition, or formal definition.

### Common wrong turn

Do not use a truth-table tool as evidence for a historical, software, first-order, or empirical AI claim. Match source type to claim type.

## Solution-set check

All exercise IDs and titles mirror the [exercise index](../exercises/README.md):

- E0.05.01 Parse formulas and mark scope
- E0.05.02 Build a truth table and classify
- E0.05.03 Translate implication language
- E0.05.04 Transform equivalences into CNF and DNF
- E0.05.05 Test validity and expose fallacies
- E0.05.06 Audit predicates, domains, and variables
- E0.05.07 Translate restricted English
- E0.05.08 Negate nested quantifiers mechanically
- E0.05.09 Compare quantifier orders and witnesses
- E0.05.10 Express unique existence
- E0.05.11 Implement an evaluator and countermodel finder
- E0.05.12 Critique logic, AI, and source claims

[Back to module](../README.md) | [Exercise set](../exercises/README.md)
