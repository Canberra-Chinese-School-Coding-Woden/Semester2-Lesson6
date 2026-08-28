import turtle
import random

# ---------- Setup ----------
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0)
t.pensize(1)
t.pencolor("black")
t.fillcolor("orange")
screen.bgcolor("skyblue")
screen.setup(1000, 500)

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def five_pointed_star():
    t.begin_fill()
    for i in range(5):
        t.forward(100)
        t.left(215)
    t.end_fill()

for i in range(30):
    go(random.randint(-500,500),random.randint(-250,250))
    five_pointed_star()







