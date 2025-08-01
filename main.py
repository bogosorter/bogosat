from atom import Atom
from operators import Not
from solver import Solver

p = Atom("p")
formula = Not(p)

solver = Solver(formula, [p], 0.1)
solver.solve()
solver.print()
