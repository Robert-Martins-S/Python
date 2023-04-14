maior_cnpj = ''
maior_qtd = -1
ct= 0
print('Digite [s] para finalizar')
while True:
    cnpj = input('Digite o CNPJ: ')
    if cnpj == 's':
        break
    qtd = int(input('Digite a quantidade de funcionários: '))
    if qtd > maior_qtd:
        maior_qtd = qtd
        maior_cnpj = cnpj
        ct += 1
if maior_qtd > -1:
    print('A empresa ' + maior_cnpj + ' possui o maior número de funcionários\nCom um total de:', maior_qtd)
else:
    print('Nenhum dado fornecido.')
print('Quantidade de empresas', ct)

