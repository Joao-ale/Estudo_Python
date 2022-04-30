numero = int(input('Entre com um valor: '))
contador = 0

# Cria laço for indo de 1 até o número desejado
for x in range(1, numero + 1):
    # Verifica se o número tem resto 0 na divisão 
    # realizando essa ação de 1 até ele
    primo = numero % x
    # Caso o resto da divisão seja 0 significa que ele é divisivel por aquele número
    # Aumentando +1 no contador
    if primo == 0:
        contador += 1
        
if contador == 2:
    print('O número {} é primo'.format(numero))
else:
    if numero == 0:
        print('O número 0 é considerado um número neutro!')
    else:
        print('O número {} não é primo'.format(numero))
    
    