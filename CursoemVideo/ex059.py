from time import sleep

n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
opção = 0
while not opção == 5:
    sleep(2)
    print('''\033[34mMenu
    [ 1 ] Somar os valores;
    [ 2 ] Multiplicar os valores;
    [ 3 ] Qual valor é o maior;
    [ 4 ] Novos números;
    [ 5 ] Encerrar o programa;\033[m''')
    opção = int(input('\033[33m>>>Qual sua opção?\033[m '))
    s = n1 + n2
    m = n1 * n2
    if opção == 1:
         print('\033[35mA soma de {} e {} é igual a {}\033[m'.format(n1, n2, s))
         print('-=-' * 20)
    elif opção == 2:
        print('\033[38mA mutiplicação de {} e {} é  igual a {}\033[m'.format(n1, n2, m))
        print('-=-' * 20)
    elif opção == 4:
        n1 = int(input('\033[33mDigite novos valores: '))
        n2 = int(input('Digite novos valores: \033[m'))
        print('-=-' * 20)
    elif opção == 3:
        if n1 > n2:
            print('\033[37mO maior valor é {}\033[m'.format(n1))
            print('-=-' * 20)
        elif n2 > n1:
            print('\033[37mO maior valor é {}\033[m'.format(n2))
            print('-=-' * 20)
    elif opção == 5:
         print('FINALIZANDO...')
         print('-=-' * 20)
    else:
        print('Opção inválida')
sleep(2)
print('Programa finalizado. Volte sempre')
