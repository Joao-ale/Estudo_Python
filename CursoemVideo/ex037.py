n1=int(input('Digite um número inteiro: '))
n2=int(input('''\033[33mEscolha uma das basase para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
Sua opção:\033[m '''))
if n2==1:
    print('O valor {} em BINÁRIO ficará {}'.format(n1,bin(n1)[2:]))
elif n2==2:
    print('O valor {} em OCTAL ficará {}'.format(n1,oct(n1)[2:]))
elif n2==3:
    print('O valor {} e HEXADECIMAL ficará {}'.format(n1,hex(n1)[2:]))
else:
    print('\033[31m OPÇÃO INVÁLIDA, TENTE NOVAENTE\033[m')