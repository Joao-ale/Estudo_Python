n=int(input('Digite um número: '))
u=n//1 % 10
d=n//10 % 10
c=n//100 % 10
m=n//1000 % 10
print('\033[33m-=-'*20)
print('Analisando o número {}...'.format(n))
print('-=-'*20)
print('\033[mUnidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
