def calculaGrau(p, t1, t2):
    return (7*p + t1 + 2*t2)/10
p, t1, t2 = [float(x) for x in input('insira as notas do bloco 1: ').split()]
p2, t3, t4 = [float(x) for x in input('insira as notas do bloco 2: ').split()]
print(f'grau 1: {calculaGrau(p,t1,t2)}\ngrau2: {calculaGrau(p2,t3,t4)}')