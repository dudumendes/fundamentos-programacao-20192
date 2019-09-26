x = (int) (input("Digite o primeiro valor: "))
y = (int) (input("Digite o segundo valor: "))
z = (int) (input("Digite o terceiro valor: "))

if (x < y < z):
    print(x, y, z)
elif(x < z < y):
    print(x, z, y)
elif(y < x < z):
    print(y, x, z)
elif(y < z < x):
    print(y, z, x)
elif(z < x < y):
    print(z, x, y)
else:
    print(z, y, x)
