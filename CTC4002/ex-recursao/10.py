def imprime(string):
    if string == '':
        return
    print(string[0])
    imprime(string[1:])

imprime('teste')
