from atom import Atom
from operators import Or, And, Not
from solver import Solver

a = Atom('a')
b = Atom('b')
c = Atom('c')
formula = And(And(Or(a, b), Or(Not(a), c)), Or(Not(b), c))

solver = Solver(formula, a, b, c)
solver.solve()
