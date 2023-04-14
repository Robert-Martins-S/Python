import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  password='uniceub',
                                  host='127.0.0.1',
                                  database='db_empresa')

print('Conexão:', conexao)
cursor = conexao.cursor()
sql = '''SELECT * FROM tb_funcionario'''
cursor.execute(sql)
l_registros = cursor.fetchall()        # Uma lista de tuplas, l_registros recebe os dados do select
print(f"Registros na tabela: {cursor.rowcount}")
cursor.close()                         # Cria o cursor para executar comandos SQL
conexao.close()
print('Conexão fechada.')


print('.', '_' * 34, '.', sep='')
print("| IDT |FUNCIONÁRIO         |SALARIO|")
print('|', '-' * 34, '|', sep='')
for tupla in l_registros:
    idt = tupla[0]
    funcionario = tupla[1]
    salario = tupla[2]
    print(f"| {idt:03d} |{funcionario:20s}|{salario}|")
print('|', '_' * 34, '|', sep='')