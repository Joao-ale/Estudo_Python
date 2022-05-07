class Error(Exception):
    pass


# Cria um Erro personalisado
class InputError(Error):
    def _init_(self, message):
        self.message = message


while True:
    try:
        x = int(input("Entre com uma nota de 0 a 10: "))
        print(x)
        # Testa o valor para que caia no erro caso seja maior que 10
        if x > 10:
            # raise é o comando que faz forçar o erro
            raise InputError("Nota não pode ser maior que 10")
        elif x < 0:
            raise InputError("Nota não pode ser menor que 0")
        break
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas numeros")
    except InputError as ex:
        print(ex)
