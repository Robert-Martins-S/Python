class Funcionario(object):
    def __init__(self, cpf, nome, salario = 0.0):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario

    def __str__(self):
        s = f"CPF: {self.cpf}\nNome: {self.nome}\nSalário: {self.salario}"
        return s

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, n_cpf):
        self.cpf = n_cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, n_nome):
        self.nome = n_nome

    def set_salario(self, n_salario):
        self.salario = n_salario

class Gerente(object):
    def __init__(self, cpf, nome, salario, senha, ct_gerencia = 0):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario
        self.senha = senha
        self.ct_gerencia = ct_gerencia

    def get_cpf(self):
        return self.cpf

    def set_salario(self, n_salario):
        self.salario = n_salario

    def get_senha(self):
        return self.senha

    def autentica(self):
        senha = input("Digite a sua senha: ")
        if senha == self.senha:
            print("Acesso permitido!")
            return True
        else:
            print("Acesso negado!")
            return False

if __name__ == '__main__':
    f1 = Funcionario("123.456.789-22", "João", 1200)
    f2 = Funcionario("444.444.444-22", "Carlos")
    g1 = Gerente("083.161.883-33", "Robert", 3000, "123", 2)

    print("Funcionário 1:\n")
    print(f1)
    print("")
    print("Funcionário 2:\n")
    print(f"CPF: {f2.get_cpf()}")
    print(f"Nome: {f2.get_nome()}")
    print(f"Salário: {f2.salario}\n")

    print("Gerente 1:\n")
    #print(g1)    //Não foi possível usar o metódo str,pois não estava na classe Gerente
    print(f"CPF: {g1.get_cpf()}")
    print(f"Nome: {g1.nome}")
    print(f"Salário: {g1.salario}")
    print(f"Senha: {g1.get_senha()}")
    print(f"Quantidade que gerencia: {g1.ct_gerencia}\n")

    g1.autentica()
    #f1.autentica() //Não foi possível usar o metódo autentica, pois não estava na classe Funcionário

    g2 = Gerente("231.444.780-44", "Marlon", 3000, "999", 4)
