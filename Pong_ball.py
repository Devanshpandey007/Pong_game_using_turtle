from turtle import Turtle,Screen
from time import sleep
from random import randint
class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.goto(0,0)
        self.x_posi = 10
        self.y_posi = 10
    def coordinates(self):
        self.new_x = self.ball.xcor()+self.x_posi
        self.new_y = self.ball.ycor()+self.y_posi
        self.ball.goto(self.new_x, self.new_y)
    def bounce(self):
        self.y_posi*=-1
    def rev_bounce(self):
        self.x_posi*=-1
    def reset(self):
        self.ball.goto(0,0)
