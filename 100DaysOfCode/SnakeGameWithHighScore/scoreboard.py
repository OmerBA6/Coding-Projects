from turtle import Turtle

SCOREBOARD_POSITION = (0, 270)
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as file:
                self.high_score = self.score
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
