nota1 = int(input('Entre com a primeira nota: '))
while nota1 > 10:
    nota1 = int(input('NOTA INVÁLIDA! Entre com a primeira nota: '))
nota2 = int(input('Entre com a segunda nota: '))
while nota2 > 10:
    nota2 = int(input('NOTA INVÁLIDA!Entre com a segunda nota: '))
med = (nota1 + nota2) / 2

if 0 <= med < 4:
    print('ALUNO REPROVADO COM NOTA {} E CONCEITO E!'.format(med))
elif 4 <= med < 6:
    print('ALUNO REPROVADO COM NOTA {} E CONCEITO D!'.format(med))
elif 6 <= med < 7.5:
    print('ALUNO APROVADO COM NOTA {} E CONCEITO C!'.format(med))
elif 7.5 <= med < 9:
    print('ALUNO APROVADO COM NOTA {} E CONCEITO B!'.format(med))
elif 9 <= med <= 10:
    print('ALUNO APROVADO COM NOTA {} E CONCEITO A!'.format(med))