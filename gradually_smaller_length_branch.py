import turtle as tl
length = 100
depth = 10


# window = tl.Screen()
# window.screensize(1366, 768)
# window.setup(width=1.0, height=1.0, startx=None, starty=None)

def signature():
    tl.up()
    tl.home()
    tl.backward(40)
    tl.left(90)
    tl.forward(250)
    
    tl.down()
    tl.write("Tree drawing with recursion", font=("Arial", 16, "normal"))
    tl.up()
    tl.backward(20)
    tl.down()
    tl.write("~Tanvir Ahmed", font=("Arial", 9, "normal"))
    tl.up()
def create_branches(n, length):

    if n == 0 :
        return
    
    tl.pendown()
    tl.left(30)
    tl.forward(length)
    create_branches(n-1, length/1.5)
    tl.penup()
    tl.backward(length)
    tl.right(60)
    tl.pendown()
    tl.forward(length)
    create_branches(n-1, length/1.5)
    tl.penup()
    tl.backward(length)
    tl.left(30)

signature()
tl.up()
tl.home()
tl.sety(-200)
# tl.forward(250)
tl.left(90)
# tl.goto((0, -330))

tl.pendown()
tl.forward(50)
create_branches(depth, length)
tl.hideturtle()




tl.exitonclick()