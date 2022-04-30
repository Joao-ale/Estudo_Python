maior=0
menor=0
for peso in range(1, 6):
    kg = float(input('Peso da {}° pessoa: '.format(peso)))
    if peso == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
                menor = kg
print('O maior peso é {}kg'.format(maior))
print('O menor peso é {}kg'.format(menor))