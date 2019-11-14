texto = input("Informe uma palavra: ")
def contadorDeConsoantes(palavra):
    vogais = 0
    consoantes = 0
    for letra in texto:
        if letra in 'aeiou':
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1
    print ("Consoantes: " , consoantes)
print (contadorDeConsoantes(texto))