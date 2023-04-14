class Pessoa:
    ct = 0
    lista = []

    def __init__(self, nome):
        self.nome = nome
        Pessoa.ct += 1
        Pessoa.lista.append(self.nome)

    def __str__(self):
        return f"O nome da pessoa é {self.get_nome()}"

    @classmethod
    def get_ct(cls):
        return Pessoa.ct

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if type(novo_nome) == str:
            self.nome = novo_nome
        else:
            print("Esse não é um nome válido.")


class Professor(Pessoa):
    def __init__(self, nome, ct_turma = 1):
        super().__init__(nome)
        self.ct_turma = ct_turma

    def __str__(self):
        str = super().__str__()
        return f"{str} e a quantidade de turmas do {self.__class__.__name__} {self.nome} é de {self.get_ct_turma()} turmas"

    def get_ct_turma(self):
        return self.ct_turma

    def set_ct_turma(self, novo_ct_turma):
        if novo_ct_turma > 0:
            self.ct_turma = novo_ct_turma
        else:
            print("Quantidade de turmas inválida")

    def rendimentos(self, valor):
        rendimento = valor * self.ct_turma
        return print(f"O rendimento do professor {self.nome} é de {rendimento}R$")


class Funcionario(Pessoa):
    def __init__(self, nome, salario = 1200.0):
        super().__init__(nome)
        self.salario = float(salario)

    def __str__(self):
        str = super().__str__()
        return str + f" e o salário do funcionário {self.nome} é de {self.get_salario()}R$"

    def get_salario(self):
        return self.salario

    def set_salario(self, novo_salario):
        if novo_salario < 0:
            print("Valor do salário inválido")
        else:
            self.salario = novo_salario


if __name__ == '__main__':

    print(Pessoa.get_ct())

    pessoa1 = Pessoa("Ricardo")
    professor1 = Professor("José", 5)
    professor2 = Professor("Joaquim")
    funcionario1 = Funcionario("Aldaberto", 1000)
    print("Lista de Pessoas:\n")
    print(pessoa1)
    print(professor1)
    print(funcionario1)
    professor1.rendimentos(200)
    funcionario1.set_salario(2000)
    print(f"Novo salário do funcionário é de {funcionario1.get_salario()}R$")
    print(professor2)
    print(Pessoa.ct)
    print(Pessoa.lista)
