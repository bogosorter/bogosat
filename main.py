from atom import Atom
from operators import Or, And, Not
from solver import Solver

p = Atom("p")
formula = And(Not(p), p)

solver = Solver(formula, p)
solver.solve()
solver.print()
