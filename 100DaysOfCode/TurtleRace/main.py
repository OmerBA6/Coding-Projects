from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []


def send_to_starting_position(turtle_to_send, position):
    turtle_to_send.penup()
    y_starting_position = 200 - ((screen.window_height()/(len(colors)+1))*position)
    turtle_to_send.goto(x=-230, y=y_starting_position)


for color in colors:
    turtles.append(Turtle(shape='turtle'))
    turtles[-1].color(color)
    starting_position = colors.index(color) + 1
    send_to_starting_position(turtles[-1], starting_position)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
