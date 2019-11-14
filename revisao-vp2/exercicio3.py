def mediaDaLista(lista) :
    total = 0
    for i in lista: 
        total = total + i

    total = total // 20
    
    return total

numeros = []

for i in range(0, 20) :
    numero = (int)(input("Digite um numero: "))
    numeros.append(numero)

print("A media dos valores eh", mediaDaLista(numeros))