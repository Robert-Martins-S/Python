def soma(x,y):
    return x + y
def subtrai(x,y):
    calculo = x - y
    return calculo
def menu():
    opcao= str(input("[+] Somar\n[-] Subtrair\nOpção: "))
    return opcao
if __name__ == '__main__':
    num1=int(input("Primeiro valor: "))
    num2=int(input("Segundo valor: "))
    retorno = menu()
    if retorno == "+":
        print("A soma é:",soma(num1,num2))
    elif retorno == "-":
        print("A subtração é:",subtrai(num1,num2))
    else:
        print("Opção inválida!")