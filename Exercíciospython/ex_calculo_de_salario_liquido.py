salarioPorHora = float(input('Quanto você ganha por hora trabalhada? R$'))
horaTrabalhada = int(input('Quantas horas voccê traalha no mês? '))

salarioMesal = salarioPorHora * horaTrabalhada
# Calcula os descontos do salario, Imposto de renda 11%, INSS 9%, Sindicato 5%
ir = (salarioMesal * 11 / 100)
inss = (salarioMesal * 8 / 100)
sindicato = (salarioMesal * 5 / 100)
salarioLiquido = salarioMesal - ir - inss - sindicato

print('Seu salário bruto é de R${:.2f}\n'
      'Você paga R${:.2f} de INSS\n'
      'Você paga R${:.2f} de sindicato\n'
      'Você paga R${:.2f} de imposto de renda'
      '\nO seu salário líquido é de {:.2f}'.format(salarioMesal, inss, sindicato, ir, salarioLiquido))
