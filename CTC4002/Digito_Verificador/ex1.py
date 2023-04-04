def calc_dv_st(digitos):
    a,b,c,d = digitos[0::]
    return(4*int(a)+int(b+c)+int(d))%8
def numero_conta_completo_st(digitos):
    return f'{digitos}{calc_dv_st(digitos)}'

digitos = input('insira os quatro digitos da conta: ')
print(f'digito verificador: {calc_dv_st(digitos)}\nnumero da conta: {numero_conta_completo_st(digitos)}')