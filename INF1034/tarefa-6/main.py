import string

def validaCpf(cpf):
    nd = cpf[0:9]
    v1 = [10,9,8,7,6,5,4,3,2]
    v2 = [11,10,9,8,7,6,5,4,3,2]
    s = 0
    for i in range(len(nd)):
        s+= int(nd[i])*int(v1[i])
    if s%11<2:
        d1 = '0'
    else:
        d1 = str(11-s%11)
    nd+=d1
    s = 0
    for i in range(len(nd)):
        s+= int(nd[i])*int(v2[i])
    if s%11<2:
        d2 = '0'
    else:
        d2 = str(11-s%11)
    nd+=d2
    return cpf == nd

def validaSenha(senha):
    return len(senha)>=8 and any(p in senha for p in string.ascii_uppercase) and any(p in senha for p in string.ascii_lowercase) and any(p in senha for p in string.digits)

def encrypt(senha):
    c = ""
    
    for l in senha:
        if l.isalpha() and '0' <= l <= 'z':
            cod = ord(l) + 3
            if l.islower() and cod > ord('z'):
                cod -= 26
            elif l.isupper() and cod > ord('Z'):
                cod -= 26
            c += chr(cod)
        else:
            c += l
    return c

def decrypt(senha):
    d = ""
    for l in senha:
        if l.isalpha() and '0' <= l <= 'z':
            cod = ord(l) - 3
            if l.islower() and cod < ord('a'):
                cod += 26
            elif l.isupper() and cod < ord('A'):
                cod += 26
            d += chr(cod)
        else:
            d += l
    return d

# funcao q junta as duas anteriores para demonstracao
def cifra_cesar(senha):
    c = ""
    d = ""
    
    for l in senha:
        if l.isalpha() and '0' <= l <= 'z':
            cod = ord(l) + 3
            if l.islower() and cod > ord('z'):
                cod -= 26
            elif l.isupper() and cod > ord('Z'):
                cod -= 26
            c += chr(cod)
        else:
            c += l
            
    for l in c:
        if l.isalpha() and '0' <= l <= 'z':
            cod = ord(l) - 3
            if l.islower() and cod < ord('a'):
                cod += 26
            elif l.isupper() and cod < ord('A'):
                cod += 26
            d += chr(cod)
        else:
            d += l
    print(f"""
    senha original: {senha}
    senha criptografada: {c}
    senha decriptografada: {d}
    """)

cpf = input('insira o seu cpf: ')
if validaCpf(cpf):
    print('cpf valido')
else:
    print('cpf invalido')
senha = input('insira a sua senha: ')
cifra_cesar(senha)