popA = int(input('Entre com o valor da população A: '))
popB = int(input('Entre com o valor da população B: '))
ano = 0

while popB > popA:
    popA += popA * 3 / 100
    popB += popB * 1.5 / 100
    ano += 1
if popA == popB:
    print('Levará {} para a população A se igualar a população B'.format(ano))
elif popA > popB:
    print('Levará {} anos para a população A ultrapassar a população B'.format(ano))
