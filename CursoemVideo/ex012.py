preço=float(input('Preço do produto: R$'))
npreço=preço-(preço*5/100)
print('O produto que custava R${:.2f}, com a promoção de 5% irá custar R${:.2f}'.format(preço,npreço))
