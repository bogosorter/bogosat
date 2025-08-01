class Solver():
    epsilon = 1e-4

    def __init__(self, formula, *atoms, step = 0.01, max_iteraions = 1000000):
        self.formula = formula
        self.atoms = atoms
        self.step = step
        self.max_iterations = max_iteraions
    
    def solve(self):
        for _ in range(self.max_iterations):
            if self.solved(): break

            self.formula.backprop(1)
            self.formula.step(self.step)

        if not self.solved():
            print(f'Solution not found within {self.max_iterations} iterations.')
            return

        print('Solution found:')
        for atom in self.atoms:
            # Rounding does not cause a problem, since only the atoms that are
            # already rounded are important for the formula satisfiability
            atom.round()
            print(f'{atom.name} = {'True' if atom.value else 'False'}')
    
    def solved(self):
        return self.formula.evaluate() >= 1 - self.epsilon
