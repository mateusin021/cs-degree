def pertence(string,char):
    if string == '':
        return False
    if string[0] == char:
        return True
    return pertence(string[1:],char)

print(pertence('teste', 't'))
