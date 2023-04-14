#programa contendo as funções main, soma e subtrai.
#função main lê dois valores inteiros, chama a função soma passando os dois valores lidos e depois chama a funão subtrai passando os dois valores lidos.
#função soma recebe dois valores inteiros, realiza a soma deles e retorna o resultado do cálculo.
#função subtrai recebe dois valores inteiros, realiza a subtração deles e retorna o resultado do cálculo.
#função main recebe o valor retornado pelas funções soma e subtrai e gera a tela de saída com ssas informações.

def soma(a,b):
    somar = a + b
    return somar

def subtrai(a,b):
    subtrair = a-b
    return subtrair

if __name__ == '__main__':
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))
    retorno_soma = soma(valor1,valor2)
    print("A soma é: ", retorno_soma)
    print("A subtração é: ", subtrai(valor1,valor2))