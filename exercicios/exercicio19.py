print("Calculo o conceito americano baseado na sua nota brasileira")

nota = (float) (input("Digite sua nota"))

if nota < 5.0:
    print("Seu conceito eh D")
elif nota < 7.0:
    print("Seu conceito eh C")
elif nota < 9.0:
    print("Seu conceito eh B")
else:
    print("Parabens, conceito A")