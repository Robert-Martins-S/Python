def valor_absoluto (a):
    if a < 0:
        r = -a          # r = -1 * a
    else:
        r = a
    return r


if __name__ == '__main__':
    valor= float(input("Digite o valor que vai se tornar absoluto: "))
    v_retorno = valor_absoluto(valor)
    print("Valor absoluto: ", v_retorno)