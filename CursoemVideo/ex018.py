import math
ang=float(input('Digite um ângulo: '))
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tan=math.tan(math.radians(ang))
print('O ângulo {:.2f} tem como SENNO {:.2f}'.format(ang,sen))
print('O ângulp {:.2f} tem como COSENNO {:.2f}'.format(ang,cos))
print('O ângulo {:.2f} tem como TANGENTE {:.2f}'.format(ang,tan))