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

cd_filme = int(input("Digite o código do filme: "))
filme = input("Digite o nome do filme: ")
tempo = int(input("Digite o tempo do filme em minutos: "))
for genero in l_generos:
    print(f"{genero[0]} {genero[1]}")
genero = int(input())

sql = f"""exec insert_filme @cd = {cd_filme}, @filme = {filme}, @tempo = {tempo}, @genero = {genero}"""

cursor.execute(sql)
cursor.commit()

