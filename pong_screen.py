import turtle
from random import choice, randint
from Pong_score import Score_Board
from testo import Turtle1,Turtle2
from Pong_ball import Ball
from time import sleep
from turtle import Screen
screen = Screen()
screen.setup(width=700,height=700)
screen.bgcolor('black')
screen.title('Pong')
x = screen.textinput('Player Info','Please Type Your Email Id')
bar1 = Turtle1()
bar2 = Turtle2()
ball = Ball()
score_table = Score_Board()
screen.onkeypress(bar1.upmov, 'Up')
screen.onkeypress(bar1.dowmov, 'Down')
screen.onkeypress(bar2.upmov, 'w')
screen.onkeypress(bar2.dowmov, 's')
screen.listen()
print(x)

game_is_on = True
while game_is_on:
    sleep(0.1)
    # screen.update()
    print(ball.ball.xcor())
    ball.coordinates()
    if ball.ball.ycor()>290 or ball.ball.ycor()<-290:
        ball.bounce()
    if ball.ball.distance(bar1.t1)<60 and ball.ball.xcor()>300:
        ball.rev_bounce()
        score_table.Update_score_l()

    if ball.ball.distance(bar2.t2)<60 and ball.ball.xcor()<-300:
        ball.rev_bounce()
        score_table.Update_score_r()
    if ball.ball.xcor()>360 or ball.ball.xcor()<-360:
        ball.reset()
        ball.rev_bounce()

screen.exitonclick()


