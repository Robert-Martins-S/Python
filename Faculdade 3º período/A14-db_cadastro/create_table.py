from funcoes import *               # from arquivo.py import *
try:
    conexao = cria_conexao()        # Chama a função do arquivo funcoes.py
    cursor = conexao.cursor()
    # sql_db = "CREATE DATABASE if not exists db_cadastro"  # Já foi criada
    # cursor.execute(sql_db)
    sql = "show tables"
    cursor.execute(sql)
    print('- Tabelas:')
    for x in cursor:
        print(x[0])                     # print(x)
    print('Qtd. tables:', cursor.rowcount)
    # Cria primeiro a tabela que não tem foreign key, a tabela de domínio.
    # sql_cargo = """ CREATE TABLE IF NOT EXISTS td_cargo(
    #     idt INT NOT NULL AUTO_INCREMENT,    # Cria automaticamente a chava primária
    #     nome VARCHAR(45) UNIQUE NOT NULL,   # Valores sem repetição
    #     PRIMARY KEY (idt)                   # Define a chave primária
    #     )   """
    #cursor.execute(sql_cargo)               # Cria a tabela cargo
    cursor.execute(sql)                     # Mostra as tabalas do database
    print('- Tabelas:')
    for x in cursor:
        print(x[0])                         # print(x)
    print('Qtd. tables:', cursor.rowcount)
    # Depois cria a tabela que tem foreign key, a tabela básica.
    # sql_empregado = """ CREATE TABLE IF NOT EXISTS tb_empregado(
    #     idt INT NOT NULL AUTO_INCREMENT,        # Atualiza automaticamente a chava primária
    #     nome VARCHAR(45) NOT NULL,              # NOT NULL para valor obrigatório
    #     dta_nascimento date NULL,               # NULL para valor opcional
    #     genero enum('M', 'F') NOT NULL,         # Aceita 'M' ou 'F'
    #     cod_cargo int NOT NULL,                 # NOT NULL para valor obrigatório
    #     PRIMARY KEY (idt),                      # Define a chave primária
    #     FOREIGN KEY(cod_cargo) REFERENCES td_cargo(idt)  # Define a chave estrangeira
    # )   """
    # cursor.execute(sql_empregado)           # Cria a tabela tb_cargo
    #cursor.execute(sql)                     # Mostra as tabelas do database
    print('- Tabelas:')
    for x in cursor:
        print(x[0])                         # print(x)
    print('Qtd. tables:', cursor.rowcount)

except Error as erro:
    print('Erro no create table.\n', erro)
else:
    cursor.close()
    fecha_conexao(conexao)                  # Chama a função do arquivo funcoes.py
