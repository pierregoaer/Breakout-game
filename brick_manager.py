from turtle import Turtle
from data import SCREEN_HEIGHT, SCREEN_WIDTH

row_colours = ["red", "red", "orange", "orange", "green", "green", "yellow", "yellow"]


class BrickManager(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        x_pos = - SCREEN_WIDTH / 2 + 40
        for _ in range(18):
            y_pos = SCREEN_HEIGHT / 2 - 30
            for row in range(5):
                new_brick = Turtle(shape="square")
                new_brick.color(row_colours[row])
                new_brick.shapesize(stretch_wid=1, stretch_len=3, outline=1)
                new_brick.penup()
                y_pos -= 25
                new_brick.goto(x_pos, y_pos)
                self.bricks.append(new_brick)
            x_pos += 65

    def remove_brick(self, brick):
        brick.hideturtle()
        self.bricks.remove(brick)
