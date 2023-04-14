l_altura = []
l_genero = list()
print("Digite (0) para sair")
while True:
    altura = float(input("Digite a altura: "))
    if altura == 0:
        break
    l_altura.append(altura)
    genero = str(input("Selecione\n (m) para masculino\n (f) para feminino\n"))
    l_genero.append(genero)
# fim do while
maior_altura = max(l_altura)
menor_altura = min(l_altura)
print("Maior altura no grupo:",maior_altura)
print("Menor altura no grupo:",menor_altura)
print("Quantidade de homens:",l_genero.count('m'))
print("Quantidade de mulheres:",l_genero.count('f'))
