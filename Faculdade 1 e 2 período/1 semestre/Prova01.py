#Robert Martins dos Santos

#Questão 1
'''
print('O valor máximo da transação é de 3000.')


conta = int(input('Digite o número de sua conta: '))
saldo = float(input('Digite o seu saldo atual: '))
while True:
    operacao = str(input('Escolha a realização de deposito ou retirada: '))
    valor = float(input('Digite o valor da operação: '))
    if valor > 3000:
        print('Esse valor ultrapassou o limite!')
        break
    if operacao == 'deposito':
        saldo = saldo + valor
        break
    elif operacao == 'retirada':
        saldo = saldo - valor
        break
print(f'O número da conta do usuário é: {conta}')
print(f'O seu saldo atual é de {saldo}')
'''
#Questão 2
'''
print('Digite o valor [-1] para saída')
ct = 0
soma = 0
nota_maxima = 99999999
while True:
    nota = float(input('Digite o valor da nota: '))
    if nota == -1:
        break
    if nota < nota_maxima:
        nota_maxima = nota
    ct = ct + 1
    soma = soma + nota
    media = soma / ct
if ct != 0:
    print(f'A média da turma é {media}')
    print(f'Quantidade de alunos: {ct}')
    print(f'A menor nota da turma foi {nota_maxima}')
else:
    print("Não pode dividir por zero")
'''
#Questão 3
'''
peso_total = 0
ct = 0
idade_velha=0
print('Digite [-1] para sair')
while True:
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    if idade == -1:
        break
    if idade > -1:
        ct = ct + 1
        peso_total = peso_total + peso
        if idade > idade_velha:
            idade_velha = idade
print(f'A quantidade de pessoas analisadas é {ct}')
print(f'A soma de pesos é: {peso_total}kg')
print(f'A pessoa mais velha tem {idade_velha}')
'''