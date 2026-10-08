
import turtle
import time

from paddle import Paddle
from ball import Ball

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

board = turtle.Turtle()
board.color("white")
board.hideturtle()
board.penup()
for i in range(-380, 410, 40):
    board.color("white")
    board.goto(0, i)
    board.write('|',True,"center",("Arial", 24, "normal"))

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

    # detect collision with walk
    if ball.ycor() > 275:
        print(f'x = {ball.xcor()}, y = {ball.ycor()}, heading = {ball.heading()}')
    if ball.ycor() > 275:
        # print(f'x = {ball.xcor()}, y = {ball.ycor()}')
        if 0 < ball.heading() < 90:
            new_heading = (90 - ball.heading()) + 270
            # print(f'new heading : {new_heading}')
            ball.setheading(new_heading)
    if ball.ycor() < -275:
        if 180 < ball.heading() < 270:
            new_heading = (270 - ball.heading()) + 90
            # print(f'new heading : {new_heading}')
            ball.setheading(new_heading)
    if ball.xcor() > 390:
        if 270 < ball.heading() < 360:
            new_heading = (360 - ball.heading()) + 180
            # print(f'new heading : {new_heading}')
            ball.setheading(new_heading)
    if ball.xcor() < -390:
        if 90 < ball.heading() < 180:
            new_heading = (180 - ball.heading()) + 0
            # print(f'new heading : {new_heading}')
            ball.setheading(new_heading)

screen.exitonclick()