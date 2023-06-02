import turtle

t = turtle.Turtle()

tamanho = 200


def quadradin(tamanho):
    if tamanho <10:
        return
    
    t.fd(tamanho)
    t.lt(90)
    quadradin(tamanho-10)

quadradin(tamanho)

turtle.done()