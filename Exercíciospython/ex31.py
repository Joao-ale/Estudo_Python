num = int(input('Entre com um valor inteiro menor que 1000: '))

cent = int(num / 100)
resto = num % 100
dec = int(resto / 10)
resto = resto % 10
uni = int(resto)

if cent > 1:
    print('{} centenas, '.format(cent), end='')
else:
    print('{} centena, '.format(cent), end='')
if dec > 1:
    print('{} dezenas e '.format(dec), end='')
else:
    print('{} dezena e '.format(dec), end='')
if uni > 1:
    print('{} unidades'.format(uni))
else:
    print('{} unidade'.format(uni))
# if num > 99:
#     cent = int(num / 100)
#     resto = num % 100
#     dec = int(resto / 10)
#     resto = resto % 10
#     uni = int(resto)
#     if cent > 1:
#         print("{} centenas".format(cent))
#     else:
#         print('{} centena'.format(cent))
#     if dec > 1:
#         print('{} dezenas'.format(dec))
#     else:
#         print('{} dezena'.format(dec))
#     if uni > 1:
#         print('{} unidades'.format(uni))
#     else:
#         print('{} unidade'.format(uni))
# elif num > 9:
#     dec = int(num / 10)
#     resto = resto % 10
#     uni = int(resto)
#     if dec > 1:
#         print('{} dezenas'.format(dec))
#     else:
#         print('{} dezena'.format(dec))
#     if uni > 1:
#         print('{} unidades'.format(uni))
#     else:
#         print('{} unidade'.format(uni))
# elif num <= 9:
#     uni = int(num)
#     if uni > 1:
#         print('{} unidades'.format(uni))
#     else:
#         print('{} unidade'.format(uni))