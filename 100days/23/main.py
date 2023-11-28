import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("TurtlPy road")
screen.tracer(0)

turtle = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(turtle.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.move_cars()

    if turtle.ycor() >= 280:
        score.level_up()
        turtle.reset_position()

    for car in cars.cars_list:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
