class Moto:
    def __init__(self, marca, modelo, cor, marcha, ligada):
        self.marca = marca
        print('Sua moto é da marca:', self.marca)
        self.modelo = modelo
        print('Modelo:', self.modelo)
        self.cor = cor
        print('Cor:', self.cor)
        self.marcha = marcha
        print('A moto está na marcha:', self.marcha)
        self.ligada = ligada
        print('A moto está ligada?', self.ligada)

    def imprimir(self):
        print(self.marca, self.modelo, self.cor, self.marcha, self.ligada)


moto_marca = input('Marca da moto: ')
moto_modelo = input('Modelo da moto: ')
moto_cor = input('Cor da moto: ')
moto_marcha = input('Marcha que a moto está: ')
moto_ligada = input('A moto está ligada?: ')

m1 = Moto(moto_marca, moto_modelo, moto_cor, moto_marcha, moto_ligada)
m1.imprimir()
