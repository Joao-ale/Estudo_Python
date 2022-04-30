n =  int(input('Entre com um número: '))
conjn = [n]
des = input('Deseja adicionar mais um número? [S/N] ').upper()
while des == 'S':
    n = int(input('Entre com um número: '))
    conjn.append(n)
    des = input('Deseja adicionar mais um número? [S/N] ').upper()
print('-' * 25)
print('Conjunto: {}\n'
      'Soma do conjunto: {}\n'
      'Menor número: {}\n'
      'Maior número: {}'.format(conjn, sum(conjn), min(conjn), max(conjn)))