
import turtle
import random

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.player_turn = 1
        self.serve_ball()

    def next_player(self):
        if self.player_turn == 1:
            self.player_turn = 2
        else:
            self.player_turn = 1

    def serve_ball(self):
        while True:
            heading = random.randrange(0,180)
            if heading != 90:
                break
        if self.player_turn == 1:
            heading = heading - 90
        else:
            heading = heading + 90
        self.setheading(heading)

    def reset_ball(self):
        self.goto(0,0)

    def move(self):
        self.forward(20)

    def wall_bounce(self,ball_heading):
        new_heading = 10
        if 0 < ball_heading < 90:
            new_heading = (90 - ball_heading) + 270
        elif 90 < ball_heading < 180:
            new_heading = (180 - ball_heading) + 180
        elif 180 < ball_heading < 270:
            new_heading = (270 - ball_heading) + 90
        elif 270 < ball_heading < 360:
            new_heading = (360 - ball_heading) + 0
        self.setheading(new_heading)

    def paddle_bounce(self,ball_heading):
        new_heading = 10
        if 270 < ball_heading < 360:
            new_heading = (360 - ball_heading) + 180
        elif 0 < ball_heading < 90:
            new_heading = (90 - ball_heading) + 90
        elif 90 < ball_heading < 180:
            new_heading = (180 - ball_heading) + 0
        elif 180 < ball_heading < 270:
            new_heading = (270 - ball_heading) + 270
        self.setheading(new_heading)