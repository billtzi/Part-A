from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
  solver = pywraplp.Solver('SolveIntegerProblem',
                           pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
  x = solver.IntVar(0.0, solver.infinity(), 'x')
  y = solver.IntVar(0.0, solver.infinity(), 'y')
  
#s.t. x1 + x2 <= 10
  constraint1 = solver.Constraint(-solver.infinity(), 10)
  constraint1.SetCoefficient(x, 1)
  constraint1.SetCoefficient(y, 1)

#s.t 2 * x1 + x2 <=18
  constraint2 = solver.Constraint(-solver.infinity(), 18)
  constraint2.SetCoefficient(x, 2)
  constraint2.SetCoefficient(y, 1)
  
#max z= 30 * x1 + 40 * x2
  objective = solver.Objective()
  objective.SetCoefficient(x, 30)
  objective.SetCoefficient(y, 40)
  objective.SetMaximization()

  result_status = solver.Solve()
  assert result_status == pywraplp.Solver.OPTIMAL

  assert solver.VerifySolution(1e-7, True)

  print('Number of variables =', solver.NumVariables())
  print('Number of constraints =', solver.NumConstraints())

  print('Optimal objective value = %d' % solver.Objective().Value())
  print()

  variable_list = [x, y]

  for variable in variable_list:
    print('%s = %d' % (variable.name(), variable.solution_value()))

if __name__ == '__main__':
  main()
