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
    turtle.pencolor(color)
    turtle.circle(size)

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
    
square(200, "yellow")
turtle.left(90)
turtle.forward(200)
turtle.right(90)
triangle(200, "red")
turtle.left(45)
turtle.penup()
turtle.forward(125)
turtle.pendown()
turtle.left(90)
turtle.penup()
turtle.forward(67)
turtle.pendown()
square(50, "skyblue")

turtle.right(135)
turtle.penup()
turtle.forward(400)
turtle.pendown()
turtle.right(135)
pr(50, 100, "brown")
#turtle.right(135)
#turtle.forward(200)
#turtle.right(135)
#turtle.forward(142)
#turtle.left(90)
#turtle.forward(142)







turtle.exitonclick()
