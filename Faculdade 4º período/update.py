import pyodbc


conexao_dados = (
    "Driver={SQL Server};"
    "Server=DESKTOP-H27IV74\MSSQLSERVERDEV22;"  # PEDRO  # DESKTOP-H27IV74\MSSQLSERVERDEV22
    "Database=db_filmes;"
)

conexao = pyodbc.connect(conexao_dados)
cursor = conexao.cursor()

sql = '''SELECT * FROM tb_filme'''
cursor.execute(sql)
l_filmes = cursor.fetchall()

cursor = conexao.cursor()

for filmes in l_filmes:
    print(f"{filmes[0]} {filmes[1]} {filmes[2]} {filmes[3]}")

codigo = input("Selecione o filme através do código: ")
escolha = input("\nEscolha o que deseja alterar:\n[1]Nome\n[2]Tempo\n[3]Gênero\n")

if escolha == '1':
    update_nome = input("Digite o novo nome do filme: ")
    sql_update = f"""exec update_filme_nome @cd = {codigo}, @filme = '{update_nome}'"""
    cursor.execute(sql_update)
    cursor.commit()
elif escolha == '2':
    update_tempo = input("Digite o novo tempo do filme: ")
    sql_update = f"""exec update_filme_tempo @cd = {codigo}, @tempo = {update_tempo}"""
    cursor.execute(sql_update)
    cursor.commit()
elif escolha == '3':
    sql = '''SELECT * FROM tb_genero'''
    cursor.execute(sql)
    l_generos = cursor.fetchall()
    cursor = conexao.cursor()
    print("Gêneros já existentes:")
    for genero in l_generos:
        print(f"{genero[0]} {genero[1]}")
    update_genero = input("Digite o novo número do gênero: ")
    sql_update = f"""exec update_filme_genero @cd = {codigo}, @genero = {update_genero}"""
    cursor.execute(sql_update)
    cursor.commit()
else:
    print("Opção inválida")
