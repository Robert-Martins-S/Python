maior_cnpj = ""
ct_maior = 0
print("Tecle <enter> para sair")

while True:
    cnpj = input("Digite o cnpj: ")
    if cnpj == '':
        break
    ct = int(input("Digite a quantidade de funcionários da empresa: "))
    if ct > ct_maior:
        ct_maior = ct
        maior_cnpj = cnpj


print(f"A maior empresa é a {maior_cnpj}, com uma quantidade de {ct_maior} funcionários.")