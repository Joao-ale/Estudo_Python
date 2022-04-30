sal_p_h = float(input("Quanto você recebe por hora trabalhada: R$ "))
hora_trab = int(input("Quantas horas você trabalha por mês: "))
sal_mes = sal_p_h * hora_trab

print('Você recebe no final do mês um total de R${:.2f}'.format(sal_mes))