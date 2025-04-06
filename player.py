from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_up(self):
        self.forward(10)

    def start_again(self):
        self.goto(STARTING_POSITION)

    def cross_last_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False