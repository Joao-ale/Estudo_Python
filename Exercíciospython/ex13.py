tam = int(input('Qual o tamanho do arquivo para download (Mb): '))
vel = int(input('Qual a velocidade de download (Mbps): '))
down_min = (tam / vel) / 60

print('O arquivo de {}Mb fazendo download a {}Mbps baixará completamente em {:.2f} minutos'.format(tam, vel, down_min))