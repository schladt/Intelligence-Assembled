# Resources for §0.01 Mathematical Notation

[Back to module](../README.md) | [Exercises](../exercises/README.md) | [Solutions](../solutions/README.md)

This page is reading guidance, not a second formal bibliography.
Numbered sources supporting claims remain in the module [reference list](../README.md#references).

## Core resources

### Mathematics for Computer Science

- **Resource:** MIT OpenCourseWare, *6.042J Mathematics for Computer Science*.
- **Why use it:** The open textbook and course materials develop definitions, sets, functions, sums, and mathematical reading in a computer-science setting. Use it when you want the next rigorous step after this module.
- **Level:** Undergraduate, introductory but proof-oriented.
- **Access:** Free online course, open textbook, videos, and problem sets. https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/

### Mathematics for Machine Learning

- **Resource:** Deisenroth, Faisal, and Ong, *Mathematics for Machine Learning*.
- **Why use it:** Its early chapters repeatedly connect declared dimensions and mathematical maps to ML objects. Read the notation and linear algebra openings to practice shape-aware reading.
- **Level:** Undergraduate; assumes basic algebra.
- **Access:** Author-hosted PDF is freely accessible; print edition is commercial. https://mml-book.github.io/

### Project notation guide

- **Resource:** [Intelligence, Assembled notation guide](../../../NOTATION.md).
- **Why use it:** This is the local contract for typography, indices, shapes, functions, calculus, probability, and optimization. Keep it open while translating papers or writing solutions.
- **Level:** Reference for all levels.
- **Access:** Free in this repository.

## Deep resources

### Concrete Mathematics

- **Resource:** Graham, Knuth, and Patashnik, *Concrete Mathematics*, 2nd edition.
- **Why use it:** Chapters 2 and 3 give a sustained treatment of finite sums, reindexing, perturbing bounds, products, floors, ceilings, and Iverson-style brackets. It is where notation manipulation becomes a working craft.
- **Level:** Intermediate undergraduate; denser than this module.
- **Access:** Commercial book. The authors' public page provides bibliographic details, errata, and sample exams. https://www-cs-faculty.stanford.edu/~knuth/gkp.html

### Notation as a Tool of Thought

- **Resource:** Kenneth E. Iverson, "Notation as a Tool of Thought."
- **Why use it:** Read it to examine a serious argument that notation should be judged by what it lets you express, infer, and verify. The APL symbols are unfamiliar, which makes the reading itself a useful notation exercise.
- **Level:** Intermediate; accessible in argument, unusual in syntax.
- **Access:** Public HTML transcription of the 1980 ACM Turing Award lecture. https://www.jsoftware.com/papers/tot.htm

### The function concept

- **Resource:** O'Connor and Robertson, "The Function Concept," MacTutor History of Mathematics Archive.
- **Why use it:** It shows how "function" moved from geometric and analytic dependence toward a general correspondence. This helps explain why modern sources sometimes mix a mapping with its formula.
- **Level:** General mathematical history.
- **Access:** Free public article. https://mathshistory.st-andrews.ac.uk/HistTopics/Functions/

### Einstein's 1916 relativity paper

- **Resource:** Albert Einstein, "Die Grundlage der allgemeinen Relativitatstheorie."
- **Why use it:** This is a primary historical anchor for the repeated-index summation convention. Read the notation declaration, not the full physics, unless you have the necessary background.
- **Level:** Historical primary source; technical content is advanced.
- **Access:** DOI landing page provides publication metadata; full-text access may depend on institution. https://doi.org/10.1002/andp.19163540702

## Practice resources

### Stanford CS103 materials

- **Resource:** Stanford, *CS103 Mathematical Foundations of Computing*.
- **Why use it:** Course handouts and proof-writing guidance provide practice turning definitions and notation into precise prose. Functions, sets, and logical parsing are especially relevant.
- **Level:** Undergraduate introductory discrete mathematics.
- **Access:** Many course pages and handouts are publicly accessible; some class systems require Stanford access. https://web.stanford.edu/class/cs103/

### NumPy indexing guide

- **Resource:** NumPy, "Indexing on ndarrays."
- **Why use it:** It is the authoritative reference for zero-based array indices, slicing, Boolean masks, and the shape effects of basic and advanced indexing. Use it to check a math-to-code translation rather than relying on memory.
- **Level:** Beginner to intermediate Python and NumPy.
- **Access:** Free official documentation. https://numpy.org/doc/stable/user/basics.indexing.html

### A paper-reading drill

- **Resource:** The module's [paper-notation archaeology exercise](../exercises/README.md#e00111-paper-notation-archaeology).
- **Why use it:** It turns passive reading into a concrete reconstruction task: build symbol tables, infer shapes, and translate equations while marking uncertainty.
- **Level:** Adjustable from introductory to advanced, depending on the papers chosen.
- **Access:** Free; use publicly accessible papers.

## Suggested sequence

1. Keep the project notation guide beside you while completing the exercises.
2. Use MIT 6.042J for a fuller treatment of functions and finite mathematics.
3. Read selected *Concrete Mathematics* sections when reindexing and bounds need more practice.
4. Use the NumPy guide while translating notation into arrays.
5. Finish with Iverson and the paper-archaeology activity to examine notation as a design choice.

[Back to module](../README.md) | [Exercises](../exercises/README.md)
