somaidade = 0
médiaidade = 0
maioridadeh = 0
nomevelho = ''
menos20f = 0
for pess in range(1, 5):
    print('-=-'*5, '{}° pessoa'.format(pess), '-=-'*5)
    nome = input('NOME: ').strip()
    idade = int(input('IDADE: '))
    somaidade += idade
    sexo = input('M/F: ').strip()
    if pess == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        menos20f += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é {}'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeh,nomevelho))
print('No grupo existe {} mulheres com menos de 20 anos'.format(menos20f))
