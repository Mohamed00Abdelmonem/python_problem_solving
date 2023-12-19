from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.creating_snake()
        self.head = self.segments[0]

    def creating_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):

