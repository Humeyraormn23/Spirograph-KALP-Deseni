import math
import turtle
window = turtle.Screen()
window.bgcolor("black")

pen= turtle.Turtle()
pen.speed(0)
pen.color("red")

def heart(t):
    x=16*math.sin(t)**3
    y=13*math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, y

pen.penup()
for i in range(10):
    pen.goto(0,0)
    pen.pendown()
    for t in range(0,100,2):
        x, y = heart(t / 10)
        pen.goto(x * i, y * i)
    pen.penup()

pen.hideturtle()
turtle.done()