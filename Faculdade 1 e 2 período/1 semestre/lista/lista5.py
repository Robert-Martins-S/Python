l_notas = list()
for i in range(1,5+1,1):
    nota = float(input("Nota do aluno: "))
    l_notas.append(nota)
soma = sum(l_notas)
qtd = len(l_notas)
media = soma/qtd
# media = sum(l_notas) / len(l_notas)
print(f"Média da turma {media:.2f}")
