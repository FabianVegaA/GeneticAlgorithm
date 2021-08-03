import random


class Knapsack:
    def __init__(self, capacity, possible_items, seed=0):
        random.seed(seed)
        self.capacity = capacity
        self._items = possible_items

    def _calculate_worths(self, items):
        worth = 0
        for item in items:
            if item is not None:
                worth += item.worth
        return worth

    def _calculate_weight(self, items):
        weight = 0
        for item in items:
            if item is not None:
                weight += item.weight
        return weight

    def to_object_list(self, items):
        return [self._items[i] if items[i] else None for i in range(len(items))]

    def fitness_function(self, items_1, items_2):
        assert len(items_1) == len(items_2)

        object_1 = self.to_object_list(items_1)
        object_2 = self.to_object_list(items_2)

        worth_1 = self._calculate_worths(object_1)
        worth_2 = self._calculate_worths(object_2)

        return items_1 if worth_1 >= worth_2 and worth_1 <= self.capacity else items_2

    def crossover(self, parent_1, parent_2):
        assert len(parent_1) == len(parent_2)
        length = len(parent_1) // 2

        child_1 = parent_1[:length] + parent_2[length:]
        child_2 = parent_2[:length] + parent_1[length:]

        return child_1, child_2

    def mutation(self, item):
        index = random.randint(0, len(item) - 1)

        item[index] = 1 if item[index] == 0 else 0

        return item
