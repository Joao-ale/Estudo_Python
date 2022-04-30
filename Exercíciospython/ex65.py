idade = int(input('Entre com sua idade: '))
d = input('Deseja inserir uma nova idade? ').upper()
c = 1
s = idade

while d == 'S':
    idade = int(input('Entre com sua idade: '))
    c += 1
    s += idade
    d = input('Deseja inserir uma nova idade? ').upper()
med = s / c

if med <= 25:
    print('A média de idade da turma é {:.0f} e a turma é jovem'.format(med))
elif 26 <= med <= 60:
    print('A média de idade da turma é {:.0f} e a turma é adulta'.format(med))
elif med > 60:
    print('A média de idade da turma é {:.0f) e a turma é idosa'.format(med))