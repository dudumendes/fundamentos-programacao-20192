# Este programa le 5 valores inteiros
# e calcula a soma somente dos ímpares
v1 = (int) (input("Digite 1 valor: "))
v2 = (int) (input("Digite 1 valor: "))
v3 = (int) (input("Digite 1 valor: "))
v4 = (int) (input("Digite 1 valor: "))
v5 = (int) (input("Digite 1 valor: "))

soma = 0

if (v1 % 2 != 0):
    soma = soma + v1
if (v2 % 2 != 0):
    soma = soma + v2
if (v3 % 2 != 0):
    soma = soma + v3
if (v4 % 2 != 0):
    soma = soma + v4
if (v5 % 2 != 0):
    soma = soma + v5

print(soma)
