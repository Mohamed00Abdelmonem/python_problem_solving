from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def up_move():

    tim.forward(10)


def right_move():
    tim.right(10)

def down_move():
    tim.backward(10)
def left_move():
    tim.left(10)

def clear_move():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(up_move, "Up")
screen.onkey(right_move, "Right")
screen.onkey(down_move, "Down")
screen.onkey(left_move, "Left")
screen.onkey(clear_move, "Delete")
screen.exitonclick()