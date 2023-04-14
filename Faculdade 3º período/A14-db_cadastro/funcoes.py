import mysql.connector
def cria_conexao():
    conexao = mysql.connector.connect(user = 'root',
                                  password = 'uniceub',
                                  host = '127.0.0.1',
                                  database = 'db_loja')
    print('Conexão:', conexao)
    return conexao

def fecha_conexao(con):
    con.close()
    print('\nConexão fechada.')
