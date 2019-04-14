import turtle

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("white")

    cir = turtle.Turtle()
    cir.shape("turtle")
    cir.color("green")
    cir.speed(10)
    cir.circle(100)
    
    window.exitonclick()

draw_circle()
