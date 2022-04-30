from datetime import date
ano = int(input('Digite o ano que você nasceu: '))
atual = date.today().year
idade = atual-ano
if idade < 18:
    saldo = 18 - idade
    alist = saldo + atual

    print('Ainda falta {} anos para você se alistar, seu alistamento será em {}'.format(saldo, alist))
elif idade == 18:
    print('Você tem que se alistar IMEDITAMENE!')
elif idade > 18:
    saldo = idade-18
    alist = atual-saldo
    print('Voê já deveria ter se alistado a {}. Seu alistamento foi em {}'.format(saldo, alist))