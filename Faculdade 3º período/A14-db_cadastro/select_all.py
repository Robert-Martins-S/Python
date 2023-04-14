from funcoes import *
try:
    conexao = cria_conexao()
    cursor = conexao.cursor()
    sql = "select * from tb_empregado"
    cursor.execute(sql)
    registros = cursor.fetchall()
    print("-Lista de tuplas:")
    print(registros)
    print("-Tuplas:")
    for row in registros:
        print(row)
    print("-Colunas, notação de vetor:")
    for row in registros:
        print("Idt:", row[0])
        print("Name:", row[1])
        print("Data nascimento:", row[2])
        print("Gênero:", row[3])
        print("Código cargo:", row[4])
    print("-Colunas, nome coluna:")
    for idt, nome, dta_nascimento, genero, cod_cargo in registros:
        print("Idt:", idt)
        print("Name:", nome)
        print("Data nascimento:", dta_nascimento)
        print("Gênero", genero)
        print("Código cargo:", cod_cargo)
    print("Registros na tabela", cursor.rowcount)
    mostra_registro_cargo(conexao)
except Error as erro:
    print("Erro no select all.\n", erro)
else:
    cursor.close()
    fecha_conexao(conexao)