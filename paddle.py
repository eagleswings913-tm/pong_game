
import turtle

class Paddle(turtle.Turtle):
    def __init__(self, paddle_location):
        super().__init__()
        self.my_paddle = turtle.Turtle(shape="square")
        self.my_paddle.penup()
        self.my_paddle.color('white')
        self.my_paddle.resizemode("user")
        self.my_paddle.shapesize(5, 1)
        self.paddle_location = paddle_location
        self.place_paddle(paddle_location)

    def place_paddle(self, paddle_location):
        if paddle_location == 'left':
            x_coordinate = -350
        else:
            x_coordinate = 350
        self.my_paddle.goto(x_coordinate, 15)

    def move_up(self):
        x_cor = self.my_paddle.xcor()
        y_cor = self.my_paddle.ycor()
        if y_cor < 275:
            self.my_paddle.goto(x_cor,y_cor + 20)

    def move_down(self):
        x_cor = self.my_paddle.xcor()
        y_cor = self.my_paddle.ycor()
        if y_cor > -265:
            self.my_paddle.goto(x_cor, y_cor - 20)
