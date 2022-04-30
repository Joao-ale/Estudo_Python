#fibonacci 1
n = int(input('Em qual número começa a sequencia: '))
b = int(input('Até qual posição você deseja ver a sequência: '))


#calcula o primeiro valor da sequência
c = n + (n - 1)
print(c)
a = c
for x in range(1, b + 1):
    #calcula o termo
    c = a + n
    print(c)
    #adiciona na memória o resultado
    n = c
    #calcula o próximo termo
    c = a + n
    print(c)
    #adiciona o novo resultado na memória, trocando com a váriavel "n"
    a = c