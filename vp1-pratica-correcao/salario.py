# Faixa salarial
salario = (float) (input("Digite seu salario: "))
faixa = ""
juros = ""

if salario < 1800.0 :
    faixa = "1"
    juros = "0"
elif salario < 2600.0 :
    faixa = "1,5"
    juros = "5"
elif salario < 3000.0 :
    faixa = "2"
    juros = "6"
elif salario < 4000.0 :
    faixa = "2"
    juros = "7"
elif salario < 7000.0 :
    faixa = "3"
    juros = "8,16"
elif salario < 9000.0 :
    faixa = "3"
    juros = "9,16"

print("Sua faixa salarial:", faixa, "Taxa de juros relativa:", juros)