controle = ""
estado = ""

while (controle != "X"):
    print("===========================")
    print("Houve evolucao no processo?")
    controle = input("Digite [S] para sim, [N] para não e [X] para sair: ")

    if (controle == "S") : 
        estado = input("Qual o novo estado? ")
        print("O estado atual do processo eh: ", estado)
    elif (controle == "N"):
        print(":( Ok")
    print("")

print("Estado final do processo: ", estado)
print("Ate a proxima")