"""
O professor aplicou a avaliação em sua turma e deseja selecionar a maior nota e sua respectiva frequência, ou seja, a
quantidade de alunos que conseguiram essa nota. Desenvolva o programa que leia a nota dos alunos e gere a tela de saída
com as informações solicitadas.
Teste 1: Nota: 6, 8, 4, -1
Saída: Maior nota: 8.0, Qtd: 1
"""

maiorn = -1
maiorf = 0
print("Digite (-1) para sair.")
while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota == -1:
        break
    if nota > maiorn:
        maiorn = nota
        maiorf = 1
    elif nota == maiorn:
        maiorf += 1
#eu quero que quando o programa identifique a maior nota, apenas comece a contar a frequência quando for a última maior nota

print(f"A maior nota foi {maiorn}, e {maiorf} conseguiram tirar essa nota.")