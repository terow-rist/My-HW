import matrix_logic
import matplotlib.pyplot as plt
import sympy as sym 
from sympy import *

# n, m = int(input("number of rows: ")), int(input("number of col: "))
e = 1e-5

matrix = [
    [5, 2, 1, 7],
    [-1, 4, 2, 3],
    [2, -3, 10, -1]
]
# matrix = matrix_logic.matrix_init(n, m)

# Values of each Xi in matrix 
# Initialize symbols for sympy
x_list = [-2.4, 5.0, 1] # or [0]*len(matrix)

x_symbols = symbols('x1:'+str(len(matrix)+1))

# Create expression for each variable
c = 0
expressions = [] 
for i in matrix:
    expr = sum([coef*var for coef, var in zip(i, x_symbols)]) - i[-1]
    expressions.append(solve(expr, x_symbols[c])[0])
    # print(solve(expr, x_symbols[c]))
    c+=1

# Iteration proccess
c = 0
result, errors = [], []
converged = False
while not converged:
    new_x_list = []
    for exp in expressions:
        res = {x_symbols[i]: x_list[i] for i in range(len(matrix))}
        new_x_list.append(float(exp.subs(res)))
    
    converged = all(abs(new_x_list[i] - x_list[i]) < e for i in range(len(x_list)))
    errors.append([abs(new_x_list[i] - x_list[i]) for i in range(len(x_list))])
    result.append(x_list)
    x_list = new_x_list
    c+=1

# Start for plotting
transposed_result = list(zip(*result))  
err_result = list(zip(*errors))
iterations = [i for i in range(c)]

for i, values in enumerate(transposed_result):
    plt.plot(iterations, values, marker="o", label=f"x{i+1}")  

plt.title("Jacobi method.")
plt.grid()
plt.xlabel("Iterations")
plt.ylabel("X's Roots")
plt.legend()
plt.show()

for i, values in enumerate(err_result):
    plt.plot(iterations, values, marker="o", label=f"x{i+1}")  

plt.title("Errors of Jacobi method.")
plt.grid()
plt.xlabel("Iterations")
plt.ylabel("X's Roots")
plt.legend()
plt.show()

