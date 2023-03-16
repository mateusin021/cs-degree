def calculaBhaskara(a,b,c):
    #calcula delta
    delta = (b**2) -(4*a*c)
    #calcula a raiz de delta
    rdelta = delta**0.5
    #calcula as duas raizes
    x1 = (-b + rdelta) /(2*a)
    x2 = (-b - rdelta) /(2*a)
    return({'x1: ': x1, 'x2: ': x2})

print(calculaBhaskara(1,3,2)) # x1 = -1 && x2 = -2