print("Troca de valores de variáveis")

a = input("Digite o valor de a: ")
b = input("Digite o valor b: ")
print("ANTES: O valor de a eh", a, "e o valor de b eh", b)

a,b = b,a

print("DEPOIS: O valor de a eh", a, "e o valor de b eh", b)