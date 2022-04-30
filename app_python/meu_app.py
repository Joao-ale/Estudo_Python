a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
soma = a + b
subtracao = a - b
multicacao = a * b
divisao = a / b
resto = a % b

result = ("Soma: {soma}"
        "\nSubtração: {sub}"
        "\nMultiplicação: {multi}"
        "\nDivisão: {divi} "
        "\nResto: {rest}".format(soma=soma,
                                        sub=subtracao,
                                        rest=resto,
                                        multi=multicacao,
                                        divi=divisao))
print(result)