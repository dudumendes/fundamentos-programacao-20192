def reajustar(preco, percentual):
    preco = preco + preco * percentual / 100
    return preco
    
preco = (float) (input("Digite o preco: "))
percentual = (float) (input("Digite o percentual: "))

precoReajustado = reajustar(preco, percentual)

print("O valor reajustado eh ", precoReajustado)