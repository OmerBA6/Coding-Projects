from turtle import Turtle
from random import randint

STEP = 20


class Ball(Turtle):

    def __init__(self, starting_direction):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.direction = starting_direction

    def move(self):
        self.setheading(self.direction)
        self.forward(STEP)

    def bounce(self, wall_bounce=False, paddle_bounce=False):
        if wall_bounce:
            if self.direction < 90:
                self.direction = randint(290, 340)
            elif self.direction > 270:
                self.direction = randint(20, 70)
            elif 90 < self.direction < 180:
                self.direction = randint(200, 250)
            elif 180 < self.direction < 270:
                self.direction = randint(110, 160)
        elif paddle_bounce:
            if 270 < self.direction < 360:
                self.direction = randint(200, 250)
            elif 0 < self.direction < 90:
                self.direction = randint(110, 160)
            elif 180 < self.direction < 270:
                self.direction = randint(290, 340)
            elif 90 < self.direction < 180:
                self.direction = randint(20, 70)

    def out_of_bounce(self):
        self.home()
        if 90 < self.direction < 270:
            self.direction = randint(20, 70)
        else:
            self.direction = randint(110, 250)
