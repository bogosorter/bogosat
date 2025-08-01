class Solver():
    def __init__(self, formula, propositions, step):
        self.formula = formula
        self.propositions = propositions
        self.step = step
    
    def solve(self):
        while self.formula.evaluate() != True:
            self.formula.backprop(1)
            self.formula.step(self.step)
    
    def print(self):
        for proposition in self.propositions:
            print(f"{proposition.name}: {proposition.value}")
        print(f"Formula: {self.formula.evaluate()}")
