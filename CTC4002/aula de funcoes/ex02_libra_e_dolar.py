def libra(qtd): 
    return qtd * 1.23
def dolar(qtd):
    return qtd * 5.14

libras = float(input('insira a quantidade em libras: '))

print(f'GBP {libras} libras equivalem a ${libra(libras)} dolares ou R${dolar(libra(libras))} reais')
