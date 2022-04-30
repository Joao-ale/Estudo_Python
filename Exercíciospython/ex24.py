sal_h = float(input('Qual o valor do seu salário por hora trabalhada: R$'))
h_trab = int(input('Quantas horas você trabalha no mês: '))
sal = sal_h * h_trab
inss = sal * 10 / 100
fgts = sal * 11 / 100
if sal <= 900:
    ir = 0
elif sal <= 1500:
    ir = sal * 5 / 100
elif sal <= 2500:
    ir = sal * 10 / 100
elif sal > 2500:
    ir = sal * 20 / 100
totaldisc = ir + inss
sal_liq = sal - totaldisc
print('Salário Bruto: R${}\n'
      'Imposto de Renda {}\n'
      'INSS: R${}\n'
      'FGTS: R${}\n'
      'Total de descontos: R${}\n'
      'Salário Liquido: R${}'.format(sal, ir, inss, fgts, totaldisc, sal_liq))