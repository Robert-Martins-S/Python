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


def criar_bd():
    print("[Criando Banco de Dados...]")
    conexao_dados = (
        f"Driver={DRIVER};"
        f"Server={SERVER};"
        "Database=master;"
        f"UID={UID};"
        f"PWD={PWD}"
    )
    conexao = pyodbc.connect(conexao_dados, autocommit=True)
    cursor = conexao.cursor()

    cursor.execute(f"create database {BD_NOME}")

    cursor.close()
    conexao.close()
    print("[Banco de Dados Criado]")


def criar_tables(cursor):
    print("[Criando Tabelas...]")
    table_genero = """
                   create table tb_genero
                   (
                   cd_genero int not null primary key identity(1, 1),
                   genero varchar(50) not null
                   )
                  """
    print("[Tabela de Gêneros Criada]")

    table_filme = """
                  create table tb_filme
                  (
                  cd_filme int not null primary key,
                  filme varchar(100) not null,
                  tempo_min int not null,
                  cd_genero int foreign key 
                  references tb_genero(cd_genero)
                  ) 
                  """
    print("[Tabela de Filmes Criada]")

    cursor.execute(table_genero)
    cursor.execute(table_filme)

    cursor.commit()
    print("[Tabelas Criadas]")


def popular_tables(cursor):
    print("[Populando Tabelas...]")
    table_genero = """
    insert into tb_genero
    (genero)
    values
    ('Ficção científica'),
    ('Drama'),
    ('Ação'),
    ('Suspense'),
    ('Romance'),
    ('Terror'),
    ('Aventura'),
    ('Cinema de arte'),
    ('Comédia'),
    ('Comédia de ação'),
    ('Comédia de terror'),
    ('Comédia dramática'),
    ('Comédia romântica'),
    ('Dança'),
    ('Documentário'),
    ('Docuficção'),
    ('Espionagem'),
    ('Faroeste'),
    ('Fantasia'),
    ('Fantasia científica'),
    ('Ficção científica'),
    ('Filmes com truques'),
    ('Filmes de guerra'),
    ('Mistério'),
    ('Musical'),
    ('Filme policial')
    """

    table_filmes = """
    insert into tb_filme
    (cd_filme, filme, tempo_min, cd_genero)
    values
    (7, 'O retorno da sua mãe', 666, 6),
    (1, 'Interestelar', 180, 1),
    (2, 'Pulp Fiction', 140, 2),
    (3, 'The Batman', 180, 3),
    (4, 'Clube da Luta', 130, 4),
    (5, 'A Culpa é das Estrelas', 130, 5)
    """

    cursor.execute(table_genero)
    cursor.execute(table_filmes)

    cursor.commit()
    print("[Tabelas Populadas]")


def view_filmes(cursor):
    print("[Criando View]")
    view = """
           create view tb_filme_all as
           select cd_filme, filme, tempo_min, G.genero 
           from tb_filme F inner join tb_genero G
           on F.cd_genero = G.cd_genero
           """

    cursor.execute(view)

    cursor.commit()
    print("[View Criada]")


def stored_procedure(cursor):
    print("[Criando Stored procedures]")

    insert_filme = """
    CREATE PROCEDURE insert_filme @cd int, @filme varchar(100), @tempo int, @genero int
    as
    insert into tb_filme
    (cd_filme, filme, tempo_min, cd_genero)
    values
    (@cd, @filme, @tempo, @genero)
    """

    insert_genero = """
    CREATE PROCEDURE insert_genero @genero varchar(50)
    as
    insert into tb_genero
    (genero)
    values
    (@genero)
    """

    update_filme_nome = """
    CREATE PROCEDURE update_filme_nome @cd int, @filme varchar(100)
    as
    update tb_filme
        set filme = @filme
        where cd_filme = @cd
    """

    update_filme_tempo = """
    CREATE PROCEDURE update_filme_tempo @cd int, @tempo int
    as
    update tb_filme
        set tempo_min = @tempo
        where cd_filme = @cd
    """

    update_filme_genero = """
    CREATE PROCEDURE update_filme_genero @cd int, @genero int
    as
    update tb_filme
        set cd_genero = @genero
        where cd_filme = @cd
    """

    delete_filme = """
    CREATE PROCEDURE delete_filme @cd int
    as
    delete from tb_filme where cd_filme = @cd
    """

    cursor.execute(insert_filme)
    print("[1/6]")
    cursor.execute(insert_genero)
    print("[2/6]")
    cursor.execute(update_filme_nome)
    print("[3/6]")
    cursor.execute(update_filme_tempo)
    print("[4/6]")
    cursor.execute(update_filme_genero)
    print("[5/6]")
    cursor.execute(delete_filme)
    print("[6/6]")

    cursor.commit()
    print("[Stored procedures Criadas]")


if __name__ == '__main__':
    # (conexao, cursor)
    criar_bd()

    conexao = open_connection()
    cursor = conexao.cursor()

    criar_tables(cursor)
    popular_tables(cursor)
    view_filmes(cursor)
    stored_procedure(cursor)

    close_connection(conexao, cursor)















