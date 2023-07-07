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
    def bar1_parts(self,pos1):
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

    def bar1_Uppermovement(self):
        for i in self.bar_1:
            self.box_1.setheading(UP)
            self.box_1.forward(20)
    def bar1_downwardMovement(self):
        for j in self.bar_1:
            self.box_1.setheading(DOWN)
            self.box_1.forward(20)
    def bar2_Uppermovement(self):
        for k in self.bar_2:
            self.box_1.setheading(UP)
            self.box_2.forward(20)
    def bar2_DownwardMovement(self):
        for l in self.bar_2:
            self.box_2.setheading(DOWN)
            self.box_2.forward(20)






screen = Screen()
screen.title('Pong')
screen.setup(width=700,height=700)
screen.bgcolor('black')
base = Bars()
screen.onclick(base.bar1_Uppermovement, 'Up')
screen.onclick(base.bar1_downwardMovement, 'Down')
screen.onclick(base.bar2_Uppermovement, 'w')
screen.onclick(base.bar2_DownwardMovement, 's')
screen.listen()
screen.exitonclick()