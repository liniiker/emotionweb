def f(x, y):
    return x - 2 * y + 1


def runge_kutta_order_4(x0, y0, h, num_intervals):
    x = [x0]
    y = [y0]

    for i in range(num_intervals):
        xi = x[i]
        yi = y[i]

        k1 = h * f(xi, yi)
        k2 = h * f(xi + h / 2, yi + k1 / 2)
        k3 = h * f(xi + h / 2, yi + k2 / 2)
        k4 = h * f(xi + h, yi + k3)

        x.append(xi + h)
        y.append(yi + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    return x, y


# Valores iniciais
x0 = 0
y0 = 1
h = 0.1
num_intervals = 10

# Resolvendo o PVI usando o método de Runge-Kutta de ordem 4
x_rk4, y_rk4 = runge_kutta_order_4(x0, y0, h, num_intervals)

# Imprimindo a solução
print("i\t xi\t\t yi")
print("-----------------")
for i in range(len(x_rk4)):
    print(f"{i}\t {x_rk4[i]:.1f}\t {y_rk4[i]:.5f}")
