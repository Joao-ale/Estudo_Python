nota = int(input('Entre com uma nota: '))
while nota > 10:
    nota = int(input('A nota deve estar entre 0 e 10! Entre com uma nota: '))
d = input('Deseja inserir uma nova nota? ').upper()
s = nota
c = 1
while d == 'S':
    nota = int(input('Entre com uma nota: '))
    while nota > 10:
        nota = int(input('A nota deve estar entre 0 e 10! Entre com uma nota: '))
    s += nota
    c += 1
    d = input('Deseja inserir uma nova nota? ').upper()
med = s / c
print('A média aritimética das notas é {}'.format(med))