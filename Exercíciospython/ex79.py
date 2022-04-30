for x in range(1,11):
    naluno = int(input('Insira o número do aluno: '))
    alt = float(input('Insira a altura do aluno {}: '.format(naluno)))
    alto = alt
    baixo = alt
    numalt = naluno
    numbaixo = naluno
#problema na verificação do luno mis bixo e mais alto
    if alt > alto:
        alto = alt
        numalt = naluno

    if alt < baixo:
        baixo = alt
        numbaixo = naluno

print('aluno mais alto: aluno {} com {}m\n'
      'aluno mais baixo: aluno {} com {}m '.format(numalt, alto, numbaixo, baixo))