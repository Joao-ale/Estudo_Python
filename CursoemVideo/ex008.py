d=int(input('Uma distância em metros: '))
cm=d*100
mm=d*1000
km=d/1000
hm=d/100
dam=d*10
print('''A distância de {} metros vale:
{} quilômetros;
{} hectômetros;
{} decimetros;
{} centímetros;
{} milimetros.'''.format(d,km,hm,dam,cm,mm))
