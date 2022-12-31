import turtle as tl
import random
pen_size = 50
length = 100
depth = 10


# window = tl.Screen()
# window.screensize(1366, 768)
# window.setup(width=1.0, height=1.0, startx=None, starty=None)

def signature():
    tl.home()
    tl.up()
    tl.goto(-150, 250)
    tl.down()
    tl.write("Drawing tree using recursion", font=("Arial", 16, "normal"))
    tl.up()
    tl.goto(-150, 230)
    tl.down()
    tl.write("~Tanvir Ahmed", font=("Arial", 11, "normal"))
    tl.up()
    tl.home()
    tl.down()

def left_branch(n, length, p_size):
    tl.left(30)
    tl.pendown()
    if n < 6:
        tl.pencolor('green')
    else:
        tl.pencolor('#572a10')
    tl.pensize(p_size)
    tl.forward(length)
    create_branches(n-1, length/1.5, p_size/2)
    tl.penup()
    tl.backward(length)
    tl.right(30)


def right_branch(n, length, p_size):
    tl.right(30)
    tl.pendown()
    if n < 6:
        tl.pencolor('green')
    else:
        tl.pencolor('#572a10')
    tl.pensize(p_size)
    tl.forward(length)
    create_branches(n-1, length/1.5, p_size/2)
    tl.penup()
    tl.backward(length)
    tl.left(30)

def create_branches(n, length, p_size):

    if n == 0 :
        return
    
    right_first = random.choice([True, False])

    f = random.randint(1, 10)


    if right_first:
        right_branch(n, length, p_size)
        left_branch(n, length, p_size)
    else:
        left_branch(n, length, p_size)
        right_branch(n, length, p_size)
    
    
    

signature()
tl.up()
tl.home()
tl.goto(0, -275)
# tl.forward(250)
tl.left(90)
# tl.goto((0, -330))

tl.pendown()
tl.pencolor('#572a10')
tl.pensize(pen_size)
tl.forward(120)
tl.speed(6)
create_branches(depth, length, pen_size/2)
tl.hideturtle()




tl.exitonclick()