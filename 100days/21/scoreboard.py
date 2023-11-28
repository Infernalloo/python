from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(x=0, y=250)
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def game_over_text(self):
        self.clear()
        self.score = 0
        self.goto(x=0, y=0)
        self.write("Game Over", False, align=ALIGN, font=FONT)