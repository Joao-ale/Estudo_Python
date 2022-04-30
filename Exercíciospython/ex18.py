nota_1 = int(input('Entre com a primeira nota: '))
nota_2 = int(input('Entre com a seginda nota: '))
med = (nota_1 + nota_2) / 2

if med > 7 or med == 7:
    print('ALUNO APROVADO! MÉDIA: {}'.format(med))
elif med == 10:
    print('ALUNO APROVADO COM DISTINÇÃO!MÉDIA:10')
else:
    print('ALUNO REPROVADO! MÉDIA: {}'.format(med))