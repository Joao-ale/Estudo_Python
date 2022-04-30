n = int(input('Entre com um valor: '))
c = 0

for x in range(1, n + 1):
    prim = n % x
    if prim == 0:
        c += 1
        print('{} é divisivel por {}'.format(n, x))
if c == 2:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))