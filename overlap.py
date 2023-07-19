import turtle
import tkinter as tk

turtle.color("black")

turtle.penup()
turtle.goto(50, 50)
turtle.pendown()

for pen in range(4):
    turtle.left(90)
    turtle.forward(300)

turtle.exitonclick()