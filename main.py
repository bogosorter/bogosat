from atom import Atom
from operators import Not, And
from solver import Solver

p = Atom("p")
q = Atom("q")
formula = And(p, Not(q))

solver = Solver(formula, [p, q], 0.01)
solver.solve()
solver.print()
