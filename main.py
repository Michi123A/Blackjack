import random
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
screen.bgcolor("dark magenta")
screen.title("Welcome to Etch-A-Sketch. Press spacebar and arrow keys to draw. To clear press 'c'.")

#create border for screen
border = Turtle()
border.penup()
border.setposition(-300, -300)
border.pendown()
border.color("black")
border.begin_fill()
for side in range(4):
    border.forward(600)
    border.left(90)
border.end_fill()
border.hideturtle()

colors = ["cyan", "lime", "deep pink", "yellow", "dark violet"]
pen.pensize(5)
pen.color(random.choice(colors))
def move_forward():
    if pen.xcor() > 285 or pen.xcor() < -285: #make sure pen does not go over border
        pen.penup()
        pen.backward(30)
        pen.right(90)
        pen.forward(15)
        pen.pendown()
    elif pen.ycor() > 285 or pen.ycor() < -285:
        pen.penup()
        pen.backward(30)
        pen.right(90)
        pen.forward(15)
        pen.pendown()
    pen.forward(10)
    pen.color(random.choice(colors))

#def move_backward():
 #   pen.backward(10)

def move_left():
    pen.left(10)

def move_right():
    pen.right(10)

def clear_screen():
    pen.penup()
    pen.clear()
    pen.home()
    pen.pendown()

screen.listen()

screen.onkey(key="space", fun=move_forward)
#screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()