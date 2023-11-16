from turtle import Turtle
# the variable is in all caps
# because it's a const, so it's never
# going to change, and so we use this
# format, so we can recognize it
STARTING_POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# create a snake class
class Snake:
    def __init__(self):
        self.body_squares = []
        self.create_snake()
        self.head = self.body_squares[0]

    def create_snake(self):
        for position in range(2):
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.body_squares[-1].position())

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(x=STARTING_POSITION[position], y=0)
        self.body_squares.append(tim)

    def move(self):
        for body_num in range(len(self.body_squares) - 1, 0, -1):
            new_x = self.body_squares[body_num - 1].xcor()
            new_y = self.body_squares[body_num - 1].ycor()
            self.body_squares[body_num].goto(x=new_x, y=new_y)
        self.body_squares[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
