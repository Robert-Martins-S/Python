lista = list()
while True:
    valor = int(input("Digite um valor: "))
    if valor == -1:
        break
    lista.append(valor) #Armazena o valor na lista
    #Fim da repetição (while)
menor = min(lista)       #Solução 1
maior = max(lista)
# lista.sort()           #Solução 2
# 5 3 10         -valores digitados
# 0 1 2          -posições positivas
# -3 -2 -1       -posições negativas
# 3 5 10         -ordenado
# menor = lista[0]
# maior = lista[-1]
print("Menor:", menor)
print("Maior", maior)