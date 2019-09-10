print("Calculo do valor liquido do salario")

horas_trabalhadas = (float) (input("Informe o numero de horas trabalhadas: "))
valor_da_hora = (float) (input("Informe o valor da sua hora de trabalho: "))
desconto = (float) (input("Informe o valor do desconto do IR: "))

salario_bruto = horas_trabalhadas * valor_da_hora

salario_liquido = salario_bruto - (salario_bruto * (desconto / 100))

print("O seu salario liquido eh", salario_liquido)