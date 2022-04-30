elei = int(input('Quantos eleitores existem? '))
cand1 = 0
cand2 = 0
cand3 = 0
nulo = 0
branco = 0
voto = ''

for x in range(1, elei + 1):
    voto = input('Vota em qual candidato (1, 2, 3, N-nulo, B-branco):  ').upper()
    while voto != '1' and voto != '2' and voto != '3' and voto != 'N' and voto != 'B':
        print('VOTO INVÁLIDO, VOTE NOVAMENTE!')
        voto = input('Vota em qual candidato (1, 2, 3, N-nulo, B-branco):  ').upper()
    if voto == '1':
        cand1 += 1
    elif voto == '2':
        cand2 += 1
    elif voto == '3':
        cand3 += 1
    elif voto == 'N':
        nulo += 1
    elif voto == 'B':
        branco += 1

print('-' * 50)
print('Candidato 1: {}\n'
      'Candidato 2: {}\n'
      'Candidato 3: {}\n'
      'Nulo: {}\n'
      'Branco {}'.format(cand1, cand2, cand3, nulo, branco))