//Test edit, do ignore.

import turtle

def drawField():
    turtle1 = turtle.Turtle()
    turtle1.speed(0)
    turtle1.penup()
    turtle1.goto(0,250)
    turtle1.pendown()
    turtle1.right(90)
    for col in range (0, 11):
        turtle1.forward(500)
        turtle1.penup()
        turtle1.left(90)
        turtle1.forward((col+1) * 50)
        turtle1.left(90)
        turtle1.pendown()
    turtle1.penup()
    turtle1.goto(-250, 0)
    turtle1.right(90)
    for row in range (0, 11):
        turtle1.pendown()
        turtle1.forward(500)
        turtle1.penup()
        turtle1.left(90)
        turtle1.forward((row+1) * 50)
        turtle1.left(90)
        turtle1.pendown()


coordsx = {1: -225, 2: -175, 3: -125, 4: -75, 5: -25, 6: 25, 7: 75, 8: 125, 9: 175, 10: 225}

coordsy = {1: 225, 2: 175, 3: 125, 4: 75, 5: 25, 6: -25, 7: -75, 8: -125, 9: -175, 10: -225}

def makeTurtle(shape, name, speed):
    name = turtle.Turtle()
    name.shape(shape)
    name.speed(speed)
    return name

def moveP1(x, y, name):
    thisOne = makeTurtle("circle", name, 0)
    thisOne.penup()
    thisOne.goto(coordsx[x], coordsy[y])

def moveP2(x, y, name):
    thisOne = makeTurtle("square", name, 0)
    thisOne.penup()
    thisOne.goto(coordsx[x], coordsy[y])

def checkWin():
    None

drawField()
for i in range (1, 102, 1):
    if i % 2 == 1:
        x = int(input("Player 1, input x: "))
        y = int(input("Player 1, input y: "))
        moveP1(x, y, i)
    elif i % 2 == 0:
        x = int(input("Player 2, input x: "))
        y = int(input("Player 2, input y: "))
        moveP2(x, y, i)
    else: None
