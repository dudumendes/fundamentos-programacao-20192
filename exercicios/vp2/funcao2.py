def g(x, y):
    if (x < 0):
        x = 1
        
    return 20 * x + y ** 3

x = (int) (input("x = "))
y = (int) (input("y = "))

resultado = g(x, y)
print(resultado)