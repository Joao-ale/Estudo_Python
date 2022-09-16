prod1 = float(input("Entre com o valor de um produto: R$"))
prod2 = float(input("Entre com o valor de outro produto: R$"))
prod3 = float(input("Entre com o valor de outro produto: R$"))

if prod1 < prod2 and prod1 < prod3:
    print("O melhor produto é primeiro de valor R${:.2f}".format(prod1))
elif prod2 < prod1 and prod2 < prod3:
    print("o melhor produto é o segundo de valor R${:.2f}".format(prod2))
else:
    print("O mellhor produto é o terceiro de valor R${:.2f}".format(prod3))
