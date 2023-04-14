class Refrigerante(object):
    def __init__(self, marca, validade):
        self.marca = marca
        self.validade = validade

    def __str__(self):
        return f"Marca: {self.marca} \nValidade: {self.validade} dias"

    def get_marca(self):
        return self.marca

    def set_marca(self, nova_marca):
        self.marca = nova_marca

    def get_validade(self):
        return self.validade

    def set_validade(self, nova_validade):
        self.validade = nova_validade

    def tempo_validade(self):
        if self.validade <= 0:
            print("[Produto vencido!]")
        elif self.validade > 0:
            print("[Produto está na validade!]")

    """
    def mostrar_dados(self):
        print(f"Marca do produto: {self.get_marca()}")
        print(f"Tempo para a bebida ficar vencida: {self.get_validade()} dias\n")
    """


if __name__ == '__main__':
    r1 = Refrigerante("Guaraná", 10)
    r2 = Refrigerante("Sprite", 14)

    print("\nPrimeiro refrigerante")
    #r1.mostrar_dados()
    print(r1.get_marca())
    print(r1.get_validade())
    print("")
    print("Segundo refrigerante")
    print(r2.get_marca())
    print(r2.get_validade())
    #r2.mostrar_dados()

    r1.set_marca("Coca Cola")
    r1.set_validade(0)
    r2.set_marca("Pepsi")
    r2.set_validade(4)

    print("\nPrimeiro refrigerante")
    print(r1)
    r1.tempo_validade()
    print("")
    print("Segundo refrigerante")
    print(r2)

    r2.tempo_validade()
