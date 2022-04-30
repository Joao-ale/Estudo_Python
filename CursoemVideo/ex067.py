from time import sleep
while True:
    print('-'*30)
    tabuada = int(input('Quer ver qual tabuada? '))
    print('-'*30)
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada:2} X {c:2} = {c*tabuada:2}')
    sleep(1.5)
print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO VOLTE SEMPRE!')
