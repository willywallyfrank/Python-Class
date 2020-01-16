import turtle

screen_width,screen_height = 600, 600
font2 = ("Arial", 10, "bold")

def gotoandprint(x, y):
    gotoresult = bob.goto(x, y)
    bob.write(str((x, y)), move=False, align="right",font = font2)
    return gotoresult

def create_axis():
    screen = turtle.Screen()
    screen.setup(screen_width,screen_height)
    screen.bgcolor('#c0c0c0')
    font1 = ("Arial", 8, "normal")
    a = screen.window_width()//2
    b = screen.window_height()//2
    dx = screen.window_width()//20
    dy = screen.window_height()//20
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
        
screen = turtle.Screen()        
create_axis()
bob = turtle.Turtle()
bob.pensize(3)
bob.color('red')
screen.onclick(gotoandprint)



    
