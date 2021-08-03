# GeneticAlgorithm

This is a generic genetic algorithm with a knapsack problem model

# How do it uses?

For the knapsack problem you must put some parameters.

| Parameter        | Description                           |
| ---------------- | ------------------------------------- |
| n_items          | Number of items                       |
| worth and weight | Worth and weight separated by a space |
| capacity         | Size of knapsack                      |
| size_sample      | Number of agents for iteration        |

If you want to try with other problem type, you can make a class with the next methods:

- generator of agents: this is able to create the agents.
- fitness function: this is used in the selection phase, able to select the best agents by epoch.
- crossover: this is used in the crossover phase, able to cross the agents.
- mutator: this able to mutate the agents.

> Warning: I recommend to use Python version > 3.8.

---

If you have any question, you can contact me at Twitter: [@fabianmativeal](https://twitter.com/fabianmativeal)
