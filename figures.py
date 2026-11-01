import turtle

def square(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pencolor(color)
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def triangle(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pencolor(color)
    turtle.forward(size)
    turtle.left(135)
    turtle.forward(size*0.707)
    turtle.left(90)
    turtle.forward(size*0.707)
    turtle.end_fill()

def ring(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pencolor(color)
    turtle.circle(size)
    turtle.end_fill()

def pr(size1, size2, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pencolor(color)
    for i in range(2):
        turtle.forward(size1)
        turtle.left(90)
        turtle.forward(size2)
        turtle.left(90)
    turtle.end_fill()
    
