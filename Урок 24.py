from figures import *
import turtle
import random
turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()
color = ["red", "black", "blue", "yellow", "green", "brown", "pink", "purple"]

for i in range(1000):
    turtle.penup()
    turtle.goto(random.randint(-400,400), random.randint(-320,320))
    ring(5,"white")
turtle.exitonclick()
