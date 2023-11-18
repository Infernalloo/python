from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_one = Paddle((350, 0))
paddle_two = Paddle((-350, 0))

ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(paddle_one.up, "Up")
screen.onkey(paddle_one.down, "Down")
screen.onkey(paddle_two.up, "w")
screen.onkey(paddle_two.down, "s")

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(paddle_one) < 50 and ball.xcor() > 320 or ball.distance(paddle_two) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.left_point()
        time.sleep += 0.1

    if ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.right_point()
        time.sleep += 0.1

screen.exitonclick()
