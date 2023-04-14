class Cachorro(object):
    def __init__(self, raca, cor = "preto", idade = 1):
        self.raca = raca
        self.cor = cor
        self.idade = idade

    def __str__(self):
        return f"Raça: {self.raca}\nCor: {self.cor}\nIdade: {self.idade}"

    def get_raca(self):
        return self.raca

    def set_raca(self, n_raca):
        self.raca = n_raca

    def get_cor(self):
        return self.cor

    def set_cor(self, n_cor):
        self.cor = n_cor

    def get_idade(self):
        return self.idade

    def set_idade(self, n_idade):
        self.idade = n_idade

    def fase_idade(self):
        if self.idade > 0 and self.idade < 1:
            print(f"O cachorro {self.raca} é um filhote")
        elif self.idade >= 1 and self.idade < 7:
            print(f"O cachorro {self.raca} está na fase adulta")
        elif self.idade > 7:
            print(f"O cachorro {self.raca} já é idoso")
        else:
            print(f"Idade inválida")

    def maior_idade(self):
        if self.idade > c2.idade and c3.idade:
            print(f"O cachorro mais velho é o {self.raca}")
        elif self.idade > c1.idade and c3.idade:
            print(f"O cachorro mais velho é o {self.raca}")
        elif self.idade > c1.idade and c2.idade:
            print(f"O cachorro mais velho é o {self.raca}")



if __name__ == '__main__':
    c1 = Cachorro("Poodle", "branco", 4)
    c2 = Cachorro("Labrador", "amarelo")
    c3 = Cachorro("Buldogue")

    print("\nLista dos cachorros:")
    print("-" *40)

    print("Cachorro 1:")
    print(f"Raça: {c1.get_raca()}")
    print(f"Cor: {c1.get_cor()}")
    print(f"Idade: {c1.get_idade()}")
    print("")

    c2.set_raca("Beagle")
    c2.set_idade(8)
    print("Cachorro 2:")
    print(c2)
    print("")

    print("Cachorro 3:")
    print(c3)
    print("-" *40)
    print("")

    print("-" *40)
    print("Análise da fase de vida dos cachorros:\n")
    c1.fase_idade()
    c2.fase_idade()
    c3.fase_idade()
    c2.maior_idade()
    print("-" *40)
