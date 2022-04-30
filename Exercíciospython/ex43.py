nome = input('Entre com seu nome: ')
while len(nome) < 3:
    nome = input('O NOME PRECISA CONTER MAIS QUE 3 LETRAS! Entre com seu nome: ')

idade = int(input('Entre com sua idade: '))
while 0 < idade > 150:
    idade = int(input('A IDADE DEVE ESTAR ENTRE 0 E 150! Entre com sua idade: '))

sal = float(input('Entre com seu salário: R$'))
while sal < 0:
    sal = float(input('O SALÁRIO TEM QUE SER MAIOR QUE 0! Entre com seu salário: R$'))

sexo = input('Entre com o seu sexo F-feminino e M-masculino: ').upper()
while sexo !='F' and sexo != 'M':
    sexo = input('SEXO INVÁLIDO! Entre com o seu sexo F-feminino e M-masculino: ').upper()

estadcivi = input('Entre com seu estado civil, S-solteiro C-casado V-viúvo e D-divorciado: ').upper()
while estadcivi != 'S' and estadcivi != 'C' and estadcivi != 'V' and estadcivi != 'D':
    estadcivi = input('INVÁLIDO! entre com seu estado civil, S-solteiro C-casado V-viúvo e D-divorciado: ').upper()

print('-' * 50)
print('Nome: {}\n'
      'Idade: {}\n'
      'Salário: R${:.2f}\n'
      'Sexo: {}\n'
      'Estado civil: {}'.format(nome, idade, sal, sexo, estadcivi))