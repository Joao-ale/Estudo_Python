n1 = int(input('Entre com a primeira nota: '))
while n1 > 10:
    n1 = int(input('NOTA INVÁLIDA! Entre com a primeira nota: '))
n2 = int(input('Entre com a segunda nota: '))
while n2 > 10:
    n2 = int(input('NOTA INVÁLIDA! Entre com a segunda nota: '))
n3 = int(input('Entre com a terceira nota: '))
while n3 > 10:
    n3 = int(input('NOTA INVÁLIDA! Entre com a terceira nota'))
med = (n1 + n2 + n3) / 3

if med >= 7 and med != 10:
    print('APROVADO COM MÉDIA: {:.2f}'.format(med))
elif med < 7:
    print('REPROVADO COM MÉDIA: {:.2f}'.format(med))
elif med == 10:
    print('APROVADO COM DISTINÇÃO!')