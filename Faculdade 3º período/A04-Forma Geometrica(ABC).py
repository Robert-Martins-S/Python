from abc import ABC, abstractmethod
import math

pi = math.pi


class FormaGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def texto(self):
        print(f"O objeto usado foi o : {self.__class__.__name__}")


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, n_lado):
        self.lado = n_lado

    def area(self):
        area = self.lado * self.lado
        return area

    def perimetro(self):
        perimetro = self.lado * 4
        return perimetro

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def get_raio(self):
        return self.raio

    def set_raio(self, n_raio):
        self.raio = n_raio

    def area(self):
        area = pi * (self.raio * self.raio) # ou pi * (self.raio ** 2)
        return area

    def perimetro(self):
        perimetro = 2*pi * self.raio
        return perimetro

if __name__ == '__main__':
    q1 = Quadrado(6)
    c1 = Circulo(4)
    print("Quadrado:\n")
    print(f"Lado = {q1.get_lado()}")
    print(f"Área = {q1.area()}")
    print(f"Perímetro = {q1.perimetro()}\n")
    print("Circulo:\n")
    print(f"Raio = {c1.get_raio()}")
    print(f"Área = {c1.area():.2f}")
    print(f"Perímetro = {c1.perimetro():.2f}")
    print("")
    q1.texto()
    c1.texto()