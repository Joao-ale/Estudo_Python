kilo_pesc = float(input('Quantos kilos você pescou? '))
excesso = kilo_pesc - 50

if excesso > 0:
    multa = excesso * 4
    print('Você pescou {:.2f}Kg acima do limite de 50Kg e pagará R${:.2f} mais atenção da próxima!'.format(excesso, multa))
else:
    print("Você teve uma pesca de {:.2f}Kg e não pagará multa.".format(kilo_pesc))