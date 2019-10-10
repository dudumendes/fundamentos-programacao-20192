# utilizando o laço for calcule e imprima
# a soma do números ímpares contidos entre 1 e 100

soma = 0
total = 0
for i in range(100):
    if (i % 2 != 0):
        total = total + 1
        soma = soma + i

print(soma)
print(total)