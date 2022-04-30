n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
média=(n1+n2)/2
if média<=5:
    print('\033[31mO aluno teve uma média de {:.1f} e foi REPROVADO\033[m'.format(média))
elif média>5 and média <=6.9:
    print('\033[33mO aluno teve uma média de {:.1f} e está de RECUPERAÇÃO\033[m'.format(média))
elif média>7:
    print('\033[34mO aluno teve uma média de {:.1f} e está APROVADO\033[m '.format(média))
