"""
Linear Programming Model for the mmmm ... tofu
optimization problem.

"""

# Import PuLP modeler functions
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("tofu",LpMaximize)

#problem variables
x1 = LpVariable("edamame_fresh",0,None, LpInteger)
x2 = LpVariable("edamame_flavored_rt",0,None, LpInteger)
x3 = LpVariable("edamame_fresh_flavored_ot",0,None, LpInteger)
x4 = LpVariable("tofu_fresh",0,None, LpInteger)
x5 = LpVariable("tofu_flavored_rt",0,None, LpInteger)
x6 = LpVariable("tofu_fresh_flavored_ot",0,None, LpInteger)
x7 = LpVariable("tempeh_fresh",0,None, LpInteger)
x8 = LpVariable("tempeh_flavored_rt",0,None, LpInteger)
x9 = LpVariable("tempeh_fresh_flavored_ot",0,None, LpInteger)

# The objective function is added to 'prob' first
prob += 4*x1 + 12*x2 + 7*x3 + 8*x4 + 14*x5 + 11*x6 + 4*x7 + 13*x8 + 9*x9

#objective is subject to these constraints
prob += x1 + x2 + x3 == 400, "EdamameAmmountRequirement"
prob += x4 + x5 + x6 == 480, "TofuAmmountRequirement"
prob += x7 + x8 + x9 == 230, "TempehAmmountRequirement"
prob += x2 + x5 + x8 <= 420, "FlavoringRegularTimeRequirement"
prob += x3 + x6 + x9 <= 250, "FlavoringOvertimeRequirement"

# The problem data is written to an .lp file
prob.writeLP("tofu.lp")

# The problem is solved using GLPK
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Optmized Daily Profit = ", value(prob.objective))