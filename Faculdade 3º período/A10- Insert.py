import sqlite3
conexao = sqlite3.connect("livraria.db")
cur = conexao.cursor()
cpf = input("Digite o cpf: ")
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
#sql = "insert into tb_cliente(cpf, nome, idade) " \
#     f"values(?, ?, ?)"
sql = "insert into tb_cliente " \
      "values(?, ?, ?)"
cur.execute(sql, (cpf, nome, idade))
print(f'rowcount: {cur.rowcount}')
print(f"lastroiwd {cur.lastrowid}")
conexao.commit()
cur.close()
conexao.close()
