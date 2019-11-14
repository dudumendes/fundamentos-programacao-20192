def contarConsoantes(texto):
    totalDeConsoantes = 0

    for letra in texto:
        if (letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u"):
            totalDeConsoantes = totalDeConsoantes + 1
    
    print(totalDeConsoantes)

def contarConsoantes2(texto):
    totalDeConsoantes = 0

    for letra in texto:
        if letra not in "aeiou":
            totalDeConsoantes = totalDeConsoantes + 1
    
    print(totalDeConsoantes)

palavra = input("Digite uma palavra: ")
contarConsoantes2(palavra)