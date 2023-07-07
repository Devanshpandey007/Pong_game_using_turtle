# class Main:
#     def __init__(self,x):
#         num = 24
#         self.calc(x)
#         m = self.calc(x)
#         print(num + m)
#     def calc(self,object):
#         count = 0
#         for i in range(6):
#             count+=i*object
#         print(count)
#         return count
# main = Main(10)
# import pyautogui
# pyautogui.typewrite("hahah")
# pyautogui.press("Enter")

# from sketchpy import library as lib
#
# obj = lib.rdj()
# obj.draw()
from random import randint
from time import sleep
from turtle import Turtle,Screen
from random import choice
# t1 = Turtle()
# t2 = Turtle()
# t3 = Turtle()
# t4 = Turtle()
sc = Screen()

ch = randint(0,255)
colour = ["red","green","blue","black","cyan","indigo","pink","yellow","orange","violet"]
class Car_body:
    def __init__(self):
        self.lst = []
    def body(self,x,y):
        self.t = Turtle()
        self.t.shape("square")
        self.t.shapesize(1,2)
        self.t.color(choice(colour))
        self.t.penup()
        self.t.goto(x,y)
        self.t.speed(10)
        self.lst.append(self.t)




# t1.forward(20)
# t2.forward(20)
# t3.forward(20)
# t4.forward(20)
car = Car_body()
while True:
    sc.tracer(1)
    x = randint(-320, -280)
    y = randint(-200, 200)
    car.body(x,y)
    for i in car.lst:
        i.forward(20)
    sc.update()




