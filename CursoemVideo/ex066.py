n = s = c = 0
while True:#Faz algo infinitamente até chegar no comando break que faz sair do while
    n = int(input('Digite um número (999 fa parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} valores e a soma deles é igual a {s}')
