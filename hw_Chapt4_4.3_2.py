#questions 4.3 1-2
import turtle


screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')

bob = turtle.Turtle()
bob.color('white','blue')

colors = ['blue','green','red','yellow']

def grid(turtle_obj,size):
    for squares in range(4):
        turtle_obj.right(90)
        bob.color('white',colors[squares])
        turtle_obj.begin_fill()
        for sides in range(4):
            turtle_obj.forward(size)
            turtle_obj.left(90)
        turtle_obj.end_fill()
    return turtle_obj


grid(bob,100)



