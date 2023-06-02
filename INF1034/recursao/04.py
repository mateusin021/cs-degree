import turtle

t = turtle.Turtle()

nivel = 1
tamanho =200
t.lt(90)

def quadrado(nivel, tamanho):
    if nivel > 4:
        return
    for i in range(4):
        t.fd(tamanho)
        t.lt(90)
        quadrado(nivel+1,tamanho*0.35)



quadrado(nivel,tamanho)

turtle.done()