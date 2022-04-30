#fibonacci 2
n = int(input('Em qual número começa a sequencia: '))

c = n + (n - 1)
print(c)
a = c

while c < 500:
    c = a + n
    print(c)
    n = c
    if c > 500:
        break
    c = a + n
    print(c)
    a = c