n1 = int(input('Entre com um valor: '))
n2 = int(input('Entre com outro valor: '))
soma = 0

for x in range(n1, n2 + 1):
    print(x, end=(' '))
    soma += x

print('\nA soma dos números é de {}'.format(soma))