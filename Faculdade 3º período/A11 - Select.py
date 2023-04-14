import sqlite3
conexao = sqlite3.connect('livraria.db')
cur = conexao.cursor()
sql = "SELECT * from tb_cliente"
cur.execute(sql)
registros = cur.fetchall()
for i, tupla in enumerate(registros):
    cpf = tupla[0]
    nome = tupla[1]
    idade = tupla[2]
    print(f"[{i + 1}] {cpf}, {nome}, {idade}")
conexao.commit()
conexao.close()


