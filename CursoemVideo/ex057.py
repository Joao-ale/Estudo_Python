sexo = input('Digite o seu sexo [M/F] ').upper().strip()[0]
while sexo not in 'MF':
    sexo = input('Dados do sexo inválido. Por favor informe seu sexo M/F ').upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
