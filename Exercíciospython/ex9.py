h_ou_m = input('Você é homem ou mulher? [H/M] ').upper()
while True:
    h_ou_m = input('Digite apenas H ou M. Você é homen ou mulher? [H/M]').upper()
    if h_ou_m =='H' or h_ou_m == 'M':
        break
altura = float(input('Qual sua altura em m: '))
imc = 0

if h_ou_m == 'H':
    imc = (72.7 * altura) - 58
    print('Para um Homem de {:.2f}m de altura seu peso ideal é de {:.2f}Kg'.format(altura, imc))
else:
    imc = (62.1 * altura) - 44.7
    print('Para um mulher de {:.2f}m de altura seu peso ideal é de {:.2f}Kg'.format(altura, imc))