sal_h = float(input('Quanto você ganha por hora trabalhada? R$'))
hora_trab = int(input('Quantas horas voccê traalha no mês? '))

sal_mes = sal_h * hora_trab
ir = (sal_mes * 11 / 100)
inss = (sal_mes * 8 / 100)
sindi = (sal_mes * 5 / 100)
sal_liq = sal_mes - ir - inss - sindi

print('Seu salário bruto é de R${:.2f}\n'
      'Você paga R${:.2f} de INSS\n'
      'Você paga R${:.2f} de sindicato\n'
      'Você paga R${:.2f} de imposto de renda'
      '\nO seu salário líquido é de {:.2f}'.format(sal_mes, inss, sindi, ir, sal_liq))
