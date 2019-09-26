print("==== Avalia se a area do triangulo eh menor do que 50 ====" )
base = (int)(input("Digite um valor para a base: "))
altura = (int)(input("Digite um valor para a altura: "))
area = (base * altura) / 2

if area < 50 :
    print("A area eh menor que 50")
else:
    print("A area não eh menor do que 50")