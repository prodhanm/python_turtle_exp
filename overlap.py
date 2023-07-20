import turtle
import tkinter as tk

def square(x,y):
    turtle.color("black")

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    for pen in range(4):
        turtle.left(90)
        turtle.forward(200)
    
square(150,-120)

def round(x):
    turtle.color("blue")
    turtle.circle(x)

round(200)
square(350,80)

def triang(x,y):
    turtle.color("red")
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    #for pen in range(3):
    #    turtle.left(45)
    #    turtle.forward(100)
    # used for a three side hex shape

    for pen in range(2):
        turtle.left(90)
        turtle.forward(200)

    turtle.left(135)
    turtle.forward(280)

    turtle.exitonclick()

triang(150,-120)
#triang(120,-150)