import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

tim = Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def up():
    tim.forward(20)

def down():
    tim.backward(20)

def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()

def colour():
    tim.color(random_color())

tim.pensize(10)

screen = Screen()
screen.listen()
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")
screen.onkey(colour, "t")

screen.exitonclick()