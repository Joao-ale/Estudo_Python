sal = int(input('Qual seu salário? R$'))
aum = 1.5 / 100
anoatu = int(input('Em que ano estamos? '))
ano = anoatu - 1996
for x in range(1, ano + 1):
    sal += sal * aum
    aum *= 2
print('O salário atual é de {:.2f}'.format(sal))
