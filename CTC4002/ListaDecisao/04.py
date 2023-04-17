def banido(idade, altura):
    if idade <18 and altura <150:
        return "nao pode entrar"
    elif idade>=65:
        return "cuidado com a velocidade"
    else:
        return "pode entrar"