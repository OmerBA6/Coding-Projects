from turtle import Turtle

FONT = ("Ariel", 14, "normal")


class StateTurtle(Turtle):

    def __init__(self, state_name, location):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(location)
        self.write(f"{state_name}", align='center', font=FONT)

