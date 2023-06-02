import turtle

t = turtle.Turtle()

tamanho = 200

def quadradin(tamanho):
    if tamanho ==0:
        return
    for i in range(4):
        t.fd(tamanho)
        t.lt(90)
    quadradin(tamanho-20)

quadradin(tamanho)

turtle.done()
