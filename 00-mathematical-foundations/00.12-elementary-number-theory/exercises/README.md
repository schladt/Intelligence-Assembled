# Exercises for §0.12 Elementary Number Theory

[Back to module](../README.md) | [Worked solutions](../solutions/README.md) | [Code](../code/README.md) | [Resources](../resources/README.md)

Attempt each problem before opening the solution set. Difficulty follows the
project's 1 through 5 scale. All programming uses the Python standard library.

## Exercise index

| ID | Title | Type | Difficulty | Objective | Time |
|---|---|---|---:|---|---:|
| E0.12.01 | Audit divisibility, signs, and zero | conceptual and proof | 2 | state divisibility and division contracts | 35 min |
| E0.12.02 | Recover arithmetic from prime exponents | calculation and proof | 3 | use unique factorization for gcd and lcm | 45 min |
| E0.12.03 | Trace Euclid's invariant | derivation and implementation | 3 | prove and execute Euclid's algorithm | 50 min |
| E0.12.04 | Produce Bézout coefficients and inverses | derivation and proof | 4 | connect extended Euclid to invertibility | 55 min |
| E0.12.05 | Reason with classes and legal cancellation | proof and critique | 4 | use congruence as an equivalence relation | 55 min |
| E0.12.06 | Construct a coprime CRT solution | calculation and derivation | 4 | solve pairwise-coprime systems | 55 min |
| E0.12.07 | Diagnose general CRT compatibility | proof and implementation | 4 | solve or refuse noncoprime systems | 60 min |
| E0.12.08 | Distinguish rings, units, and prime fields | proof and calculation | 4 | prove the field criterion for prime moduli | 55 min |
| E0.12.09 | Count units and apply Euler's theorem | derivation and calculation | 4 | compute phi and reduce powers | 55 min |
| E0.12.10 | Separate Fermat evidence from primality proof | experiment and critique | 4 | state Fermat's contract and converse failure | 60 min |
| E0.12.11 | Audit the implementation contracts | implementation and testing | 4 | test boundaries against trusted references | 70 min |
| E0.12.12 | Prove and delimit textbook RSA | proof, implementation, and critique | 5 | integrate the complete theorem chain | 90 min |

## E0.12.01 Audit divisibility, signs, and zero

- **Type:** conceptual and proof
- **Difficulty:** 2
- **Objective:** State divisibility and division contracts.
- **Estimated time:** 35 minutes
- **Allowed tools:** Definitions and hand calculation.
- **Assumptions:** All variables are integers.

### Problem

1. Decide each statement and justify it from $a\mid b\iff b=ak$:
   $6\mid-42$, $-6\mid42$, $7\mid0$, $0\mid0$, $0\mid7$, and $1\mid n$.
2. Prove $a\mid b$ if and only if $-a\mid b$.
3. For $a=-37$ and positive divisor $n=8$, find the unique $q,r$ with
   $a=qn+r$ and $0\le r<n$.
4. Explain why the division algorithm excludes divisor zero.
5. Audit: "If $a\mid b$, then $|a|\le|b|$."

**Deliverable:** Six decisions, two short proofs or repairs, and one division.

## E0.12.02 Recover arithmetic from prime exponents

- **Type:** calculation and proof
- **Difficulty:** 3
- **Objective:** Use unique factorization for gcd and lcm.
- **Estimated time:** 45 minutes
- **Allowed tools:** Hand factorization.
- **Assumptions:** Prime means a positive integer at least $2$.

### Problem

Let $a=-2^4 3^2 7$ and $b=2^2 3^5 5$.

1. Compute $\gcd(a,b)$ and $\mathrm{lcm}(a,b)$ from exponents.
2. Verify their product is $|ab|$.
3. Count the positive divisors of $|a|$.
4. State the fundamental theorem of arithmetic with its exact domain and
   uniqueness clause.
5. Explain how to factor a negative integer and why $0$ has no prime
   factorization.
6. Prove Euclid's lemma implies that a prime dividing a finite product divides
   at least one factor.

**Deliverable:** Two factorizations, two numerical audits, and two proof notes.

## E0.12.03 Trace Euclid's invariant

- **Type:** derivation and implementation
- **Difficulty:** 3
- **Objective:** Prove and execute Euclid's algorithm.
- **Estimated time:** 50 minutes
- **Allowed tools:** Hand calculation and module code.
- **Assumptions:** The gcd is normalized to be nonnegative.

### Problem

1. Trace Euclid on $1071$ and $462$, recording every quotient and remainder.
2. Prove that if $a=bq+r$, then $(a,b)$ and $(b,r)$ have exactly the same
   common divisors.
3. Explain why the algorithm terminates.
4. Run `gcd_trace(1071, 462)` and compare every row.
5. Test all sign choices and the boundaries $(0,0)$, $(a,0)$, and $(0,b)$.
6. Compare only final gcd values with `math.gcd` and state why this is a
   reference comparison rather than the implementation.

**Deliverable:** A trace, invariant proof, termination argument, and tests.

## E0.12.04 Produce Bézout coefficients and inverses

- **Type:** derivation and proof
- **Difficulty:** 4
- **Objective:** Connect extended Euclid to invertibility.
- **Estimated time:** 55 minutes
- **Allowed tools:** Back-substitution and module code.
- **Assumptions:** Moduli are at least $2$.

### Problem

1. Back-substitute your Euclid trace to find $x,y$ with
   $1071x+462y=\gcd(1071,462)$.
2. Use extended Euclid to find $17^{-1}\pmod{43}$.
3. Prove $[a]_n$ has an inverse if and only if $\gcd(a,n)=1$.
4. Explain why Bézout coefficients are not unique.
5. Determine whether $14$ has an inverse modulo $35$ and justify refusal.
6. Compare `modular_inverse(17, 43)` with `pow(17, -1, 43)` only after the
   derivation.

**Deliverable:** Two coefficient calculations, the iff proof, and one refusal.

## E0.12.05 Reason with classes and legal cancellation

- **Type:** proof and critique
- **Difficulty:** 4
- **Objective:** Use congruence as an equivalence relation.
- **Estimated time:** 55 minutes
- **Allowed tools:** Definitions and proof.
- **Assumptions:** $n\ge2$.

### Problem

1. Prove congruence modulo $n$ is reflexive, symmetric, and transitive.
2. List $[3]_5$ using a set-builder description and five representatives.
3. Prove addition and multiplication of classes are well-defined.
4. Solve $7x\equiv4\pmod{15}$ by legal cancellation or inversion.
5. Solve $6x\equiv9\pmod{15}$, stating the weakened modulus and all classes
   modulo $15$.
6. Give a counterexample to unrestricted cancellation.
7. Repair: "Congruence means two integers have the same remainder" when
   negative divisors or unstated remainder conventions are allowed.

**Deliverable:** Three relation proofs, two solutions, and two critiques.

## E0.12.06 Construct a coprime CRT solution

- **Type:** calculation and derivation
- **Difficulty:** 4
- **Objective:** Solve pairwise-coprime systems.
- **Estimated time:** 55 minutes
- **Allowed tools:** Extended Euclid and hand arithmetic.
- **Assumptions:** Moduli are pairwise coprime.

### Problem

Solve

$$
x\equiv1\pmod4,
\qquad x\equiv4\pmod5,
\qquad x\equiv6\pmod7.
$$

1. Construct $N$, each $N_i$, and each inverse $M_i$.
2. Build the CRT sum and normalize it.
3. Verify all three congruences.
4. Prove uniqueness modulo $N$.
5. Compare with `chinese_remainder`.
6. Explain why pairwise coprimality is stronger than merely having a common gcd
   of $1$ across all three moduli.

**Deliverable:** A constructive solution, verification, and uniqueness proof.

## E0.12.07 Diagnose general CRT compatibility

- **Type:** proof and implementation
- **Difficulty:** 4
- **Objective:** Solve or refuse noncoprime systems.
- **Estimated time:** 60 minutes
- **Allowed tools:** Gcd, extended Euclid, brute force, and module code.
- **Assumptions:** Every modulus is at least $2$.

### Problem

1. Prove $x\equiv a\pmod m$ and $x\equiv b\pmod n$ is solvable exactly
   when $a\equiv b\pmod{\gcd(m,n)}$.
2. Solve $x\equiv4\pmod6$ and $x\equiv10\pmod{15}$.
3. State the uniqueness modulus.
4. Refuse $x\equiv3\pmod6$ and $x\equiv4\pmod{15}$ with a compatibility
   witness.
5. Extend the compatible system with $x\equiv1\pmod7$ and solve it.
6. Verify both outcomes with `chinese_remainder` and bounded brute force.

**Deliverable:** The iff proof, two solved systems, and one exact refusal.

## E0.12.08 Distinguish rings, units, and prime fields

- **Type:** proof and calculation
- **Difficulty:** 4
- **Objective:** Prove the field criterion for prime moduli.
- **Estimated time:** 55 minutes
- **Allowed tools:** Class arithmetic and Bézout.
- **Assumptions:** Only the limited field definition in the lesson is needed.

### Problem

1. List every unit in $\mathbb{Z}/12\mathbb{Z}$ and its inverse.
2. Build the nonzero multiplication table for $\mathbb{F}_5$.
3. Prove every nonzero class modulo a prime has an inverse.
4. Prove a composite modulus has nonzero zero divisors.
5. Conclude $\mathbb{Z}/n\mathbb{Z}$ is a field exactly when $n$ is prime.
6. Compute $4/3$ in $\mathbb{F}_7$.
7. Use the module code to refuse division by zero and a composite "field"
   modulus.

**Deliverable:** Two finite audits, the field iff proof, and refusal tests.

## E0.12.09 Count units and apply Euler's theorem

- **Type:** derivation and calculation
- **Difficulty:** 4
- **Objective:** Compute phi and reduce powers.
- **Estimated time:** 55 minutes
- **Allowed tools:** Inclusion-exclusion, CRT, and module code.
- **Assumptions:** Euler's theorem requires coprimality.

### Problem

1. Derive $\varphi(p^e)=p^e-p^{e-1}$.
2. Use CRT to explain why $\varphi(mn)=\varphi(m)\varphi(n)$ for coprime
   $m,n$.
3. Compute $\varphi(360)$ from its factorization.
4. Compute $7^{222}\bmod40$ using Euler's theorem.
5. Explain why the same theorem cannot be invoked for $10^{222}\bmod40$,
   then compute that residue another way.
6. Compare with `phi` and `modular_power`.

**Deliverable:** Two derivations, three exact values, and one refusal rationale.

## E0.12.10 Separate Fermat evidence from primality proof

- **Type:** experiment and critique
- **Difficulty:** 4
- **Objective:** State Fermat's contract and converse failure.
- **Estimated time:** 60 minutes
- **Allowed tools:** Proof, module code, and bounded enumeration.
- **Assumptions:** No primality-testing theorem beyond the lesson.

### Problem

1. State both forms of Fermat's little theorem and reconcile their domains.
2. Prove the nonzero form by permuting nonzero residue classes.
3. For $n=15$, find a base coprime to $15$ that exposes compositeness through
   $a^{14}\not\equiv1\pmod{15}$.
4. Verify $2^{560}\equiv1\pmod{561}$ even though $561$ is composite.
5. Verify a base sharing a factor with $561$ need not satisfy that equation.
6. Explain precisely why passing several Fermat checks is evidence, not a proof
   of primality.

**Deliverable:** A theorem proof, three computations, and an evidence boundary.

## E0.12.11 Audit the implementation contracts

- **Type:** implementation and testing
- **Difficulty:** 4
- **Objective:** Test boundaries against trusted references.
- **Estimated time:** 70 minutes
- **Allowed tools:** Standard library and module code.
- **Assumptions:** Exhaustive ranges must be stated.

### Problem

Write additional `unittest` cases that:

1. compare `gcd(a, b)` with `math.gcd(a, b)` for every
   $-30\le a,b\le30$;
2. verify every returned Bézout identity on the same range;
3. compare `modular_power` with `pow` for bases $-10$ through $10$,
   exponents $0$ through $12$, and moduli $2$ through $20$;
4. compare every existing modular inverse with `pow(a, -1, n)` and verify
   refusal for nonunits over $2\le n\le25$;
5. brute-force every pair of congruences with moduli $2$ through $10$ and
   compare existence and the normalized CRT class;
6. explain why these exhaustive finite ranges still do not prove the algorithms.

**Deliverable:** Passing tests, exact ranges, and an evidence statement.

## E0.12.12 Prove and delimit textbook RSA

- **Type:** proof, implementation, and critique
- **Difficulty:** 5
- **Objective:** Integrate the complete theorem chain.
- **Estimated time:** 90 minutes
- **Allowed tools:** Lesson theorems and module code.
- **Assumptions:** Use distinct primes $p=11,q=17$ and $e=7$.

### Problem

1. Compute $n$, $\varphi(n)$, and the private exponent $d$.
2. State every key and message-representative condition.
3. Encrypt and decrypt $m=42$.
4. Repeat for $m=0$, $11$, $17$, and $22$.
5. Prove $m^{ed}\equiv m\pmod p$ by splitting into $p\mid m$ and
   $p\nmid m$; repeat modulo $q$.
6. Use CRT uniqueness to complete correctness for every $0\le m<n$.
7. Explain why an Euler-only proof modulo $n$ misses some messages.
8. Exhaustively test all representatives with the toy implementation.
9. List at least six security features or responsibilities absent from the toy
   code.
10. Explain the distinction among raw RSA exponentiation, RSAES-OAEP, and
    RSASSA-PSS without implementing any of them.

**Deliverable:** Key arithmetic, five traces, the all-residue proof, exhaustive
finite evidence, and a security-boundary audit.

[Back to module](../README.md) | [Worked solutions](../solutions/README.md)