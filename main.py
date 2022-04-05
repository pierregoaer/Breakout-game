from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick_manager import BrickManager
from score import Score
from data import SCREEN_HEIGHT, SCREEN_WIDTH
import time


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
brick_manager = BrickManager()
score = Score()

screen.listen()
screen.onkey(fun=paddle.go_left, key="Left")
screen.onkey(fun=paddle.go_right, key="Right")


game_is_on = True
sleep_time = 0.07
speed_increase_count = 0

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()
    speed_increase_count += 1

    if score.score != 0 and speed_increase_count % 150 == 0:
        sleep_time *= 0.95

    if ball.xcor() > SCREEN_WIDTH / 2 - 20 or ball.xcor() < - SCREEN_WIDTH / 2 + 20:
        ball.left_right_bounce()

    if ball.ycor() > SCREEN_HEIGHT / 2 - 20 or\
            (ball.distance(paddle) < 80 and ball.ycor() < - SCREEN_HEIGHT / 2 + 50 and ball.y_move < 0):
        ball.top_bottom_bounce()

    if ball.ycor() < - SCREEN_HEIGHT / 2:
        game_is_on = False
        # ball.reset_ball()
        screen.update()
        score.update_highscore()
        score.game_over()

    if len(brick_manager.bricks) == 0:
        game_is_on = False
        score.update_highscore()
        score.game_won()

    for brick in brick_manager.bricks:
        if ball.distance(brick) < 25:
            brick_manager.remove_brick(brick)
            ball.top_bottom_bounce()
            score.increase_score()


screen.exitonclick()
