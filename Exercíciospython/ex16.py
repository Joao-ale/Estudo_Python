letra = input('Digite F para feminino ou M para masculino: ').upper()

if letra == 'F':
    print('A letra digitada foi F e se refere ao sexo feminino')
elif letra == 'M':
    print('A letra digitada foi M e se refere ao sexo feminno')
else:
    print('A letra digitada foi {} e é um sexo inválido'.format(letra))