def maximo(num1,num2):
    if num2 > num1:
        maior = num2
    else:
        maior = num1
    return maior

if __name__ == '__main__':
    numero1=int(input("Primeiro número: "))
    numero2=int(input("Segundo número: "))
    vl_retorno=maximo(numero1,numero2)
    print("O maior é", vl_retorno)