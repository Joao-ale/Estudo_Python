from time import sleep
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)#computdor pensa
print('\033[33m-=-' * 20)
print('Vamos jogar JOKENPÔ...')
print('-=-' * 20)
print('''Suas opções
[ 0 ] Pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ\033[m')
if computador == 0:#pedra
    if jogador == 0:
        print('\033[33mEMPATOU!\033[m')
    elif jogador == 1:
        print('\033[34mJOGADOR GANHOU!\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR GANHOU!\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:#papel
    if jogador == 0:
        print('\033[31mCOMPUTADOR GANHOU!\033[m')
    elif jogador == 1:
        print('\033[33mEMPATOU!\033[m')
    elif jogador == 2:
        print('\033[34mJOGADOR GANHOU!\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:#tesoura
    if jogador == 0:
        print('\033[34mJOGADOR GANHOU!\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR GANHOU!\033[m')
    elif jogador == 2:
        print('\033[33mEMPATOU!\033[m')
    else:
        print('JOGADA INVÁLIDA!')
print('\033[37mO jogador jogou {} e o computador jogou {}\033[m'.format(itens[jogador], itens[computador]))
sleep(2)
opção = input('\033[33mVocê quer jogar denovo? S/N\033[m ').upper()
while not opção == 'N':
    computador = randint(0, 2)
    print('\033[33m-=-' * 20)
    print('Vamos jogar JOKENPÔ...')
    print('-=-' * 20)
    print('''Suas opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] tesoura''')
    jogador = int(input('Qual sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ\033[m')
    if computador == 0: #Pedra
        if jogador == 0:
            print('\033[33mEMPATOU!\033[m')
        elif jogador == 1:
            print('\033[34mJOGADOR GANHOU!\033[m')
        elif jogador == 2:
            print('\033[31mCOMPUTADOR GANHOU!\033[m')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 1: #Papel
        if jogador == 0:
            print('\033[31mCOMPUTADOR GANHOU!\033[m')
        elif jogador == 1:
            print('\033[31mEMPATOU!\033[m')
        elif jogador == 2:
            print('\033[34mJOGADOR GANHOU!\033[m')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 2: #tesoura
        if jogador == 0:
            print('\033[34mJOGADOR GANHOU!\033[m')
        elif jogador == 1:
            print('\033[31mCOMPUTADOR GANHOU!\033[m')
        elif jogador == 2:
            print('\033[33mEMPATOU!\033[m')
        else:
            print('JOGADA INVÁLIDA')
    print('\033[37mO jogador jogou {} e o computador jogou {}\033[m'.format(itens[jogador], itens[computador]))
    sleep(2)
    opção = input('\033[33mQuer jogador denovo? S/N\033[33m ').upper()
print('\033[32mFIM\033[m')
