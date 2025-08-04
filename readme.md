# bogosat

This is a toy SAT solver that uses fuzzy logic and gradient ascent.

## Usage

```python
from atom import Atom
from operators import Or, And, Not, Implies
from solver import Solver

p = Atom('p')
q = Atom('q')

formula = And(Implies(p, Not(q)), p)

solver = Solver(formula, p, q)
solver.solve()
```
```bash
python bogosat.py
```

```
Solution found:
p = True
q = False
```

## Under the hood

This solver uses fuzzy logic. This means that the atoms are converted from boolean variables into variables in the $[0, 1]$ range. At each step, the solver calculates the truth value of the current assignment. There are many different ways to do this. The one used here is based on product fuzzy logic:

- The atoms are evaluated into a value in the range $[0, 1]$.
- $V(\lnot p) = 1 - V(p)$
- $V(p \lor q) = V(p) + V(q) - V(p) \cdot V(q)$
- $V(p \land q) = V(p) \cdot V(q)$

These formulas can be differentiated to compute the gradient with respect to the atomic variables. The solver makes a step in the direction of the gradient until the formula is satisfied or the maximum number of steps is reached.

There is just one last aspect to take care of. Let's suppose that we want to discover the solution to $p \land q$, starting with the assignment $p = q = 0$:

$$
\frac{\partial V(p) \cdot V(q)}{\partial V(p)} = V(q) = 0
$$

The same is valid for the gradient with respect to $q$. This means that the solver will not make any progress towards the solution. To avoid this, the solver adds a small value $\epsilon$ to the gradient, thus ensuring that it cannot be zero.

> It should be noted that the use of product operators has some drawbacks. In particular, some of the equivalences in propositional logic do not hold: it is obvious that $p$ should be equivalent to $p \land p$, but the fuzzy logic evaluation of this expression is $V(p) \cdot V(p) = V(p)^2$, which is not equal to $V(p)$ unless $V(p)$ is either $0$ or $1$.
>
> There are other operators that deal with this issue (using, for instance, minimum and maximum), but they have their own problems.
