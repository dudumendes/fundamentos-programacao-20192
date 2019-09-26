print("==== Calculadora ====")

operando1 = (float) (input("Digite o primeiro operando: "))
operando2 = (float) (input("Digite o segundo operando: "))
operador = input("Digite qual operacao quer realizar: ")

if (operador == "+"):
    print(operando1 + operando2)
elif (operador == "-"):
    print(operando1 - operando2)
elif (operador == "*"):
    print(operando1 * operando2)
elif (operador == "/"):
    if (operando2 == 0):
        print("Nao eh possivel realizar divisao por Zero")
    else:
        print(operando1 / operando2)
else:
    print("Operacao invalida")