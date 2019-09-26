# Potencia ou raiz

base = (int) (input("Digite o valor da base: "))
potencia_raiz = (int) (input("Digite o valor da potencia/raiz: "))
opcao = input("Para potencia digite 'p', para raiz digite 'r': ")

if opcao == 'p':
    print(base ** potencia_raiz)
else:
    print(base ** (1 / potencia_raiz))