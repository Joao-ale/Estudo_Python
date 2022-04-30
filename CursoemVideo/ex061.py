print("Gerador de PA")
print("-=-" * 20)
inicio = int(input('Primeiro termo da PA: '))
razão = int(input('Razão: '))
termo = inicio
count = 1
while count <= 10:
    print("{} --> ".format(termo), end='')
    termo += razão
    count += 1
print('FIM')
