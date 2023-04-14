class Animal(object):
    def __init__(self, idade):
        self.idade = idade

    def get_idade(self):
        return self.idade

    def set_idade(self, n_idade):
        self.idade = n_idade

    def envelhecer(self):
        envelhecer = 1
        self.idade += envelhecer


class Cachorro(Animal):
    def __init__(self, idade, raca, cor_pelo):
        super().__init__(idade)
        self.raca = raca
        self.cor_pelo = cor_pelo

    def get_raca(self):
        return self.raca

    def set_raca(self, n_raca):
        self.raca = n_raca

    def get_cor_pelo(self):
        return self.cor_pelo

    def set_cor_pelo(self, n_cor):
        self.cor_pelo = n_cor

    def fase_idade(self):
        if self.idade > 0 and self.idade < 1:
            print(f"O cachorro {self.raca} é um filhote")
        elif self.idade >= 1 and self.idade <= 7:
            print(f"O cachorro {self.raca} está na fase adulta")
        elif self.idade > 7:
            print(f"O cachorro {self.raca} já é idoso")
        else:
            print(f"Idade inválida")


class Peixe(Animal):
    def __init__(self, idade, tamanho_cauda, tipo):
        super().__init__(idade)
        self.tipo = tipo
        self.tamanho_cauda = tamanho_cauda

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, n_tipo):
        self.tipo = n_tipo

    def get_tamanho_cauda(self):
        return self.tamanho_cauda

    def set_tamanho_cauda(self, n_tamanho):
        self.tamanho_cauda = n_tamanho


if __name__ == '__main__':
    a1 = Animal(4)
    c1 = Cachorro(7, "Pug", "Preto")
    p1 = Peixe(6, "Grande", "Tubarão")

    print("Animal 1:")
    print(f"\nIdade do animal 1: {a1.get_idade()}")
    a1.set_idade(8)
    print(f"Nova idade do animal 1: {a1.get_idade()}\n")

    print("Cachorro 1:")
    print(f"Idade: {c1.get_idade()}")
    print(f"Raça: {c1.get_raca()}")
    print(f"Cor do pelo: {c1.get_cor_pelo()}")
    c1.set_raca("Poodle")
    print(f"\nNova raça do cachorro: {c1.raca}")
    c1.set_cor_pelo("Branco")
    print(f"Nova cor do pelo do animal: {c1.cor_pelo}\n")

    print("Peixe 1:")
    print(f"Idade: {p1.get_idade()}")
    print(f"Tamanho da cauda: {p1.get_tamanho_cauda()}")
    print(f"Tipo do peixe: {p1.get_tipo()}")
    p1.set_tamanho_cauda("Pequena")
    p1.set_tipo("Sardinha")
    print(f"\nNovo tipo do peixe: {p1.tipo}")
    print(f"Novo tamanho da cauda do peixe: {p1.tamanho_cauda}\n")
    c1.envelhecer()
    print("Verifica fase da vida do cachorro:")
    c1.fase_idade()
    p1.envelhecer()
    print("")
    print("Verifica a idade dos animais após envelhecerem:")
    print(f"Idade do peixe 1 após envelhecer 1 ano: {p1.idade}")
    print(f"Idade do cachorro 1 após envelhecer 1 ano: {c1.idade}")


