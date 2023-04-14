from abc import ABC, abstractmethod

class Carro(ABC):
    def __init__(self, modelo, preco_locacao):
        self.modelo = modelo
        self.preco_locacao = preco_locacao

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, n_modelo):
        self.modelo = n_modelo

    def get_preco(self):
        return self.preco_locacao

    def set_preco(self, n_preco):
        self.preco_locacao = n_preco

    @abstractmethod
    def diaria(self):
        pass

class Economico(Carro):
    def __init__(self, modelo, preco_locacao):
        super().__init__(modelo, preco_locacao)

    def diaria(self):
        diaria = self.preco_locacao + (self.preco_locacao * (5/100))
        return diaria

class Intermediario(Carro):
    def __init__(self, modelo, preco_base):
            super().__init__(modelo, preco_base)

    def preco_diaria(self):
            valor = self.get_preco_base() * 1.1
            return valor

if __name__ == '__main__':
    carroe1 = Economico("Duster", 1000)
    carroi1 = Intermediario("Hyundai", 1500)
    print(carroe1.diaria())
    print(carroi1.diaria())
