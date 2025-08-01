class Solver():
    def __init__(self, formula, *atoms, step = 0.01, max_iteraions = 1000000):
        self.formula = formula
        self.atoms = atoms
        self.step = step
        self.max_iterations = max_iteraions
    
    def solve(self):
        for _ in range(self.max_iterations):
            if self.formula.evaluate() == True: break

            self.formula.backprop(1)
            self.formula.step(self.step)
    
    def print(self):
        if self.formula.evaluate() != True:
            print(f"Solution not found within {self.max_iterations} iterations.")
            return

        for atom in self.atoms:
            # Rounding does not cause a problem, since only the atoms that are
            # already rounded are important for the formula satisfiability
            atom.round()
            print(f"{atom.name}: {atom.value}")
