import turtle as tl
length = 30
depth = int(input('Enter depth of the tree: '))
nob = int(input('Enter number of branch: '))


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

def create_branches(n):

    if n == 0 :
        return
    
    tl.pendown()

    ang = 180 / (nob+1)
    tl.left(90)
    for b in range(nob):
        tl.right(ang)
        tl.pendown()
        tl.forward(length)
        create_branches(n-1)
        tl.penup()
        tl.backward(length)
    
    tl.left(90-ang)


signature()
tl.up()
tl.home()
tl.sety(-50)
# tl.forward(250)
tl.left(90)
# tl.goto((0, -330))

tl.pendown()
tl.forward(50)
create_branches(depth)
tl.speed(1)
tl.hideturtle()




tl.exitonclick()