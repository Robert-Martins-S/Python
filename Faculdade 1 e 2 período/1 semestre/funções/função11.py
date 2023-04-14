def potencia (b, e):
    vl_potencia = 1
    if e >= 1:
        for i in range(1, e + 1):
            vl_potencia = vl_potencia * b
    elif e <= 1:
        for i in range(-1, e - 1, -1):
            vl_potencia /= b
    return vl_potencia
if __name__ == '__main__':
    base = int(input("Digite aqui o valor da base: "))
    expoente = int(input("Digite aqui o valor do expoente: "))
    retorno = potencia(base, expoente)
    print("O valor da potenciação é: ", retorno)