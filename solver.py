class Solver():
    def __init__(self, formula, atoms, step):
        self.formula = formula
        self.atoms = atoms
        self.step = step
    
    def solve(self):
        while self.formula.evaluate() != True:
            self.formula.backprop(1)
            self.formula.step(self.step)
    
    def print(self):
        for atom in self.atoms:
            # Rounding does not cause a problem, since only the atoms that are
            # already rounded are important for the formula satisfiability
            atom.round()
            print(f"{atom.name}: {atom.value}")
