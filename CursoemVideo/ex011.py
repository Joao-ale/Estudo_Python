l=float(input('Qual a largura da parede: '))
a=float(input('Qual a altura da parede: '))
area=l*a
tinta=a/2
print('Uma parede de largura {} metros com a altura de {} metros tem uma area de {} m².\n E precisará de {} litros para pintar tal parede completamente.'.format(l,a,area,tinta))