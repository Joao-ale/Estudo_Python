frase=input('Digite uma frase: ').strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
'''for c in range(len(junto) - 1, -1, -1):
    inverso+=junto[c]'''
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print(']a frase NÃO é um palíndromo')
