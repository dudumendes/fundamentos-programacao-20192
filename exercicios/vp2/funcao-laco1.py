def imprimeImparesAte(limite):
    if (limite % 2 == 0) :
        limite = limite - 1

    while (limite > 0) :
        print(limite)
        limite = limite - 2

limite = (int) (input("Digite o maior numero impar e te darei todos eles até 0: "))

imprimeImparesAte(limite)