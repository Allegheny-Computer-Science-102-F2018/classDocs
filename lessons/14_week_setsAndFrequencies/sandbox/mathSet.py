from sympy import Interval, Symbol, solve, solve_univariate_inequality, sin
from sympy.plotting import plot
from pylab import plot, show
import math
#plot: where are these solutions?
x = [i*.1 for i in range(-20,45)]
y = [math.sin(i*.1) for i in range(-20,45)]
plot(x,y)
show()


# define the variables
x = Symbol('x')
# define equation
ineq_obj = sin(x) > 0
# solve an equation
s = solve_univariate_inequality(ineq_obj,x, relational=False)
#Interval.open(0, pi)
