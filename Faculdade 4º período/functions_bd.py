import pyodbc


DRIVER = "{SQL Server Native Client 11.0}"
SERVER = "PEDRO"
BD_NOME = "db_filmes"
UID = "sa"
PWD = "Phjc1985!"

"""
DRIVER = "{SQL Server}"
SERVER = "T20017452069149\SQLEXPRESS"
BD_NOME = "db_filmes"
UID = "sa"
PWD = "uniceub"
"""


def open_connection():
    conexao_dados = (
        f"Driver={DRIVER};"
        f"Server={SERVER};"
        f"Database={BD_NOME};"
        f"UID={UID};"
        f"PWD={PWD}"
    )

    conexao = pyodbc.connect(conexao_dados)
    return conexao


def close_connection(conexao, cursor):
    cursor.close()
    conexao.close()


def insert_filme(cursor, cd_filme, filme, tempo, genero):

    sql = f"""
        exec insert_filme 
        @cd = {cd_filme}, 
        @filme = {filme}, 
        @tempo = {tempo}, 
        @genero = {genero}
        """

    cursor.execute(sql)


def select_filmes(cursor, mode=0):
    sql = ''
    if mode == 0:
        sql = "select * from tb_filme_all"
    elif mode == 1:
        sql = "select * from tb_filme"
    else:
        print("Modo invalido")

    if mode == 0 or mode == 1:
        cursor.execute(sql)
        l_filmes = cursor.fetchall()

        print(f"┌────────┬────────────────────────────────┬──────────┬──────────────────────┐")
        print(f"│Código: │Filme:                          │Minutos:  │Gênero:               │")
        print(f"├────────┼────────────────────────────────┼──────────┼──────────────────────┤")
        #       │ 000000 │ ABCDEFGHIJKLMNOPQRSTUVWXYZABCD │   0000   │ ABCDEFGHIJKLMNOPQRST │
        for cd, filme, minutos, genero in l_filmes:
            print(
              f"│ {cd:6d} │ {filme:30s} │   {minutos:4d}   │ {genero:20s} │")
        #       │ 000000 │ ABCDEFGHIJKLMNOPQRSTUVWXYZABCD │   0000   │ ABCDEFGHIJKLMNOPQRST │
        print(f"└────────┴────────────────────────────────┴──────────┴──────────────────────┘")


def select_generos(cursor):
    sql = "select * from tb_genero"

    cursor.execute(sql)
    l_generos = cursor.fetchall()

    print(f"┌────────┬──────────────────────┐")
    print(f"│Código: │Gênero:               │")
    print(f"├────────┼──────────────────────┤")
    #       │ 000000 │ ABCDEFGHIJKLMNOPQRST │
    for cd, genero in l_generos:
        print(f"│ {cd:6d} │ {genero:20s} │")
    print(f"└────────┴──────────────────────┘")


