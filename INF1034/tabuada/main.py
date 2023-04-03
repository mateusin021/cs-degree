numeros = [1,2,3,4,5,6,7,8,9,10]
for x in range(10):
    numero = x
    print(f'tabuada do {numero}')
    for i in range(10):
        atual = numero * numeros[i]
        print(f'{numero} * {numeros[i]} = {atual}')