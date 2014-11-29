"""
Linear Programming Model for the 
least squares isn't good enough 
for me optimization problem.

"""

# Import PuLP modeler functions
from pulp import *

a = LpVariable('a',None,None,LpInteger)
b = LpVariable('b',None,None,LpInteger)
c = LpVariable('c',None,None,LpInteger)

x = [1,2,3,5,7,8,10]
y = [3,5,7,11,14,15,19]

# Create the 'prob' variable to contain the problem data
prob = LpProblem("notleastsquares",LpMinimize)

# The objective function is added to 'prob' first
prob += ???

# Other constraints are added to the problem
prob += a != b != c != 0, "NotZerosRequirement"

# The problem data is written to an .lp file
prob.writeLP("notleastsquares.lp")

# The problem is solved using GLPK
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Optimized fit = ", value(prob.objective))