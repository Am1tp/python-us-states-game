from turtle import Turtle

class StateTurtle(Turtle):

    def __init__(self, x , y, text):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y) # go to x,y coor
        self.write(text) # turtle should write state name