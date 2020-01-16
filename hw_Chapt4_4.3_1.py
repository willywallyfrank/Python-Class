#questions 4.3 1-2
import turtle
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('homework problem 4.3.1')

bob = turtle.Turtle()
bob.color('white','blue')


def square(turtle_obj,size):
    for rep in range(4):
        turtle_obj.forward(size)
        turtle_obj.left(90)
    return turtle_obj

size =100
bob.begin_fill()
square(bob,size)
bob.end_fill()

bob.color('white','green')
bob.right(90)
size = 200
bob.begin_fill()
square(bob,size)
bob.end_fill()


