from funcoes import *

conexao = cria_conexao()
cursor = conexao.cursor()
qtd_registros(conexao)
sql = '''delete from tb_produto
        where idt = 2                  # uso do where obrigatório
        '''
cursor.execute(sql)
conexao.commit()