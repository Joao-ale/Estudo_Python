valor = int(input('Qual valor deseja sacar? R$'))

cem = int(valor / 100)
resto = valor % 100
cinq = int(resto / 50)
resto = resto % 50
dez = int(resto / 10)
resto = resto % 10
cinc = int(resto / 5)
resto = resto % 5
um = int(resto)

if cem > 1:
    print('{} notas de R$100,00 , '.format(cem), end='')
else:
    print('{} nota de R$100,00 , '.format(cem), end='')
if cinq > 1:
    print('{} notas de R$50,00 , '.format(cinq), end='')
else:
    print('{} nota de R$50,00 , '.format(cinq), end='')
if dez > 1:
    print('{} notas de R$10,00 , '.format(dez), end='')
else:
    print('{} nota de R$10,00 , '.format(dez), end='')
if cinc > 1:
    print('{} notas de R$5,00 e '.format(cinc), end='')
else:
    print('{} nota de R$5,00 e '.format(cinc), end='')
if um > 1:
    print('{} notas de R$1,00 '.format(um))
else:
    print('{} nota de R$1,00  '.format(um))