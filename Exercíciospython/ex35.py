#
# n = input('Entre com um valor: ')
# #dificuldade ao especificar a casa decimal a ser avaliada
#
#
# if '.' in n:
#     n = float(n)
#     print('O número é decimal')
# else:
#     print('O número é inteiro')
# print(n)
n = input('Entre com um valor: ')
if '.' in n:
    n = float(n)
if type(n) is float:
    print('decimal')
print(type(n))