from turtle import Turtle, Screen
import random


tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed('fastest')

def generate_random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


num_of_circles = int(input("Enter the number of circles (1 - 360): "))
for _ in range(num_of_circles):
    tim.color(generate_random_color())
    tim.circle(100)
    tim.right(360/num_of_circles)

screen.exitonclick()
