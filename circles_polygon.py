#inscribed and circumscribed polygon
import turtle
from math import *
#circle and polygon definitions:
out_radius = 270
sides = 6
#screem object:
screen_width = 600
screen_height = 600
screen = turtle.Screen()
screen.setup(screen_width,screen_height)
screen.bgcolor('#909090')
font1 = ("Arial", 8, "normal")
screen.title('inscribed and circumscribed polygon')
#turtle objects:
bob = turtle.Turtle()
bob.color('red','brown')
bob.pensize(5)
sam = turtle.Turtle()
sam.color('yellow','light blue')
sam.pensize(5)
ian = turtle.Turtle()
ian.color('green','light green')
ian.pensize(5)

#bob.speed(0)
#functions
def create_axis():
    a = screen_width//2
    b = screen_height//2
    dx = screen_width//20
    dy = screen_height//20
    axis = turtle.Turtle()
    axis.hideturtle()
    axis.speed(0)
    axis.color('blue','blue')
    axis.pensize(5)
    axis.penup()
    axis.goto(-a+5,0)
    axis.pendown()
    axis.write(str(-a), move=False, align="left",font = font1)
    axis.goto(a,0)
    axis.goto(a-30,0)
    axis.write(str(a), move=False, align="left", font = font1)
    axis.penup()
    axis.goto(0,-b+5)
    axis.pendown()
    axis.write(str(-b), move=False, align="right",font = font1)
    axis.goto(0,-b)
    axis.goto(0,b-15)
    axis.write(str(b), move=False, align="right", font = font1)
    axis.goto(0,b)
    axis.pensize(1)

    for n in range(21):
        x = -a + n*dx
        axis.penup()
        axis.goto(x,-b)
        axis.pendown()
        axis.goto(x,b)
    for n in range(21):
        y = -b + n*dy
        axis.penup()
        axis.goto(-a,y)
        axis.pendown()
        axis.goto(a,y)        

def poly(turtle,size,sides,D):
    x, y = D,-size/2
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(90)
    angle = (360/sides)
    for n in range(sides):
        turtle.forward(size)
        turtle.left(angle)

def out_circle(turtle,radius,arc):
    turtle.penup()
    turtle.goto(radius, 0)
    turtle.pendown()
    turtle.setheading(90)
    turtle.circle(radius,arc)
    
def in_circle(turtle,radius,arc):
    turtle.penup()
    turtle.goto(radius, 0)
    turtle.pendown()
    turtle.setheading(90)
    turtle.circle(radius,arc)
    
def create_axis():
    a = screen_width//2
    b = screen_height//2
    dx = screen_width//20
    dy = screen_height//20
    axis = turtle.Turtle()
    axis.hideturtle()
    axis.speed(0)
    axis.color('blue','blue')
    axis.pensize(5)
    axis.penup()
    axis.goto(-a+5,0)
    axis.pendown()
    axis.write(str(-a), move=False, align="left",font = font1)
    axis.goto(a,0)
    axis.goto(a-30,0)
    axis.write(str(a), move=False, align="left", font = font1)
    axis.penup()
    axis.goto(0,-b+5)
    axis.pendown()
    axis.write(str(-b), move=False, align="right",font = font1)
    axis.goto(0,-b)
    axis.goto(0,b-15)
    axis.write(str(b), move=False, align="right", font = font1)
    axis.goto(0,b)
    axis.pensize(1)

    for n in range(21):
        x = -a + n*dx
        axis.penup()
        axis.goto(x,-b)
        axis.pendown()
        axis.goto(x,b)
    for n in range(21):
        y = -b + n*dy
        axis.penup()
        axis.goto(-a,y)
        axis.pendown()
        axis.goto(a,y)        

create_axis()

arc = 360

theta = 2*pi/(2*sides)
D = out_radius*cos(theta)
size = 2*out_radius*sin(theta)
in_radius = D

out_circle(sam,out_radius,arc)
poly(bob,size,sides,D)
in_circle(ian,in_radius,arc)

