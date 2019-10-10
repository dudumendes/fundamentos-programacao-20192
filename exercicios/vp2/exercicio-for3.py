# crie uma lista com 3 tipos de vinhos: tinto, rose e branco
# apresente os valores da lista
# e peça 10x para o usuario selecionar 1 das opcoes
# ao final apresente as quantidades
# para tinto, rose e branco
tinto = 0
branco = 0
rose = 0

vinhos = ["Tinto", "Branco", "Rose"]

for i in range(10):
    print("Selecione 1 dos tipos abaixo, digitando a primeira letra")

    for tipo in vinhos:
        print(tipo)
    
    escolha = input()

    if(escolha == "T"):
        tinto += 1 
    elif(escolha == "B"):
        branco += 1
    elif(escolha == "R"):
        rose += 1
    else:
        print("Opcao invalida")


print("Tinto: ", tinto)
print("Branco: ", branco)
print("Rose: ", rose)