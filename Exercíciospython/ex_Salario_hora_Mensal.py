salarioPorHora = float(input("Quanto você recebe por hora trabalhada: R$ "))
horaTrabalhada = int(input("Quantas horas você trabalha por mês: "))
salarioMesal = salarioPorHora * horaTrabalhada

print('Você recebe no final do mês um total de R${:.2f}'.format(salarioMesal))