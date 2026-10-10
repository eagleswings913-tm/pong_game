
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
missed_ball = False

screen.listen()
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.update()

def reset_game():
    ball.reset_ball()
    ball.next_player()
    right_paddle.place_paddle('right')
    left_paddle.place_paddle('left')
    ball.serve_ball()
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
        ball.move()
        score_board.update_score(1)
        missed_ball = True
    if ball.xcor() < -380:
        ball.move()
        score_board.update_score(2)
        missed_ball = True
    if missed_ball:
        reset_game()
        while True:
            user_input = (screen.textinput(title="Play again? ('y' or 'n')", prompt="Wait for a key")).lower()
            if user_input == 'n':
                game_on = False
                break
            elif user_input == 'y':
                break
        missed_ball = False
        screen.getcanvas().focus_force()
        screen.listen()

print("Game over! Thanks for playing!")

screen.exitonclick()