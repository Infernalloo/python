from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"
POSITION = (-225, 255)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(POSITION)
        self.level = 1
        self.write(f"Level: {self.level}", False, font=FONT, align=ALIGN)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, font=FONT, align=ALIGN)

    def game_over(self):
        self.clear()
        self.level = 0
        self.goto(0, 0)
        self.write("Game Over", False, font=FONT, align=ALIGN)
