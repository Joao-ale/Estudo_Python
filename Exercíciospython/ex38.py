tipocomb = input('Qual o tipo de combustivel a ser abstecido (G-gasolina, A-álcool): ').upper()
litros = int(input('Quantos litros deseja abastecer: '))

if tipocomb == 'A':
    if litros <= 20:
        pag = (1.90 - (1.90 * 3 / 100)) * litros
        print('O total a pagar é R${:.2f}'.format(pag))
    elif litros > 20:
        pag = (1.90 - (1.90 * 5 / 100)) * litros
        print('O total a pagar é R${:.2f}'.format(pag))
else:
    if litros <= 20:
        pag = (2.50 - (2.50 * 4 / 100)) * litros
        print('O total a pagar é R${:.2f}'.format(pag))
    elif litros > 20:
        pag = (2.50 - (2.50 * 6 / 100)) * litros
        print('O total a pagar é R${:.2f}'.format(pag))