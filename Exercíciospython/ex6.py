# grau_fahren = int(input('Quantos graus fahrenheit: '))
# grau_cel = 5*((grau_fahren-32)/9)
#
# print('{}ºF corresnponde a {:.2f}ºC'.format(grau_fahren,grau_cel))
grau_cel = int(input(('Quantos graus celsius: ')))
grau_fahren = grau_cel * 1.8 + 32

print('{}ºC corresponde a {:.2f}ºF'.format(grau_cel,grau_fahren))