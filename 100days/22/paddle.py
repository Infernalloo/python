from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        new_ycord = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_ycord)

    def down(self):
        new_ycord = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_ycord)
