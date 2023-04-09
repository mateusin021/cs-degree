def funcao_a(n,sima,simb):
    return (sima * n) + (simb *n)

def funcao_b(meses):
    return f'{meses//12} anos e {meses%12} meses'

def funcao_c(nome,idade):
    enfeite = funcao_a(len(nome),'#','=')
    return f'{enfeite} {nome} tem {funcao_b(idade)} {enfeite[::-1]}'

nome = input('insira o nome da pessoa: ')
idade = int(input('insira a idade em meses da pessoa: '))

print(funcao_c(nome,idade))