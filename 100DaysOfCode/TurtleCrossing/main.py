import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


FINISH_LINE_Y = 280
CARS_TOUCH_SENSITIVITY = 17.5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # If reached to finish line
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        scoreboard.level_up()
        car_manager.level_up()

    # If touches a car
    for car in car_manager.all_cars:
        if player.distance(car) < CARS_TOUCH_SENSITIVITY:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
