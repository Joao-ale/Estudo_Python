qcd = int(input('Quantos CDs você comprou: '))
s = 0

for x in range(1, qcd + 1):
    preccd = float(input('Qual foi o preço do {}º CD: R$'.format(x)))
    s += preccd
med = s / qcd
print('Você gastou um total de R${:.2f} e com a média de R${:.2f} por CD'.format(s, med))