## informa se o triângulo é retângulo ou não

angulo1 = (float) (input("Digite o valor do primeiro angulo: "))
angulo2 = (float) (input("Digite o valor do segundo angulo: "))
angulo3 = (float) (input("Digite o valor do terceiro angulo: "))

if (angulo1 + angulo2 + angulo3 ) == 180.0:
    if (angulo1 == 90 or angulo2 == 90 or angulo3 == 90):
        print("O triangulo eh retangulo")
else: 
    print("Os valores não representam um triangulo")