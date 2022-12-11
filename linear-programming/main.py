import pulp  # type: ignore

problem = pulp.LpProblem("test", pulp.LpMaximize)

# variables
x1 = pulp.LpVariable("x1", lowBound=0, cat="Continuous")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Continuous")

# objective function
problem += 3 * x1 + 2 * x2

# constraints
problem += 2 * x1 + 5 * x2 <= 40
problem += 3 * x1 + x2 <= 30
problem += 3 * x1 + 4 * x2 <= 39

# solve
status = problem.solve()
print(pulp.LpStatus[status])

# print results
print(f"x1 = {x1.value()}")
print(f"x2 = {x2.value()}")
print(f"objective = {pulp.value(problem.objective)}")
