altura=float(input('Digite sua altura: '))
peso=float(input('Digite seu peso: '))
imc=peso/(altura**2)
if imc < 18.5:
    print('Com o imc de {:.2f} você está abaixo do peso'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Com o imc de {:.2f} vocÊ está no peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Com o imc de {:.2f} você está sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Com o imc de {:.2f} você está com obesidade'.format(imc))
elif imc > 40:
    print('Com o imc de {:.2f} você está com obesidade mórbida'.format(imc))