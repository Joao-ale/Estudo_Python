mor = float(input('Quantos kg de morango irá levar? '))
mac = float(input('Quantos kg de maçã irá levar? '))
totkg = mor + mac

#desconto morango
if mor <= 5:
    premor = mor * 2.50
elif mor > 5:
    premor = mor * 2.20
#desconto maçã
if mac <=5:
    premac = mac * 1.80
elif mac > 5:
    premac = mac * 1.50

pag = premac + premor
#desconto pelo preço
if pag > 25:
    pag -= pag * 10 / 100
else:
    #desconto pelo kilo
    if totkg > 8:
        pag -= pag * 10 / 100
print('Você comprou {}Kg de morango e {}Kg de maçã irá pagar um total de R${:.2f}'.format(mor, mac, pag))