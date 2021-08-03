class Object:
    def __init__(self, worth, weight):
        self.worth = worth
        self.weight = weight

    def __repr__(self):
        return "Object(worth={}, weight={})".format(self.worth, self.weight)
