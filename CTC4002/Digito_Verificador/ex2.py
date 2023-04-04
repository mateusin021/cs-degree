def calc_dv_int(digitos):
    a = digitos //1000
    bc =(digitos//10)%100
    d = digitos %10
    return(4*a+bc+d)%8
def numero_conta_completo_int(digitos):
    return int(f'{digitos}{calc_dv_int(digitos)}')

digitos = int(input('insira os quatro digitos da conta: '))
print(f'digito verificador: {calc_dv_int(digitos)}\nnumero da conta: {numero_conta_completo_int(digitos)}')
