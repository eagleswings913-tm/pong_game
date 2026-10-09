
import turtle
import time

from board import Board
from border import Border
from paddle import Paddle
from ball import Ball

screen = turtle.Screen()
screen.setup(width=850, height=650)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

board = Board()
border = Border()
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
    time.sleep(0.2)
    ball.move()

    # detect collision with paddle
    if ball.distance(left_paddle) < 20:
        print(ball.distance(left_paddle))
        paddle_top = left_paddle.ycor() + 40
        paddle_bottom = left_paddle.ycor() - 40
        if paddle_bottom < ball.ycor() < paddle_top:
            ball.setheading(45)
    if ball.distance(right_paddle) < 20:
        print(ball.distance(right_paddle))
        paddle_top = right_paddle.ycor() + 40
        paddle_bottom = right_paddle.ycor() - 40
        if paddle_bottom < ball.ycor() < paddle_top:
            ball.setheading(135)


    # detect collision with wall
    if ball.ycor() > 280:
        if 0 < ball.heading() < 90:
            new_heading = (90 - ball.heading()) + 270
            ball.setheading(new_heading)
        elif 90 < ball.heading() < 180:
            new_heading = (180 - ball.heading()) + 180
            ball.setheading(new_heading)
    if ball.ycor() < -280:
        if 180 < ball.heading() < 270:
            new_heading = (270 - ball.heading()) + 90
            ball.setheading(new_heading)
        elif 270 < ball.heading() < 360:
            new_heading = (360 - ball.heading()) + 0
            ball.setheading(new_heading)
    if ball.xcor() > 380:
        if 270 < ball.heading() < 360:
            new_heading = (360 - ball.heading()) + 180
            ball.setheading(new_heading)
        elif 0 < ball.heading() < 90:
            new_heading = (90 - ball.heading()) + 90
            ball.setheading(new_heading)
    if ball.xcor() < -380:
        if 90 < ball.heading() < 180:
            new_heading = (180 - ball.heading()) + 0
            ball.setheading(new_heading)
        if 180 < ball.heading() < 270:
            new_heading = (270 - ball.heading()) + 270
            ball.setheading(new_heading)

screen.exitonclick()