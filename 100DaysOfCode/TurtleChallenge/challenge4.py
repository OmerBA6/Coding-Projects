from turtle import Turtle, Screen
import random


tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed('fastest')
tim.pensize(15)

for _ in range(1000):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    num_of_turns = random.randint(0,3)
    for __ in range(num_of_turns):
        tim.right(90)
    tim.forward(30)

screen.exitonclick()
