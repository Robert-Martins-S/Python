class Livro:

    def __init__(self, titulo, autor, pagina, preco = 50):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina
        self.preco = preco

    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.pagina}\nPreço: {self.preco}"

    def get_preco(self):
        return self.preco

    def set_novo_preco(self, valor):
        if valor < 0:
            print("O valor não pode ser menor que 0")
        else:
            self.preco = valor

    def get_paginas(self):
        return self.paginas

    def aumento_preco(self, valor):
        self.preco += valor

    def desconto(self,pct):
        preco = self.preco
        desconto = pct/100

        desconto_preco = preco - (desconto * preco)
        self.set_novo_preco(desconto_preco)


if __name__ == '__main__':
    l1 = Livro("O hobbit", "Tolkien", 300, 60)
    l2 = Livro("The witcher", "Andrej", 250)
    print(l1)
    print("")
    print(l2)