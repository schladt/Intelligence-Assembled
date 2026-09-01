# Exercises for §0.06 Proof Techniques

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Hints become progressively more specific but do not state final answers. Difficulty follows the project's 1 through 5 scale.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.06.01 | Plan proofs from logical form | planning | 2 | transform targets into proof obligations | 30 min |
| E0.06.02 | Prove directly from definitions | proof | 3 | use arbitrary objects and definitions | 35 min |
| E0.06.03 | Audit cases and WLOG | proof and critique | 3 | verify coverage and symmetry reductions | 40 min |
| E0.06.04 | Compare contraposition and contradiction | proof and critique | 3 | distinguish indirect proof routes | 40 min |
| E0.06.05 | Prove biconditionals and equivalence cycles | proof | 3 | establish every required direction | 40 min |
| E0.06.06 | Prove existence and uniqueness | proof | 4 | separate witnesses, classical existence, and uniqueness | 45 min |
| E0.06.07 | Find counterexamples and repair conjectures | experiment | 4 | disprove universals and repair claims | 50 min |
| E0.06.08 | Prove set and function equality | proof | 3 | use elementwise and pointwise equality | 40 min |
| E0.06.09 | Apply generalized pigeonhole | proof and implementation | 4 | derive and test finite capacity bounds | 50 min |
| E0.06.10 | Double count one incidence set | combinatorial proof | 4 | count one finite set in two ways | 50 min |
| E0.06.11 | Build a diagonal impossibility argument | proof | 4 | construct indexed disagreement | 45 min |
| E0.06.12 | Audit proof, code, and sources | critique | 4 | inspect dependencies and evidence boundaries | 60 min |

## E0.06.01 Plan proofs from logical form

- **Type:** planning
- **Difficulty:** 2
- **Objective:** Normalize theorem statements and turn connectives and quantifiers into explicit proof obligations.
- **Estimated time:** 30 minutes
- **Allowed tools:** Pencil and paper; §0.05 logic tables.
- **Assumptions:** Use classical logic. Do not prove the statements yet.

### Problem

For each target below, produce a proof-planning ledger with columns `Logical form`, `Arbitrary objects`, `Assumptions`, `Target`, `Candidate route`, `Useful definitions`, `Edge cases`, and `Variable provenance`.

1. For every integer $n$, if $12\mid n$, then $4\mid n$.
2. For all sets $A,B,C$, if $A\subseteq B$ and $B\subseteq C$, then $A\subseteq C$.
3. For every integer $n$, $n$ is even if and only if $n^2$ is even.
4. There exists an integer $m$ such that $m^2-m=20$.
5. There is exactly one real $x$ such that $5x-7=18$.
6. No integer has square congruent to $2$ modulo $4$.
7. For every function $f:A\to B$ and sets $S,T\subseteq A$,
   $$
   f(S\cap T)\subseteq f(S)\cap f(T).
   $$
8. Every assignment of $31$ jobs to $6$ queues places at least $6$ jobs in one queue.

Then answer:

9. Which targets naturally expose a witness?
10. Which target has two direction obligations?
11. Which target is negative, and what is the negation of the full target?
12. Which candidate routes are alternatives rather than mandatory choices?
13. For item 8, list every finite-assignment assumption needed before invoking a capacity argument.
14. State why selecting a route is not itself a proof.

**Deliverable:** Eight complete ledgers and a short route-selection commentary.

<details>
<summary>Hint 1</summary>

Expand divisibility, subset, biconditional, unique existence, and finite assignment before choosing a route.
</details>

<details>
<summary>Hint 2</summary>

For a universal implication, the ordinary opening chooses an arbitrary object and assumes the antecedent. For a biconditional, write both arrows before planning either proof.
</details>

## E0.06.02 Prove directly from definitions

- **Type:** proof
- **Difficulty:** 3
- **Objective:** Write direct universal and implication proofs with arbitrary objects, correctly scoped witnesses, and exact definition use.
- **Estimated time:** 35 minutes
- **Allowed tools:** Pencil and paper; no theorem prover.
- **Assumptions:** Use $a\mid b\iff\exists k\in\mathbb{Z}, b=ak$. An odd integer has form $2k+1$.

### Problem

Write complete direct proofs of all four claims.

1. If integers $a,b,c$ satisfy $a\mid b$ and $a\mid c$, then $a\mid(5b-2c)$.
2. The sum of two odd integers is even.
3. If $A\subseteq B$ and $B\subseteq C$, then $A\subseteq C$.
4. If $R$ and $S$ are transitive relations on $A$, their intersection $R\cap S$ is transitive.

For each proof:

5. label every variable as arbitrary, existentially obtained, or explicitly chosen;
6. identify the line that first uses each assumption;
7. identify the line that reaches the exact target definition;
8. state whether zero or an empty set requires a separate case;
9. remove any sentence that does not introduce an object, set a subgoal, or derive a needed claim.

**Deliverable:** Four proofs and a variable/dependency ledger for each.

<details>
<summary>Hint 1</summary>

For item 1, introduce separate divisibility witnesses for $b$ and $c$. For item 4, begin with arbitrary $x,y,z\in A$ satisfying both relations at the two needed pairs.
</details>

<details>
<summary>Hint 2</summary>

In item 1, factor $a$ from $5b-2c$. In item 4, use transitivity once in $R$ and once in $S$, then rebuild membership in the intersection.
</details>

## E0.06.03 Audit cases and WLOG

- **Type:** proof and critique
- **Difficulty:** 3
- **Objective:** Prove by exhaustive cases, allow harmless overlap, and justify or reject WLOG through an explicit transformation.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper; the module's finite case-coverage checker for verification.
- **Assumptions:** Real numbers satisfy trichotomy. Integers are even or odd.

### Problem

1. Prove by cases that $|x|\ge0$ for every real $x$ using cases $x\ge0$ and $x\le0$. Explain why overlap at zero is harmless.
2. Audit the alternative cases $x>0$ and $x<0$. Give the uncovered value and repair the proof.
3. Prove that $n^2+n$ is even for every integer $n$ by parity cases.
4. For real $x,y$, prove
   $$
   \max(x,y)+\min(x,y)=x+y
   $$
   using a justified WLOG reduction.
5. State the swap transformation and prove it preserves the domain, assumptions, and target in item 4.
6. Diagnose this argument: "For every ordered pair of distinct reals, WLOG $x<y$, so the first coordinate is smaller."
7. Diagnose this argument: "For every integer $n$, either $n<0$ or $n>0$, and the result follows in both cases."
8. Use `audit_case_coverage` on the finite domain $\{-5,\ldots,5\}$ for the case families in items 1, 2, and 7. Explain what the code verifies and why the symbolic coverage argument remains necessary over $\mathbb{R}$ or $\mathbb{Z}$.

**Deliverable:** Three complete proofs, two WLOG/coverage audits, executable assertions, and limitations.

<details>
<summary>Hint 1</summary>

Overlapping cases are acceptable when their union is the domain. A WLOG swap is valid only if the conclusion can be transferred back after swapping.
</details>

<details>
<summary>Hint 2</summary>

For item 4, after assuming $x\le y$, identify the maximum and minimum explicitly. Then explain what happens to an input with $x>y$ under $(x,y)\mapsto(y,x)$.
</details>

## E0.06.04 Compare contraposition and contradiction

- **Type:** proof and critique
- **Difficulty:** 3
- **Objective:** Distinguish the assumptions and targets of contraposition and contradiction, then remove contradiction sandwiches.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper; §0.05 logical equivalences.
- **Assumptions:** Use classical logic and ordinary integer parity.

### Problem

1. Prove by contraposition: if $n^2$ is odd, then $n$ is odd.
2. Prove by contradiction: there are no integers $m,n$ with $m$ even, $n$ odd, and $m=n$.
3. For each proof, write the original target, transformed target or negated full target, opening assumptions, and closing inference.
4. Explain why assuming $\neg Q$ while proving $P\implies Q$ is not yet a contradiction proof.
5. Audit this proof:

   > Assume for contradiction that two even integers have an odd sum. Write them as $2a$ and $2b$. Their sum is $2(a+b)$, so it is even. This contradicts the assumption, so two even integers have an even sum.

6. Rewrite item 5 using the shortest appropriate route.
7. A proof of $P\implies Q$ assumes $P\land\neg Q$, derives $R\land\neg R$, and closes. Explain why this is contradiction rather than contraposition.
8. Give one theorem for which the contrapositive exposes a useful positive definition and one for which a direct proof is shorter.

**Deliverable:** Two proofs, route-comparison table, and repaired contradiction sandwich.

<details>
<summary>Hint 1</summary>

The contrapositive of $P\implies Q$ is $\neg Q\implies\neg P$. The negation of the full implication is $P\land\neg Q$.
</details>

<details>
<summary>Hint 2</summary>

In item 5, inspect whether the central algebra used the assumption that the sum was odd. If not, remove the wrapper.
</details>

## E0.06.05 Prove biconditionals and equivalence cycles

- **Type:** proof
- **Difficulty:** 3
- **Objective:** Prove both directions of a biconditional and show that a directed implication cycle makes every condition equivalent.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper.
- **Assumptions:** $n\in\mathbb{Z}$. You may use elementary parity and divisibility definitions.

### Problem

1. Prove
   $$
   6\mid n\iff(2\mid n\text{ and }3\mid n).
   $$
   Show both directions and construct every divisibility witness you use.
2. Consider conditions:
   - $A$: $n$ is even;
   - $B$: $n+1$ is odd;
   - $C$: $n^2$ is even.
3. Prove $A\implies B$, $B\implies C$, and $C\implies A$.
4. List directed paths proving all six ordered implications among $A,B,C$.
5. Explain why the cycle proves pairwise equivalence.
6. Explain why $A\implies B\implies C$ alone does not prove equivalence.
7. Audit a draft that proves only $6\mid n\implies2\mid n$ and labels the theorem "if and only if."
8. State whether a four-condition cycle $A\implies B\implies C\implies D\implies A$ also suffices, and justify your answer using reachability.

**Deliverable:** One biconditional proof, one equivalence cycle, a reachability table, and one failure diagnosis.

<details>
<summary>Hint 1</summary>

For the reverse direction of item 1, if $n=2a=3b$, use parity or divisibility to show that the needed witness exists without dividing illegally.
</details>

<details>
<summary>Hint 2</summary>

From $2\mid n$ and $3\mid n$, write $n=3b$. Since $n$ is even and $3$ is odd, determine the parity of $b$, then substitute.
</details>

## E0.06.06 Prove existence and uniqueness

- **Type:** proof
- **Difficulty:** 4
- **Objective:** Separate constructive witnesses, classically nonconstructive existence, existential scope, and uniqueness.
- **Estimated time:** 45 minutes
- **Allowed tools:** Pencil and paper; module references for the classical/nonconstructive distinction.
- **Assumptions:** Use classical excluded middle only where explicitly identified.

### Problem

1. Constructively prove that every integer $n$ is the difference of two perfect squares if and only if $n$ is odd or divisible by $4$.
2. Identify explicit witnesses in both constructive directions.
3. Reproduce the classical case proof that irrational positive reals $a,b$ exist with rational $a^b$. Mark the exact use of excluded middle and state why the proof does not decide a branch.
4. Prove there exists exactly one real $x$ satisfying $3x+4=19$.
5. Split item 4 into existence and at-most-one obligations.
6. Show by example that at-most-one does not imply existence.
7. From $\exists x\,P(x)$ and $\forall x(P(x)\implies Q)$, derive $Q$ without leaking the temporary witness into the conclusion.
8. Explain why one example can prove an existential but cannot prove a universal.
9. Classify each proof above as constructive, classically nonconstructive, or uniqueness reasoning. State any domain or nonzero assumptions.

**Deliverable:** Three proof packages, one scoped existential derivation, and a classification table.

<details>
<summary>Hint 1</summary>

For odd $n$, compare consecutive squares. For $n=4k$, compare two squares centered around a convenient integer expression.
</details>

<details>
<summary>Hint 2</summary>

Use $(k+1)^2-k^2=2k+1$ and $(k+1)^2-(k-1)^2=4k$. For the reverse direction, analyze the parity of the two square bases.
</details>

## E0.06.07 Find counterexamples and repair conjectures

- **Type:** experiment
- **Difficulty:** 4
- **Objective:** Find minimal counterexamples, distinguish disproof obligations, and repair a conjecture without overstating finite evidence.
- **Estimated time:** 50 minutes
- **Allowed tools:** Python 3 standard library only; symbolic reasoning for the final repair.
- **Assumptions:** Search domains and tie-breaking orders must be explicit.

### Problem

Investigate these conjectures:

1. Every integer $n\ge2$ satisfies $n^2-n+41$ prime.
2. For all integers $a,b,c$, $ab=ac$ implies $b=c$.
3. Every relation that is symmetric and transitive is reflexive.
4. Every nonempty finite list of integers has an element at least as large as its average.
5. If $x^2=y^2$ for reals $x,y$, then $x=y$.

For each conjecture:

6. specify a deterministic finite search domain;
7. use `first_counterexample` or a small equivalent to find the first failure, if one exists;
8. verify the failure by hand;
9. identify whether one counterexample settles the original claim;
10. repair the statement by adding a necessary assumption, weakening the conclusion, or restricting the domain honestly;
11. prove the repaired statement symbolically when it remains an infinite claim;
12. distinguish "no counterexample found" from "proved over the exhausted finite domain" and from "proved generally";
13. for the existential statement "there exists an integer solution to $x^2=2$," explain why checking many candidates does not disprove it over every possible domain and why a universal argument is needed over $\mathbb{Z}$.

**Deliverable:** Executable search, counterexample table, five repaired claims, symbolic proofs, and limitations.

<details>
<summary>Hint 1</summary>

Include $a=0$ for cancellation, the empty relation on a nonempty base set, opposite real values for equal squares, and the earliest values of the quadratic.
</details>

<details>
<summary>Hint 2</summary>

Symmetric plus transitive implies reflexivity only on elements that occur in the relation's field. Equal squares imply equality up to sign.
</details>

## E0.06.08 Prove set and function equality

- **Type:** proof
- **Difficulty:** 3
- **Objective:** Prove set equality by elementwise biconditional or two inclusions and function equality pointwise.
- **Estimated time:** 40 minutes
- **Allowed tools:** Pencil and paper; finite Python checks only after the proofs.
- **Assumptions:** Complements are relative to a declared universe $U$. Functions in an equality have the same domain and codomain.

### Problem

1. Prove by elementwise biconditional:
   $$
   A\setminus(B\cap C)=(A\setminus B)\cup(A\setminus C).
   $$
2. Prove by two inclusions:
   $$
   A\mathbin{\triangle}B=(A\cup B)\setminus(A\cap B).
   $$
3. Explain why one inclusion does not prove equality.
4. Define $f,g:\mathbb{R}\to\mathbb{R}$ by
   $$
   f(x)=x^3-3x^2+3x-1,
   \qquad
   g(x)=(x-1)^3.
   $$
   Prove $f=g$ pointwise.
5. Define $p,q:\mathbb{R}\to\mathbb{R}$ by $p(x)=x^2$ and $q(x)=|x|^2$. Prove $p=q$ without checking only sample inputs.
6. Explain why two functions with the same formula but different codomains need not be the same declared function.
7. Prove that equality modulo $m\ge1$ is an equivalence relation on $\mathbb{Z}$ by expanding reflexivity, symmetry, and transitivity.
8. Create a finite checker for items 1, 2, 4, 5, and 7 on declared finite samples. State why those checks audit arithmetic and implementation but do not replace the general proofs.

**Deliverable:** Two set proofs, two function proofs, one relation proof, executable checks, and limitations.

<details>
<summary>Hint 1</summary>

For set equality, begin with one arbitrary $x$. For function equality, begin with one arbitrary domain input and compare output values.
</details>

<details>
<summary>Hint 2</summary>

Translate difference to conjunction with negated membership. For congruence, write divisibility witnesses for differences and combine them.
</details>

## E0.06.09 Apply generalized pigeonhole

- **Type:** proof and implementation
- **Difficulty:** 4
- **Objective:** State exact assignment assumptions, apply ceiling and capacity forms, and verify finite boundary cases.
- **Estimated time:** 50 minutes
- **Allowed tools:** Pencil and paper; Python 3 standard library only for exhaustive finite verification.
- **Assumptions:** Each counted object is assigned to exactly one of $k\ge1$ categories unless an incidence interpretation is explicitly substituted.

### Problem

1. Prove that assigning $73$ tasks to $8$ workers gives one worker at least $10$ tasks.
2. Prove that among $41$ integers, at least $5$ have the same remainder modulo $9$.
3. A storage system has $7$ shards, each with capacity $12$. Prove that $85$ records cannot be stored when every record occupies exactly one shard.
4. Explain why the conclusion in item 1 says at least $10$, not exactly $10$.
5. State how item 3 changes if each record is replicated to two shards and the counted objects become storage incidences.
6. Derive the generalized bound $\lceil N/k\rceil$ from a capacity contradiction, including the ceiling inequality and the condition $k>0$.
7. For $1\le k\le5$ and $0\le N\le8$, enumerate every assignment in `product(range(k), repeat=N)` and verify that the minimum possible maximum load equals $\lceil N/k\rceil$.
8. Construct a balanced assignment attaining the bound for arbitrary finite $N,k$ using quotient and remainder.
9. Audit a proof that uses $\lfloor N/k\rfloor$ as the guaranteed lower bound and calls it sharp.
10. State exactly what the exhaustive program proves.

**Deliverable:** Three applications, general derivation, attaining construction, executable boundary test, and claim audit.

<details>
<summary>Hint 1</summary>

To force at least $r+1$ in one category, suppose every category holds at most $r$ and compare total capacity $kr$ with $N$.
</details>

<details>
<summary>Hint 2</summary>

Write $N=qk+s$ with $0\le s<k$. Use $s$ categories of load $q+1$ and the rest of load $q$.
</details>

## E0.06.10 Double count one incidence set

- **Type:** combinatorial proof
- **Difficulty:** 4
- **Objective:** Define one finite incidence set, count it in two ways, and distinguish a proof from matching expressions.
- **Estimated time:** 50 minutes
- **Allowed tools:** Pencil and paper; Python 3 standard library for incidence verification.
- **Assumptions:** Graphs are finite, undirected, and loop-free. Edge instances are distinct.

### Problem

1. Define the vertex-edge incidence set of a graph and prove
   $$
   \sum_{v\in V}\deg(v)=2|E|.
   $$
2. Deduce that the number of odd-degree vertices is even.
3. For a finite $m\times n$ zero-one matrix, define the set of positions containing one and prove that the sum of row sums equals the sum of column sums.
4. Define one set counted by both sides of
   $$
   \sum_{k=0}^{n}k\binom{n}{k}=n2^{n-1}
   $$
   for $n\ge1$, and prove the identity.
5. Explain why the $n=0$ case should be stated separately.
6. Build a record-shard incidence relation with at least five records, four shards, unequal row counts, and unequal column counts. Verify both totals with `verify_incidence_count`.
7. Mutate one row count manually and show that the inconsistent summaries disagree even though the underlying incidence relation has not changed.
8. Audit this sentence: "Both formulas equal $24$, so this is a double-counting proof." State what definition and bijective accounting are missing.
9. Explain what changes in the handshake argument if loops are permitted under a convention that counts each loop twice toward degree.
10. State which fuller counting topics are deferred to §0.08.

**Deliverable:** Three double-counting proofs, one implementation audit, conventions, and scope note.

<details>
<summary>Hint 1</summary>

The common object is an ordered incidence, not an edge alone or a degree alone. Partition that one set by first coordinate and then by second coordinate.
</details>

<details>
<summary>Hint 2</summary>

For the binomial identity, count pairs $(S,x)$ with $S\subseteq U$ and $x\in S$. First fix $|S|$; then fix $x$.
</details>

## E0.06.11 Build a diagonal impossibility argument

- **Type:** proof
- **Difficulty:** 4
- **Objective:** Construct a well-defined object that differs from every indexed candidate at its corresponding coordinate.
- **Estimated time:** 45 minutes
- **Allowed tools:** Pencil and paper; a finite prefix program for illustration only.
- **Assumptions:** Binary sequences are functions $\mathbb{N}\to\{0,1\}$. Do not repeat the full Cantor power-set proof from §0.04.

### Problem

1. Suppose $s_0,s_1,s_2,\ldots$ is claimed to enumerate every infinite binary sequence. Define a diagonal sequence $t$.
2. Prove $t$ is a well-defined binary sequence.
3. For arbitrary $j$, identify one coordinate proving $t\ne s_j$.
4. Explain why changing only coordinate zero would not escape every row.
5. Generalize the construction to sequences over a finite alphabet with at least two symbols by declaring a fixed no-match operation.
6. Explain why the argument needs an indexed coordinate corresponding to each candidate.
7. Describe, without proving a full undecidability theorem, how later computability arguments may index programs and compare program $i$ on input $i$.
8. Distinguish diagonalization from self-reference. Give one diagonal construction with no self-referential sentence and one later-style scenario where encoding an object as its own input adds self-reference.
9. Implement a deterministic $8\times8$ finite prefix illustration and assert that the constructed prefix differs from row $j$ at coordinate $j$.
10. Explain why an $8\times8$ illustration is not an uncountability or impossibility proof.
11. Audit a proposed diagonal object whose coordinate rule can produce the value $2$ even though the target space is binary.
12. Cite §0.04 rather than duplicating its complete Cantor theorem argument.

**Deliverable:** General proof, alphabet extension, computability preview, finite illustration, and scope audit.

<details>
<summary>Hint 1</summary>

Use $t(i)=1-s_i(i)$ in the binary case. Compare $t$ with row $j$ at coordinate $j$.
</details>

<details>
<summary>Hint 2</summary>

Well-definedness and disagreement are separate obligations. A rule that leaves the target alphabet does not construct a valid candidate.
</details>

## E0.06.12 Audit proof, code, and sources

- **Type:** critique
- **Difficulty:** 4
- **Objective:** Audit variable provenance, proof dependencies, specification assumptions, finite code claims, AI claims, and source licensing.
- **Estimated time:** 60 minutes
- **Allowed tools:** Module references, directly opened authoritative sources, and Python 3 standard library. No generated summary counts as evidence.
- **Assumptions:** Treat mathematical, software, empirical, and licensing claims as different evidence types.

### Problem

Audit this paragraph:

> A proof is any convincing sequence of examples. Valid arguments must have true premises, so testing a claim on a million inputs proves it universally. To prove $P\implies Q$, assume $Q$ and derive $P$. For cases, overlap is fatal but missing a boundary is harmless. WLOG permits any convenient order. Contraposition and contradiction are the same because both mention negation. An iff needs only its easier direction. At-most-one proves unique existence, and one failed candidate disproves an existential. Set equality needs one inclusion. If each of $k$ buckets has fewer than $N/k$ items, one has exactly $\lceil N/k\rceil$. Double counting means obtaining the same number from unrelated expressions. A diagonal object need not belong to the target space. Dividing $ab=ac$ by $a$ is always legal. A local existential witness becomes a global name. A proof may cite a lemma that depends on the theorem being proved. Property tests prove algorithm correctness, and benchmark success proves an AI system is robust without assumptions. Stanford's checklist is CC licensed, Hammack allows adaptations, and an AI summary is enough to verify both.

1. Identify at least twenty errors, ambiguities, or unsupported claims.
2. Create a table with columns `Claim`, `Proof obligation`, `Diagnosis`, `Repair`, and `Evidence`.
3. Give a counterexample or dependency graph for every false universal, converse, cancellation, equality, or circularity claim.
4. Use `audit_dependency_dag` to reject a graph where target $T$ supports lemma $L$ and $L$ supports $T$.
5. Mutate a correct implication by reversing it and find a finite countermodel.
6. Explain exactly what a property test can establish and what a proof of algorithm correctness additionally needs.
7. State assumptions required before making a theorem about an ML system, and separate those from empirical benchmark evidence.
8. Open the Summer 2026 Stanford checklist and Hammack edition 3.4 landing page. Record the copyright or license boundaries and confirm that no exercise was adapted.
9. Open *Mathematics in Lean* Chapter 5 and identify two assumptions made explicit in its irrational-root development.
10. Rewrite the paragraph accurately in at most 260 words.
11. Submit a source ledger with each opened URL, access date, exact supported claim, and reuse limitation.
12. Draw an acyclic proof dependency graph from assumptions and definitions to a target, then contrast it with the rejected cycle.

**Deliverable:** Audit table, counterexamples, executable mutation and DAG checks, corrected paragraph, dependency diagrams, and source ledger.

<details>
<summary>Hint 1</summary>

Sort claims into logic, quantifiers, cases, route selection, existence, equality, counting, operations, dependencies, software testing, empirical AI, and licensing before repairing them.
</details>

<details>
<summary>Hint 2</summary>

Stanford states copyright for its course materials. Hammack's CC BY-NC-ND license permits sharing with attribution but not adaptation. Match every evidence source to the kind of claim it can support.
</details>

## Completion check

Before opening the [solutions](../solutions/README.md), confirm that your work includes:

- exact assumptions and targets before route selection;
- provenance for every arbitrary object, witness, and chosen value;
- exhaustive case coverage, with overlap treated correctly;
- an explicit symmetry or reduction behind every WLOG step;
- contraposition separated from contradiction;
- both directions of every biconditional and full reachability for cycles;
- existence separated from uniqueness and local witnesses kept in scope;
- one valid counterexample for every universal disproof;
- both membership directions for set equality and pointwise function equality;
- the ceiling bound and capacity contradiction with $k>0$;
- one named finite incidence set behind every double count;
- a well-defined diagonal object that differs from every indexed candidate;
- no circular dependency, hidden converse, or illegal cancellation;
- finite computation claims limited to exhausted domains;
- source licenses and empirical AI claims audited independently.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)
