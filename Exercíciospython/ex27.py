a = int(input('Entre com o valor do primeiro lado: '))
b = int(input('Entre com o valor do segundo lado: '))
c = int(input('Entre com o valor do terceiro lado: '))

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('O triângulo de lados {}, {} e {} existe!'.format(a, b, c))
    if a == b == c:
        print('O triângulo é equilátero')
    elif a == b and a < c:
        print('O triângulo é Isósceles')
    elif b == c and b < a:
        print('O triângulo é Isósceles')
    elif c == a and c < b:
        print('O triângulo é Isósceles')
    elif a == b and a > c:
        print('O triângulo é Isósceles')
    elif b == c and b > a:
        print('O triângulo é Isósceles')
    elif c == a and c > b:
        print('O triângulo é Isósceles')
    elif a != b and a != c and c != b:
        print('O triângulo é Escaleno')
else:
    print('O triângulo de lados {}, {} e {} não existe'.format(a, b, c))