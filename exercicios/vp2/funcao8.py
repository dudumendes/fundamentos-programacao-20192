print("Calculo o conceito estadunidense baseado na sua nota brasileira")

def notaBrasileiraParaEstadunidense(notaBrasileira):
    if notaBrasileira < 5.0:
        return "D"
    elif notaBrasileira < 7.0:
        return "C"
    elif notaBrasileira < 9.0:
        return "B"
    else:
        return "A"

nota = (float) (input("Digite sua nota: "))

conceitoEstadunidense = notaBrasileiraParaEstadunidense(nota)

print("Seu conceito eh", conceitoEstadunidense)