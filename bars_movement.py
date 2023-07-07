import turtle
from turtle import Turtle, Screen
# POSITION_1 = (-330,0), (-330,20), (-330,40), (-330,-20), (-330,-40)
# class guh:
#     def __init__(self):
#         self.list = []
#         self.whole()
#     def body(self,posi):
#         box = Turtle()
#         box.shape('square')
#         box.color('black')
#         box.penup()
#         box.goto(posi)
#         self.list.append(box)
#     def whole(self):
#         for posi in range(len(POSITION_1)):
#             self.body(posi)
# screen = Screen()
# screen.setup(width=700,height=700)
# bar = guh()
screen = Screen()
t1 = Turtle()
t1.shape('square')
t1.shapesize(6,1)
t2 = Turtle()
t2.shape('square')
t2.shapesize(6,1)
screen.setup(width=700,height=700)
t1.penup()
t1.goto(-330,280)
t2.penup()
t2.goto(330,-200)
screen.exitonclick()