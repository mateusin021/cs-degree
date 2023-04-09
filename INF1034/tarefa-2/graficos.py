import turtle
from math import sqrt
import eixos_turtle

t=turtle.Turtle()
eixos_turtle.plotEixosCartesianos(t,25,15)
x=0
while(x<=10): 
  y=sqrt(x)*-1
  eixos_turtle.plotponto(t,x,y,15)
  x=x+0.2

t.clear()

eixos_turtle.plotEixosCartesianos(t,25,15)
x=-5
while(x<=0): 
  y=(1/x**2) * (-1)
  eixos_turtle.plotponto(t,x,y,15)
  x=x+0.2

t.clear()

eixos_turtle.plotEixosCartesianos(t,25,15)
x=-5
while(x<=5): 
  y=(2**x) * (-1)
  eixos_turtle.plotponto(t,x,y,15)
  x=x+0.2

t.clear()

eixos_turtle.plotEixosCartesianos(t,25,15)
x=-5
while(x<=5): 
  y=(5-x**2) * (-1)
  eixos_turtle.plotponto(t,x,y,15)
  x=x+0.2

t.clear()

eixos_turtle.plotEixosCartesianos(t,25,15)
x=-5
while(x<=5): 
  y=((x+2)*(x-2)) * (-1)
  eixos_turtle.plotponto(t,x,y,15)
  x=x+0.2

turtle.done()