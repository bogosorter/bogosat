from atom import Atom
from operators import Or, And, Not
from solver import Solver

p = Atom("p")
q = Atom("q")
formula = And(Not(p), Or(p, q))

solver = Solver(formula, [p, q], 0.01)
solver.solve()
solver.print()
