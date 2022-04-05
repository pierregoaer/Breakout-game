from turtle import Turtle
from data import SCREEN_HEIGHT, SCREEN_WIDTH


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=8, outline=1)
        self.penup()
        self.goto(0, -SCREEN_HEIGHT / 2 + 30)

    def go_left(self):
        if not self.xcor() < -SCREEN_WIDTH / 2 + 90:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def go_right(self):
        if not self.xcor() > SCREEN_WIDTH / 2 - 90:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
