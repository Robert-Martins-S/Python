h=0
numerador=1
n = int(input('Digite a quantidade desejada: '))
for denominador in range(1,n+1,1):
    h = h + numerador/denominador
print(f'H = %.5f' %(h))