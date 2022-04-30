from datetime import date
atual=date.today().year
ano=int(input('Em que ano você nasceu? '))
idade=atual-ano
if idade <= 9:
    print('O atleta irá disputar na categoria MIRIM!')
elif idade > 9 and idade <= 14:
    print('O atleta irá disputar na categoria INFATIL!')
elif idade > 14 and idade <= 19:
    print('O atleta irá disputar na categoria JUNIOR!')
elif idade > 19 and idade <= 25:
    print('O atleta irá disputar na categoria SÊNIOR!')
elif idade > 25:
    print('O atleta irá disputar na categoria MASTER!')