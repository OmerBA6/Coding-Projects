from turtle import Turtle

PADDLE_STRETCH_WIDTH = 1
PADDLE_STRETCH_HEIGHT = 5
UP_HEADING = 90
DOWN_HEADING = 270
STEP = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=PADDLE_STRETCH_WIDTH, stretch_len=PADDLE_STRETCH_HEIGHT)
        self.goto(position)
        self.setheading(UP_HEADING)

    def move_up(self):
        self.forward(STEP)

    def move_down(self):
        self.backward(STEP)

