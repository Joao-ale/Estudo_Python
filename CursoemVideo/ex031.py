km=float(input('Qual a distância da viagem? '))
if km <= 200:
    passa=km*0.50
    print('Sua viagem de {}km irá custar R${:.2f}!'.format(km,passa))
else:
    passa=km*0.45
    print('Su viagem de {}km irá custar R${}'.format(km,passa))
