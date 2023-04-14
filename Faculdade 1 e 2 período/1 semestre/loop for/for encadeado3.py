produto = 1
n = int(input("Digite a quantidade que você quer multiplicar: "))
for i in range(1,n+1):
    valor_lido = int(input("Digite um valor: "))
    produto = produto * valor_lido
print("O produto de todos os valores digitados é: ")