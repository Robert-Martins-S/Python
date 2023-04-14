class Veiculo(object):
    def __init__(self, valor, modelo, km = 1):
        self.valor = valor
        self.modelo = modelo
        self.km = km

    def __str__(self):
        return f"Valor: {self.valor}\nModelo: {self.modelo}\nQuilometragem: {self.km}"

    def get_valor(self):
        return self.valor

    def set_valor(self, n_valor):
        self.valor = n_valor

    def get_modelo(self):
        return self.modelo

    def get_km(self):
        return self.km

    def atualizavalor(self, aumento):
        #Abaixo usando input, e sem fazer a crítica do tipo do valor
        #atualizavalor = float(input("Digite o valor: "))
        #if atualizavalor > 0:
        #    self.valor += atualizavalor
        #else:
        #   print("Insira um número valido!")
        if isinstance(aumento, (int, float)):
            if aumento > 0:
                self.valor += aumento
            else:
                print("Valor negativo!")
        else:
            print("Valor apenas pode ser int ou float!")

    def atualizavalorpct(self, pct):
        if pct > 0:
            self.valor += (self.valor * pct / 100)
        else:
            print("Valor negativo!")

    def verificakm(self):
        if self.km == 0:
            print("Veículo novo")
        elif self.km <= 20000:
            print("Veículo seminovo")
        else:
            print("Veículo usado")

    def verifica(self):
        tipo = self.__class__.__name__
        print(f"{tipo} do modelo {self.modelo}, valor R$ {self.valor}")
        if self.km == 0:
            print(f"{tipo} novo")
        elif self.km <= 20000:
            print(f"{tipo} seminovo")
        else:
            print(f"{tipo} usado")

    def ipvageral(self):
        tipo = self.__class__
        if tipo == Carro:
            ipva = self.valor * (3 / 100) + 100
            print(f"IPVA do {tipo.__name__} {self.modelo} é de R${ipva}")
        elif tipo == Moto:
            ipva = self.valor * (2 / 100)
            print(f"IPVA da {tipo.__name__} {self.modelo} é de R${ipva}")
        else:
            print("Veículo não indicado!")


class Carro(Veiculo):
    def __init__(self, valor, modelo, km = 1, ct_portas = 4):
        super().__init__(valor, modelo, km)
        self.ct_portas = ct_portas

    def get_ct_portas(self):
        return self.ct_portas

    def __str__(self):
        s = super().__str__()
        return s + f"\nQuantidade de portas: {self.ct_portas}"

    def set_ct_portas(self, n_portas):
        self.ct_portas = n_portas

    def carroipva(self):
        ipva = (self.valor * 3 / 100) + 100
        return ipva

class Moto(Veiculo):
    def __init__(self, valor, modelo, km = 1, cilindradas = 1300):
        super().__init__(valor, modelo, km)
        self.cilindradas = cilindradas

    def motoipva(self):
        ipva = (self.valor * 2 / 100)
        return ipva

if __name__ == '__main__':
    c1 =Carro(10000, "Duster", 30000, 5)
    c2 = Carro(5000, "Chevrolet", 0)
    c3 = Carro(8000, "Onix")
    m1 = Moto(5000, "BMW", 8000, 2000)
    m2 = Moto(6000, "Honda", 1200)
    print(c1)
    print("")
    print(m1) #Sem o str na subclasse Moto, não vai aparecer o argumneto cilindradas
    print(f"Dicionário do Carro 1: {vars(c1)}")
    print(f"Dicionário da Moto 1: {m1.__dict__}")
    c1.atualizavalor(1000)
    print(f"Novo valor do Carro 1: {c1.valor}")
    m1.atualizavalorpct(5)
    print(f"Valor da moto somado com 5% do antigo valor: {m1.valor}")
    print("")
    m2.verificakm()
    c1.verificakm()
    c2.verificakm()
    c2.verifica()
    m2.ipvageral()
    c1.ipvageral()



