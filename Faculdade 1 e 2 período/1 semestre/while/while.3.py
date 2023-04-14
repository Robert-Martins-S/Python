soma_par = 0
soma_impar = 0
ct_par = 0
ct_impar = 0
print("Digite o [ -1 ] para sair")
while True:
    valor = int(input("Digite um número: "))
    if valor == -1:
        break
    if valor % 2 == 0:
        soma_par = soma_par + valor
        ct_par = ct_par + 1
    else:
        soma_impar = soma_impar + valor
        ct_impar = ct_impar + 1
if ct_par != 0:
    media_par = soma_par / ct_par
    print(f"Média dos pares: %.2f" %(media_par))
else:
    print("Não tem número par")
if ct_impar != 0:
    media_impar = soma_impar / ct_impar
    print("Média dos ímpares: %.2f" %(media_impar))
else:
    print("Não tem número ímpar")