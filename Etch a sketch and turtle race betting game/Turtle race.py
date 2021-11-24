from turtle import Turtle, Screen
import random

race_on = False
color = ["red", "blue", "green", "cyan", "pink", "orange"]
screen= Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter a color: ").lower()
y_position = [-75, -45, -15, 15, 45, 75]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x= -230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 215:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} Turtle is the winner")

            else:
                print(f"You've lost! The {winning_color} Turtle is the winner")


        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)

screen.exitonclick()

