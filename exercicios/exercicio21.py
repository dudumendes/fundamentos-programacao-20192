print("==== Conversor de temperaturas ====")

temperatura = (float) (input("Digite um valor para temperatura: "))
tipo = input("Digite C para Celsius e F para Farenheit: ")

resultado = 0.0

if tipo == "C" or "c":
    resultado = temperatura * 1.8 + 32
    print(temperatura, "ºC em Farenheit eh", resultado, "ºF")
elif tipo == "F" or "f":
    resultado = (temperatura - 32) / 1.8
    print(temperatura, "ºF em Celsius eh", resultado, "ºC")
else:
    print("Voce digitou uma opcao invalida")
