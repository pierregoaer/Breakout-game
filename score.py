from turtle import Turtle
from data import SCREEN_HEIGHT, SCREEN_WIDTH
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.score = 0
        self.highscore = 0
        self.get_highscore()

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(SCREEN_WIDTH / 2 - 170, SCREEN_HEIGHT / 2 - 30)
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", align="center", font=FONT)

    def get_highscore(self):
        try:
            with open('highscore.txt') as file:
                self.highscore = int(file.read())
        except FileNotFoundError:
            self.highscore = 0
        self.write_score()

    def update_highscore(self):
        if self.score >= self.highscore:
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.score}")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! Score: {self.score}", align="center", font=FONT)

    def game_won(self):
        self.goto(0, 0)
        self.write(f"You Won!", align="center", font=FONT)
