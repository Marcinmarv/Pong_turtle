from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
scoreboard = Scoreboard()

screen.title("Pong")
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 410:
        scoreboard.increase_score_left()
        ball.refresh()
    if ball.xcor() < -410:
        scoreboard.increase_score_right()
        ball.refresh()

screen.exitonclick()