import pyodbc

conexao_dados = (
    "Driver={SQL Server};"
    "Server=DESKTOP-H27IV74\MSSQLSERVERDEV22;"
    "Database=db_filmes;"
)

conexao = pyodbc.connect(conexao_dados)

cursor = conexao.cursor()

sql = '''SELECT * FROM tb_genero'''
cursor.execute(sql)
l_generos = cursor.fetchall()

cursor = conexao.cursor()

print("Gêneros já existentes:")
for genero in l_generos:
    print(f"{genero[0]} {genero[1]}")
genero = input("Digite o nome do gênero: ")




sql = f"""exec insert_genero @genero = {genero}"""

cursor.execute(sql)
