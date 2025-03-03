# import colorgram
#
# color_from_image = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in color_from_image:
#     rgb_tup = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rgb_tup)
#
# print(rgb_colors)


# window width = 720
# window height = 675

from turtle import Turtle, Screen
import random

colors_list = [(43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147),
               (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110), (116, 168, 37),
               (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108), (154, 222, 193), (181, 170, 221),
               (30, 163, 170), (84, 35, 39), (40, 46, 80), (233, 167, 180), (237, 172, 162), (76, 40, 39),
               (154, 208, 221), (115, 46, 43)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.screensize(500, 500)
tim.speed('fastest')
tim.hideturtle()
starting_x = -225
starting_y = -225


def draw_line_of_dots():
    for _ in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.penup()
        tim.forward(50)


tim.penup()
tim.setpos(starting_x, starting_y)

for _ in range(10):
    draw_line_of_dots()
    tim.penup()
    tim.setpos(starting_x, tim.ycor() + 50)










screen.exitonclick()
