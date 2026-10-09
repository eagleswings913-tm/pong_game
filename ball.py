
import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.setheading(170)

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