# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import turtle
import twilio


def drawSquare(_turtle):

    for i in range(0, 4):
        _turtle.forward(100)
        _turtle.right(90)


def drawStuff():
    print(twilio.__version__)
    window = turtle.Screen()
    window.bgcolor("red")
    
    kyle = turtle.Turtle()

    kyle.color("blue")
    kyle.shape("turtle")

    for i in range(0, 36):
        drawSquare(kyle)        
        kyle.right(10)
    
    #isaac = turtle.Turtle()
    #isaac.shape("arrow")
    #isaac.circle(100)

    window.exitonclick()

drawStuff()