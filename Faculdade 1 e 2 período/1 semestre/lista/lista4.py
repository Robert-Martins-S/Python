l_cnpj = list()
l_qtd = list()
print('Digite <enter> para sair')
while True:
    cnpj = input("CNPJ: ")
    if cnpj == '':
        break
    qtd = int(input("Quantidade de funcionários: "))
    l_cnpj.append(cnpj)
    l_qtd.append(qtd)
if len(l_cnpj) > 0:
    maior_qtd = max(l_qtd)
    indice = l_qtd.index(maior_qtd)
    maior_empresa = l_cnpj[indice]
    print("A empresa " + maior_empresa + "quantidade de funcionários com um total de ", maior_qtd)
else:
    print("Nenhuma empresa válida recebida")