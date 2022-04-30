sal = float(input('Entre com o valor do seu salário: R$'))
nsal = 0
if sal <= 280:
    nsal = (sal * 20 / 100) + sal
    peraum = 20
elif 280 < sal <= 700:
    nsal = (sal * 15 / 100) + sal
    peraum = 15
elif 700 < sal <= 1500:
    nsal = (sal * 10 /100) + sal
    peraum = 10
elif 1500 < sal:
    nsal = (sal * 5 / 100) + sal
    peraum = 5

aum = nsal - sal

print('Seu salário era de R${:.2f}\n'
      'Você teve um percentual de {}%\n'
      'Seu salário teve um aumento de R${:.2f}\n'
      'Seu novo salário é de R${:.2f}'.format(sal, peraum, aum, nsal))