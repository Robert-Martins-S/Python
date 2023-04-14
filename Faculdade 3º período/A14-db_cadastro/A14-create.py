from funcoes import *

try:
    conexao = cria_conexao()
    print("Data Base: [online]")
    print(f"Conexão: {conexao}")

    db_info = conexao.get_server_info() # Pega as Informações do servidor
    print(f"Connected to MySQL Server Version: {db_info}")

    cursor = conexao.cursor()

    cursor.execute("SHOW TABLES")
    #print("Create database if not exists db_cadastro")
    for x in cursor:
        print(x, x[0])

    print(f"Qtd.database {cursor.rowcount}")

except Error as erro:
    print("Erro na conexão\n")
else:
    cursor.close()
    conexao.close()
    print("Conexão fechada.")