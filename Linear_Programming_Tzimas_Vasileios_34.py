from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():

  solver = pywraplp.Solver('LinearExample',
                           pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)


  x = solver.NumVar(-solver.infinity(), solver.infinity(), 'x')
  y = solver.NumVar(-solver.infinity(), solver.infinity(), 'y')
#s.t. 2 * x1 + x2 <= 100
  constraint1 = solver.Constraint(-solver.infinity(), 100)
  constraint1.SetCoefficient(x, 2)
  constraint1.SetCoefficient(y, 1)
#s.t. 2 * x1 + x2 <= 100
  constraint2 = solver.Constraint(-solver.infinity(), 80)
  constraint2.SetCoefficient(x, 1)
  constraint2.SetCoefficient(y, 1)
#max z = 50 * x1 + 18 * x2
  objective = solver.Objective()
  objective.SetCoefficient(x, 50)
  objective.SetCoefficient(y, 18)
  objective.SetMaximization()

  solver.Solve()
  opt_solution = 6 * x.solution_value() + 8 * y.solution_value()
  print('Number of variables =', solver.NumVariables())
  print('Number of constraints =', solver.NumConstraints())

  print('Solution:')
  print('x = ', x.solution_value())
  print('y = ', y.solution_value())


  print('Optimal objective value =', opt_solution)

  print(('%s: reduced cost = %f' % (x, x.reduced_cost())))
  print(('%s: reduced cost = %f' % (y, y.reduced_cost())))
  print(('%s: Dual Value = %f' % (y, constraint1.dual_value())))
  print(('%s: Dual Value = %f' % (y, constraint2.dual_value())))

if __name__ == '__main__':
  main()
