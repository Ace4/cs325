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
z = ['p1','p2','p3','p4','p5','p6','p7']

x = [1,2,3,5,7,8,10]
y = [3,5,7,11,14,15,19]

# x = {
# 	 'p1': 1,
# 	 'p2': 2,
# 	 'p3': 3,
# 	 'p4': 5,
# 	 'p5': 7,
# 	 'p6': 8,
# 	 'p7': 10}

# y = {
# 	 'p1': 3,
# 	 'p2': 5,
# 	 'p3': 7,
# 	 'p4': 11,
# 	 'p5': 14,
# 	 'p6': 15,
# 	 'p7': 19}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("notleastsquares",LpMinimize)

# A dictionary called 'Points' is created to contain the referenced Variables
Points = LpVariable.dicts("Points", z)

# First constraint is the objective
prob += lpSum([a*x[i] + b*y[i] - c for i in range(len(z))]), "MinimizeObjective"

# Add maximum absolute value constraints
for i in range(len(z)):
	prob += a  != 0  or b  != 0  or c != 0 
	j = z[i]
	prob += Points[j] >= a*x[i] + b*y[i] - c, "PositiveAbsoluteRequiement_%s" % Points[j]
	prob += Points[j] >= -a*x[i] - b*y[i] + c, "NegativeAbsoluteRequiement_%s" % Points[j]
	
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