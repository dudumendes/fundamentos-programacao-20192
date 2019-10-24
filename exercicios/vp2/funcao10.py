def saudar(nome) :
    print("Ola, " + nome)

def crazyFunction(x , y) :
    x = 2 * y + 3 * x ** (1/2)
    y = x * y + 10

    return [x , y]

resultado = crazyFunction(144, 20)
print("x = ", resultado[0])
print("y = ", resultado[1])

saudar("Adamor")