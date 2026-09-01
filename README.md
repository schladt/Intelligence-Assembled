# Intelligence, Assembled

### *From first principles to modern AI.*

Modern artificial intelligence sits on top of a surprisingly deep stack of ideas. Calculus. Linear algebra. Probability. Statistics. Optimization. Information theory. Algorithms. Machine learning. Neural networks. Large language models. And a lot of things in between.

**Intelligence, Assembled** is my attempt to work through that stack from the ground up.

---

## Why This Exists

I recently finished my PhD in computer science, where my research focused on computational intelligence. You might think that means I have every theorem, derivation, algorithm, and mathematical identity permanently loaded into memory.

I do not.

My path through academia was long and anything but linear. I earned my first engineering degrees in Electrical Engineering and Computer Engineering back in 2010, then stepped away from academia. I spent the next decade working in industry while the academic side of my brain collected dust. I returned in 2020 to begin a master's program, finished it in 2022, and then went straight into the PhD program I completed this year.

That makes it a sixteen-year journey, with a ten-year gap in the middle.

During that gap, entire subfields shifted. Deep learning moved from a research curiosity to the dominant paradigm. Transformers were invented. Large language models went from theoretical to world-changing. The field I returned to in 2020 was not the same one I had left in 2010.

And honestly, the deeper I go, the more I find I want to understand better: concepts I learned once and forgot, topics I skimmed but never internalized, foundations I skipped on the way to something more advanced, and connections I never had time to sit with properly.

So I am going back to the beginning.

This repository is part curriculum, part reference, and part personal learning project. It is my attempt to build, rebuild, and eventually master the skills and first principles required to truly understand how modern AI works. Not just use it. Understand it.

I am building this because I need it. If it turns out to be useful to anyone else, all the better.

---

## The Idea

There is a tendency in modern AI education to begin somewhere around:

```
model.fit(X, y)
```

or:

> Here is a transformer. Let's explain attention.

That is useful, but it skips an enormous amount of interesting machinery.

Why does gradient descent work? What exactly is a vector space? Why is variance defined the way it is? Where does entropy come from? Why does the sigmoid function keep appearing? What does an eigenvector actually represent? Why can a neural network approximate complicated functions? How did we get from probability and statistics to machine learning, neural networks, transformers, and large language models?

The goal of this project is to keep asking **why** until there is nowhere useful left to go.

---

## The Stack

The roadmap moves through fifteen sections, with each one building on what came before:

| # | Section | Focus |
|---|---------|-------|
| 0 | Mathematical Foundations | Arithmetic, algebra, functions, sets, logic, notation |
| 1 | Calculus | Derivatives, integrals, gradients, chain rule |
| 2 | Linear Algebra | Vectors, matrices, eigenvalues, decompositions |
| 3 | Probability | Distributions, Bayes' theorem, sampling, CLT |
| 4 | Statistics | Inference, estimation, hypothesis testing, regression |
| 5 | Optimization | Gradient descent, convexity, constrained optimization |
| 6 | Information Theory | Entropy, cross-entropy, KL divergence |
| 7 | Data & Intelligent Data Analysis | Features, dimensionality reduction, clustering, evaluation |
| 8 | Machine Learning | Supervised/unsupervised learning, SVMs, ensembles, regularization |
| 9 | Evolutionary Computation | Genetic algorithms, evolution strategies, neuroevolution |
| 10 | Neural Networks | Perceptrons, backpropagation, CNNs, RNNs |
| 11 | Deep Learning | Embeddings, attention, generative models, scaling |
| 12 | Transformers | Self-attention, multi-head attention, encoder/decoder |
| 13 | Large Language Models | Pretraining, RLHF, RAG, agents, reasoning |
| 14 | Beyond | Reinforcement learning, causal inference, AI safety, and more |

The full [roadmap](ROADMAP.md) goes much deeper: over 240 topic modules with granular subtopics, learning objectives, and a prerequisite graph. I built it by comparing what MIT, Stanford, Harvard, CMU, Berkeley, Cornell, and Princeton actually teach.

## Philosophy

- **Start from first principles.** Build concepts from simpler concepts rather than treating them as magic.
- **Understand before abstracting.** Implement things before reaching for high-level frameworks. Calling a function is not the same as understanding what that function does.
- **Math is part of the subject.** The mathematics will not be hidden behind "you don't really need to understand this." Sometimes you really do.
- **Intuition and rigor should coexist.** Knowing an equation is useful. Knowing what the equation *means* is better.
- **Exercises matter.** Reading something and understanding something are not the same thing. Conceptual questions, derivations, programming exercises, experiments, and implementations from scratch.
- **Go deep.** This is not a collection of five-minute tutorials. When a rabbit hole is interesting, all bets are off.

## Module Structure

```
module/
├── README.md        # Overview and learning objectives
├── notes/           # Explanations and derivations
├── exercises/       # Problems
├── solutions/       # Worked solutions
├── notebooks/       # Jupyter notebooks
├── code/            # Implementations
└── resources/       # References and further reading
```

Each topic aims to move through: **Intuition → Mathematics → Derivation → Implementation → Experimentation → Exercises**

Not every topic needs all six, but that is the path I am aiming for.

## Who Is This For

I expect it will be most useful to:

- Students studying CS, math, data science, or AI
- Software engineers who want to understand the theory underneath modern AI
- Researchers revisiting foundational material
- Practitioners who learned frameworks before learning the mathematics
- People teaching themselves machine learning
- People who are simply curious about how all of this fits together

And, very explicitly, **me.**

This repository exists because there are things I want to relearn, things I want to understand more deeply, and things I somehow managed to earn a PhD without being able to derive on a whiteboard from memory.

That is fine. Knowing everything is not the goal. Understanding more than I did yesterday is.

## Current Status

🚧 **Very early development.** I am building this repository incrementally, so expect incomplete modules, reorganized directories, rewritten explanations, questionable first drafts, exercises without solutions, and occasional mathematical crimes. It will improve as I work through it.

## Contributing

I started this as a personal learning project, but it is public for a reason. Corrections, better explanations, additional exercises, alternative derivations, and thoughtful discussions are welcome.

If something here is wrong, please [open an issue](https://github.com/schladt/Intelligence-Assembled/issues). I would much rather publicly correct a mistake than privately preserve one.

## License

[MIT](LICENSE)