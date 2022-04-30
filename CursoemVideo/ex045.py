from random import randint
from time import  sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2) #computador pensando
print('\033[33mVamos jogar jokenpô')
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ\033[m')
sleep(1)
#resposta = 'S'
#while resposta == 'Nn':
if computador == 0:#pedra
    if jogador == 0:
        print('\033[33mEMPATE!\033[m')
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
        print('\033[33mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[34mJOGADOR GANHOU!\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:#tesoura
    if jogador == 0:
        print('\033[34mJOGADOR GANHOU!\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR GANHOU!\0333[m')
    elif jogador == 2:
        print('\033[33mEMPATE!\033[m')
    else:
        print('JOGADA INVÁLIDA!')
print('\033[35mO computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}\033[m'.format(itens[jogador]))
    #resposta = input('Quer jogar novamente? [S/N] ').to1
# upper()