"""
import numpy as np

def f(x, y):
    return -2 * x * y**2

def exact(x):
    return 1 / (x**2 + 2)

def euler(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        y += h * f(x, y)
        x += h
    return y

def modified_euler(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        y += h * k2
        x += h
    return y
"""
"""
def improved_euler(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y += h * (k1 + k2) / 2
        x += h
    return y

x0 = 0
y0 = 0.5
b = 1
m = 10
h = (b - x0) / m

x_values = np.linspace(x0, b, m+1)
y_exact_values = exact(x_values)

y_euler_values = [y0]
y_modified_euler_values = [y0]
y_improved_euler_values = [y0]

for i in range(m):
    y_euler_values.append(euler(f, x_values[i], y_euler_values[-1], h, 1))
    y_modified_euler_values.append(modified_euler(f, x_values[i], y_modified_euler_values[-1], h, 1))
    y_improved_euler_values.append(improved_euler(f, x_values[i], y_improved_euler_values[-1], h, 1))

print("| i | xi | yEi - y(xi)| yEmodi - y(xi)| yEmeli - y(xi)|")
print("|---|---|---|---|---|")
"""
#for i in range(m+1):
#    print("| {} | {:.1f} | {:.2e} | {:.2e} | {:.2e} |".format(i, x_values[i], abs(y_exact_values[i] - y_euler_values[i]), abs(y_exact_values[i] - y_modified_euler_values[i]), abs(y_exact_values[i] - y_improved_euler_values[i])))

import numpy as np

def f(x, y):
    return -2 * x * y**2

def exata(x):
    return 1 / (x**2 + 2)

def euler(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        y += h * f(x, y)
        x += h
    return y

def euler_modificado(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        y += h * k2
        x += h
    return y

def euler_aprimorado(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y += h * (k1 + k2) / 2
        x += h
    return y

x0 = 0
y0 = 0.5
b = 1
m = 10
h = (b - x0) / m

x_valores = np.linspace(x0, b, m+1)
y_valores_exatos = exata(x_valores)

y_valores_euler = [y0]
y_valores_euler_modificado = [y0]
y_valores_euler_aprimorado = [y0]

for i in range(m):
    y_valores_euler.append(euler(f, x_valores[i], y_valores_euler[-1], h, 1))
    y_valores_euler_modificado.append(euler_modificado(f, x_valores[i], y_valores_euler_modificado[-1], h, 1))
    y_valores_euler_aprimorado.append(euler_aprimorado(f, x_valores[i], y_valores_euler_aprimorado[-1], h, 1))

print("| i | xi | yEi - y(xi)| yEmodi - y(xi)| yEmeli - y(xi)|")
print("|---|---|---|---|---|")
for i in range(m+1):
    print("| {} | {:.1f} | {:.2e} | {:.2e} | {:.2e} |".format(i, x_valores[i], abs(y_valores_exatos[i] - y_valores_euler[i]), abs(y_valores_exatos[i] - y_valores_euler_modificado[i]), abs(y_valores_exatos[i] - y_valores_euler_aprimorado[i])))
