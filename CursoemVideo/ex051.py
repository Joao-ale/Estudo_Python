n1 = int(input('Primeiro termo de uma P.A: '))
r = int(input('Razão da P.A: '))
decimo = n1 + (10 - 1) * r
for c in range(n1, decimo + r, r):
    print('{:2}'.format(c), end=' -> ')
print('ACABOU')