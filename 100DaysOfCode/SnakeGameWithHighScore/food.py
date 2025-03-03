from turtle import Turtle
import random

FOOD_LIMIT_X = 270
FOOD_LIMIT_Y = 260


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-FOOD_LIMIT_X, FOOD_LIMIT_X)
        random_y = random.randint(-FOOD_LIMIT_Y, FOOD_LIMIT_Y)
        self.goto(random_x, random_y)