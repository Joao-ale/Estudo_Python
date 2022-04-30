dia = int(input('Entre com um dia: '))
mes = int(input('Entre com um mês: '))
ano = int(input('Entre com um ano: '))

bisses = ano % 4
bis100 = ano % 100
bis400 = ano % 400

mes31 = [1, 3, 5, 7, 8, 10, 12]
mes30 = [4, 6, 9, 11]

if mes in mes31:
    if dia > 31:
        print('DATA INVÁLIDA!')
    else:
        print('A data digitada foi {}/{}/{} e é válida'.format(dia, mes, ano))
if mes in mes30:
    if dia > 30:
        print('DATA INVÁLIDA!')
    else:
        print('A data digitada foi {}/{}/{} e é válida'.format(dia, mes, ano))
elif mes == 2:
    if bisses == 0:
        if bis100 != 0:
            if dia > 29:
                print('DATA INVÁLIDA!')
            else:
                print('A data digitada foi {}/{}/{} e é válida e o ano foi bissexto'.format(dia, mes, ano))
        else:
            if bis400 == 0:
                if dia > 29:
                    print('DATA INVÁLIDA!')
                else:
                    print('A data digitada foi {}/{}/{} e é válida e o ano foi bissexto'.format(dia, mes, ano))
            else:
                if dia > 28:
                    print('DATA INVÁLIDA!')
                else:
                    print('A data digitada foi {}/{}/{} e é válida'.format(dia, mes, ano))
else:
    print('DATA INVÁLIDA!')