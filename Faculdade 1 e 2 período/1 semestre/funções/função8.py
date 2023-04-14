def minuscula_maiuscula(letra):
    if letra.islower():
        return letra.upper()
    else:
        return letra

entrada = input("Digite uma letra: ")
retorno = minuscula_maiuscula(entrada)
print("Valor de retorno: ", retorno)