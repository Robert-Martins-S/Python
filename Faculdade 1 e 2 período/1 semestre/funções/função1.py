def soma_valores(a,b):
    valor = a + b
    return valor

if __name__ == '__main__':
    valor1 = int(input("Primeiro valor: "))
    valor2 = int(input("Segundo valor: "))
    v_retorno = soma_valores(valor1,valor2)
    print("Soma = ", v_retorno)