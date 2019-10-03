def soma(x , y) :
    print(x + y)

def subtracao(x, y) :
    print(x - y)

def multiplicacao(x, y):
    print(x * y)

def divisao(x, y):
    if (y == 0):
        print("Nao eh possivel realizar divisao por Zero")
    else:
        print(x / y)

def calcular(op, x, y):
    if (op == "+"):
        soma(x, y)
    elif (op == "-"):
        subtracao(x, y)
    elif (op == "*"):
        multiplicacao(x, y)
    elif (op == "/"):
        divisao(x, y)
    else:
        print("Operacao invalida")

print("==== Calculadora ====")
operando1 = (float) (input("Digite o primeiro operando: "))
operando2 = (float) (input("Digite o segundo operando: "))
operador = input("Digite qual operacao quer realizar: ")

calcular(operador, operando1, operando2)

