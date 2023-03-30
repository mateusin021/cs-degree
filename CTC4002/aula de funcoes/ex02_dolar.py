def cotacao(qtd):
    return qtd * 5.14

quantidade = float(input('insira o valor em dolares: '))

print(f'${quantidade} dolares equivalem a R${cotacao(quantidade)} reais')