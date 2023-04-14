from funcoes import *
try:
    conexao = cria_conexao()
    cursor = conexao.cursor()
    mostra_registro_cargo(conexao)
    qtd_registros_cargo(conexao)
    sql = """ insert into tb_empregado(nome, dta_nascimento, genero, cod_cargo)
            values (%s, %s, %s, %s)"""
    a_nome = input("Nome empregado: ")
    a_dta_nascimento = input("Data nascimento: aaaa-mm-dd: ")
    a_genero = input("Gênero [M] ou [F]: ")
    a_cod_cargo = int(input("Código Cargo: "))
    tupla = (a_nome, a_dta_nascimento, a_genero, a_cod_cargo)
    cursor.execute(sql, tupla)
    print("Registros inseridos: ", cursor.rowcount)
    conexao.commit()
except Error as erro:
    print("Erro no insert.\n", erro)
else:
    cursor.close()
    fecha_conexao(conexao)
