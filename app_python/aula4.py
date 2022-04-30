a = int(input("Primeiro Bimestre: "))
while a > 10:
    a = int(input("Você digitou errado. Primeiro biestre: "))
b = int(input("Segundo Bimertre: "))
while b > 10:
    b = int(input("Você digitou errado. Segundo bimestre: "))
c = int(input("Terceiro Bimertre: "))
while c > 10:
    c = int(input("Você digitou errado. Terceiro bimestre: "))
d = int(input("Quarto Bimertre: "))
while d > 10:
    d = int(input("Você digitou errado. Quarto bimestre"))
med = (a+b+c+d) / 4
print("média: {}".format(med))

# nota = int(input("Entre com a nota: "))
# while nota > 10:
#     nota = int(input("Nota inválida. Entre com a nota correta: "))
# print(nota)

# a = int(input("Entre com um valor: "))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num +1):
#         resto = num % x
#         if resto == 0:
#            div += 1
#     if div == 2:
#         print(num)
#

# a = int(input("Digite um número: "))
#
# div = 0
# for x in range(1,a+1):
#     resto = a % x
#     print("{} dividido por {} tem o resto da divisão é {}".format(a, x, resto))
#     if resto == 0:
#        div += 1
# if div == 2:
#     print("O número {} é primo".format(a))
# else:
#     print("O número {} não é primo".format(a))
