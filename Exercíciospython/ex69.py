print(' LOJAS QUASE DOIS - TABELA DE PREÇOS')

for x in range(1,51):
    print('-' * 25)
    print('Quantidade {} - R${:.2f}'.format(x, 1.99 * x))