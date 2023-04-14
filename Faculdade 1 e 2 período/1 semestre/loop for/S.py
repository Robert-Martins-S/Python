s = 0
for numerador in range(1,11,2):
    denominador = numerador ** 2
    s = s + numerador / denominador
for numerador in range(2,11,2):
    denominador = numerador ** 2
    s = s - numerador / denominador
print('Valor da soma: %.2f' %s)