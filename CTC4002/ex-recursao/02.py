def tamanho(inteiro):
    if inteiro < 10:
        return 1
    return 1+ tamanho(inteiro//10)

print(tamanho(1337))
