saldo = 100.0
saque = float(input("Digite o valor a ser sacado: "))

if (saque <= saldo) :
    saldo = saldo - saque
    print("Aguarde o seu dinheiro ser entregue: R$", saque )
else:
    print("Saldo insuficiente")

print("Saldo atual: R$", saldo)