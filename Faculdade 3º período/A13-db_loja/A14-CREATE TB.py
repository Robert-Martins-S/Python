from funcoes import *

conexao = cria_conexao()
cursor = conexao.cursor()
sql = '''CREATE TABLE IF NOT EXISTS tb_produto(
        idt INT NOT NULL AUTO_INCREMENT,             # cria automaticamente a chave primária
        nome VARCHAR(45) UNIQUE NOT NULL,
        preco DECIMAL(9,2) NOT NULL,
        dta_validade DATE NULL,
        PRIMARY KEY (idt)
        )
    '''
cursor.execute(sql)
cursor.close()
fecha_conexao(conexao)