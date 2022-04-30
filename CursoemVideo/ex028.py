from random import randint
from time import sleep
cores={'limpa':'\033[m',
       'amarelo':'\033[33m',
       'azul':'\033[34m',
       'vermelho':'\033[31m'}
computador=randint(0,5)#faz o computador pensar
print('{}-=-'.format(cores['amarelo'])*20)
print('{}{}Vou pensar em um número de 0 a 5.Tente adivinhar...{}'.format(cores['limpa'],cores['azul'],cores['limpa']))
print('{}-=-'.format(cores['amarelo'])*20)
jogador=int(input('Em que número eu pensei? '))#jogador respondendo
print('PROCESSANDO...{}'.format(cores['limpa']))
sleep(2)
if computador ==jogador:
    print('{} PARABÉNS você conseguiu me vecer{}'.format(cores['azul'],cores['limpa']))
else:
    print('{} Eu GANHEI, eu pensei no número {} e não no número {}'.format(cores['vermelho'],computador,jogador,cores['limpa']))
