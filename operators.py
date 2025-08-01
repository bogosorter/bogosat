class Not():
    def __init__(self, formula):
        self.formula = formula
    
    def evaluate(self):
        return 1 - self.formula.evaluate()
    
    def backprop(self, value):
        self.formula.backprop(-value)

    def step(self, size):
        self.formula.step(size)
