sal=float(input('Digite o salário do funcionátrio: R$'))
nsal=sal+(sal*15/100)
print('O funcionário que ganhava R${:.2f}, com o aumento de 15% irá ganhar R${:.2f}'.format(sal,nsal))
