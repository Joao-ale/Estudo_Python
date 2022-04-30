from random import randint
print('-=' * 50)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-='*50)
vitórias = 0
while True:
    jog = int(input('Escolha um número: '))
    comp = randint(0, 10)
    result = jog + comp

    opção = ' '
    while opção not in 'PI':
        opção = input('Par ou Ímpar: [P/I] ').upper().strip()[0]
    print('-' * 50)
    if opção == 'P':
        if result % 2 == 0:
            print(f'O JOGADOR jogou {jog} e o COMPUTADOR jogou {comp} o total é {result} e deu é PAR')
            print('-' * 50)
            print('\033[34m O JOGADOR GANHOU! \033[m')
            vitórias += 1
        else:
            print(f'O JOGADOR jogou {jog} e o COMPUTADOR jogou {comp} a soma é {result} e deu é IMPAR')
            print('-' * 50)
            print('\033[31m O JOGADOR PERDEU \033[m')
            break
    elif opção == 'I':
        if result % 2 == 1:
            print(f'O JOGADOR jogou {jog} e o COMPUTADOR jogou {comp} a soma é {result} e deu é IMPAR')
            print('-' * 50)
            print('\033[34m O JOGADOR GANHOU! \033[m')
            vitórias += 1
        else:
            print(f'O JOGADOR jogou {jog} e o COMPUTADOR jogou {comp} a soma é {result} e deu é PAR')
            print('-' * 50)
            print('\033[31m O JOGADOR PERDEU \033[m')
            break
    print('-' * 50)
    print('VAMOS JOGAR NOVAMENTE!')
print('-' * 50)
print(f'GAME OVER! Você ganhou um total de {vitórias} vezes')
