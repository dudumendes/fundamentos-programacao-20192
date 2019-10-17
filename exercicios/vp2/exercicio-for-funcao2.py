# Escreva uma função que recebe uma lista com o
# preço de 10 produtos e que exibe os preços dos
# produtos reajustados em 15%
# Teste o funcionamento da funcao no final do codigo
def reajustar(lista) :
    for item in lista :
        reajuste = item + item * 0.15
        print(reajuste)


produtos = [100.0, 51.99, 45.90, 34.45, 4055.50, 230.0, 230.3, 232.0, 2324.33, 231.33]

reajustar(produtos)