class Livro:

    def __init__(self, titulo, autores, pagina, preco = 50):
        self.titulo = titulo
        self.autores = autores
        self.pagina = pagina
        self.preco = preco

    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor(es): {self.autores}\nPáginas: {self.pagina}\nPreço: {self.preco}"

    def get_autores(self):
        return self.autores

    def set_autores(self, novos_autores):
        if isinstance(novos_autores, list) and len(novos_autores) > 0:
            self.autores = novos_autores
        else:
            print("Autor inválido")

    def mostra_autores(self):
        ct = 1
        print("Autores:")
        for autor in self.autores:
            print(f"[{ct}] {autor}")
            ct += 1

    def get_preco(self):
        return self.preco

    def set_novo_preco(self, valor):
        if valor < 0:
            print("O valor não pode ser menor que 0")
        else:
            self.preco = valor

    def get_paginas(self):
        return self.pagina

    def aumento_preco(self, valor):
        self.preco += valor

    def desconto(self,pct):
        preco = self.preco
        desconto = pct/100

        desconto_preco = preco - (desconto * preco)
        self.set_novo_preco(desconto_preco)

    def add_autor(self, novo_autor):
        self.autores.append(novo_autor)

    def remove_autor(self, remove_autor):
        if remove_autor in self.autores:
            self.autores.remove(remove_autor)
        else:
            print("Autor não encontrado")

    def search_autor(self, autor_encontra):
        ct = 1
        for autor in self.autores:
            if autor == autor_encontra:
                print(f"O autor {autor_encontra} está no index [{ct}]")
            else:
                print("Esse autor não está na lista")
            ct += 1

    def atualiza_autor(self):
        self.mostra_autores()

if __name__ == '__main__':
    l1 = Livro("O hobbit", "Tolkien", 300, 60)
    l2 = Livro("The witcher", "Andrej", 250)
    l3 = Livro("Senhor dos Anéis", ["Tolkien", "Andrej"], 1000)
    print(l1)
    print("")
    print(l2)
    print("")
    print(l3)
    l3.set_autores(["Robert", "João"])
    print(f"Novos autores: {l3.get_autores()}")
    l3.add_autor("Carlos")
    l3.remove_autor("Carlos")
    l3.mostra_autores()
    l3.search_autor("Robert")
    l3.atualiza_autor()