letra = input('Entre com uma letra: ').upper()
vogal = ['A', 'E', 'I', 'O', 'U']
if letra in vogal:
    print('A letra {} é uma vogal'.format(letra))
else:
    print('A letra {} é uma consoante'.format(letra))