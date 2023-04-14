"""
1- Crie um novo projeto e a classe Point.
2- Crie o método construtor, ele atribui o valor default zero para os parâmetros de x e y
3- No construtor, crie os atributos x e y.
4- Na função main, crie o objeto p1 (ponto p1) sem passar argumentos. Teste
5- Crie os métodos gets e sets.
6- Mostre o valor do atributo x e y.
7- Faça pelo menos uma crítica no método set_x, teste
"""

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self,valor):
        if type(valor) in (int, float):
            self.x = valor
        else:
            print("Erro: tipo tem que ser int ou float")

    def get_y(self):
        return self.y

    def __str__(self):
        s = f"({self.x}, {self.y})"
        return s

if __name__ == '__main__':
    p1 = Point()
    print("objeto p1 da classe pint", p1)
    print("objeto p1 da classe point", p1.__str__)
    print("atributo x do ponto p1", p1.get_x())
    print("atributo y do ponto p1", p1.get_y())
    p1.set_x(2)
    print("atributo x do ponto p1", p1.get_x())
    p1.set_x("mensagem")
    print("atributo x do ponto p1", p1.get_x())
    p2 = Point(2, 3)
    print("objeto p2 da classe point", p2)