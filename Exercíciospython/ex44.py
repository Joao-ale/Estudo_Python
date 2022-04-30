popA = 80000
popB = 200000
ano = 0
while popB > popA:
    popA += popA * 3 / 100
    popB += popB * 1.5 / 100
    ano += 1
print('levará {} anos para a população A se igualar ou passar a população B'.format(ano))