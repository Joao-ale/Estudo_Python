num1 = int(input('Entre com um valor: '))
num2 = int(input('Entre com outro valor: '))
num3 = int(input('Entre com outro valor: '))

if num1 > num2 > num3:
    print('O maior valor é o número {}'.format(num1))
elif num2 > num1 > num3:
    print('O maior valor é o número {}'.format(num2))
else:
    print('O maior valor é o número {}'.format(num3))
if num1 < num2 and num1 < num3:
    print('O menor valor é o número {}'.format(num1))
elif num2 < num1 and num2 < num3:
    print('O menor valor é o número {}'.format(num2))
else:
    print('o menor valor é o número {}'.format(num3))