# Resources for §0.15 Computability and Complexity

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)

Use these sources to deepen a specific proof or model. The primary lesson is
self-contained enough to complete the exercises without copying external text or
figures.

## Core course maps

### MIT OpenCourseWare 6.045J

- **Link:** [Automata, Computability, and Complexity, Spring 2011](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/)
- **Best for:** a compact syllabus and lecture sequence spanning automata,
  Turing machines, undecidability, mapping reducibility, P, NP-completeness, and
  probabilistic computation.
- **Use:** compare this module's boundary with a full university theory course.
- **License:** CC BY-NC-SA 4.0. Attribute any reused course material and follow
  the noncommercial share-alike terms.

### Foundations of Computation

- **Link:** [Carol Critchlow and David Eck, Version 2.3.2](https://math.hws.edu/FoundationsOfComputation/FoundationsOfComputation_2.3.2_6x9.pdf)
- **Best for:** a readable progression from regular languages and finite
  automata through context-free grammars, pushdown automata, Turing machines, and
  limits of computation.
- **Use:** expand the formal-language portion or practice machine constructions.
- **License:** CC BY-NC-SA 4.0. Link or adapt with attribution under its terms.

### Introduction to Theoretical Computer Science

- **Link:** [Boaz Barak, online draft](https://introtcs.org/public/index.html)
- **Best for:** modern treatment of representation, universality,
  uncomputability, polynomial reductions, NP, Cook-Levin, P versus NP, and
  randomized computation.
- **Use:** study the proof architecture behind the lesson's concise statements.
- **License:** CC BY-NC-ND 4.0. Link and quote within applicable limits; do not
  distribute modified versions.

## Decidability and complexity

### Clay Mathematics Institute: P versus NP

- **Link:** [Official problem page](https://www.claymath.org/millennium/p-vs-np/)
- **Best for:** authoritative current status and the checking-versus-finding
  framing.
- **Use:** verify that any conclusion depending on $P\ne NP$ is labeled
  conditional.
- **Reuse boundary:** link and summarize. Site terms and page-specific rights
  govern reuse.

### Jeff Erickson: NP-Hardness

- **Link:** [Algorithms, Chapter 12](https://jeffe.cs.illinois.edu/teaching/algorithms/book/12-nphard.pdf)
- **Best for:** precise reductions, NP-hardness proof obligations, canonical
  problems, and the practical interpretation of hardness.
- **Use:** work through additional reductions after mastering arrow direction.
- **License:** the Algorithms text is CC BY 4.0. Attribute adapted material.

### Complexity Zoo

- **Link:** [Complexity Zoo](https://complexityzoo.net/Complexity_Zoo)
- **Best for:** looking up named complexity classes after the core definitions
  are stable.
- **Use:** reference, not linear reading. Check each class's machine, resource,
  and error convention before comparing it with another.
- **Reuse boundary:** link to entries and verify their cited sources rather than
  reproducing the catalog.

## Algorithms beyond exact polynomial time

### The Design of Approximation Algorithms

- **Link:** [David P. Williamson and David B. Shmoys](https://www.designofapproxalgs.com/book.pdf)
- **Best for:** approximation definitions, proofs, linear-programming methods,
  set cover, metric TSP, and limits of approximation.
- **Use:** continue from the vertex-cover factor-2 proof to systematic design
  techniques.
- **Reuse boundary:** the freely available electronic manuscript is copyrighted
  and provided for personal use. Link and summarize only. Do not repost or adapt
  its text or figures without permission.

### Cornell CS 6810 parameterized complexity notes

- **Link:** [Parameterized Complexity, Fall 2023](https://courses.cs.cornell.edu/cs6810/2023fa/Parameterized.pdf)
- **Best for:** FPT, XP, parameterized reductions, branching, vertex cover, and
  kernelization.
- **Use:** check the exact exponent boundary in an FPT claim and study more
  complete kernel arguments.
- **Reuse boundary:** link and summarize unless the course identifies broader
  reuse permission.

## Reading paths

### Formal-language path

1. Critchlow and Eck on DFAs, NFAs, and regular expressions.
2. Their context-free grammar and pushdown-automaton chapters.
3. MIT 6.045 calendar topics on nonregular languages and computability.
4. Barak on finite models and equivalent computational models.

### Undecidability path

1. Barak on universality and uncomputability.
2. Reconstruct the diagonal proof without notes.
3. MIT 6.045 topics on mapping reducibility, Rice's theorem, and self-reference.
4. Critchlow and Eck for additional machine examples.

### Complexity and practical-response path

1. Erickson on NP-hardness and reductions.
2. Clay on the unresolved P versus NP boundary.
3. Williamson and Shmoys on approximation guarantees.
4. Cornell notes on FPT and kernelization.
5. Complexity Zoo only when a named class needs a precise lookup.

## Source-use checklist

Before reusing an external item:

1. check the exact page or file license;
2. distinguish linking, quotation, adaptation, and redistribution;
3. attribute authors and source;
4. do not copy publisher figures into this repository without compatible
   permission;
5. prefer a fresh derivation or original diagram when teaching the same concept;
6. record whether a claim is a theorem, an open question, a conditional result,
   or an empirical observation.

The four SVGs in this module are original teaching visuals created for this
repository.

---

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md) | [Code](../code/README.md)
