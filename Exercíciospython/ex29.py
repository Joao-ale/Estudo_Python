
ano = int(input('Entre com um ano: '))

bisses = ano % 4
bis100 = ano % 100
bis400 = ano % 400

if bisses == 0:
    if bis100 != 0:
            print('O ano {} é bissexto!'.format(ano))
    else:
        if bis400 == 0:
            print('O ano {} é bissexto!'.format(ano))
        else:
            print('O ano {} não é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))