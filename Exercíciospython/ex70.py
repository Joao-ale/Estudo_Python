print('PANIFICADORA PÃO DE ONTEM - TABELA DE PREÇO')
prec = float(input('Preço do pão: R$'))
for x in range(1, 51):
    print('-' * 25)
    print('Quant.{} - R${:.2f}'.format(x, prec * x))