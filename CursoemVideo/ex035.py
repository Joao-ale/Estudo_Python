r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))
if r1 < r2 + r3 or r2 < r1 + r3 or r3 < r1 + r2:
    print('\033[33mPode formar um triângulo\033[m')
else:
    print('\033[31mNão pode formar um triângulo\033[m')