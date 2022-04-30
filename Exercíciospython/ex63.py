from time import sleep

n = int(input('Até qual valor deseja ver os números primos: '))
c = 0

for t in range(1, n+1):
    for x in range(1, t + 1):
        if t % x == 0:
            c += 1
            print('{} é divisivel por {}'.format(t, x))
        if t == x:
            if c == 2:
                print('-' * 25)
                print('Número {} é primo'.format(t))
            else:
                print('-' * 25)
                print('Número {} não é primo'.format(t))
            c = 0
            print('-' * 25)
