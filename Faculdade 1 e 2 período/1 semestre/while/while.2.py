soma = 0
ct = 0
print("Digite [0] para sair")
while True:
    valor = int(input('Digite um número:'))
    if valor == 0:
        break
    resto = valor % 2
    if resto == 0:
        soma = soma+valor
        ct = ct+1
        media = soma / ct
print('Média', media)





