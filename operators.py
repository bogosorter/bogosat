class Not():
    def __init__(self, formula):
        self.formula = formula
    
    def evaluate(self):
        return 1 - self.formula.evaluate()
    
    def backprop(self, value):
        self.formula.backprop(-value)

    def step(self, size):
        self.formula.step(size)

class And():
    # This value is used to prevent stall gradients when both values are at zero
    epsilon = 1e-4

    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()
    
    def backprop(self, value):
        self.left.backprop(value * (self.right.evaluate() + self.epsilon))
        self.right.backprop(value * (self.left.evaluate() + self.epsilon))

    def step(self, value):
        self.left.step(value)
        self.right.step(value)
