class Produto(object):
    def __init__(self,nome, vl_compra, vl_venda, ct_estoque, ct_minima):
        self.nome = nome
        self.vl_compra = vl_compra
        self.vl_venda = vl_venda
        self.ct_estoque = ct_estoque
        self.ct_minima = ct_minima

    def __str__(self):
        return f"Nome: {self.nome} \nValor das compras: {self.vl_compra}\nValor das vendas: {self.vl_venda}\n" \
               f"Quantidade em estoque: {self.ct_estoque}\nQuantidade minima: {self.ct_minima}"

    def get_nome(self):
        return self.nome
    def set_nome(self,nvnome):
        self.nome = nvnome
    def get_vl_compra(self):
        return self.vl_compra
    def set_vl_compra(self,nvvl_compra):
        self.vl_compra = nvvl_compra




if __name__ == '__main__':
    p1 = Produto("Arroz", 15.00, 19.50, 67, 20)
    print(p1)
