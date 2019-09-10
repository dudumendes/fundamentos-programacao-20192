print("Esse programa calcula os valores possiveis de x, baseados na fórmula de Bhaskara")
a = (float)(input("Digite o valor de a: "))
b = (float)(input("Digite o valor de b: "))
c = (float)(input("Digite o valor de c: "))

# calcula o valor do delta
delta = b ** 2 - 4 * a * c

# calcula o valor de x com delta positivo
x1 = (-b + (delta ** (1/2)) ) / 2 * a

# calcula o valor de x com delta negativo
x2 = (-b - (delta ** (1/2)) ) / 2 * a

print("Os valores possiveis de x sao ", x1, "e", x2)

