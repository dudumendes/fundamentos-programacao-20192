# faça um programa utilizando o for
# que apresente a tabuada de um inteiro informado
# pelo o usuário
def multiplicao(n):
    for i in range(11):
        print(n, "x", i, "=", (n*i))

def divisao(n):
    for i in range(10):
        print(n * (i + 1), "/", n, "=", i+1)

def soma(n):
    for i in range(11):
        print(n, "+", i, "=", (n+i))

def subtracao(n):
    for i in range(11):
        print(i + n, "-", n, "=", i )

def tabuada(n):
    print("Tabuada do ", n)
    print("---------------")
    soma(n)
    print("---------------")
    subtracao(n)
    print("---------------")
    multiplicao(n)
    print("---------------")
    divisao(n)

valor = (int)(input("Digite um valor para tabuada: "))
tabuada(valor)