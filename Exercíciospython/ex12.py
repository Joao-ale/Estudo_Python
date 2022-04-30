area = float(input('Qual a área a ser pintada em m²: '))
tinta_pintar = area / 3
lata_comprar = tinta_pintar / 18
if lata_comprar is not int:
    lata_comprar = lata_comprar * 2
tot_pagar = lata_comprar * 80
print('Você comprará {} latas e pagará R${:.2f}'.format(lata_comprar,tot_pagar))