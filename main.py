import time

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()
car=CarManager()
screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True

dongu=0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # if random.randint(1, 100) <= 10:  # Yüzde 10 olasılık
    if dongu%6==0:
        car.create_car()
    car.move()
    for each_car in car.all_cars:
        if player.distance(each_car) < 20:
            print("kaybettin")
            scoreboard.is_lose()
            game_is_on = False

    if player.ycor()==280:
        player.control()
        car.hız_art()
        scoreboard.level_up()
    dongu+=1
screen.exitonclick()

