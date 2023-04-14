l_cnpj = list()
l_ct = list()
print("Type <enter> to leave the program")

while True:
    cnpj = input("Type the cnpj: ")
    if cnpj == "":
        break
    ct = int(input("Type the amount of employees: "))
    l_cnpj.append(cnpj)
    l_ct.append(ct)
if len(l_cnpj) > 0:
    maior_ct = max(l_ct)
    index = l_ct.index(maior_ct)
    maior_cnpj = l_cnpj[index]
    print(f"A maior empresa é a {maior_cnpj} com uma quantidade de {maior_ct} funcionários")
#lct(20,90,80,100,200,400)
#lcnpj(1000,2500,1002,500,4000,3500,\0)
