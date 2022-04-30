turma = int(input('Quantas turmas existem? '))
s = 0

for x in range(1, turma + 1):
    aluno = int(input('Quantos alunos há na turma {}: '.format(x)))
    while aluno > 40:
        print('As turmas suportam apenas 40 alunos.')
        aluno = int(input('Quantos alunos há na turma {}: '.format(x)))
    s += aluno
    print('-' * 50)
med = s / turma

print('A média entre {} alunos e {} turmas é {:.0f}'.format(s, turma, med))