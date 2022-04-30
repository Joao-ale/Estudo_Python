km=int(input('Quantos km percorreu: '))
dias=int(input('Quantos dias ficou com o carro: '))
preçokm=km*0.15
preçodia=dias*60
preço=preçokm+preçodia
print('Você ficou {} dias com o carro e rodou um total de {} kms e com isso você irá pagar R${:.2f} '.format(dias,km,preço))