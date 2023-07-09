def euler_method(f, a, b, y0, m):
    # Define o tamanho do passo h com base no intervalo [a,b] e no número de subintervalos m
    h = (b - a) / m
    # Inicializa as listas x e y com os valores iniciais a e y0
    x = [a]
    y = [y0]

    # Loop para calcular a solução aproximada em cada subintervalo
    for i in range(m):
        # Obtém os valores de x e y no passo atual
        xi = x[i]
        yi = y[i]
        # Calcula o valor da função f(x,y) no passo atual
        fi = f(xi, yi)

        # Adiciona o próximo valor de x e y às listas
        x.append(xi + h)
        y.append(yi + h * fi)

    # Retorna as listas x e y contendo a solução aproximada
    return x, y


# Função que define a equação diferencial: y' = x - 2y + 1
def f(x, y):
    return x - 2 * y + 1


# Valores iniciais
a = 0
b = 1
y0 = 1
m = 20  # Número de subintervalos

# Resolvendo o PVI usando o método de Euler
x, y = euler_method(f, a, b, y0, m)

# Imprimindo a solução aproximada com 4 casas decimais
print("i\t x\t\t\t y\t\t\t f(x,y)")
print("--------------------------------------")
for i in range(len(x)):
    print("{}\t {:.1f}\t {:.5f}\t {:.5f}".format(i, x[i], y[i], f(x[i], y[i])))
