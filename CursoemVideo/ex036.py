casa=float(input('Digite o valor da casa:R$'))
sal=float(input('Digite seu salário:R$'))
ano=int(input('Digte em quantos anos deseja pagar: '))
prest=casa / (ano * 12)
minimo=sal*30/100
print('Para pagar uma casa de R${:.2f} em {} anos terá  uma prestação de R${:.2f} por mês'.format(casa,ano,prest))
if prest<=minimo:
    print('O empréstimo APROVADO!!')
else:
    print('O epréstimo NEGADO!!')
