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
            # Rounding does not cause a problem, since only the atoms that are
            # already rounded are important for the formula satisfiability
            proposition.round()
            print(f"{proposition.name}: {proposition.value}")
