from turtle import *
import math


length = int(input('Enter length of arm: '))
depth = int(input('Enter depth: '))

def draw_arm(length, depth):

    if depth == 1:
        forward(length)
        return
    
    draw_arm(length/3, depth-1)
    forward(length/3)
    penup()
    backward(length/3)
    pendown()
    left(60)
    draw_arm(length/3, depth-1)
    right(120)
    draw_arm(length/3, depth-1)
    left(60)
    draw_arm(length/3, depth-1)

def draw_triangle(length, depth):
    left(60)
    draw_arm(length, depth)
    right(120)
    draw_arm(length, depth)
    right(120)
    draw_arm(length, depth)

x_redx = -(length/2)
y_redx = -(length/(3*math.sqrt(2)))

home()
penup()
goto(x_redx, y_redx)
pendown()
draw_triangle(length, depth)

hideturtle()
exitonclick()