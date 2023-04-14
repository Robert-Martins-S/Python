ct_menos_5_salarios = 0
ct_5_ate_10_salarios = 0
ct_maisde_10_salarios = 0
total = 0
print('Digite [0] para finalizar')
salario_minimo = float(input('Digite o valor do salário mínimo: '))
while True:
    salario = float(input('Digite o salario do funcionário: '))
    if salario == 0:
        break
    if salario < 5 * salario_minimo:
        ct_menos_5_salarios += 1
    elif salario >= 5* salario_minimo and salario < 10 ** salario_minimo:
        ct_5_ate_10_salarios += 1
    else:
        ct_maisde_10_salarios += 1
    total = total + salario
if total == 0:
    print('Nenhum valor foi digitado.')
else:
    print('Ganham menos que cinco salários minimos:', ct_menos_5_salarios)
    print('Estão na faixa de cinco até dez salários minimos:', ct_5_ate_10_salarios)
    print('Ganham dez ou mais salários minimos', ct_maisde_10_salarios)
    print('Folha de pagamento: R$', total)

