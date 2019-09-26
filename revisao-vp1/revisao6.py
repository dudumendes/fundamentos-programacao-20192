x = (int) (input("Digite o primeiro valor: "))
y = (int) (input("Digite o segundo valor: "))
z = (int) (input("Digite o terceiro valor: "))

if (x < y):
    if (y < z):
        print(x, y, z)
    else:
        if (x < z):
            print(x, z, y)
        else:
            print(z, x, y)
else:
    if (y < z):
        if (x < z):
            print(y, x, z)
        else:
            print(y, z, x)
    else:
        print(z, y, x)