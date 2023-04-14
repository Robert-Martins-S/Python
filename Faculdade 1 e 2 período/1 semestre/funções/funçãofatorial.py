def fatorial(n):
    resultado = 1
    for x in range(1,n+1,1):
        resultado = resultado * x
    return resultado


if __name__ == '__main__':
    valor = int(input("Digite um valor: "))
    retorno = fatorial(valor)
    print(f"{valor}! = {retorno}")
