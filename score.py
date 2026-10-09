
import turtle
FONT = ("Arial", 24, "normal")

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.write_score()

    def write_score(self):
        self.goto(-100,250)
        self.write(f"{self.player1_score}",font=FONT)
        self.goto(80,250)
        self.write(f"{self.player2_score}",font=FONT)

    def update_score(self):
        pass
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
