h_ou_m = input('Você é homem ou mulher? [H/M] ').upper()

#Força a aceitar apenas H ou M
while True:
    if h_ou_m =='H' or h_ou_m == 'M':
        break
    h_ou_m = input('Digite apenas H ou M. Você é homen ou mulher? [H/M]').upper()
    

altura = float(input('Qual sua altura em m: '))
imc = 0

#Calcula o IMC para homens
if h_ou_m == 'H':
    imc = (72.7 * altura) - 58
    print('Para um Homem de {:.2f}m de altura seu peso ideal é de {:.2f}Kg'.format(altura, imc))
#Calcula o IMC para mulheres
else:
    imc = (62.1 * altura) - 44.7
    print('Para um mulher de {:.2f}m de altura seu peso ideal é de {:.2f}Kg'.format(altura, imc))