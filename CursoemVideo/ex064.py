n = int(input('Digite um número: '))
count = n
c = 0
while not n == 999:
    n = int(input('Digite um número: '))
    c += 1
    if n != 999:
        count += n
print('Você digitou {} valores e a soma de todos é {}!'.format(c, count))
