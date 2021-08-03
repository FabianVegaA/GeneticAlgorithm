from functools import reduce
from collections import Counter


class GeneticAlgorithm:
    def __init__(self, size, generator):
        self.size = size
        self.sample = list(generator() for _ in range(size))

    def _break_into_batches(self, sample, size_batch):
        assert len(sample) >= size_batch
        for i in range(0, len(sample), size_batch):
            result = sample[i : i + size_batch]
            if len(result) < size_batch:
                result += result[: size_batch - len(result)]
            yield result

    def _batcher(self, sample, batch_size):
        for i in range(len(sample)):
            if i + batch_size < len(sample):
                result = sample[i : i + batch_size]
            else:
                result = (sample[i:] * batch_size)[:batch_size]
            print(f"\t\tBatch {i}:", result)
            yield result

    def selection(self, fitness):
        return [fitness(*data) for data in self._break_into_batches(self.sample, 2)]

    def crossover(self, crossover_method, mutator, parent1, parent2):
        return [mutator(r) for r in crossover_method(parent1, parent2)]

    def train(self, fitness, crossover_method, mutator, iterations=100):
        for i in range(iterations):
            print(f"Iteration {i}\n\tSample: {self.sample}\n    Starting selection...")
            selection = self.selection(fitness)
            print(f"\t Selection: {selection}\n    Starting crossover...")
            crossovers = sum(
                [
                    self.crossover(crossover_method, mutator, parent1, parent2)
                    for parent1, parent2 in self._batcher(selection, 2)
                ],
                [],
            )
            print(f"\t Crossovers: {crossovers}")
            self.sample = crossovers

        return self.selection(fitness)
