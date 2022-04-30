soma = 0
med = 0
for x in range(1, 6):
    n = int(input('Entre com um valor: '))
    soma += n
    med += n
    if x == 5:
        med /= 5
print('a soma foi {} e a média foi {}'.format(soma, med))