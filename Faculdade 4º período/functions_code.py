import os

from functions_bd import *


def list_filmes():
    conexao = open_connection()
    cursor = conexao.cursor()
    while True:
        os.system('cls')
        print('')
        print("====== Lista de Filmes ======")
        select_filmes(cursor)
        print("=============================")
        print("| 1 | - Atualizar")
        print("| 0 | - Menu")

        opc_num = input(" > ")

        if opc_num == "1":
            pass
        elif opc_num == "0":
            break
        else:
            print("Opção Invalida")


def list_generos():
    os.system('cls')  # Limpa o terminal
    print('')
    conexao = open_connection()
    cursor = conexao.cursor()

    select_generos(cursor)


def regis_filme():
    os.system('cls')  # Limpa o terminal
    print('')
    conexao = open_connection()
    cursor = conexao.cursor()

    print("====== Registrar um Filme ======")
    print("Lista de Filmes registrados:")
    select_filmes(cursor)
    print('')

    cd_filme = input("Digite o código do filme > ")
    filme = input("Digite o nome > ")
    tempo = input("Digite o tempo em minutos > ")

    select_generos(cursor)
    print('')
    genero = input("Escolha o Gênero > ")

    sql = f"""exec insert_filme @cd = {cd_filme}, @filme = '{filme}', @tempo = {tempo}, @genero = {genero}"""

    cursor.execute(sql)
    cursor.commit()


def edit_filme():
    conexao = open_connection()
    cursor = conexao.cursor()
    while True:
        os.system('cls')
        print("====== Lista de Filmes ======")
        select_filmes(cursor)
        print("=============================")
        print("Escolha um registro")
        print("| 0 | - Menu")
        cd_filme = input(" > ")
        if cd_filme == '0':
            break

        print("Editar: ")
        print("| 1 | - Nome")
        print("| 2 | - Minutos")
        print("| 3 | - Gênero")
        opc = input(" > ")

        sql_update = ''
        if opc == '1':
            update_nome = input("Digite o novo nome do filme: ")
            sql_update = f"""exec update_filme_nome @cd = {cd_filme}, @filme = '{update_nome}'"""
            cursor.execute(sql_update)
            cursor.commit()
        elif opc == '2':
            update_tempo = input("Digite o novo tempo do filme: ")
            sql_update = f"""exec update_filme_tempo @cd = {cd_filme}, @tempo = {update_tempo}"""
            cursor.execute(sql_update)
            cursor.commit()
        elif opc == '3':
            sql = '''SELECT * FROM tb_genero'''
            cursor.execute(sql)
            l_generos = cursor.fetchall()
            cursor = conexao.cursor()
            print("Gêneros:")
            for genero in l_generos:
                print(f"{genero[0]} {genero[1]}")
            update_genero = input("Digite o novo número do gênero: ")
            sql_update = f"""exec update_filme_genero @cd = {cd_filme}, @genero = {update_genero}"""
            cursor.execute(sql_update)
            cursor.commit()
        else:
            print("Opção inválida")


