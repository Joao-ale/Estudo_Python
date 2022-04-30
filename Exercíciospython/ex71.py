print('LOJA TABAJARA')
prec = float(input('Produto 1: R$'))
c = 1
s = prec
while prec != 0:
    c += 1
    prec = float(input('Produto {}: R$'.format(c)))
    s += prec
print('-' * 15)
print('Total: R${:.2f}'.format(s))
din = float(input('Dinheiro: R$'))
print('-' * 15)
print('Troco: R${:.2f}'.format(din - s))