n = int(input('Qual número deseja ver o fatorial? '))
fat = n
print('{}! = {}'.format(n, n), end=' . ')
while n != 1:
   fat *=  (n - 1)
   n -= 1
   if n == 1:
      print('{}'.format(n), end=' ')
   else:
      print('{} . '.format(n), end=' ')
print('= {}'.format(fat))
