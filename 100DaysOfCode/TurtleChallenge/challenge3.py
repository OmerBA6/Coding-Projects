from turtle import Turtle, Screen
import random


tim = Turtle()
screen = Screen()
screen.colormode(255)


def draw_shape(sides_number):
    for i in range(sides_number):
        tim.right(360/sides_number)
        tim.forward(100)


for num_of_sides in range(3, 11):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw_shape(num_of_sides)

screen.exitonclick()
