velo=int(input('Quala velocidade do veículo: '))
if  velo >80:
    multa=(velo-80)*7
    print('\033[31mTENHA CUIDADO, você foi multado em R${:.2f}\033[m'.format(multa))
else:
    print('\033[32mTenha um bom dia, dirija com segurança\033[m ')