# Exercises for §0.05 Logic and Quantifiers

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Hints become progressively more specific but do not state final answers. Difficulty follows the project's 1 through 5 scale.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.05.01 | Parse formulas and mark scope | conceptual | 2 | parse formulas and operator scope | 25 min |
| E0.05.02 | Build a truth table and classify | calculation | 2 | evaluate and classify connectives | 30 min |
| E0.05.03 | Translate implication language | translation | 3 | distinguish implication variants | 30 min |
| E0.05.04 | Transform equivalences into CNF and DNF | derivation | 3 | apply equivalences and normal forms | 40 min |
| E0.05.05 | Test validity and expose fallacies | proof and countermodel | 3 | distinguish validity from truth | 40 min |
| E0.05.06 | Audit predicates, domains, and variables | conceptual | 3 | interpret first-order formulas | 35 min |
| E0.05.07 | Translate restricted English | translation | 3 | formalize quantified statements | 40 min |
| E0.05.08 | Negate nested quantifiers mechanically | derivation | 3 | push negation to predicates | 40 min |
| E0.05.09 | Compare quantifier orders and witnesses | experiment | 4 | diagnose witness dependency | 45 min |
| E0.05.10 | Express unique existence | derivation | 3 | separate existence and uniqueness | 35 min |
| E0.05.11 | Implement an evaluator and countermodel finder | implementation | 4 | exhaust finite valuations | 60 min |
| E0.05.12 | Critique logic, AI, and source claims | critique | 4 | audit terminology and evidence | 50 min |

## E0.05.01 Parse formulas and mark scope

- **Type:** conceptual
- **Difficulty:** 2
- **Objective:** Identify main operators, subformulas, precedence, quantifier scope, and free or bound variables.
- **Estimated time:** 25 minutes
- **Allowed tools:** Pencil and paper; no parser or truth-table tool.
- **Assumptions:** Use the module's local precedence convention only where parentheses are absent.

### Problem

For each expression below:

1. add enough parentheses to make the parse explicit;
2. name the main operator;
3. draw or describe its parse tree;
4. list every atomic formula;
5. for quantified formulas, mark each variable occurrence free or bound and identify its binder.

$$
P\lor Q\land\neg R,
$$

$$
(P\lor Q)\implies(\neg R\land S),
$$

$$
\neg P\implies Q\iff R,
$$

$$
\forall x\,(A(x)\implies\exists y\,R(x,y))\land B(y),
$$

$$
\forall x\,(P(x)\lor\exists x\,(Q(x)\land R(x,z))).
$$

Then produce two valuations that separate

$$
P\lor(Q\land R)
$$

from

$$
(P\lor Q)\land R.
$$

Finally, rewrite the shadowed-variable formula with distinct bound names without changing which occurrences are bound together.

**Deliverable:** Five explicit parses, variable ledger, separating valuations, and renamed formula.

<details>
<summary>Hint 1</summary>

Find the lowest-precedence unparenthesized operator first. Quantifiers bind their following formula only as far as the grammar or parentheses permit.
</details>

<details>
<summary>Hint 2</summary>

For the final formula, the inner quantifier introduces a new variable that shadows the outer one. Rename only the occurrences governed by the inner quantifier.
</details>

## E0.05.02 Build a truth table and classify

- **Type:** calculation
- **Difficulty:** 2
- **Objective:** Compute exact truth values for inclusive OR, XOR, implication, and biconditional, then classify formulas.
- **Estimated time:** 30 minutes
- **Allowed tools:** Hand calculation first; Stanford's truth-table tool or a short program for verification afterward.
- **Assumptions:** $\lor$ is inclusive and $\oplus$ is XOR.

### Problem

Construct one eight-row table for $P,Q,R$ with columns for:

$$
P\lor Q,
\qquad
P\oplus Q,
\qquad
P\implies Q,
$$

$$
(P\oplus Q)\implies R,
\qquad
(P\implies Q)\iff(\neg Q\implies\neg P),
$$

$$
(P\land\neg P)\lor R.
$$

For each final formula:

1. state whether it is satisfiable;
2. classify it as tautology, contradiction, or contingent;
3. list all satisfying valuations or describe them exactly;
4. identify one row that distinguishes inclusive OR from XOR;
5. explain why a formula may be satisfiable without being tautological.

**Deliverable:** Complete truth table, classifications, and short explanations.

<details>
<summary>Hint 1</summary>

Implication is false only on $T\to F$. A biconditional is true when both sides have the same truth value.
</details>

<details>
<summary>Hint 2</summary>

The contrapositive has the same truth column as the original implication. Simplify $(P\land\neg P)\lor R$ before classifying it.
</details>

## E0.05.03 Translate implication language

- **Type:** translation
- **Difficulty:** 3
- **Objective:** Translate if, only if, if and only if, necessary, and sufficient language and distinguish converse, inverse, and contrapositive.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper.
- **Assumptions:** Let $A$ mean authenticated, $Z$ mean authorized, and $G$ mean access is granted.

### Problem

Translate each sentence into a formula:

1. Access is granted only if the user is authenticated.
2. Authentication is sufficient for access.
3. Authentication is necessary but not sufficient for access.
4. Access is granted if the user is authenticated and authorized.
5. Access is granted if and only if the user is authenticated and authorized.
6. Unless the user is authenticated, access is not granted. State your reading of "unless."
7. Authorization is required whenever access is granted.

For the claim $G\implies A$:

8. write its converse, inverse, and contrapositive in symbols and English;
9. identify which are logically equivalent;
10. give a tiny access-policy interpretation where the original is true and the converse false;
11. explain why causal or temporal meaning is not supplied by material implication alone.

**Deliverable:** Seven translations, a four-form comparison table, and one counterinterpretation.

<details>
<summary>Hint 1</summary>

"$P$ only if $Q$" means $P\implies Q$. "$P$ if $Q$" means $Q\implies P$.
</details>

<details>
<summary>Hint 2</summary>

"Necessary but not sufficient" requires one implication plus the denial of the reverse implication. A policy with an authenticated but unauthorized user can separate necessity from sufficiency.
</details>

## E0.05.04 Transform equivalences into CNF and DNF

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Use De Morgan, implication elimination, biconditional expansion, and double negation to produce and verify normal forms.
- **Estimated time:** 40 minutes
- **Allowed tools:** Symbolic work first; truth tables or the module evaluator for verification.
- **Assumptions:** A literal is an atom or negated atom; clauses are disjunctions and terms are conjunctions.

### Problem

For each formula, eliminate $\implies$ and $\iff$, push negations to atoms, and produce both a CNF and a DNF:

$$
\varphi_1=\neg(P\implies(Q\lor R)),
$$

$$
\varphi_2=P\iff(Q\land R),
$$

$$
\varphi_3=(P\oplus Q)\implies R.
$$

Then:

1. label every literal, clause, and term in your final forms;
2. derive one form algebraically and one from truth-table rows;
3. verify each result under all eight valuations;
4. distinguish a canonical normal form from a shortest normal form;
5. explain why blindly distributing can cause a much larger formula;
6. state which false rows determine the canonical CNF of $\varphi_3$.

**Deliverable:** Transformation chains, final CNF and DNF forms, and exhaustive verification summary.

<details>
<summary>Hint 1</summary>

Use $P\implies Q\equiv\neg P\lor Q$ and $P\iff Q\equiv(P\implies Q)\land(Q\implies P)$.
</details>

<details>
<summary>Hint 2</summary>

For canonical DNF, create one selecting term per true row. For canonical CNF, create one excluding clause per false row.
</details>

## E0.05.05 Test validity and expose fallacies

- **Type:** proof and countermodel
- **Difficulty:** 3
- **Objective:** Decide semantic validity, produce countervaluations, and separate validity, truth, and argument soundness.
- **Estimated time:** 40 minutes
- **Allowed tools:** Hand reasoning; exhaustive evaluator for verification.
- **Assumptions:** Treat letters as independent propositional atoms unless an interpretation is explicitly supplied.

### Problem

Classify each argument as valid or invalid. For a valid argument, name a rule or give a semantic justification. For an invalid argument, provide a valuation making every premise true and the conclusion false.

1. $P\implies Q,\ P\therefore Q$.
2. $P\implies Q,\ \neg Q\therefore\neg P$.
3. $P\implies Q,\ Q\therefore P$.
4. $P\implies Q,\ \neg P\therefore\neg Q$.
5. $P\lor Q,\ \neg P\therefore Q$.
6. $P\implies Q,\ Q\implies R\therefore P\implies R$.
7. $P\therefore Q\lor\neg Q$.
8. $P\implies Q,\ R\therefore Q$.

Then analyze:

9. Give a valid argument with false premises and a false conclusion.
10. Give an invalid argument whose actual premise and conclusion are all true.
11. Give a sound ordinary argument.
12. Explain why "valid + false premises" remains valid but is not sound.
13. Explain how soundness of a deductive system differs from soundness of one ordinary argument.

**Deliverable:** Classification table, countervaluation ledger, and five-sentence terminology audit.

<details>
<summary>Hint 1</summary>

Only rows with every premise true can challenge validity. The conclusion need not be true on rows where a premise is false.
</details>

<details>
<summary>Hint 2</summary>

For affirming the consequent use $P=F,Q=T$. For denying the antecedent use $P=F,Q=T$ as well.
</details>

## E0.05.06 Audit predicates, domains, and variables

- **Type:** conceptual
- **Difficulty:** 3
- **Objective:** Distinguish propositions, predicates, open formulas, sentences, domains, interpretations, and assignments.
- **Estimated time:** 35 minutes
- **Allowed tools:** Pencil and paper.
- **Assumptions:** Standard first-order domains are nonempty.

### Problem

Let $E(x)$ mean "$x$ is even" and $L(x,y)$ mean "$x<y$."

For each expression, classify it as an atomic or compound formula and as open or a sentence. List free and bound variables.

$$
E(x),
\qquad
E(4),
\qquad
\forall x\,E(x),
$$

$$
\exists y\,L(x,y),
\qquad
\forall x\,\exists y\,L(x,y),
$$

$$
\forall x\,(E(x)\lor\exists x\,L(x,z)).
$$

Then:

1. evaluate the first five over $D=\{0,1,2\}$ for every needed assignment;
2. compare $\exists x\,(x^2=2)$ over $\mathbb{Q}$ and $\mathbb{R}$;
3. explain why $E(x)$ has no standalone truth without an assignment;
4. rename the shadowed variable safely;
5. state how the empty-domain convention would affect universal and existential sentences, then restate this module's convention;
6. specify an interpretation for a constant $c$, unary predicate $P$, and binary predicate $R$ over a three-object domain.

**Deliverable:** Classification table, evaluation ledger, two-domain comparison, and explicit finite interpretation.

<details>
<summary>Hint 1</summary>

A quantifier binds only matching occurrences in its scope. A formula is a sentence exactly when it has no free variables.
</details>

<details>
<summary>Hint 2</summary>

An interpretation supplies the domain and meanings of nonlogical symbols. An assignment supplies values for free variables.
</details>

## E0.05.07 Translate restricted English

- **Type:** translation
- **Difficulty:** 3
- **Objective:** Translate universal and existential restrictions correctly and make domain assumptions explicit.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper.
- **Assumptions:** Unless restated, the domain is all people. Use $S(x)$ for student, $R(x)$ for researcher, $P(x)$ for programmer, and $M(x,y)$ for mentors.

### Problem

Translate:

1. Every student is a programmer.
2. Some student is a programmer.
3. No student is a programmer.
4. Some student is not a programmer.
5. Every researcher mentors some student.
6. Some student is mentored by every researcher.
7. No researcher mentors every student.
8. Exactly one researcher mentors Ada, using a constant $a$ for Ada.
9. Every student who is a researcher mentors themselves.
10. Only programmers mentor researchers.

For sentences 1 through 4:

11. explain why universal restrictions use implication and existential restrictions use conjunction;
12. give countermodels to the two swapped-connective mistranslations;
13. rewrite the formulas when the domain is already all students;
14. identify any natural-language ambiguity in sentences 6, 8, or 10 and state your chosen reading.

**Deliverable:** Ten formulas, two countermodels, domain-relative rewrites, and ambiguity notes.

<details>
<summary>Hint 1</summary>

"Only programmers mentor researchers" restricts the mentor, not necessarily the person being mentored.
</details>

<details>
<summary>Hint 2</summary>

"No researcher mentors every student" begins by denying that any researcher has the universal mentoring property.
</details>

## E0.05.08 Negate nested quantifiers mechanically

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Negate formulas by flipping quantifiers and applying connective negation rules one layer at a time.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper; a formal tool only after deriving by hand.
- **Assumptions:** Use classical logic and push negation until it applies only to atomic predicates.

### Problem

Negate and simplify each formula. Show one line per operator crossed.

$$
\forall x\,(A(x)\implies B(x)),
$$

$$
\exists x\,(A(x)\land\forall y\,R(x,y)),
$$

$$
\forall x\,\exists y\,(P(x,y)\implies Q(y)),
$$

$$
\neg\exists x\,\forall y\,(P(x)\lor\neg R(x,y)),
$$

$$
(\exists x\,P(x))\implies(\forall y\,Q(y)),
$$

$$
\exists!x\,P(x).
$$

Then translate each original and negated result into careful English. For the unique-existence item, expand $\exists!$ before negating and give a readable description of the two ways uniqueness can fail.

**Deliverable:** Six mechanical derivations and paired English readings.

<details>
<summary>Hint 1</summary>

Crossing $\forall$ produces $\exists$ and a negation; crossing $\exists$ produces $\forall$ and a negation.
</details>

<details>
<summary>Hint 2</summary>

Use $\neg(P\implies Q)\equiv P\land\neg Q$. Failure of unique existence means either no witness or at least two distinct witnesses.
</details>

## E0.05.09 Compare quantifier orders and witnesses

- **Type:** experiment
- **Difficulty:** 4
- **Objective:** Compare $\forall\exists$ with $\exists\forall$ using finite relations and explicit witness dependencies.
- **Estimated time:** 45 minutes
- **Allowed tools:** Python 3 standard library only.
- **Assumptions:** Domains are finite and nonempty.

### Problem

Let $X=\{0,1,2\}$ and $Y=\{a,b\}$. A relation is a subset of $X\times Y$.

1. Implement helpers corresponding to $\forall$ and $\exists$ with `all` and `any`.
2. Enumerate all $2^6$ relations on $X\times Y$.
3. For each relation, evaluate
   $$
   \forall x\in X\,\exists y\in Y\,R(x,y)
   $$
   and
   $$
   \exists y\in Y\,\forall x\in X\,R(x,y).
   $$
4. Count relations in each pair of truth categories.
5. Find the smallest separating relation by number of pairs, using deterministic tie-breaking.
6. For that relation, report a witness choice $y_x$ for every $x$ and explain why no shared witness works.
7. Verify that the second formula implies the first for every enumerated relation.
8. Verify that adjacent universal quantifiers commute and adjacent existential quantifiers commute on at least two predicates.
9. Repeat with an empty right domain and explain why that code experiment is outside this module's standard first-order convention.
10. State exactly which conclusions are proved by exhaustive finite enumeration and which general claim is disproved by one countermodel.

**Deliverable:** Executable code, assertions, count table, witness report, and limitations.

<details>
<summary>Hint 1</summary>

Enumerate subsets by pairing the six possible edges with six Boolean inclusion decisions from `itertools.product`.
</details>

<details>
<summary>Hint 2</summary>

A separating relation needs at least one edge leaving each of the three left objects, but its edges must not all share one right endpoint.
</details>

## E0.05.10 Express unique existence

- **Type:** derivation
- **Difficulty:** 3
- **Objective:** Expand $\exists!$, prove equivalent formulations, and separate existence from at-most-one claims.
- **Estimated time:** 35 minutes
- **Allowed tools:** Pencil and paper.
- **Assumptions:** Equality has its ordinary interpretation.

### Problem

1. Expand $\exists!x\,P(x)$ as
   $$
   \exists x\left(P(x)\land\forall y\,(P(y)\implies y=x)\right).
   $$
2. Prove it equivalent to
   $$
   (\exists x\,P(x))\land
   \forall y\,\forall z\,((P(y)\land P(z))\implies y=z).
   $$
3. Explain why
   $$
   \forall y\,\forall z\,((P(y)\land P(z))\implies y=z)
   $$
   alone says "at most one," not "exactly one."
4. Formalize "there is exactly one identity element" for a binary operation $\circ$ on domain $D$.
5. Formalize "every account has exactly one primary owner" with $PrimaryOwner(o,a)$.
6. Compare
   $$
   \forall a\,\exists!o\,PrimaryOwner(o,a)
   $$
   with
   $$
   \exists!o\,\forall a\,PrimaryOwner(o,a).
   $$
7. Give a finite interpretation where the first is true and the second false.
8. Negate the first formula and describe the failure condition in plain English.

**Deliverable:** Equivalence proof, two formalizations, separating model, and negation.

<details>
<summary>Hint 1</summary>

From the first expansion, save its witness and show any two $P$ objects both equal it. In the reverse direction, combine an existence witness with the at-most-one premise.
</details>

<details>
<summary>Hint 2</summary>

Different accounts may have different unique owners. The second formula instead requires one unique person to own every account.
</details>

## E0.05.11 Implement an evaluator and countermodel finder

- **Type:** implementation
- **Difficulty:** 4
- **Objective:** Build an explicit propositional AST evaluator, classify formulas, test equivalence and validity, and return countermodels.
- **Estimated time:** 60 minutes
- **Allowed tools:** Python 3 standard library only; do not use `eval`, a parser package, or a SAT library.
- **Assumptions:** Atoms are strings and compound nodes have explicit operator tags.

### Problem

Implement an AST or explicit callable representation supporting:

- atoms;
- negation;
- conjunction;
- inclusive disjunction;
- XOR;
- material implication;
- biconditional.

Then implement:

```python
atoms(formula)
evaluate(formula, valuation)
truth_rows(formula)
classify(formula)
satisfiable(formulas)
equivalent(left, right)
countermodel(premises, conclusion)
valid(premises, conclusion)
```

Required tests:

1. exact connective truth tables;
2. excluded middle is a tautology;
3. $P\land\neg P$ is a contradiction;
4. $P\implies Q$ is contingent;
5. implication elimination and contraposition are equivalences;
6. $\neg(P\implies Q)\equiv P\land\neg Q$;
7. $\{P,\neg P\}$ is jointly unsatisfiable;
8. modus ponens, modus tollens, hypothetical syllogism, and disjunctive syllogism are valid;
9. affirming the consequent and denying the antecedent return countermodels;
10. a true conclusion is not used as a shortcut for validity;
11. deterministic atom order and countermodel output;
12. unknown operators fail loudly.

Extend the program with canonical CNF construction from false rows. Assert that the original and generated CNF agree on every valuation for at least ten formulas.

**Deliverable:** Executable implementation, assertions, sample output, complexity discussion, and limits.

<details>
<summary>Hint 1</summary>

Use `itertools.product((False, True), repeat=n)` over sorted atoms. Keep syntax constructors separate from recursive evaluation.
</details>

<details>
<summary>Hint 2</summary>

Validity fails exactly when all premises evaluate true and the conclusion evaluates false under one shared valuation.
</details>

## E0.05.12 Critique logic, AI, and source claims

- **Type:** critique
- **Difficulty:** 4
- **Objective:** Diagnose errors involving semantics, inference, AI claims, software behavior, and evidence quality.
- **Estimated time:** 50 minutes
- **Allowed tools:** Module references and directly opened authoritative sources. No generated summary counts as evidence.
- **Assumptions:** Audit claims narrowly and distinguish mathematical error from unsupported empirical assertion.

### Problem

Audit this paragraph:

> Logic proves whether statements are true. Any argument with a true conclusion is valid, while a valid argument must have true premises. Satisfiable formulas are tautologies. "All A are B" means $\forall x(A(x)\land B(x))$, and "some A are B" means $\exists x(A(x)\implies B(x))$. Because $\forall x\exists y$ and $\exists y\forall x$ use the same variables, they are equivalent. Negating implication gives another implication. Universal generalization works after checking one convenient example, and an existential witness may be named permanently. Python `and` and `or` implement formal conjunction and disjunction exactly for every object. SAT software proves all first-order validities. Neural networks are classical theorem provers because they output chains of thought. Soundness means the same thing for arguments and proof systems, and completeness means every true English sentence is provable. Stanford CS103's truth-table tool and the SEP entry prove all these claims.

1. Identify at least fifteen errors, ambiguities, or unsupported claims.
2. Create a table with columns `Claim`, `Layer`, `Diagnosis`, `Repair`, and `Evidence`.
3. Give a countervaluation or countermodel for every false equivalence or inference claim.
4. Use the 2026 SEP entry to distinguish derivability, semantic validity, soundness, and completeness.
5. Use official Python documentation or a direct Python demonstration to explain operand-return behavior of `and` and `or`.
6. Explain what a finite propositional evaluator can prove and what it cannot prove about first-order validity.
7. Rewrite the paragraph accurately in at most 220 words.
8. Submit a source ledger with every opened URL and the exact claim it supports.
9. State why a claim about neural-network internals needs empirical evidence and why behavioral output alone does not establish classical deduction.
10. Confirm that no exercise, example, or figure was copied from proprietary course material.

**Deliverable:** Audit table, counterexamples, corrected paragraph, and source ledger.

<details>
<summary>Hint 1</summary>

Sort each problem into syntax, semantics, consequence, deduction, metatheory, software behavior, or empirical AI claim before repairing it.
</details>

<details>
<summary>Hint 2</summary>

SEP soundness connects $\vdash$ to $\models$ for a deductive system. Ordinary argument soundness adds actual premise truth to validity. They are related but not identical definitions.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that your work includes:

- explicit parentheses and scope for every parsed formula;
- inclusive OR separated from XOR;
- implication false only on $T\to F$;
- converse and inverse separated from contrapositive;
- satisfiable separated from tautological;
- countermodels using one shared valuation or interpretation;
- truth, validity, ordinary soundness, and system soundness kept distinct;
- universal restrictions translated with implication;
- existential restrictions translated with conjunction;
- every free variable assigned or bound;
- mixed quantifier order treated as witness dependency;
- quantifier and implication negations performed mechanically;
- arbitrary-object and fresh-witness side conditions stated;
- finite checks limited to their declared finite space;
- every source opened before it is used as evidence.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)
