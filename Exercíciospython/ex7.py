num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro:'))
num3 = float(input('Digite um número real: '))

eq1 = (num1 * 2) * (num2 / 2)
eq2 = num1 * 3 + num3
eq3 = num3 * num3 * num3

print('O produto do dobro do primeiro com metade do segundo é = {:.2f} \n'
      'A soma do triplo do primeiro com o terceiro é = {:.2f} \n'
      'o terceiro elevado ao cubo é = {:.2f}'.format(eq1, eq2, eq3))