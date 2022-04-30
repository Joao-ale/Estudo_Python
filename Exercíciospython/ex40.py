tipocarn = input('Qual tipo de carne irá pedir (file duplo(FL), alcatra(A), picanha(P)): ').upper()
kgcarn = float(input('Quantos Kilos de carne você deseja? '))

tipopag = input('Qual o tipo de pagamento, Cartão tabajara(CT), Cartão de débito(CD), Cartão de crédito(CC), '
                'Dineiro(D), PIX(P): ').upper()

#calcula quanto pagar para File duplo
if tipocarn == 'FL':
    if kgcarn <= 5:
        prectot = 4.90 * kgcarn
    elif kgcarn > 5:
        prectot = 5.80 * kgcarn
    if tipopag == 'CT':
        disc = (prectot * 5 / 100)
    else:
        disc = 0
    pag = prectot - disc
    print('-' * 50)
    print('tipo de carne: Filé Duplo\n'
          'Kilos: {}Kg\n'
          'preço total: R${:.2f}\n'
          'Tipo de pagamento: {}\n'
          'Valor do desconto: R${:.2f}\n'
          'Valor a pagar: R${:.2f}'.format(kgcarn, prectot, tipopag, disc, pag))
    print('-' * 50)
#calcula o quanto pagar para Alcatra
elif tipocarn == 'A':
    if kgcarn <= 5:
        prectot = 5.90 * kgcarn
    elif kgcarn > 5:
        prectot = 6.80 * kgcarn
    if tipopag == 'CT':
        disc = (prectot * 5 / 100)
    else:
        disc = 0
    pag = prectot - disc
    print('-' * 50)
    print('tipo de carne: Alcatra\n'
          'Kilos: {}Kg\n'
          'preço total: R${:.2f}\n'
          'Tipo de pagamento: {}\n'
          'Valor do desconto: R${:.2f}\n'
          'Valor a pagar: R${:.2f}'.format(kgcarn, prectot, tipopag, disc, pag))
    print('-' * 50)
#calcula quanto pagar para Picanha
elif tipocarn == 'P':
    if kgcarn <= 5:
        prectot = 6.90 * kgcarn
    elif kgcarn > 5:
        prectot = 7.80 * kgcarn
    if tipopag == 'CT':
        disc = (prectot * 5 / 100)
    else:
        disc = 0
    pag = prectot - disc
    print('-' * 50)
    print('tipo de carne: Picanha\n'
          'Kilos: {}Kg\n'
          'preço total: R${:.2f}\n'
          'Tipo de pagamento: {}\n'
          'Valor do desconto: R${:.2f}\n'
          'Valor a pagar: R${:.2f}'.format(kgcarn, prectot, tipopag, disc, pag))
    print('-' * 50)
