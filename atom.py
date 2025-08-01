from random import random

class Atom():
    def __init__(self, name):
        self.name = name
        self.value = random()
        self.gradient = 0

    def evaluate(self):
        return self.value

    def backprop(self, value):
        self.gradient += value

    def step(self, size):
        self.value += self.gradient * size
        self.value = max(0, min(1, self.value))
        self.gradient = 0
