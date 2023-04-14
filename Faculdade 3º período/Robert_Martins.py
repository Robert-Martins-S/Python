import mysql.connector

conexao = mysql.connector.connect(user= 'robert',
                                  password = 'Msantos10072002rt!',
                                  host= '192.168.0.85',
                                  database= 'db_escola')

print(f"Conexão: {conexao}\n")
cursor = conexao.cursor()
# 1

# sql = 'create database if not exists db_escola'
# sql = """create table if not exists tb_professor(
#         idt int not null auto_increment,
#         nome varchar(40) not null,
#         email varchar(30) unique null,
#         idade int null,
#         aniversario date,
#         primary key(idt)
#         )"""
# cursor.execute(sql)

# 2

# sql = """insert into tb_professor
#         (idt, nome, email, idade, aniversario)
#         values
#         (1, 'Ricardo', 'ricardo@hotmail.com', 40, '1982/08/25')
#         (2, 'Paula', 'paula@gmail.com', 45, '1977/07/14')
#         """
# cursor.execute(sql)

# 3

# sql = """select * from tb_professor"""
l_registros = cursor.fetchall()
for tupla in l_registros:
    idt = tupla[0]
    nome = tupla[1]
    email = tupla[2]
    idade = tupla[3]
    aniversario = tupla[4]
    print(f"{idt}|{nome}|{email}|{idade}|{aniversario}")
# cursor.execute(sql)
# 4

# sql = """delete from tb_professor
#         where idt = 2"""
# cursor.execute(sql)

# 5

# sql = """insert into tb_professor
#         (idt, nome, email, idade, aniversario)
#         values
#         (%s, %s, %s, %s, %s)"""
# v_idt = input("Idt: ")
# v_nome = input("Nome: ")
# v_email = input("E-mail: ")
# v_idade = input("Idade: ")
# v_aniversario = input("Aniversário: ")
# record = (v_idt, v_nome, v_email, v_idade, v_aniversario)
# cursor.execute(sql, record)

conexao.commit()
cursor.close()
conexao.close()
print("\nConexão encerrada")