import pyomo.environ as pyo  # type: ignore

model = pyo.ConcreteModel()
model.x = pyo.Var([1, 2], domain=pyo.NonNegativeIntegers)
model.Objective = pyo.Objective(expr=2 * model.x[1] + 3 * model.x[2], sense=pyo.maximize)
model.Constraint1 = pyo.Constraint(expr=2 * model.x[1] + model.x[2] <= 10)
model.Contstaint2 = pyo.Constraint(expr=3 * model.x[1] + 6 * model.x[2] <= 40)
res = pyo.SolverFactory("glpk").solve(model)

print("x_1 =", model.x[1]())
print("x_2 =", model.x[2]())
print("Objective =", model.Objective())
