print("Gerador de PA")
print("-=-" * 20)
inicio = int(input('Primeiro termo da PA: '))
razão = int(input('Razão: '))
termo = inicio
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print("{} --> ".format(termo), end='')
        termo += razão
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão foi finalizada com {} termos.'.format(total))
