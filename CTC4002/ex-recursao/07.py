def contachar(string):
    if string =='':
        return 0
    return 1+ contachar(string[1:])

print(contachar('teste'))
