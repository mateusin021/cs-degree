def cotacao(qtd):
    return qtd * 1.23

quantidade = float(input('insira o valor em libras: '))

print(f'{quantidade} libras equivalem a ${cotacao(quantidade)} dolares')