ct_homens = 0
ct_mulheres = 0
maiora = 0
menora = 3

print("Digite (0) para sair.")
while True:
    altura = float(input("Digite a altura: "))
    if altura == 0:
        break
    if altura > maiora:
        maiora = altura
    if altura < menora:
        menora = altura
    genero = input("Selecione: \nm para masculino\nf para feminino\n")
    if genero == "m":
        ct_homens += 1
    elif genero == "f":
        ct_mulheres += 1
    else:
        print("Essa opção não existe!")


print(f"Maior = {maiora}")
print(f"Menor = {menora}")
print(f"A quantidade de homens é: {ct_homens}")
print(f"A quantidade de mulheres é: {ct_mulheres}")

