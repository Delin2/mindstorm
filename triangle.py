import turtle
import math

def draw_triangle(turtle):
    turtle.right(45)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(math.sqrt(2*math.pow(100, 2)))
    turtle.right(135)
    turtle.forward(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    tri = turtle.Turtle()
    tri.shape("turtle")
    tri.color("green")
    tri.speed(10)
    draw_triangle(tri)
    
    window.exitonclick()

draw_art()
