def ehPositivoOuNegativo(valor):
    if (valor > 0) :
        print(valor, "eh positivo")
    elif (valor < 0):
        print(valor, "eh negativo")
    else:
        print("Nem chove nem molha")

ehPositivoOuNegativo(10)
ehPositivoOuNegativo(-20)
ehPositivoOuNegativo(123123)
ehPositivoOuNegativo(-23123)
ehPositivoOuNegativo(0)

respostaDoUsuario = (int) (input("Digite um valor e te direi seu sinal"))
ehPositivoOuNegativo(respostaDoUsuario)
