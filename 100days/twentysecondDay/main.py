from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_one = Paddle((350, 0))
paddle_two = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle_one.up, "Up")
screen.onkey(paddle_one.down, "Down")
screen.onkey(paddle_two.up, "w")
screen.onkey(paddle_two.down, "s")

game_over = False
while not game_over:
    screen.update()

screen.exitonclick()
