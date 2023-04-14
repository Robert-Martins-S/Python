l_voto = []
while True:
    voto = int(input("1 para candidato 1\n2 para candidato 2\n3 para candidato 3"
                     "\n5 para voto nulo\n6 para voto em branco\n9 para encerrar\nDigite seu voto: "))
    if voto == 9:
        break
# Fim da estrutura de repetição
l_voto.append(voto) #Armazena o valor do voto no final da lista l_voto
ct_candidato1 = l_voto.count(1)
ct_candidato2 = l_voto.count(2)
ct_candidato3 = l_voto.count(3)
ct_nulo = l_voto.count(5)
ct_branco = l_voto.count(6)
print("Candidato1 = ", ct_candidato1, "votos.")
print("Candidato2 = ", ct_candidato2, "votos.")
print("Candidato3 = ", ct_candidato3, "votos.")
#print("Candidato1 = ", l_voto.count(1), "votos.")
ct_total = len(l_voto)
pct_nulo = ct_nulo/ct_total * 100
pct_branco = ct_branco / ct_total * 100
print("Porcentagem nulo: ", pct_nulo, '%')
print("Porcentagem branco: ", pct_branco, '%')
