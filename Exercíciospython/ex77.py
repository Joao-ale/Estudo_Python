cod = input('Código: ')

peso = float(input('Peso (Kg): '))

altura = float(input('Altura (m): '))

des = input('Deseja inserir mais um aluno (0-não 1-sim): ')
c = 1
sal = altura
spes = peso
maia = altura
mena = altura
maip = peso
menp = peso
codmaia = cod
codmena = cod
codmaip = cod
codmenp = cod
while des != '0':
    print('-' * 20)
    cod = input('Código:')
    peso = float(input('Peso(Kg): '))
    altura = float(input('Altura(m): '))
    if maia < altura:
        maia = altura
        codmaia = cod
    elif mena > altura:
        mena = altura
        codmena = cod
    if maip < peso:
        maip = peso
        codmaip = cod
    elif menp > peso:
        menp = peso
        codmenp = cod
    des = input('Deseja inserir mais um aluno (0-não 1-sim)')
    sal += altura
    spes += peso
    c += 1


print('Mais alto: aluno {} com {:.2f}m\n'
      'Mais baixo: aluno {} com {:.2f}m\n'
      'Mais gordo: aluno {} com {:.1f}Kg\n'
      'Mais magro: aluno {} com {:.1f}Kg\n'
      'Média altura: {:.2f}\n'
      'Media peso: {:.1f}'.format(codmaia, maia, codmena, mena, codmaip, maip, codmenp, menp, sal / c, spes / c))