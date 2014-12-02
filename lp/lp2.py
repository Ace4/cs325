"""
Linear Programming Model for the 
least squares isn't good enough 
for me optimization problem.

"""

# Import PuLP modeler functions
from pulp import *

a = LpVariable('a')
c = LpVariable('c')
z = LpVariable('z')
points = ['p1','p2','p3','p4','p5','p6','p7']

x = {
	 'p1': 1,
	 'p2': 2,
	 'p3': 3,
	 'p4': 5,
	 'p5': 7,
	 'p6': 8,
	 'p7': 10}

y = {
	 'p1': 3,
	 'p2': 5,
	 'p3': 7,
	 'p4': 11,
	 'p5': 14,
	 'p6': 15,
	 'p7': 19}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("notleastsquares",LpMinimize)

# A dictionary called 'Points' is created to contain the referenced Variables
Points = LpVariable.dicts("Points", points)

# First constraint is the objective
prob += z, "MinimizeObjective"

# Add maximum absolute value constraints
for i in points:
	prob += z + (y[i] - a*x[i] - c) >= 0, "PositiveAbsoluteRequiement_%s" % Points[i]
	prob += z - (y[i] - a*x[i] - c) >= 0, "NegativeAbsoluteRequiement_%s" % Points[i]

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
print("Maximum Absolute Deviation = ", value(prob.objective))