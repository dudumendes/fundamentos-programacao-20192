# Faça um programa que lê uma palavra e uma letra. 
# Escreva também uma função que receba a palavra (lista de caracteres) 
# e letra lidas e que retorne o total de ocorrências 
# dessa letra na palavra fornecida. 
# Execute essa função em seu programa.

def ocorrenciasDaLetra(palavra, letra) :
    total = 0
    for l in palavra:
        if l == letra:
            total = total + 1
    return total

palavra = input("Digite uma palavra: ")
letra = input("Agora, digite uma letra: ")

ocorrencias = ocorrenciasDaLetra(palavra, letra)

print("A letra", letra, "possui", ocorrencias, "ocorrencias na palavra", palavra)
