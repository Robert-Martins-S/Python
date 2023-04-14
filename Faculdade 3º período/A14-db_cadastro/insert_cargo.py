from funcoes import *
try:
    conexao = cria_conexao()                # Chama a função no funcoes.py
    cursor = conexao.cursor()
    qtd_registros_cargo(conexao)            # Chama a função no funcoes.py
    # Inserir primeiro os dados na tabela domínio, td_cargo
    sql = """
        insert into td_cargo
        (nome)                      
        values (%s)                         """  # Inserir na tabela tb_cargo
    a_nome = input('Nome do cargo: ')
    cursor.execute(sql, (a_nome, ))  # Parênteses e vírgula obrigatórios
    # tupla = (a_nome, )
    # cursor.execute(sql, tupla)     # Parênteses obrigatórios (sql, (tupla))
    conexao.commit()                    # Confirma a alteração no database
    print('Registros inseridos:', cursor.rowcount)
    qtd_registros_cargo(conexao)
except Error as erro:
    print('Erro no insert.\n', erro)
else:
    cursor.close()
    fecha_conexao(conexao)              # Chama a função no funcoes.py