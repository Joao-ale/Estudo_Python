soma = quant = média = maior = menor = 0
opção = 'S'
while not opção == 'N':
    n = int(input('Digite um valor: '))
    opção = input('Quer continuar? S/N ').upper()
    soma += n
    quant += 1
    if n == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
média = soma / quant
print('Você digitou {} números e a média é {}!'.format(quant, média))
print('O maior é {} e o menor é {}'.format(maior, menor))
print('FIM')
