#estrutura de repetição
'''for c in range(7,-1,-1):
    print(c)
print('FIM')
--------------------------------------
n = int(input('Dgite um número: '))
for c in range(0,n+1):
    print(c)
print('FIM')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)'''
s = 0
for c in range(0,4):
    n=int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores é {}'.format(s))
