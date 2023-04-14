from funcoes import *

conexao = cria_conexao()
cursor = conexao.cursor()

sql = '''INSERT INTO tb_produto
        (nome, preco, dta_validade)
        values
        ('arroz', 10.00, '2022/08/20') 
        ('feijão', 10.00, '2022/08/10')
        '''
cursor.execute(sql)
conexao.commit()
cursor.close()
fecha_conexao(conexao)