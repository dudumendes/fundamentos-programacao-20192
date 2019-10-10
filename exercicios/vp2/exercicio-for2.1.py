# Faça um programa que leia um conjunto de 10 números inteiros
# e ao final mostre qual foi o maior e o menor número lido.
import math

menor = math.inf
maior = - math.inf

for i in range(10):
    
    numero = (int) (input("Digite um numero, por favor: "))
    maior = numero if numero > maior else maior
    menor = numero if numero < menor else menor

print("O maior valor eh ", maior)
print("O menor valor eh ", menor)
    