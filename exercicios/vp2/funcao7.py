def celsiusToFar(temperatura):
    return temperatura * 1.8 + 32

def farToCelsius(temperatura):
    return (temperatura - 32) / 1.8

print("==== Conversor de temperaturas ====")

temperatura = (float) (input("Digite um valor para temperatura: "))
tipo = input("Digite C para Celsius e F para Farenheit: ")

resultado = 0.0

if tipo == "C" or tipo == "c":
    resultado = celsiusToFar(temperatura)
    print(temperatura, "ºC em Farenheit eh", resultado, "ºF")
elif tipo == "F" or tipo == "f":
    resultado = farToCelsius(temperatura)
    print(temperatura, "ºF em Celsius eh", resultado, "ºC")
else:
    print("Voce digitou uma opcao invalida")
