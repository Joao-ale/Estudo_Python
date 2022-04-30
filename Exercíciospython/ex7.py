numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite mais um número inteiro:'))
numero3 = float(input('Digite um número real: '))

#Calcula o dobro do primeiro número vezes a metade do segundo numero
equacao1 = (numero1 * 2) * (numero2 / 2)
# Calcula o triplo do primeiro número somado ao terceiro número
equacao2 = numero1 * 3 + numero3
# Calcula o terceiro número elevado ao cubo
equacao3 = numero3 * numero3 * numero3

print('O produto do dobro do primeiro com metade do segundo é = {:.2f} \n'
      'A soma do triplo do primeiro com o terceiro é = {:.2f} \n'
      'o terceiro elevado ao cubo é = {:.2f}'.format(equacao1, equacao2, equacao3))