n = int(input('Entre com um número para saber seu fatorial: '))
fat = n
c = n

while True:
    if c == 1:
        break
    fat *= (c - 1)
    c -= 1
print('{}! = {}'.format(n, fat))
