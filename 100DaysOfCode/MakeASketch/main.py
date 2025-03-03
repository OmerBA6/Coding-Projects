import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def forward():
    tim.forward(10)


def backwards():
    tim.backward(10)


def clockwise():
    tim.right(20)


def counter_clockwise():
    tim.left(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


turtle.onkey(fun=forward, key='w')
turtle.onkey(fun=backwards, key='s')
turtle.onkey(fun=counter_clockwise, key='a')
turtle.onkey(fun=clockwise, key='d')
turtle.onkey(fun=clear, key='c')


screen.exitonclick()
