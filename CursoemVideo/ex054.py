from datetime import date
atual = date.today().year
count = 0
countmenor = 0
for pess in range(1, 8):
    nasc = int(input('Qual ano a {}° pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        count += 1
    else:
        countmenor += 1
print('{} pessoas ATINGIRAM a maioridade e {} NÃO ATINGIRAM a maioridade'.format(count,countmenor))
