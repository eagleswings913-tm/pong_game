
import turtle

class Border(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.pensize(4)
        self.penup()
        self.draw_border()
        self.hideturtle()

    def draw_border(self):
        self.goto(400, 300)
        self.pendown()
        self.setheading(180)
        self.forward(400 * 2)
        self.setheading(270)
        self.forward(300 * 2)
        self.setheading(0)
        self.forward(400 * 2)
        self.setheading(90)
        self.forward(300 * 2)
