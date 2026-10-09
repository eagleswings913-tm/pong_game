
import turtle

class Board(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.draw_center_line()

    def draw_center_line(self):
        for i in range(-300, 300, 40):
            self.color("white")
            self.goto(0, i)
            self.write('|',True,"center",("Arial", 24, "normal"))
