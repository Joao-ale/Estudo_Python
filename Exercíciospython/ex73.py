temp = float(input('Entre com uma temperatura: '))
conj = [temp]
ntemp = input('Deseja adicionar uma nova temperatura [S/N]: ').upper()
s = temp
c = 1
while ntemp == 'S':
    temp = float(input('Entre com uma temperatura: '))
    s += temp
    c += 1
    conj.append(temp)
    ntemp = input('Deseja adicionar uma nova temperatura? [S/N]').upper()
print('-' * 35)
print('Maior temperatura: {}º\n'
      'Menor temperatura: {}º\n'
      'Média das temperaturas: {:.1f}º'.format(max(conj), min(conj), s / c))