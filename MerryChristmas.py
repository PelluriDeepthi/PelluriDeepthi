from turtle import *
from random import randint

def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    turtle.end_fill()       #fill the above shape
    turtle.setheading(0)        #Reset the orientation of the turtle

def create_circle(turtle, x, y, radius, color):
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(x, y)
    oogway.pendown()
    oogway.begin_fill()
    oogway.circle(radius)
    oogway.end_fill()

BG_COLOR = "#0080ff"

oogway = Turtle()
oogway.speed(2)
screen = oogway.getscreen()
screen.bgcolor(BG_COLOR)
screen.title("Merry Christmas")
screen.setup(width=1.0, height=1.0)     #Maximize the screen

y = -100
create_rectangle(oogway, "red", -15, y-60, 30, 60)      #Create Tree Trunk

# Create Tree
width = 240
oogway.speed(10)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width/2
    create_rectangle(oogway, "green", x, y, width, height)
    y = y + height

# Create a star on top of tree
oogway.speed(1)
oogway.penup()
oogway.color('yellow')
oogway.goto(-20, y+10)
oogway.begin_fill()
oogway.pendown()
for i in range(5):
    oogway.forward(40)
    oogway.right(144)
oogway.end_fill()

tree_height = y + 40

# Create moon in sky
create_circle(oogway, 230, 180, 60, "white")
create_circle(oogway, 220, 180, 60, BG_COLOR)       #Overlap with full circle of bg color to make a crescent shape

# Add few stars in sky
oogway.speed(10)
number_of_stars = randint(20, 30)
for _ in range(0, number_of_stars):
    x_star = randint(-(screen.window_width()//2), screen.window_width()//2)
    y_star = randint(tree_height, screen.window_height()//2)
    size = randint(5, 20)
    oogway.penup()
    oogway.color('white')
    oogway.goto(x_star, y_star)
    oogway.begin_fill()
    oogway.pendown()
    for i in range(5):
        oogway.forward(size)
        oogway.right(144)
    oogway.end_fill()

# Greeting message
oogway.speed(1)
oogway.penup()
msg = "Merry Christmas from Deepthi"
oogway.goto(0, -200)
oogway.color("white")
oogway.pendown()
oogway.write(msg, move=False, align="center", font=("Arial", 15, "bold"))

oogway.hideturtle()
screen.mainloop()