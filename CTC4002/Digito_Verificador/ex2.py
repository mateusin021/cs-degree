import math

def calc_dv_int(digitos):
    a,b,c,d = separa_inteiros(digitos)
    return(4*a+int(str(b)+str(c))+d)%8
def numero_conta_completo_int(digitos):
    return int(f'{digitos}{calc_dv_int(digitos)}')

def separa_inteiros(an_int):
    x = math.log(an_int, 10)
    y = math.ceil(x)

    a,b,c,d = [(an_int//(10**i)) % 10 for i in range(y, -1, -1)][bool(math.log(an_int, 10) % 1):]

    return a,b,c,d
digitos = int(input('insira os quatro digitos da conta: '))
print(f'digito verificador: {calc_dv_int(digitos)}\nnumero da conta: {numero_conta_completo_int(digitos)}')