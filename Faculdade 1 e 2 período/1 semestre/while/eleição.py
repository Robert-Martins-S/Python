ct_candidato1 = 0
ct_candidato2 = 0
ct_candidato3 = 0
ct_nulo = 0
ct_branco = 0
while True:
    voto = int(input('[1] para candidato 1\n[2] para candidato 2\n[3] para candidato 3' 
                     '\n[5] para voto nulo\n[6] para voto em branco\n[9] para encerrar\nDigite seu voto: ' ))
    if voto == 9:
        break
    if voto == 1:
        ct_candidato1 += 1
    elif voto == 2:
        ct_candidato2 += 1
    elif voto == 3:
        ct_candidato3 += 1
    elif voto == 5:
        ct_nulo += 1
    elif voto == 6:
        ct_branco +=1
    else:
        print('Voto não registrado.')
ct_total = ct_candidato1 + ct_candidato2 + ct_candidato3 + ct_nulo + ct_branco
if ct_total == 0:
    print('Ninguém votou.')
else:
    print('Candidato1 =', ct_candidato1, 'votos.')
    print('Candidato2 =', ct_candidato2, 'votos.')
    print('Candidato3 =', ct_candidato3, 'votos.')
    print('Votos nulos = ', ct_nulo)
    print('Votos em branco = ', ct_branco)
    pct_nulo = ct_nulo/ct_total * 100
    pct_branco = ct_branco/ct_total * 100
    print('Porcentagem nulo: ', pct_nulo)
    print('Porcentagem branco: ',pct_branco)