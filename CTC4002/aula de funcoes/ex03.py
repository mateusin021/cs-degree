nome = input('nome: ')
data = input('data de nascimento: ')

def senha(nome, data):
    nome_impares = nome[1::2]
    return nome_impares + data[::-1]

print(f'sugestao de senha: {senha(nome, data)}')