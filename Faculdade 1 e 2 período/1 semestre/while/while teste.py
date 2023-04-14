maior_altura = 0
menor_altura = 3
ctm = 0
ctf = 0
print('Digite [0] para sair')

while True:
    altura = float(input('Digite a sua altura: '))
    if altura == 0:
        break
    genero = str(input('Selecione\n [m] para Masculino\n [f] para Feminino\n '))
    if genero == 'm':
        ctm = ctm+1
    elif genero == 'f':
        ctf = ctf+1
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
print('A maior altura é:', maior_altura)
print('A menor altura é:', menor_altura)
print('Quantidade de pessoas do gênero masculino:', ctm)
print('Quantidade de pessoas do gênero feminino:', ctf)







