def simple_double_function(a):
    return a * 2


class MyObject:
    def __init__(self, name, multiplier):
        self.name = name
        self.multiplier = multiplier

    def simple_multiplier(self, a):
        return a * self.multiplier
