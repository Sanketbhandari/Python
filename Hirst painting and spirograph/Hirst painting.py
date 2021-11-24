import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.pu()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1,101):
    tim.dot(25,random_color())
    tim.pu()
    tim.forward(50)
    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
