from math import sqrt
a = int(input('Entre com o valor de A: '))
b = int(input('Entre com o valor de B: '))
c = int(input('Entre com o valor de C: '))

if a == 0:
    print('Não é uma equação de segundo grau! Fim programa!')
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print('O valor de delta é negativo e por isso não possui raizes reais!')
    elif delta == 0:
        print('O valor de delta é igual a zero e por isso possui apenas uma raiz real!')
        bask = (- b - sqrt(delta)) / 2 * a
        print('O delta = {:.2f}'.format(delta))
        print('x = {:.2f}'.format(bask))
    else:
        print('O valor de delta é positivo e por isso possui duas raizes reais!')
        bask1 = (- b - sqrt(delta)) / 2 * a
        bask2 = (- b + sqrt(delta)) / 2 * a
        print('O delta = {:.2f}'.format(delta))
        print('x1 = {:.2f}'.format(bask1))
        print('x2 = {:.2f}'.format(bask2))