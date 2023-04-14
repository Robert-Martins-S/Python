from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, idade):
        self.idade = idade

    def get_idade(self):
        return self.idade

    @abstractmethod
    def movimenta(self):
        pass

class Cachorro(Animal):
    def __init__(self, idade, cor_pelo, raca):
        self.cor = cor_pelo
        self.raca = raca
        super().__init__(idade)

    def get_cor(self):
        return self.cor

    def set_cor(self, n_cor):
        self.cor = n_cor

    def get_raca(self):
        return self.raca

    def set_raca(self, n_raca):
        self.raca = n_raca

    def movimenta(self):
        andar = 0
        correr = andar + 2
        print(f"O cachorro está correndo {correr} vezes mais rápido")


class Peixe(Animal):
    def __init__(self, idade, tamanho_cauda):
        self.cauda = tamanho_cauda
        super().__init__(idade)

    def get_cauda(self):
        return self.cauda

    def set_cauda(self, n_cauda):
        self.cauda = n_cauda

    def movimenta(self):
        nadar = 0
        nadar_rapido = nadar + 3
        print(f"O peixe está nadando {nadar_rapido} vezes mais rápido")

if __name__ == '__main__':
    #animal1 = Animal(4)
    cachorro1 = Cachorro(6, "branco", "Poodle")
    peixe1 = Peixe(3, "Média")

    print("Mamíferos:")
    print(f"Idade: {cachorro1.get_idade()}")
    print(f"Cor: {cachorro1.get_cor()}")
    print(f"Raça: {cachorro1.get_raca()}")
    cachorro1.set_cor("preto")
    cachorro1.set_raca("Labrador")
    print(f"Nova raça do cachorro: {cachorro1.get_raca()}"
          f"\nNova cor: {cachorro1.get_cor()}")
    cachorro1.movimenta()

    print("\nPeixes:")
    print(f"Idade: {peixe1.get_idade()}")
    print(f"Tamanho da cauda: {peixe1.get_cauda()}")
    peixe1.set_cauda("Pequena")
    print(f"Novo tamanho da cauda do peixe: {peixe1.get_cauda()}")
    peixe1.movimenta()
