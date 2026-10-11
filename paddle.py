
import turtle

class Paddle(turtle.Turtle):
    def __init__(self, paddle_location):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color('white')
        self.resizemode("user")
        self.shapesize(5, 1)
        self.location = paddle_location
        self.place_paddle(paddle_location)

    def place_paddle(self, paddle_location):
        if paddle_location == 'left':
            x_coordinate = -350
        else:
            x_coordinate = 350
        self.goto(x_coordinate, 15)

    def move_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        if y_cor < 250:
            self.goto(x_cor,y_cor + 30)
        # print(f'xcor = {x_cor}, ycor = {y_cor}')

    def move_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        if y_cor > -240:
            self.goto(x_cor, y_cor - 20)
        # print(f'xcor = {x_cor}, ycor = {y_cor}')