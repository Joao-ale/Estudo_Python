n = int(input('Entre com um número para saber seu fatorial: '))
fat = n
c = n

if 16 > n > 0:
    while c != 1:
        fat *= (c - 1)
        c -= 1
    print('{}! = {}'.format(n, fat))
else:
    print('O número tem que ser menor que 16 e maior que 0')

d = input('Deseja calcular novamente? [S/N] ').upper()
print('-' * 50)
while d == 'S':
    n = int(input('Entre com um número para saber seu fatorial: '))
    fat = n
    c = n

    if 16 > n > 0:
        while c != 1:
            fat *= (c - 1)
            c -= 1
        print('{}! = {}'.format(n, fat))
    else:
        print('O número tem que ser menor que 16 e maior que 0')
    d = input('Deseja calcular novamente? [S/N] ').upper()
    print('-' * 50)