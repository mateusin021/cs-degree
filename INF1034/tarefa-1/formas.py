def quadrado(t,x,y,tamanho,cor):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(cor)
    for i in range(4):
        t.forward(tamanho)
        t.left(90)
    t.penup()

def triangulo(t,x,y,tamanho,cor):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(cor)
    for i in range(3):
        t.forward(tamanho)
        t.right(120)
    t.penup()

def circulo(t,x,y,tamanho,cor):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(cor)
    t.circle(tamanho)
    t.penup()

def estrela(t,x,y,tamanho,cor):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(cor)
    for i in range(5):
        t.forward(tamanho)
        t.right(144)

    t.penup()