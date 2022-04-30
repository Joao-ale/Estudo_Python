s = c1000 = menor = cont = 0
barato = ' '
print('-' * 30)
print('LOJÃO DO JOÃO')
print('-' * 30)
while True:
    produt = input('Nome do produto: ').strip()
    preço = int(input('Preço: R$'))
    cont += 1
    if preço >= 1000:
        c1000 += 1
    s += preço
    if cont == 1 or preço < menor:
        menor = preço
        barato = produt
    proseguir = ' '
    while proseguir not in 'SN':
        proseguir = input('Quer continuar? [S/N] ').upper().strip()[0]
    if proseguir == 'N':
        break
print('-' * 40)
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'A soma dos produtos é R${s:.2f}.')
print(f'Na sua compra tem {c1000} produtos acima de R$1000.00')
print(f'O produto mais barato é {barato} que custa R${menor:.2f}')