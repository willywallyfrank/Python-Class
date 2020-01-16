#home work problem: 4.3_4
import turtle
from math import *
#screem object:
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
screen.bgcolor('#909090')
screen.title('Homework problem 4.3_4')
#turtle objects:
bob = turtle.Turtle()
bob.color('red','brown')
bob.pensize(5)
sam = turtle.Turtle()
sam.color('blue','light blue')
sam.pensize(5)
ian = turtle.Turtle()
ian.color('green','light green')
ian.pensize(5)

#bob.speed(0)
#functions
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
    

out_radius = 300
sides = 5
arc = 360

theta = 2*pi/(2*sides)
D = out_radius*cos(theta)
size = 2*out_radius*sin(theta)
in_radius = D

out_circle(sam,out_radius,arc)
poly(bob,size,sides,D)
in_circle(ian,in_radius,arc)

