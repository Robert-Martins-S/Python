import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  password='uniceub',
                                  host='127.0.0.1',
                                  database='db_empresa')

print('Conexão:', conexao)
cursor = conexao.cursor()
# sql = "CREATE DATABASE if not exists db_empresa"
# sql = '''CREATE TABLE IF NOT EXISTS tb_funcionario(
#         idt INT,                       # Primary key
#         nome VARCHAR(50) NOT NULL,     # Obrigatória
#         salario DECIMAL(9,2) NULL,     # Opcional
#         PRIMARY KEY (idt)              # Not NULL é default na primary key
#         )'''
sql = '''INSERT INTO tb_funcionario
        (idt, nome, salario)
        values
        (1, 'Bruno', 1200.00),
        (2, 'Pedro', 1200.00) 
        '''
cursor.execute(sql)
conexao.commit()
cursor.close()                         # Cria o cursor para executar comandos SQL
conexao.close()
print('Conexão fechada.')