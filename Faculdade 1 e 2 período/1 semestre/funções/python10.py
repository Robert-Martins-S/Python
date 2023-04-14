def converte_em_minuto(horas,minutos):
    vl_minutos = horas * 60 + minutos
    return vl_minutos


if __name__ == '__main__':
    h = int(input("Digite às horas: "))
    m = int(input("Digite os minutos: "))
    retorno = converte_em_minuto(h,m)
    print(f"{h} horas e {m} minutos totalizam {retorno} minutos.")

