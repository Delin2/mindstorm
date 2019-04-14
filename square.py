import turtle

def draw_square(turtle):
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("green")
    bob.speed(10)
    draw_square(bob)
    
    window.exitonclick()

draw_art()
