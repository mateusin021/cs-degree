import random

def ehVogal(caracter):
    return caracter in "aeiouAEIOU"

def gerNum(a,b):
    return random.randint(a,b) + random.randint(a,b)

def fazAlgumaCoisa(nome, mae):
    if ehVogal(nome[0]) and ehVogal(nome[-1]) and ehVogal(mae[0]) and ehVogal(mae[-1]):
        if len(nome) %2 ==0:
            return gerNum(1, len(nome))
        else:
            return gerNum(1, len(nome))
    elif (ehVogal(nome[0]) and ehVogal(nome[-1])) or (ehVogal(mae[0]) and ehVogal(mae[-1])):
        return gerNum(2,4*(len(nome)/2))
    else:
        return gerNum(1,(len(nome)+len(mae)))