'''for c in range (1, 10):
   print(c)
c = 1
while c < 11:
    print(c)
    c += 1'''
'''r = 'S'
while r == 'S':
    n=int(input('Digite um valor: '))
    r = input('Deseja continuar? [S/N] ').upper()
print('FIM!')'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Dos números digitados {} foram pares e {} foram ímpares'.format(par, impar))
print('Acabou')