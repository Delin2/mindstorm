from turtle import *

def draw_square():
    window.bgcolor("black")

    bob = turtle.Turtle()
    bob.speed(10)
    bob.forward(100)
    bob.right(90)
    bob.forward(100)
    bob.right(90)
    bob.forward(100)
    bob.right(90)
    bob.forward(100)
    bob.right(90)

    window.exitonclick()
