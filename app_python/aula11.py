lista = [1, 10]
try:
    arquivo = open("teste.txt", "r")
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]


except ZeroDivisionError:
    print("Nao e possivel realizar divisao por 0")
except ArithmeticError:
    print("Houve um erro ao realizar a expressao aritimetica")
except IndexError:
    print("Erro ao acessar um indice invalido da lista")
except Exception as ex:
    print("erro desconhecido. Erro: {}".format(ex))
else:
    print("Executa quando nao ocorre excecao")
finally:
    print("Sempre executa")
    arquivo.close
