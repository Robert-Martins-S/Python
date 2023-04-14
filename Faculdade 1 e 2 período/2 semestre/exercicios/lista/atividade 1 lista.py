l_altura = list()
l_genero = list()
print("Digite (0) para sair")
while True:
    altura = float(input("Digite a altura: "))
    if altura == 0:
        break
    l_altura.append(altura)
    genero = input("Selecione: \nm para masculino\nf para feminino\n")
    l_genero.append(genero)

print(f"Maior: {max(l_altura)}")
print(f"Menor: {min(l_altura)}")
print(f"Quantidade de homens: {l_genero.count('m')}")
print(f"Quantidade de mulheres: {l_genero.count('f')}")