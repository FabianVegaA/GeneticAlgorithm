import random
import pprint

from src.knapsack import Knapsack
from src.object import Object
from src.genetic import GeneticAlgorithm


def main():

    items = []
    n_items = int(input("Enter number of items: "))
    for i in range(n_items):
        worth, weight = input(f"{i+1}. Enter worth and weight: ").split()
        items.append(Object(int(worth), float(weight)))

    capacity = int(input("Enter knapsack capacity: "))
    knapsack = Knapsack(capacity, items, seed=0)
    random.seed(0)

    pprint.pprint(items)

    size_sample = int(input("Enter size of sample: "))
    genetic = GeneticAlgorithm(
        size_sample, lambda: [random.randint(0, 1) for _ in range(len(items))]
    )

    results = genetic.train(
        fitness=knapsack.fitness_function,
        crossover_method=knapsack.crossover,
        mutator=knapsack.mutation,
        iterations=100,
    )
    for result in results:
        objs = list(filter(lambda o: o is not None, knapsack.to_object_list(result)))
        if (
            weight := knapsack._calculate_weight(objs)
        ) <= knapsack.capacity and weight > 0:
            print(
                "Knapsack: {} TotalWorth: {} TotalWeight: {}".format(
                    objs,
                    knapsack._calculate_worths(objs),
                    knapsack._calculate_weight(objs),
                )
            )


if __name__ == "__main__":
    main()
