import turtle

t = turtle.Turtle()

nivel = 1
tamanho =100
t.lt(90)

def galho(nivel, tamanho):
    if nivel > 5:
        return
    t.fd(tamanho)
    t.lt(30)
    galho(nivel+1,tamanho-20)
    t.rt(60)
    galho(nivel+1,tamanho-20)
    t.lt(30)

    t.bk(tamanho)


galho(nivel,tamanho)

turtle.done()