n1 = int(input('Entre com o valor da base: '))
n2 = int(input('Entre com o valor do expoente: '))
exp = n1

for x in range(1, n2):
    exp *= n1

print('{} elevado a {} é igual a {}'.format(n1, n2, exp))