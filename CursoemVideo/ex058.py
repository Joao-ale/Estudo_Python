from random import randint

computador = randint(0, 10)  # computador sorteia
print('\033[33m-=-' * 20)
print('Eu sou seu computador,irei pensar em um número de 0 a 10 tente adivinhar')
print('-=-' * 20)
erros = 0
acertou = False
while not acertou:
    jogador = int(input('\033[m\033[33mQual número eu pensei:\033[m '))
    erros += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[33mMais... Tente de novo\033[m')
        elif jogador > computador:
            print('\033[33mMenos... Tente de novo\033[m')
print('\033[34mParabéns você me venceu!\033[m')
print('\033[34mVocê tentou {} vezes\033[m'.format(erros))
