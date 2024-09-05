import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.turn_east,'Right')
screen.onkey(snake.turn_west,'Left')
screen.onkey(snake.turn_north,'Up')
screen.onkey(snake.turn_south,'Down')
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for body in snake.body[1:]:
        if body.distance(snake.head) < 10:
            scoreboard.reset()
            snake.reset()


    
screen.exitonclick()