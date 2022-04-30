num = int(input('Entre com um valor: '))

if num > 0:
    print('O número {} é positivo'.format(num))
elif num == 0:
    print('O número é neutro, pois é 0')
else:
    print('O número {} é negativo'.format(num))