p1 = input('Telefonou para a vitima? [S/N] ').upper()
p2 = input('Esteve no local do crime? [S/N] ').upper()
p3 = input('Mora perto da vitima? [S/N] ').upper()
p4 = input('Devia para a vitima? [S/N] ').upper()
p5 = input('Já trabalhou com a vitima? [S/N] ').upper()

perg = [p1, p2, p3, p4, p5]

if perg.count('S') <= 2:
    print('PESSOA É SUSPEITA')
elif perg.count('S') <= 4:
    print('PESSOA É CÚMPLICE')
elif perg.count('S') == 5:
    print('A PESSOA É O ASSASINO')