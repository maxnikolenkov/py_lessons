import turtle 
#Настройки окна
screen = turtle.Screen()
screen.title("Проект paint")
screen.bgcolor("black")
#Настройки turtle(Ручки)
t = turtle.Turtle()
t.color("white")
t.speed(3)
t.width(5)
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#Буква P
move(-250,50)
t.left(90)
t.forward(100)
t.right(90)
t.circle(-25,180)
#Буква A
move(-170, 50)
t.goto(-140,150)
t.goto(-110,50)
move(-150,90)
t.goto(-130,90)
#Буква I
move(-70,50)
t.setheading(90)
t.forward(100)
#Буква N
move(-20,50)
t.setheading(90)
t.forward(100)
t.goto(30,50)
t.setheading(90)
t.forward(100)
#Буква T
move(130,50)
t.setheading(90)
t.forward(100)
move(80,150)
t.setheading(0)
t.forward(100)
t.hideturtle()

#Настройки кисточки
brush=turtle.Turtle()
brush.shape("turtle")
brush.color("red")
brush.width(4)
brush.speed(0)
brush.penup()
brush.goto(0,-50)
brush.pendown()

#Функция рисования
def start_draw(x,y):
    brush.penup()
    brush.goto(x,y)
    brush.pendown()

def draw(x,y):
    brush.goto(x,y)

#Хождение по кнопку
step=20
def move_up():
    brush.setheading(90)
    brush.forward(step)
def move_right():
    brush.setheading(0)
    brush.forward(step)
def move_left():
    brush.setheading(180)
    brush.forward(step)
def move_down():
    brush.setheading(270)
    brush.forward(step)
#Функции фигур
def draw_square():
    for i in range(4):
        brush.forward(50)
        brush.left(90)
def draw_triangle():
    for i in range(3):
        brush.forward(50)
        brush.left(120)
def draw_circle():
    brush.circle(30)
def clear_screen():
    brush.clear()
screen.listen()
screen.onscreenclick(start_draw, 1)
brush.ondrag(draw)
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")
screen.onkeypress(draw_square, "1")
screen.onkeypress(draw_triangle, "2")
screen.onkeypress(draw_circle, "3")
screen.onkeypress(clear_screen, "4")
turtle.mainloop()






