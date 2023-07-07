import turtle
from turtle import Turtle
class Score_Board():
    def __init__(self):
        self.sc1 = Turtle()
        self.sc2 = Turtle()
        self.sc1.color('white')
        self.sc2.color('white')
        self.sc1.penup()
        self.sc2.penup()
        self.sc1.hideturtle()
        self.sc2.hideturtle()
        self.score_table_1 = 0
        self.score_table_2 = 0
        self.left_score()
        self.right_score()
    def left_score(self):
        self.sc1.goto(150, 310)
        self.sc1.write(f'Score = {self.score_table_1}', False, align='left', font=('Arial', 15, 'normal'))
    def right_score(self):
        self.sc2.goto(-240, 310)
        self.sc2.write(f'Score = {self.score_table_1}', False, align='left', font=('Arial', 15, 'normal'))
    def Update_score_l(self):
        self.score_table_1+=10
        self.sc1.clear()
        self.left_score()
    def Update_score_r(self):
        self.score_table_2+=10
        self.sc2.clear()
        self.right_score()


