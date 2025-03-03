from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

SCREE_WIDTH = 600
SCREEN_HEIGHT = 600
X_BORDER = 280
Y_BORDER = 280
FOOD_SENSITIVITY = 17.5
TAIL_SENSITIVITY = 10


screen = Screen()
screen.setup(width=SCREE_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < FOOD_SENSITIVITY:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > X_BORDER or snake.head.xcor() < -X_BORDER or snake.head.ycor() > Y_BORDER or snake.head.ycor() < -Y_BORDER:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < TAIL_SENSITIVITY:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
