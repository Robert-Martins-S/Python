#Robert Martins dos Santos
#RA:22108154
"""
1. Resolva estes itens com funções de lista:
a. Crie uma lista vazia e acrescente alguns valores numéricos usando pelo menos dois métodos diferentes.
b. Leia um valor e verifique se ele está na lista. Se estiver, mostre também a posição (índice) do valor encontrado na pesquisa;
c. Mostre a lista na ordem crescente.
d. Insira (acrescente) o valor 55 na posição (índice) 1 da lista.
e. Mostre a lista na ordem decrescente.
f. Elabore o enunciado e a implementação de mais uma questão na lista criada. A complexidade do enunciado e da implementação da questão serão considerados para mensurar a avaliação da questão. Não faça exercício igual aos ministrados nas aulas.
- Vale 40%

#a)

lista_vazia = list()
lista_vazia.append(10)
lista_vazia.insert(0, 50)
print(f"Lista em ordem normal: {lista_vazia}")
#b)

valor = int(input("Digite o valor que você quer ver a posição: "))
if valor in lista_vazia:
    print(f"O valor que você digitou está na posição: {lista_vazia.index(valor)}")
else:
    print("O valor digitado não está na lista!")

#c)

lista_vazia.sort()
print(f"Lista em ordem crescente: {lista_vazia}")

#d)

lista_vazia.insert(1, 55)
print(f"Lista com o valor 55 adicionado no index 1: {lista_vazia}")

#e)

lista_vazia.sort(reverse=True)
print(f"Lista em ordem decrescente: {lista_vazia}")

#f)


Faça um programa em que o usuário irá digitar um número o seu respectivo index que será adicionado em uma lista já criada, e
depois verifique se o número que foi adicionado realmente está dentro da lista, imprimindo uma mensagem dizendo se o número
está dentro da lista, ou se não está. E depois some os valores dentro dessa lista após as mudanças que você fez e imprima a soma.


num = int(input("Digite o número que será adicionado: "))
index = int(input("Digite o index em que esse número vai estar posicionado: "))
lista_vazia.insert(index, num)
verifica = int(input("Digite o número que você quer verificar se está na lista: "))
if verifica in lista_vazia:
    print("O valor digitado está dentro da lista!")
else:
    print("O valor digitado não está dentro da lista!")
soma = sum(lista_vazia)
print(f"A soma da lista após o número adicionado é: {soma}")
"""

"""
2. Crie a classe conta corrente com as características titular, número da conta , saldo. 
   Crie o método construtor recebendo self e os três parâmetros, coloque pelo menos um desses parâmetros com valor default (padrão).
   Crie pelo menos um método get e pelo menos um método set e faça crítica no método set.
   Crie o método funcional depósito, ele recebe um valor que será depositado na conta corrente, faça crítica.

   No método main, instancie dois objetos dessa classe. Crie o objeto conta1 passando os rgtrês aumentos e o 
   crie o objeto conta2 passando apenas dois argumentos. Use (teste) todos os método criados na classe para os objetos conta1 e conta2.

Elabore o enunciado e a implementação de mais um método funcional na classe ContaCorrente. 
A complexidade do enunciado e da implementação do método serão considerados para mensurar a avaliação do método.
Obs.: este método deve ser diferente dos métodos vistos nos exemplos usados nas aulas.
- Vale 60%


class Conta_corrente(object):
    def __init__(self, titular, numconta, saldo = 2000):
        self.titular = titular
        self.numconta = numconta
        self.saldo = saldo

    def __str__(self):
        return f"Nome do titular: {self.titular}\nNúmero da conta: {self.numconta}\nSaldo disponível: {self.saldo}"

    def get_titular(self):
        return self.titular

    def set_titular(self, novo_titular):
        self.titular = novo_titular

    def get_numconta(self):
        return self.numconta

    def set_numconta(self, novo_numconta):
        self.numconta = novo_numconta

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo
        if novo_saldo < 0:
            print("O saldo é negativo!")

    def deposito(self,valor):
        if valor > 20000:
            print("Você atingiu o máximo de deposito permitido!")
        elif valor <= 0:
            print("Esse valor não é válido!")
        else:
            self.saldo = self.saldo + valor
            print(f"Depósito realizado com sucesso!\n")

    def extrato(self):
        print(f"O seu extrato atual é de: {self.saldo}")


if __name__ == '__main__':
    conta1 = Conta_corrente("Robert", 1, 800)
    conta2 = Conta_corrente("Carlos", 2)

    print("Conta 1:")
    print(conta1)
    print("\nConta 2:")
    print(conta2)

    print("")

    conta1.deposito(200)
    conta2.deposito(20001)

    print("")

    conta1.extrato()
    conta2.extrato()
"""
