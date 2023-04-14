somador = 0
inicial = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))
if inicial < final:
    for x in range(inicial, final+1,1):
        print(x)
        somador = somador + x
else:
    for x in range(inicial, final-1, -1):
        print(x)
