import turtle
import tkinter as tk

def square():
    turtle.color("black")

    turtle.penup()
    turtle.goto(100, -120)
    turtle.pendown()

    for pen in range(4):
        turtle.left(90)
        turtle.forward(260)
    
square()

def round():
    turtle.color("blue")
    turtle.circle(260)

    turtle.exitonclick()

round()