n1 = float(input('Entre com um valor: '))
n2 = float(input('Entre com outro valor: '))
opera = input('Qual operação você deseja (M-multiplicação, D- divisão, A-adição, S-subtração): ').upper()
# while opera != 'M' or opera != 'D' or opera != 'A' or opera != 'S':
#     opera = input('OPERAÇÃO INVÁLIDA! Qual operação você deseja (M-multiplicação, D- divisão, A-adição, S-subtração): ').upper()

#verifica a operação e a realiza
if opera == 'D':
    operac = n1 / n2
    print('A divisão entre {} e {} tem como resultado {:.2f}'.format(n1, n2, operac))

elif opera == 'M':
    operac = n1 * n2
    print('A multiplicação entre {} e {} tem como resultado {:.1f}'.format(n1, n2, operac))

elif opera == 'A':
    operac = n1 + n2
    print('A adição entre {} e {} tem como resultado {}'.format(n1, n2, operac))

elif opera == 'S':
    operac = n1 - n2
    print('A subtração entre {} e {} tem como resultado {}'.format(n1, n2, operac))


# testa para ver se é par ou impar
if operac % 2 == 0:
    print('O resultado da operação é par')
else:
    print('O resultado da operação é impar')

# testa para ver se é positivo ou negativo
if operac > 0:
    print('O resultado da operação é positivo')
else:
    print('O resultado da operação é negativo')
operac = str(operac)
if '.' in operac:
    operac = float(operac)
    print('O resultado da operação é decimal')
else:
    operac = int(operac)
    print('O resultado da operação é inteiro')