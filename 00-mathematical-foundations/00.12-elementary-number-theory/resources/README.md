# Resources for §0.12 Elementary Number Theory

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)

This page is annotated reading guidance and a provenance record, not a second
bibliography. Numbered evidence remains in the module [reference list](../README.md#references).

## Core route

### Crisman, Number Theory: In Context and Interactive

- **What was directly inspected:** The 2024/6 front matter, table of contents,
  student prerequisites, colophon, integers-modulo-$n$ section, unit group,
  Euler phi definition and theorem, Euler applications, CRT route, finite-field
  statement for prime modulus, and cryptography chapter placement.
- **Why it is included:** It provides directly inspectable HTML from integer
  arithmetic through the limited algebraic language used here.
- **Assumed level:** Undergraduate students with an introduction to proof.
- **Access and rights:** Free HTML. The text is CC BY-ND 4.0, and some images
  have additional noncommercial restrictions. Nothing was adapted, copied, or
  translated from it.

The source writes $\mathbb{Z}_n$ where this project writes
$\mathbb{Z}/n\mathbb{Z}$. It develops more group language than this module
requires. Primitive roots, quadratic congruences, elliptic curves, and deeper
analytic number theory remain outside §0.12.

### MIT 6.042J, Mathematics for Computer Science

- **What was directly inspected:** The official Spring 2015 course page,
  instructor and undergraduate metadata, course description, reading index,
  open textbook route, Chapter 8 reading assignments, and OCW license.
- **Why it is included:** It is an independent computer-science-oriented route
  through modular arithmetic and related discrete structures.
- **Assumed level:** Undergraduate computer science and engineering.
- **Access and rights:** MIT OpenCourseWare, CC BY-NC-SA 4.0.

The textbook resource endpoint was blocked by the web client in this session,
so no unextracted PDF passage is treated as unique theorem evidence. The
official reading index and course metadata were inspectable. Crisman is the
primary directly inspectable theorem route.

## RSA route

### Rivest, Shamir, and Adleman, 1978

- **What was directly inspected:** DOI and bibliographic metadata as reproduced
  in RFC 8017's authoritative reference list, including title, authors, venue,
  volume, issue, pages, month, and year.
- **Why it is included:** It is the primary historical citation for the RSA
  construction.
- **Assumed level:** Advanced algorithms, number theory, and cryptography.
- **Access and rights:** ACM publication. No prose, notation, code, or example
  was copied.

The publisher text was not needed for the module's correctness proof, which is
derived independently. RFC 8017 is the directly inspectable source for current
primitive and scheme contracts.

### RFC 8017, PKCS #1 v2.2

- **What was directly inspected:** The complete RFC HTML, especially notation,
  public and private key validity, message-representative ranges, RSAEP and
  RSADP, CRT private operations, the statement that primitives do not provide
  security apart from a scheme, RSAES-OAEP, RSASSA-PSS, and security
  considerations.
- **Why it is included:** It gives the exact boundary between modular
  exponentiation and a cryptographic scheme.
- **Assumed level:** Cryptographic implementation standards.
- **Access and rights:** Public RFC with IETF Trust terms; no code component or
  specification prose was reused.

RFC 8017 supports multi-prime RSA and uses $\lambda(n)$ for key validity. The
module intentionally teaches a narrower two-prime, $\varphi(n)$-based
construction because it is enough for the requested proof chain. This narrowing
is not represented as the full standard.

### NIST FIPS 186-5 and SP 800-56B Rev. 2

- **What was directly inspected:** Official CSRC titles, authorship, dates,
  abstracts, DOI and PDF links, supersession notes, and the 2026 reaffirmation
  of SP 800-56B Rev. 2.
- **Why they are included:** They show that approved digital signatures and RSA
  key establishment are specification-level subjects beyond bare arithmetic.
- **Assumed level:** Security engineering and compliance.
- **Access and rights:** Public United States government publications.

The HTML landing pages do not expose every PDF requirement. They are cited only
for their documented scope and current status, not for an uninspected parameter
or security claim.

## Computing connections

### Python 3.14 documentation

- **What was directly inspected:** Built-in `pow` with three integer arguments,
  negative-exponent modular inversion and its coprimality condition,
  `math.gcd`, `math.lcm`, and `math.isqrt` contracts.
- **Why it is included:** These APIs provide trusted reference comparisons and
  exact arithmetic support after the mechanisms are implemented from scratch.
- **Assumed level:** Basic Python.
- **Access and rights:** PSF License Version 2; documentation examples also
  0BSD.

### NIST SP 800-90A Rev. 1 and SP 800-90B

- **What was directly inspected:** Official titles, authors, dates, abstracts,
  DOI links, and the separation between deterministic random-bit mechanisms
  based on hashes or block ciphers and the entropy sources that seed them.
- **Why they are included:** They prevent a classroom modular recurrence from
  being presented as modern secure random generation.
- **Assumed level:** Cryptographic random-bit generation.
- **Access and rights:** Public United States government publications.

Number theory still provides useful language for periods, residues, and finite
state. The standards show that secure randomness needs much more than a long
modular cycle.

### NIST FIPS 180-4

- **What was directly inspected:** Official title, date, abstract, DOI, and the
  scope of message-digest algorithms for detecting message changes.
- **Why it is included:** It distinguishes cryptographic hashing from the
  modular hash families encountered in data structures and algorithms.
- **Assumed level:** Security engineering.
- **Access and rights:** Public United States government publication.

## Error-correcting-code route

Prime-field arithmetic in this module is enough to recognize why symbols can be
added, multiplied, and divided during coding constructions. Actual code design,
distance, decoding, extension fields, and performance claims are deliberately
deferred. No coding theorem is stated here, so no external coding result is
used as numbered evidence.

## Suggested sequence

1. Use Crisman Chapters 2 and 4-6 beside divisibility, gcd, and congruence.
2. Read Chapters 8-9 beside residue classes, fields, units, phi, Euler, and CRT.
3. Use MIT 6.042J Chapter 8 as a second discrete-mathematics route.
4. Read RFC 8017 §§3 and 5 for key and primitive contracts.
5. Read RFC 8017 §§6-10 before making any claim about secure RSA practice.
6. Use Python documentation only after hand derivations and from-scratch code.
7. Stop before primality testing, cryptographic proof, elliptic curves, coding
   theory, or number-theoretic transforms.

## Provenance and originality ledger

| Source | Accessed | Exact support used | Inspection limit | Reuse boundary |
|---|---|---|---|---|
| Crisman 2024/6 HTML | 2026-09-01 | residue classes, units, phi, Euler, CRT, prime field, route metadata | several initially guessed deep links were wrong; only resolved TOC links were used | CC BY-ND; no adaptation |
| MIT 6.042J | 2026-09-01 | official undergraduate route, Chapter 8 placement, license | textbook resource endpoint blocked by client | no unique uninspected theorem claim |
| RSA DOI metadata | 2026-09-01 | historical paper identity | article text not used | no text or example reused |
| RFC 8017 | 2026-09-01 | RSA key, primitive, range, CRT, scheme, and security boundary | informational RFC, not a complete application profile | no specification prose or code reused |
| NIST FIPS 186-5 | 2026-09-01 | digital-signature standard scope and current metadata | PDF details not extracted | scope citation only |
| NIST SP 800-56B Rev. 2 | 2026-09-01 | RSA key-establishment scope and 2026 reaffirmation | PDF details not extracted | scope citation only |
| Python 3.14 docs | 2026-09-01 | `pow`, gcd, lcm, isqrt behavior | implementation performance not inferred | API semantics only |
| NIST SP 800-90A/B | 2026-09-01 | DRBG and entropy-source separation | full PDF mechanisms not extracted | scope citation only |
| NIST FIPS 180-4 | 2026-09-01 | cryptographic hash standard scope | revision is planned | scope citation only |

Failed fetches and generated search summaries are not numbered evidence. No
Wikipedia or MathWorld page was used. The lesson's proofs, examples, exercises,
solutions, Python code, tests, Mermaid diagrams, and four SVG figures are
original.

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)