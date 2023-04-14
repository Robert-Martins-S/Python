#Robert Martins dos Santos

#Questão 1
'''
print("Digite [0] para finalizar o programa.")
valort = 0
ct = 0
ctpar = 0
ctimpar = 0
while True:
    val = int(input("Digite os valores desejados: "))
    if val == 0:
        break
    if val % 2 == 0:
        ctpar += 1
    if val % 2 != 0:
        ctimpar += 1
    ct += 1
    valort = valort + val
media = valort/ct
pctimpar = ctimpar/ct*100
print(f"A média dos valores digitados é: {media:.2f}")
print(f"A quantidade de valores pares é: {ctpar}")
print(f"A porcentagem dos números ímpares é {pctimpar:.2f}%")
'''
#Questão 2
'''
n = int(input("Digite a quantidade de vezes que o for irá repetir: "))
num = list()
num2 = list()
for x in range(1,n+1):
    val = int(input("Digite o valor: "))
    num2.append(val*2)
    num.append(val)
print(f"Os valores lidos foram: {num}")
print(f"O dobro de cada valor lido respectivamente foi: {num2}")
print(f"O menor valor lido foi o: {min(num)}")
print(f"O maior valor lido foi o: {max(num)}")
'''
#Questão 3
#Elabore um programa que vai gerar uma n quantidade de números aleatórios de 0 a 100, com a n quantidade sendo escolhida pelo usuário.
'''
import random
def forrandom(x):
    lista = []
    for i in range(0,x):
        lista.append(random.randint(0,100))
    return lista

if __name__ == '__main__':
    x = int(input("Digite a quantidade de números aleatórios que vão ser gerados: "))
    print(forrandom(x))
'''