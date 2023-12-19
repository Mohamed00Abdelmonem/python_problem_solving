import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(20)


def random_color():
    r = random.randint(0, 255)
    d = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, d, b)
    return tuple


# move = [0, 90, 180, 270]
def draw(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.width(2)
        tim.color(random_color())
        tim.circle(100)

        tim.setheading(tim.heading() + size_of_gap)


draw(7)

screen = t.Screen()
screen.exitonclick()
