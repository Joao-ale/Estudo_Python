n = int(input('Até qual número deseja ver os números primos: '))
c = 0

for f in range(1, n + 1):
    for x in range(1, f + 1):
        prim = f % x
        if prim == 0:
            c += 1
    if c == 2:
        print('O número {} é primo'.format(f))
    else:
        print('O número {} não é primo'.format(f))
    if f == x:
        c = 0