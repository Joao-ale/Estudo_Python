n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
n3=int(input('Terceiro número: '))
if n1 > n2 > n3:
    print('O primeiro número  é o maior!')
    print('O terceiro número é o menor!')
elif n1>n3>n2:
    print('O primeiro número é o maior!')
    print('O segundo número é o menor!')
elif n2> n1 >n3:
    print('O segundo número é o maior!')
    print('O terceiro número é o menor!')
elif n2>n3>n1:
    print('O segundo número é o maior!')
    print('O primeiro número é o menor!')
elif n3 > n1 and n3 > n2:
    print('O terceiro número é o maior!')
    print('O segundo número é o menor1')
elif n3>n2>n1:
    print('O terceiro número é o maior!')
    print('O primeiro número é o menor!')
