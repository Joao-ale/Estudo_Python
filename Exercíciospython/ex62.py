n = int(input('Entre com um valor: '))
c = 0

for x in range(1, n + 1):
    pri = n % x
    if pri == 0:
        c += 1
        print('Ele é divisível por {}'.format(x))
print('-' * 20)
if c == 2:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))