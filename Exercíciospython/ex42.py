nome = input('Digite seu nome de usuário: ').upper()
senha = input('Digite sua senha (não pode ser o mesmo que o nome de usuário): ').upper()
while nome == senha:
    print('ERRO! O NOME NÃO PODE SER IGUAL A SENHA!')
    nome = input('Digite seu nome de usuário: ').upper()
    senha = input('Digite sua senha ( não pode ser o mesmo que o nome de usuário): ').upper()
print('Prazer {} sua senha foi registrada com sucesso!'.format(nome))