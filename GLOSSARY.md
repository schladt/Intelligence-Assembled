# Glossary

## Purpose

This glossary disambiguates terms used differently across mathematics, statistics, machine learning, computational intelligence, and modern AI. It is an index, not a second textbook. Full explanations belong in the owning modules listed with each entry.

Entries are concise. Each gives the primary meaning, important overloads, and the most common confusion.

## Activation

**Primary meaning:** The output of a neuron or layer after applying an activation function (§10.03).

**Also used for:** The activation function itself, activation statistics used for debugging, and stored activations used during backpropagation.

**Common confusion:** Activation checkpointing stores or recomputes intermediate values. It is not a kind of activation function.

## Algorithm

**Primary meaning:** A finite, well-defined procedure for solving a class of problems (§0.14).

**Also used for:** A high-level method whose implementation leaves choices unspecified, such as `the EM algorithm` or `gradient descent`.

**Common confusion:** A model describes a relationship or distribution; an algorithm computes, estimates, trains, searches, or acts.

## Attention

**Primary meaning:** A learned weighted combination of values in which weights depend on query-key compatibility (§12.02).

**Variants:** Self-attention, cross-attention, multi-head attention, and an individual attention weight or head.

**Common confusion:** An attention weight is one scalar in the mechanism. It is not automatically a causal explanation of the model's decision.

## Bias

**Statistical bias:** The systematic difference between an estimator's expected value and the target parameter (§4.03).

**Neural-network bias:** An additive learned parameter in a layer (§10.05).

**Social or measurement bias:** Systematic differences arising from data, labels, institutions, or deployment (§7.16).

**Common confusion:** These meanings are related only loosely. Always write `statistical bias`, `bias parameter`, or `social bias` when context could be unclear.

## Capacity

**Primary meaning:** The range or complexity of functions a model class can represent (§8.16).

**Also used for:** Channel capacity in information theory (§6.07), system throughput, and expert capacity in mixture-of-experts models (§12.08).

**Common confusion:** More model capacity can reduce approximation error while increasing estimation or optimization difficulty. It is not synonymous with performance.

## Convergence

**Mathematics and probability:** A sequence approaches a limit, under a named mode such as almost sure or in probability (§3.11).

**Optimization:** Iterates, objective values, or gradients approach a target condition (§5.06).

**MCMC:** A chain approaches its stationary distribution (§4.12).

**Common confusion:** Always state what converges, to what, and under which assumptions.

## Dimension

**Primary meaning:** The number of basis vectors in a vector space (§2.01).

**Also used for:** An array axis, feature count, latent width, model width, and physical unit.

**Common confusion:** Matrix rank is not the same as the number of columns, though it cannot exceed it.

## Distribution

**Probability:** A rule assigning probabilities to outcomes of a random variable (§3.01).

**Data:** The empirical pattern of observed values.

**Systems:** The act of spreading computation or data across machines.

**Common confusion:** A probability distribution is a mathematical object. An empirical distribution is constructed from finite observations.

## Embedding

**Primary meaning:** A representation of an object as a vector in a space where geometry carries useful structure (§10.17).

**Also used for:** A mathematical structure-preserving map, a token lookup, or a latent representation.

**Common confusion:** An embedding is not necessarily low-dimensional, interpretable, or unique.

## Entropy

**Primary meaning:** Expected surprisal under a probability distribution (§6.01).

**Related terms:** Cross-entropy compares a target distribution with a model distribution. KL divergence measures an ordered discrepancy between distributions.

**Common confusion:** Entropy, cross-entropy, and KL divergence are related but not interchangeable.

## Epoch

**Machine learning:** One nominal pass through a training dataset.

**Evolutionary computation:** Sometimes used informally for a generation or migration interval.

**Common confusion:** With sampling, shuffling, streaming, or distributed training, an epoch may not mean every example was seen exactly once.

## Estimator and Estimate

**Estimator:** A rule or random variable that maps data to a proposed parameter value (§4.01).

**Estimate:** The realized value produced for one dataset.

**Common confusion:** Before observing data, $\widehat{\theta}$ is random. After observing data, its computed value is fixed.

## Feature

**Primary meaning:** An input variable or derived measurement used by a model (§7.07).

**Representation learning:** A learned direction or pattern that responds to some property of the data.

**Interpretability:** A hypothesized meaningful component in an internal representation (§14.16).

**Common confusion:** A feature need not correspond to one human-readable concept.

## Fitness

**Primary meaning:** The quantity used to evaluate or rank individuals in an evolutionary algorithm (§9.04).

**Common confusion:** Some algorithms maximize fitness while others minimize cost. State the direction explicitly. Fitness may differ from the original objective after scaling, penalties, or multi-objective ranking.

## Generalization

**Primary meaning:** Performance on relevant unseen data (§8.16).

**Variants:** Generalization gap, length generalization, compositional generalization, and out-of-distribution generalization.

**Common confusion:** Good performance on a fixed test set does not establish every kind of generalization.

## Gradient

**Primary meaning:** The vector representing the derivative of a scalar-valued function under an inner product (§1.09, §2.12).

**Gradient descent:** An optimization algorithm that moves opposite the gradient (§5.06).

**Stochastic gradient:** An estimate of a population or full-data gradient (§5.09).

**Common confusion:** The gradient is a mathematical object. Gradient descent is an algorithm that uses it.

## Hyperparameter

**Primary meaning:** A setting chosen outside the fitted parameter update, such as regularization strength, tree depth, or learning-rate schedule (§8.18).

**Common confusion:** A value can be a parameter in one formulation and a hyperparameter in another. State how it is selected.

## Information

**Self-information:** The surprisal $-\log p(x)$ of an outcome (§6.01).

**Mutual information:** The reduction in uncertainty about one variable from observing another (§6.02).

**Fisher information:** The sensitivity of a likelihood to a parameter (§4.04).

**Common confusion:** These share a name and mathematical relationships, but they answer different questions.

## Iteration

**Primary meaning:** One update of an algorithm.

**Related terms:** A batch step, epoch, generation, time step, and decoding step are different units of progress.

**Common confusion:** Report which unit a metric or schedule uses.

## Latent Variable

**Primary meaning:** A variable included in a model but not directly observed (§8.14).

**Also used for:** A latent code or representation produced by an encoder (§11.03).

**Common confusion:** `Latent` means hidden in the model, not necessarily meaningful, causal, or disentangled.

## Likelihood

**Primary meaning:** The probability model for observed data viewed as a function of its parameters (§4.02).

$$
\mathcal{L}(\theta;\mathcal{D})=p(\mathcal{D}\mid\theta).
$$

**Common confusion:** A likelihood is not automatically a probability distribution over $\theta$.

## Loss, Risk, and Objective

**Loss:** A penalty for one prediction or example.

**Population risk:** Expected loss under the data-generating distribution.

**Empirical risk:** Average loss over a finite dataset.

**Objective:** The complete quantity optimized, possibly including regularization or constraints (§5.01, §8.01).

**Common confusion:** Calling all four `loss` can hide which quantity a theorem or implementation actually uses.

## Model

**Statistical model:** A family of probability distributions (§4.01).

**Predictive model:** A function mapping inputs to predictions (§8.01).

**Neural model:** A parameterized neural network.

**Causal model:** A structure describing interventions and counterfactuals (§14.14).

**Common confusion:** Specify the kind of model when its commitments matter.

## Parameter

**Primary meaning:** A value learned or estimated from data.

**Common confusion:** Parameters, hyperparameters, inputs, hidden states, and optimizer states play different roles even when all are stored as arrays.

## Probability and Density

**Probability:** A number assigned to an event, between zero and one.

**Density:** A function whose integral over a region gives probability (§3.04).

**Common confusion:** A continuous density can exceed one. The probability of one exact continuous value is usually zero.

## Regularization

**Primary meaning:** A preference or constraint that discourages certain solutions to improve generalization, stability, or identifiability (§8.03).

**Examples:** Penalties, priors, early stopping, dropout, data augmentation, and architectural constraints.

**Common confusion:** Weight decay and L2 regularization are equivalent for ordinary SGD under common formulations but differ under adaptive optimizers.

## Representation

**Primary meaning:** The form in which information is encoded for computation.

**Evolutionary computation:** The genotype and its mapping to a candidate solution (§9.03).

**Deep learning:** Learned activations or embeddings (§10.17).

**Common confusion:** A useful representation depends on the operations and task applied to it.

## Sample and Sampling

**Data sample:** One observation or a finite dataset, depending on context.

**Probability sampling:** Drawing a realization from a distribution (§3.04).

**Monte Carlo:** Estimating a quantity using random samples.

**Common confusion:** State whether `sample` means one observation, the dataset, or the act of drawing.

## State

**Dynamical systems:** The information needed to evolve a system forward (§8.21).

**Reinforcement learning:** The environment representation used by the decision process (§14.02).

**Software:** Mutable program data at a point in execution.

**Common confusion:** An observation need not be a complete state.

## Token

**Primary meaning:** A discrete unit produced by a tokenizer and represented by an integer ID (§13.02).

**Common confusion:** A token is not necessarily a word or character. Token boundaries depend on the tokenizer and vocabulary.

## Training

**Primary meaning:** Adjusting model parameters using data and an objective.

**Related terms:** Fitting, optimization, pretraining, fine-tuning, and post-training describe different scopes or stages.

**Common confusion:** Training loss measures objective performance on training data. It does not by itself measure generalization.

## Variance

**Probability:** Expected squared deviation from a mean (§3.03).

**Statistics:** Variation of an estimator across repeated samples (§4.03).

**Machine learning:** One component of the bias-variance decomposition (§8.17).

**Common confusion:** Data variance, estimator variance, predictive variance, and uncertainty are not interchangeable.

## Maintaining the Glossary

Add an entry when:

- a term has several meanings in the curriculum;
- readers repeatedly confuse it with a nearby term;
- the project uses a term more narrowly than common usage;
- different fields use incompatible conventions.

Keep entries short. Link to the owning module for the full explanation. If an entry grows into a lesson, move the lesson into the module and leave only the distinction here.
