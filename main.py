from atom import Atom
from operators import Or, And, Not, Implies
from solver import Solver

p = Atom('p')
q = Atom('q')

formula = And(Implies(p, Not(q)), p)

solver = Solver(formula, p, q)
solver.solve()
