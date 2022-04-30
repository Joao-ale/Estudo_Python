print('-=-'*20)
print('LOJAS C&A')
print('-=-'*20)
preço = float(input('Qual o preço das compras:R$'))
print('''Formas de pagamento:
[ 1 ] Á vista/cheque
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é sua opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total=preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc=int(input('Quantas parcelas serão? '))
    parcela=total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc,parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

