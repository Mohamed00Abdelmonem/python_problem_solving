from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Test Snake game")
# screen.tracer(0)


snake = Snake()

snake.creating_snake()

is_on = True

while is_on:
    screen.update()




screen.exitonclick()
