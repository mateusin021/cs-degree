from math import pi

def volEsfera(r):
    return (4/3) * r**3 * pi

def volCubo(a):
    return a**3

def vazio(cubo, esfera):
    return cubo - esfera

r = float(input('insira o raio da esfera: '))
a = float(input('insira a aresta do cubo: '))

print(f'o espaco vazio no dado cubo é: {vazio(volCubo(a),volEsfera(r)):.2f}')
