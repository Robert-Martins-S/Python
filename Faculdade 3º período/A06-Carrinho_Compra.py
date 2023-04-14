#from datetime import datetime
#Carrinho de Compra
#Produto
#Cliente
class Cliente(object):
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def __str__(self):
        return f"Cpf do cliente: {self.cpf}\nNome do cliente: {self.nome}"

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, n_cpf):
        self.cpf = n_cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, n_nome):
        self.nome = n_nome

class CarrinhoCompra(object):
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.produtos = list()

    def __str__(self):
        return f"Número do pedido: {self.get_numero()}\nCliente: {self.get_cliente()}"

    def get_numero(self):
        return self.numero

    def set_numero(self, n_numero):
        self.numero = n_numero

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, n_cliente):
        self.cliente = n_cliente

    def get_produtos(self):
        return self.produtos

    def set_produtos(self, n_produtos):
        self.produtos = n_produtos

    def mostra_carrinho(self):
        if len(self.produtos) < 1:
            print("Carrinho vazio")
        else:
            print("Mostra carrinho:")
            for o_produto in self.produtos:
                print(f"Descrição:{o_produto.get_nome()}")
            print(f"Quantidade de produtos:{len(self.produtos)}")

    def insere_produto(self, o_produto):
        self.produtos.append(o_produto)

class Produto(object):
    def __init__(self, identificador, nome, preco, quantidade = 1):
        self.identificador = identificador
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Identificador do produto: {self.get_identificador()}\nNome: {self.get_nome()}\nPreço: {self.get_preco()}\nQuantidade: {self.get_quantidade()}"

    def get_identificador(self):
        return self.identificador

    def set_identificador(self, n_identificador):
        self.identificador = n_identificador

    def get_nome(self):
        return self.nome

    def set_nome(self, n_nome):
        self.nome = n_nome

    def get_preco(self):
        return self.preco

    def set_preco(self, n_preco):
        self.preco = n_preco

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, n_quantidade):
        self.quantidade = n_quantidade

if __name__ == '__main__':
    cliente1 = Cliente("921.000.332-55", "Carlos")
    carrinho1 = CarrinhoCompra(1, cliente1.nome)
    produto1 = Produto(1, "Leite", 40.0)
    produto2 = Produto(2,"Pipoca", 20.0)
    print(cliente1)
    carrinho1.insere_produto(produto1)
    carrinho1.insere_produto(produto2)
    carrinho1.mostra_carrinho()
    print(carrinho1)