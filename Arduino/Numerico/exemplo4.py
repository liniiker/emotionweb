import numpy as np
from scipy.integrate import solve_ivp

def f(x, y):
    return x - 2*y + 1

def solucao_exata(x):
    return (x**2 + 2*x - 1) / 4

a = 0
b = 1
m = 10
y0 = 1

x_valores = np.linspace(a, b, m+1)

sol = solve_ivp(f, (a, b), [y0], method='RK45', t_eval=x_valores)

print("Método Dormand-Prince")
print("i  x        y        Erro")
for i, (x, y) in enumerate(zip(sol.t, sol.y[0])):
    erro = np.abs(y - solucao_exata(x))
    print(f"{i}  {x:.5f}  {y:.5f}  {erro:.3e}")
