#função potencia que recebe dois valores inteiros, a base e o expoente, e retorna o valor da potência correspondente. A função main lê o valor da a base e do expoente, chama a função potencia passando os dois argumentos (os valores lidos) e mostra o valor retornado pela função potencia. Considere que a base pode ser um valor inteiro positivo, nulo ou negativo e o expoente, um inteiro positivo ou nulo.
#Não use o operador ** e nem a função pow da linguagem python
#definição: potência é a base multiplicada por ela mesma expoente vezes.
#base = 2, expoente = 3, potência = 8


def potencia (b, e):
    valor_potencia = 1
    for i in range(1,e+1,1):
        valor_potencia = valor_potencia * b
    return valor_potencia

if __name__ == '__main__':
    base = int(input("Valor da base: "))
    expoente = int(input("Valor do expoente: "))
    r = potencia(base,expoente)
    print(f"O resultado é: {r}")