from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
import random

SCREE_WIDTH = 800
SCREEN_HEIGHT = 600

PADDLE_R_STARTING_POSITION = (350, 0)
PADDLE_L_STARTING_POSITION = (-350, 0)
BALL_START_HEADING_DIRECTION = random.randint(0, 360)


TOP_BORDER = 280
BOTTOM_BORDER = -280

PADDLE_TOUCH_SENSITIVITY = 50
PADDLE_WALL_TOUCH_SENSITIVITY = 320
OUT_OF_BOUNCE_SENSITIVITY = 390


screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREE_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(PADDLE_R_STARTING_POSITION)
l_paddle = Paddle(PADDLE_L_STARTING_POSITION)
ball = Ball(BALL_START_HEADING_DIRECTION)
scoreboard = ScoreBoard()

screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with top or bottom walls
    if ball.ycor() > TOP_BORDER or ball.ycor() < BOTTOM_BORDER:
        ball.bounce(wall_bounce=True)

    # detect collision with paddles
    if ball.distance(r_paddle) < PADDLE_TOUCH_SENSITIVITY and ball.xcor() > PADDLE_WALL_TOUCH_SENSITIVITY:
        ball.bounce(paddle_bounce=True)
    elif ball.distance(l_paddle) < PADDLE_TOUCH_SENSITIVITY and ball.xcor() < -PADDLE_WALL_TOUCH_SENSITIVITY:
        ball.bounce(paddle_bounce=True)

    # Left paddle point
    if ball.xcor() > OUT_OF_BOUNCE_SENSITIVITY:
        ball.out_of_bounce()
        scoreboard.l_point()

    # Right paddle point
    if ball.xcor() < -OUT_OF_BOUNCE_SENSITIVITY:
        ball.out_of_bounce()
        scoreboard.r_point()


screen.exitonclick()
