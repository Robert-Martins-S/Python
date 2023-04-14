class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome

    def get_ra(self):
        return self.ra

    def set_ra(self, n_ra):
        self.ra = n_ra

    def get_nome(self):
        return self.nome


class Curso:
    def __init__(self,nome, valor):
        self.nome = nome
        self.valor = valor
        self.alunos = []

    def get_nome(self):
        return self.nome

    def set_nome(self, n_nome):
        self.nome = n_nome

    def insere_aluno(self, aluno):
        self.alunos.append(aluno)

    def mostra_dados(self):
        print(f"Dados do curso:\nNome: {self.nome}\nValor:")

    def consulta_nome(self):
        if not self.alunos:
            print("A lista está vazia.")
        else:
            print("Lista de alunos: ")
            for i, aluno in enumerate(self.alunos):
                print(f"[{i + 1}] RA: ({aluno.get_ra()}) - {aluno.get_nome()}")


if __name__ == '__main__':
    curso1 = Curso("Ciência da Computação", 1000)
    curso2 = Curso("Engenharia de software", 2000)
    aluno1 = Aluno(8317236, "Robert")
    aluno2 = Aluno(2394959 , "João")
    curso1.insere_aluno(aluno1)
    curso1.insere_aluno(aluno2)
    curso1.consulta_nome()
