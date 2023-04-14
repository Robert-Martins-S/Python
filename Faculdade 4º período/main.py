"""
20/11/2022
Débora Ferreira de Oliveira - 22051517
Pedro Henrique Jaber Cavalcante - 22107003
Robert Martins dos Santos - 22108154
"""
import os

from functions_code import *


def menu(msg):  # Função menu

    os.system('cls')  # Limpa o terminal

    # Mensagens
    texto = msg.center(20)  # Centraliza o alerta
    print(f"\n[  {texto}  ]")  # Printa o alerta
    #      [                        ]

    print("====== MENU ======")
    print("[1] - Lista de Filmes")
    print("[2] - Registrar Filme")
    print("[3] - Editar Filme")
    print("[4] - Lista de Generos")
    print("[0] - Sair")

    opc = input(" > ")
    return opc


def main():
    msg = ''
    while True:
        opc = menu(msg)
        msg = ''

        # MENU ###############################
        if opc == '0':
            break
        elif opc == '1':
            list_filmes()
        elif opc == '2':
            regis_filme()
        elif opc == '3':
            edit_filme()
        elif opc == '4':
            list_generos()
        else:
            msg = "Opção inválida"
        ######################################


if __name__ == '__main__':
    main()


