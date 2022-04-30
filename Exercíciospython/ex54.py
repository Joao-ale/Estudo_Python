par = 0
impar = 0
for x in range(1,11):
    n = int(input('Entre com um valor: '))
    if n % 2 == 0:
        par += 1
    elif n % 2 !=0:
        impar += 1
print('Nos números digitados apareceu {} pares e {} impares'.format(par, impar))