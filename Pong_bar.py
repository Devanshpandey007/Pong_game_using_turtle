import turtle
from turtle import Turtle, Screen
POSITION_1 = (-330,0), (-330,20), (-330,40), (-330,-20), (-330,-40)
POSITION_2 = (330,0), (330,20), (330,40), (330,-20), (330,-40)
UP = 90
DOWN = 270
class Bars:
    def __init__(self):
        self.bar_1 = []
        self.bar1_body()
        self.bar_2 = []
        self.bar2_body()
        # self.bar_1_head = self.bar_1[0]
        # self.bar_1_tail = self.bar_1[4]
        # self.bar_2_head = self.bar_2[0]
        # self.bar_2_tail = self.bar_2[4]
    def bar1_parts(self, pos1):
        self.box_1 = Turtle()
        self.box_1.shape('square')
        self.box_1.color('white')
        self.box_1.penup()
        self.box_1.goto(pos1)
        self.bar_1.append(self.box_1)
    def bar1_body(self):
        for pos1 in POSITION_1:
            self.bar1_parts(pos1)
    def bar2_parts(self,pos2):
        self.box_2 = Turtle()
        self.box_2.shape('square')
        self.box_2.color('white')
        self.box_2.penup()
        self.box_2.goto(pos2)
        self.bar_2.append(self.box_2)
    def bar2_body(self):
        for pos2 in POSITION_2:
            self.bar2_parts(pos2)

    def bar1_movement(self):
        for i in range(self.bar_1):
            self.box_1.setheading(UP)
            self.box_1.forward(20)
    def upper_movement(self):
        for i in self.bar_1:
            screen=Screen()
            screen.onclick()



