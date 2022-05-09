tamanho = int(input("Qual o tamanho do arquivo para download (Mb): "))
velocidade = int(input("Qual a velocidade de download (Mbps): "))

download_min = (tamanho / velocidade) / 60

print(
    "O arquivo de {} Mb fazendo download a {} Mbps baixará completamente em {:.2f} minutos".format(
        tamanho, velocidade, download_min
    )
)
