class Animal(object):                                 #Superclasse
    def __init__(self, idade = 1):
        self.idade = idade

    def get_idade(self):
        return self.idade

    def set_idade(self, n_idade):
        self.idade = n_idade

    def maior_idade(self):
        if a1.idade > a2.idade:
            print("O animal 1 é o mais velho")
        elif a2.idade > a1.idade:
            print("O animal 2 é o mais velho")


class Mamifero(Animal):                               #Subclasse
    def __init__(self, idade, cor_pelo, ct_dentes):
        super().__init__(idade)
        self.cor_pelo = cor_pelo
        self.ct_dentes = ct_dentes

    def get_cor_pelo(self):
        return self.cor_pelo

    def set_cor_pelo(self, n_cor):
        self.cor_pelo = n_cor

    def get_ct_dentes(self):
        return self.ct_dentes

    def set_ct_dentes(self, n_dentes):
        self.ct_dentes = n_dentes


if __name__ == '__main__':
    a1 = Animal(4)
    a2 = Animal(10)
    m1 = Mamifero(8, "Preto", 42)
    print("-" * 40)
    print("Animal 1:\n")
    print(f"Idade do animal 1: {a1.get_idade()}\n")
    print(f"Idade do animal 2: {a2.get_idade()}\n")
    a1.set_idade(4)
    print(f"Nova idade do animal 1: {a1.get_idade()}\n")
    a1.maior_idade()
    print("-" * 40)
    print("")
    print("-" * 40)
    print("Mamífero 1:\n")
    print(f"Idade do mamífero: {m1.get_idade()}")
    print(f"Cor do pelo do mamífero: {m1.get_cor_pelo()}")
    print(f"Quantidade de dentes do mamífero: {m1.get_ct_dentes()}\n")
    m1.set_cor_pelo("Branco")
    print(f"Nova cor do pelo do mamífero: {m1.get_cor_pelo()}")
    print("-" * 40)