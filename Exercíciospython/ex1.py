
primeiroBimestre = int(input("Primeiro Bimestre: "))
#Verifica se a nota entrada pelo usuário não ultrapassa 10
while primeiroBimestre > 10:
    primeiroBimestre = int(input("Nota inválida. Primeiro Bimestre: "))

segundoBimestre =  int(input("Segundo Bimestre: "))
while segundoBimestre > 10:
    segundoBimestre = int(input("Nota inválida. Segundo Bimestre: "))

terceiroBimestre =  int(input("Terceiro Bimestre: "))
while terceiroBimestre > 10:
    terceiroBimestre = int(input("Nota inválida. Terceiro Bimestre: "))
    
quartoBimestre =  int(input("Quarto Bimestre: "))
while quartoBimestre > 10:
    quartoBimestre = int(input("Nota inválida. Quarto Bimestre: "))

media = (primeiroBimestre + segundoBimestre + terceiroBimestre + quartoBimestre ) / 4

print("A média do aluno foi {}".format(media))