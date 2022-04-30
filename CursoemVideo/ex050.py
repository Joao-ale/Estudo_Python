s=0
cont=0
for c in range(1,7):
    n=int(input('Digite o valor {}° número: '.format(c)))
    if n % 2 == 0:
        s += n
        cont+=1
print('Você digitou {} valores e a soma  é {}'.format(cont,s))