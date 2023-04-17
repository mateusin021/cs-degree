def ehVogal(caracter):
    return caracter in "aeiouAEIOU"

def provaA(curso,nome):
    if curso == 1:
        if ehVogal(nome[0]):
            return 11
        elif ehVogal(nome[-1]):
            return 32
        else:
            return 32
    elif curso == 2:
        if ehVogal(nome[0]):
            return 11
        elif ehVogal(nome[-1]):
            return 24
        else:
            return 33
    elif curso == 3:
        if ehVogal(nome[0]):
            return 11
        elif ehVogal(nome[-1]):
            return 24
        else:
            return 33

def provaB(curso,nome):
    if curso == 1:
        if ehVogal(nome[0]):
            return 13
        elif ehVogal(nome[-1]):
            return 32
        else:
            return 35
    elif curso == 2:
        if ehVogal(nome[0]):
            return 17
        elif ehVogal(nome[-1]):
            return 28
        else:
            return 33
    elif curso == 3:
        if ehVogal(nome[0]):
            return 19
        elif ehVogal(nome[-1]):
            return 24
        else:
            return 43

if __name__ == "__main__":
    nome = input("insira o nome do aluno: ")
    print("""
    1) Agropecuaria
    2) Alimentos
    3) Eletronica
    """)
    curso = int(input("insira o codigo do curso: "))
    print(provaB(curso,nome))