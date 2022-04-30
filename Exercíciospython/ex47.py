nmaior = 0
for x in range(1,6):
    n = int(input('Entre com um valor: '))
    if n > nmaior:
        nmaior = n
print('O maior número é {}'.format(nmaior))