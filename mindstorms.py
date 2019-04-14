import turtle

def draw_square(turtle):
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)

def draw_art():
    window = turtle.Screen()

    #make square with turtle named bob
    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("green")
    bob.speed(30)

    #make circle out of squares
    for i in range(0, 36):
        draw_square(bob)
        bob.right(10)

    #make circle with turtle named cir
    #cir = turtle.Turtle()
    #cir.shape("arrow")
    #cir.color("black")
    #cir.speed(30)
    #cir.circle(100)

    window.exitonclick()

draw_art()
