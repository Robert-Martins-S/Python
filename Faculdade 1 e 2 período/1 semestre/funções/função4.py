def soma (x,y,z,a):
    return x + y + z + a
def subtrai(x,y):
    subtrair = x - y
    return subtrair
if __name__ == '__main__':
    opcao = int(input("[1] somar\n[2] subtrair\nOpção: "))
    if opcao == 1:
        v1 = int(input("Primeiro valor: "))
        v2 = int(input("Segundo valor: "))
        v3=int(input("Terceiro valor: "))
        v4=int(input("Quarto valor: "))
        print('Soma:',soma(v1,v2,v3,v4))
    elif opcao == 2:
        v1 = int(input("Primeiro valor: "))
        v2 = int(input("Segundo valor: "))
        print("Subtração: ", subtrai(v1,v2))
    else:
        print("Opção inválida.")
