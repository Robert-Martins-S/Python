class Pessoa(object):
    def __init__(self,nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    def get_nome(self):
        return self.nome
    def set_nome(self, p_nome):
        self.nome = p_nome
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade