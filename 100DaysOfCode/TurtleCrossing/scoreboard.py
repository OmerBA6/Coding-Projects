from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_ALIGNMENT = 'left'
SCOREBOARD_POSITION = (-275, 250)
GAME_OVER_ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Level: {self.level}", align=SCOREBOARD_ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.home()
        self.write("GAME OVER.", align=GAME_OVER_ALIGNMENT, font=FONT)