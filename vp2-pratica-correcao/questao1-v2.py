opcao = input("Você quer números pares ou ímpares: ")

if (opcao == "pares") :
    # corpo do
    i = 0
    while (i < 200):
        if (i % 2 == 0):
            print(i)
        i = i + 1
    
elif (opcao == "impares"):
    #c orpo do elif
    i = 0
    while (i < 200):
        if (i % 2 != 0):
            print(i)
        i = i + 1
    
else:
    # corpo do else
    print("Opcao invalida")