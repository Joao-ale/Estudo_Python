n = int(input('Montar a tabuada de : '))
come = int(input('Começar por: '))
term = int(input('Terminar em: '))

print('\nVou montar a tabuada do {}, começando por {} e terminando em {}:'.format(n, come, term))
for x in range(come, term + 1):
    print('{} X {} = {}'.format(n, x, n * x))