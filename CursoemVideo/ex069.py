cidade = chomens = cmulheres20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper().strip()[0]
    if idade >= 18:
        cidade += 1
    if sexo == 'M':
        chomens += 1
    elif sexo == 'F':
        if idade < 20:
            cmulheres20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break

print('==========FIM DO PROGRAMA==========')
print(f'Total de pessoas com mais de 18 anos cadastradas é {cidade} \n Total de homens cadastrados é de {chomens} \n Total de mulheres com menos de 20 anos cadastradas são {cmulheres20}')
