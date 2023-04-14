menor=999999
maior=-999999
ct=0
soma=0
print('Digite [-1] para sair')

while True:
    valor = int(input('Digite um valor: '))
    if valor == -1:
        break
    ct=ct+1
    soma=valor+soma
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print('Menor', menor)
print('Maior', maior)
print ('Quantidade', ct)
print ('Soma', soma)


