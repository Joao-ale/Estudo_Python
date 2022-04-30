class Televisao:
    # Inicia os métodos
    def __init__(self):
        # cria duas váriaveis
        self.ligada = False
        self.canal = 5

    # liga e desliga tv
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    # aumenta um canal
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    # diminui um canal
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1



if __name__ == '__main__':
    # instancia a classe Televisao, assim chama televisao para acessar os métodos
    televisao = Televisao()

    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))

    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print("Canal: {}".format(televisao.canal))
