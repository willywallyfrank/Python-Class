#questions 4.3 3
import turtle

screen = turtle.Screen()
screen.setup(1.0,1.0)
screen.bgcolor('black')
screen.title('homework problem 4.3.3')
bob = turtle.Turtle()
bob.color('white','blue')

num_sides = 12
size = 100
angle = 360/num_sides
rotate = 180 - angle
num_poly = int(360//rotate)

def poly(turtle_obj,size):
    for rep in range(num_sides):
        turtle_obj.forward(size)
        turtle_obj.left(angle)
    return turtle_obj

def main():
    for polygons in range(num_poly):        
        bob.begin_fill()
        poly(bob,size)
        bob.end_fill()
        bob.left(rotate)
main()

