import turtle
import formas
import eixos_turtle
import bandeiras
from random import randint

t = turtle.Turtle()
# desenha o eixo cartesiano
t.penup()
t.goto(-400, 0)
t.pendown()
t.goto(400, 0)
t.penup()
t.goto(0, -400)
t.pendown()
t.goto(0, 400)

cor = turtle.textinput("cor", 'insira a cor da primeira forma')
formas.quadrado(t, randint(0, 300), randint(0, 300), 100, cor)

cor = turtle.textinput("cor", 'insira a cor da segunda forma')
formas.triangulo(t, randint(-300, 0), randint(0, 300), 50, cor)

cor = turtle.textinput("cor", 'insira a cor da terceira forma')
formas.circulo(t, randint(-300, 0), randint(-300, 0), 50, cor)

cor = turtle.textinput("cor", 'insira a cor da quarta forma')
formas.estrela(t, randint(0, 300), randint(-300, 0), 50, cor)

cor = turtle.textinput("cor", 'insira a cor da espiral')
formas.espiral(t, randint(-300, 0), randint(-300, 0), 40, cor)

t.reset()


bandeiras.bandeira_marrocos(t, -200, 200)

bandeiras.bandeira_turquia(t, 200, 200)

bandeiras.bandeira_brasil(t, -100, 0)

turtle.done()
