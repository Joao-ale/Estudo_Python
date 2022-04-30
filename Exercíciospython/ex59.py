#CORRIGIR O CÓDIGO

n = int(input('Entre com um número: '))
if 0 > n > 1000:
    print('Só é válido valores entre 0 e 1000')
    n = int(input('Entre com um número: '))

conjn = [n]
des = input('Deseja adicionar mais um número? [S/N] ').upper()
while des == 'S':
    #PROBLEMA DE LEITURA DOS NÚMEROS INVÁLIDOS
    n = int(input('Entre com um número: '))
    if n < 0 and n > 100:
        print('Só é válido valores entre 0 e 1000')
        n = int(input('Entre com um número: '))
    conjn.append(n)
    des = input('Deseja adicionar mais um número? [S/N] ').upper()
print('-' * 25)
print('Conjunto: {}\n'
      'Soma do conjunto: {}\n'
      'Menor número: {}\n'
      'Maior número: {}'.format(conjn, sum(conjn), min(conjn), max(conjn)))