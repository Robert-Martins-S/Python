import mysql.connector

conexao = mysql.connector.connect(user = 'root',
                                  password = 'uniceub',
                                  host = '127.0.0.1',
                                  database = '')

print('Conexão: ', conexao)
cursor = conexao.cursor()
sql = 'CREATE DATABASE if not exists db_loja'
cursor.execute(sql)
cursor.close()
conexao.close()
print('Conexão fechada')


