tab = int(input('Qual tabuada você deseja? '))
print('tabuada do {}:'.format(tab))
print('-' * 14)
for x in range(1, 11):
    multi = tab * x
    print('{} X {} = {}'.format(tab, x, multi))
    print('-' * 14)