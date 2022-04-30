a = int(input("Primeiro Bimestre: "))
if a > 10:
    a = int(input("Você digitou errado. Primeiro biestre: "))
b = int(input("Segundo Bimertre: "))
if b > 10:
    b = int(input("Você digitou errado. Segundo bimestre: "))
c = int(input("Terceiro Bimertre: "))
if c > 10:
    c = int(input("Você digitou errado. Terceiro bimestre: "))
d = int(input("Quarto Bimertre: "))
if d > 10:
    d = int(input("Você digitou errado. Quarto bimestre"))
med = (a+b+c+d) / 4
print("média: {}".format(med))
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#
# else:
#     print("Foi infromado alguma nota errada")

# a = int(input("Entre com o primeirp  valor: "))
# b = int(input("Entre com o segundo  valor: "))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print("Foi digitado um número par")
# else:
#     print("Nenhum número par foi digitdo")


# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))
# if a>b and a>c:
#     print("O maior número é {}".format(a))
# elif b>a and b>c:
#     print("O maior número é {}".format(b))
# else:
#     print("O maior número é {}".format(c))