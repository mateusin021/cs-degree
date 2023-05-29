def contachar(string, char):
    if string == '':
        return 0
    if string[0] == char:
        return 1+contachar(string[1:], char)
    return contachar(string[1:], char)

print(contachar('teste', 't'))
