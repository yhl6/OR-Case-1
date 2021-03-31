from gurobipy import *
# build a new model
eg1 = Model("eg1")  # build a new model, name it as "eg1"

x1 = eg1.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = 'x1')
x2 = eg1.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = "x2")
# setting the objective function
# use GRB.MAXIMIZE for a maximization problem
eg1.setObjective(700 * x1 + 900 * x2, GRB.MAXIMIZE)

# add constraints and name them
eg1.addConstr(3 * x1 + 5 * x2 <= 3600, "resource_wood")
eg1.addConstr(x1 + 2 * x2 <= 1600, "resource_labor")
eg1.addConstr(50 * x1 + 20 * x2 <= 48000, "resource_machine")
eg1.optimize()