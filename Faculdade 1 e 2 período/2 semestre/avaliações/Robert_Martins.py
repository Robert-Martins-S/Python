#Robert Martins dos Santos
#RA:22108154

"""
Questão 1:

class Empregado(object):
    def __init__(self, nome, idade = 16, salario = 1200):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.idade}\nIdade: {self.idade}\nSalário mensal: {self.salario}"

    def get_nome(self):
        return self.nome

    def set_nome(self, n_nome):
        self.nome = n_nome

    def get_idade(self):
        return self.idade

    def set_idade(self, n_idade):
        if n_idade > 0:
            self.idade = n_idade
        else:
            print("Essa idade é inválida!")

    def get_salario(self):
        return self.salario

    def set_salario(self, n_salario):
        self.salario = n_salario

    def aumentopct(self, pct):
        aumento = (pct/100) * self.salario
        self.salario = self.salario + aumento

    # Crie um método funcional dentro da classe Empregado que reduza o salário do empregado, de acordo com uma porcentagem que seja inserida
    # pelo usuário

    def reducaosalario(self):
        pct = int(input("Digite a porcentagem que será usada para a redução salárial do empregado: "))
        reducao = (pct/100) * self.salario
        self.salario = self.salario - reducao


if __name__ == '__main__':
    e1 = Empregado("João")
    e2 = Empregado("Carlos", 25)
    e3 = Empregado("Ricardo", salario=1600)
    print("Empregado 1:")
    print(f"Nome: {e1.get_nome()}")
    print(f"Idade: {e1.get_idade()}")
    print(f"Salário mensal: {e1.get_salario()}")
    salarioanual = e1.salario * 12
    print(f"Salário anual do Empregado 1: {salarioanual}\n")
    print("Empregado 2:")
    print(e2)
    e2.aumentopct(10)
    print(f"Salário mensal do Empregado 2 após o aumento de 10%: {e2.get_salario()}")
    print("")
    print("Empregado 3:")
    print(e3)
    e3.set_idade(17)
    print(f"Nova idade do Empregado 3 é: {e3.get_idade()}")
    e3.reducaosalario()
    print(f"Com a redução do salário, o empregado 3 ficou com um salário de: {e3.salario}")
"""

"""
Questão 2:

class Pessoa(object):
    qtd_funcionario = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.qtd_funcionario = Pessoa.qtd_funcionario + 1

    def get_nome(self):
        return self.nome

    def set_nome(self, n_nome):
        self.nome = n_nome

    @classmethod
    def cadastro(cls):
        return Pessoa.qtd_funcionario

class Professor(Pessoa):
    def __init__(self, nome, qtd_turma = 1):
        super().__init__(nome)
        self.qtd_turma = qtd_turma

    def get_qtd_turma(self):
        return self.qtd_turma

    def set_qtd_turma(self, n_qtd):
        if self.qtd_turma > 0:
            self.qtd_turma = n_qtd
        else:
            print("Esse professor não tem nenhuma turma!")

    def rendimentos(self):
        valor_turma = 300
        valor = self.qtd_turma * valor_turma
        return print(f"O professor {self.nome} recebe: R${valor}")


class Funcionario(Pessoa):
    def __init__(self, nome, salario = 1200.0):
        super().__init__(nome)
        self.salario = salario

    def get_salario(self):
        return self.salario

    def set_salario(self, n_salario):
        if self.salario > 0:
            self.salario = n_salario
        else:
            print("Esse Funcionário não está recebendo um salário!")


if __name__ == '__main__':
    p1 = Professor("José", 4)
    f1 = Funcionario("Fernanda")
    f2 = Funcionario("Henrique", 1800)
    print("Professor 1:")
    print(f"Nome do professor: {p1.nome}")
    print(f"Quantidade de turmas que o professor leciona: {p1.get_qtd_turma()}\n")
    print("Funcionário 1:")
    print(f"Nome do funcionário: {f1.get_nome()}")
    print(f"Salário mensal do funcinario: {f1.get_salario()}")
    f1.set_salario(1400)
    print(f"Novo salário do funcionário 1: {f1.get_salario()}\n")
    p1.rendimentos()
    print(f"A quantidade de pessoas cadastradas no sistema é de {Pessoa.qtd_funcionario} pessoas")
"""
