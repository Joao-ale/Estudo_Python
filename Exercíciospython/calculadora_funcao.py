def soma ():
  return (a + b)

def sub ():
  return (a - b)

def multi ():
  return (a * b)

def divisao ():
  return (a / b)

a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))

while True:
  operacao = input("Qual operação deseja realizar?\n+: soma\n-: subtração \n*:  multiplicação\n/: divisão\n \nSua opção: ")
  match(operacao):
    case '+':
      print("\n{} + {} = {}".format(a, b,soma()))
      break
    case '-':
      print("\n{} - {} = {}".format(a, b, sub()))
      break
    case '*':
      print("\n{} * {} = {}".format(a, b, multi()))
      break
    case '/':
      print("\n{} / {} = {:.2f}".format(a, b, divisao()))
      break
    case _:
      print("\nOperação inválida, digite corretamente as opções.")
    