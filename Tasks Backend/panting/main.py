# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_rgp = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_rgp.append(new_color)
#
# print(color_rgp)

import random

color = [(226, 226, 225), (236, 236, 239), (182, 65, 34), (213, 149, 97), (14, 24, 42), (230, 237, 233), (239, 208, 94),
         (241, 234, 238), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), (166, 141, 66), (67, 41, 35),
         (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127), (229, 175, 161), (165, 64, 70), (167, 141, 150),
         (98, 113, 112), (160, 168, 165), (189, 190, 196), (217, 174, 180), (15, 25, 24), (79, 70, 43), (183, 196, 189),
         (119, 121, 147), (248, 196, 4)]

import turtle as t

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)
tim.setheading(225)
tim.penup()
tim.forward(350)
tim.setheading(0)

# def round_left():
#     tim.setheading(90)
#     tim.forward(50)
#     tim.setheading(180)
#
#     # tim.forward(50)
# def round_right():
#     tim.setheading(180)
#     tim.forward(50)
#     tim.setheading(90)

# def dot():
number_of_dot = 100
for dot_count in range(1, number_of_dot + 1):
    colors = random.choice(color)
    tim.dot(20, colors)

    tim.penup()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# for i in range(5):
#     dot()
#     round_left()
#     dot()
#     round_right()
screen = t.Screen()
screen.exitonclick()
