
import turtle
import time

from board import Board
from border import Border
from score import Score
from paddle import Paddle
from ball import Ball

screen = turtle.Screen()
screen.setup(width=850, height=650)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

board = Board()
border = Border()
score_board = Score()
right_paddle = Paddle('right')
left_paddle = Paddle('left')
ball = Ball()

screen.listen()
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    new_heading = 10
    # detect collision with paddle
    if (330 <= ball.xcor() < 350 and ball.distance(right_paddle) <= 50) or (-330 >= ball.xcor() >= -350 and ball.distance(left_paddle) <= 50):
        ball.paddle_bounce(ball.heading())

    # detect collision with top and bottom walls
    ball_y = ball.ycor()
    if ball_y > 280 or ball_y < -280:
        ball.wall_bounce(ball.heading())

    # detect player missing the ball
    if ball.xcor() > 380:
        if 270 < ball.heading() < 360:
            new_heading = (360 - ball.heading()) + 180
        elif 0 < ball.heading() < 90:
            new_heading = (90 - ball.heading()) + 90
        ball.setheading(new_heading)
    if ball.xcor() < -380:
        if 90 < ball.heading() < 180:
            new_heading = (180 - ball.heading()) + 0
        if 180 < ball.heading() < 270:
            new_heading = (270 - ball.heading()) + 270
        ball.setheading(new_heading)

screen.exitonclick()