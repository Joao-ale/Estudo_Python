sal=float(input('Digite o salário: R$'))
if sal <=1250:
    aument=sal+(sal*15/100)
    print('Com o aumento de 15% seu salário que era de R${:.2f} passou a ser de R${:.2f}'.format(sal,aument))
else:
    aument=sal+(sal*10/100)
    print('Com o aumento de 10% seu salário qu era de R${:.2f} passou a ser de R${:.2f}'.format(sal,aument))