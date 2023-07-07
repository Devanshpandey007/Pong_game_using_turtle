from turtle import Turtle, Screen
UP = 0
DOWN = 180
screen = Screen()
class Turtle1:
    def __init__(self):
        self.t1 = Turtle()
        self.t1.shape('square')
        self.t1.color('white')
        self.t1.penup()
        self.t1.goto(330,0)
        self.t1.shapesize(6,1)
    def upmov(self):
        self.b2 = self.t1.ycor()
        if self.b2<=280:
            self.t1.goto(330,self.b2+30)
        else:
            self.t1.goto(330,self.b2+0)
    def dowmov(self):
        self.b2= self.t1.ycor()
        if self.b2>=-280:
            self.t1.goto(330,self.b2-30)
        else:
            self.t1.goto(330,self.b2-0)
class Turtle2:
    def __init__(self):
        self.t2 = Turtle()
        self.t2.shape('square')
        self.t2.color('white')
        self.t2.penup()
        self.t2.goto(-330,0)
        self.t2.shapesize(6,1)
    def upmov(self):
        self.b1 = self.t2.ycor()
        if self.b1<=280:
            self.t2.goto(-330,self.b1+30)
        else:
            self.t2.goto(-330,self.b1+0)
    def dowmov(self):
        self.b1 = self.t2.ycor()
        if self.b1>=-280:
            self.t2.goto(-330,self.b1-30)
        else:
            self.t2.goto(-330,self.b1-0)
# bar1 = Turtle1()
# bar2 = Turtle2()
# screen.setup(height=700,width=700)
# screen.onkeypress(bar1.upmov, 'Up')
# screen.onkeypress(bar1.dowmov, 'Down')
# screen.onkeypress(bar2.upmov, 'w')
# screen.onkeypress(bar2.dowmov, 's')
# screen.listen()
# screen.exitonclick()