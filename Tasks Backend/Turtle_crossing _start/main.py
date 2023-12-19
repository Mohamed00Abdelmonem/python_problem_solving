from turtle import Screen
import time
from player import Player
from car_manger import Car_manger
from scoreboard import Scoreboard


screen = Screen()
car_manger = Car_manger()
player = Player()
scoreboard = Scoreboard()
screen.bgcolor("white")
screen.setup(600, 600)
screen.tracer(0)
screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manger.create_car()
    car_manger.move_cars()

    # Detect collision with car
    for car in car_manger.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manger.level_up()
        scoreboard.new_score()



screen.exitonclick()