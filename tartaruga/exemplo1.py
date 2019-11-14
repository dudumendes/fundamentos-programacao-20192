import turtle

def square1():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)

def square2(side):
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)

def square3(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

def square4(side):
    i = 0
    while(i < 4):
        turtle.forward(side)
        turtle.left(90)
        i = i + 1

def eight(side):
    square4(side)
    turtle.right(90)
    square4(side)

def rectangle(base, height):
    for i in range(2):
        turtle.forward(base)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def triangle(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)

triangle(100)
