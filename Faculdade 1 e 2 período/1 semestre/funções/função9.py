def maiuscula_minuscula(letra):
    if letra.isupper():
        retorno = letra.lower()
    else:
        retorno = letra
    return retorno

a = input("Digite uma letra: ")
print("Letra minúscula: ", maiuscula_minuscula(a))
