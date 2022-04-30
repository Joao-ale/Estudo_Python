altura = float(input('Qual sua altura em m: '))
imc = (72.7 * altura) - 58

print('Seu peso ideal para uma pessoa de {}cm de altura é de {:.2f}Kg'.format(altura, imc))