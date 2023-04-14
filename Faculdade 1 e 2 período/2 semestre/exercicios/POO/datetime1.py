"""
1- Crie a classe Pessoa
2- Crie o método construtor: ele recebe quatro parâmetros que serão armazenados nos atributos.
  No construtor, crie os três atributos da classe (nome, peso, altura e data de nascimento)
3- No método main, crie o objeto pessoa1 e passe os argumentos.
4- Mostre o objeto criado, o objeto pessoa1, teste (rode) a classe
5- Crie os métodos get (consultar) e set (alterar) para os atributos nome e dta_nascimento.
6- No main, teste os métodos gets dos atributos da classe Pessoa (consulte e mostre)
    Mostre o atributo nome, altere o nome do objeto pessoa1 e mostre o atributo data
7- Use o método set para alterar o valor do atributo dta_nascimento para 1985-12-13. Teste
8- Crie o método IMC (Índice de Massa Corporal), ele recebe o objeto e retorna o valor do imc.
   O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
9- No programa (main), crie o objeto pessoa2 e passe os argumentos
10- Teste o item anterior, ou seja, mostre o valor dos atributos do objeto pessoa2
11- Altere o construtor para ele instanciar um objeto sem a dta_nascimento,
    valor default 2000-01-21.Ele recebe somente o nome, o peso e a altura.
12- Sobrescreva o método especial __str__ . Ele recebe o objeto e retorna os dados de uma
     pessoa (nome, peso e data de nascimento). Teste.
13- Crei o método set_nome com crítica, evitar dados inconsitentes. Teste
14- Crie o método calcula_idade, ele recebe o objeto e retorna a idade da pessoa. Teste abaixo:
  No final do main, altere a data da pessoa1 para: (2000, 11, 13). Qual a idade da pessoa1?
"""

import datetime


class Pessoa(object):
    def __init__(self, nome, peso, altura, data):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.data = data

    def get_nome(self):
        return self.nome

    def set_nome(self, n_nome):
        self.nome = n_nome

    def get_data(self):
        return self.data

    def set_data(self, n_data):
        self.data = n_data

    def imc(self):  # indíce de massa corporal peso/altura²
        vl_imc = self.peso/pow(self.altura, 2)        # pow (base, expoente) serve para elevar algum número
        return vl_imc


if __name__ == '__main__':
    data1 = datetime.date(2002, 7, 10)
    p1 = Pessoa("Robert", 71, 1.80, data1)
    print(p1)
    nome = p1.get_nome()
    print("Pessoa 1:\nNome:", nome)
    print("data de nascimento: ", p1.get_data())
    p1.set_nome("Ailton")
    print("Nome:", p1.get_nome())
    p1.set_data(datetime.date(1985, 12, 14))
    print(p1.altura)
    print(f"IMC: {p1.imc():.2f}", )