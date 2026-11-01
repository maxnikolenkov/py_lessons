import turtle

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


def triangle(size):
    turtle.forward(size)
    turtle.left(135)
    turtle.forward(size*0.707)
    turtle.left(90)
    turtle.forward(size*0.707)
    
square(200)
triangle(200)







turtle.exitonclick()
