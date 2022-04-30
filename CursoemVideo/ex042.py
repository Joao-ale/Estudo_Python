r1=int(input('Primeira reta: '))
r2=int(input('Segunda reta: '))
r3=int(input('Terceira reta :'))
if r1 < r2 + r3 or r2 < r1 + r3 or r3 < r1 + r2:
    print('\033[35mOs valores PODEM formar um triângulo!\033[m')
    if r1==r2==r3:
        print('\033[34mO triângulo é EQUILATERO!\033[m')
    elif r1!=r2==r3 or r2!=r1==r3 or r3!=r1==r3:
        print('\033[32mO triângulo é ISÓCELES!\033[m')
    elif r1!=r2!=r3:
        print('\033[36mO triângulo é ESCALENO!\033[m')
else:
    print('\033[31mOs valores NÃO PODEM formar um triângulo!\033[m')