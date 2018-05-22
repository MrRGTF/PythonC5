import turtle, sys

#========================Variables========================#

tableSize = 10

coordsx = {1: -225, 2: -175, 3: -125, 4: -75, 5: -25, 6: 25, 7: 75, 8: 125, 9: 175, 10: 225}

coordsy = {1: 225, 2: 175, 3: 125, 4: 75, 5: 25, 6: -25, 7: -75, 8: -125, 9: -175, 10: -225}

tableGrid = []

#========================Functions========================#

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
   
def initiateTableGrid(tableGrid, tableSize):
    for row in range(0, tableSize):
        row = []
        for column in range(0, tableSize):
            row.append(0)
        tableGrid.append(row)


#------------------Win Conditions------------------#
def checkWin(tableGrid, player, tablelength):
    if checkHorizontal(tableGrid, player) == True or checkVertical(tableGrid, player, 0, 0, tablelength) == True:
        return True

def checkHorizontal(tableGrid, player):
    for row in tableGrid:
        for cIndex, column in enumerate(row):
            if cIndex < 6:
                count = 0
                for number in range(0,5):
                    if row[cIndex] == player:
                        count += 1
                        cIndex += 1
                    else:
                        break
                if count > 4:
                    return True
    return False
                
def checkVertical(tableGrid, player, x, y, tablelength):
    for column in range(x, tablelength):
        for row in range(y, tablelength):
            count = 0
            if tableGrid[row][column] == player and count < 5:
                count += 1
                checkVertical(tableGrid, player, x, y + 1, tablelength)
            elif tableGrid[row][column] != player:
                count = 0
            elif tableGrid[row][column] == player and count == 4:
                count = 5
                return True
            else: return False

#def checkDiagonal(tableGrid, player):
    

#========================Code========================#

drawField()
initiateTableGrid(tableGrid, 10)

for i in range (1, 102, 1):
    print(tableGrid)
    if i % 2 == 1:
    
        while True:
            x = int(input("Player 1, input x: "))
            y = int(input("Player 1, input y: "))
            if x < 1 or x > 10:
                print("Not valid")
            elif y < 1 or y > 10:
                print("Not valid")
            elif tableGrid[y-1][x-1] != 0:
                print("You can't place a piece here!")
            else:
                break  
        moveP1(x, y, i)
        tableGrid[y-1][x-1] = 1
        if checkWin(tableGrid, 1, 10) == True:
            print("Player 1 won")
            finish = input("Press enter to exit")
            sys.exit(1)
    elif i % 2 == 0:
        while True:
            x = int(input("Player 2, input x: "))
            y = int(input("Player 2, input y: "))
            if x < 1 or x > 10:
                print("Not valid")
            elif y < 1 or y > 10:
                print("Not valid")
            elif tableGrid[y-1][x-1] != 0:
                print("You can't place a piece here!")
            else:
                break
        moveP2(x, y, i)
        tableGrid[y-1][x-1] = 2
        if checkWin(tableGrid, 2, 10) == True:
            print("Player 2 won")
            finish = input("Press enter to exit")
            sys.exit(1)
            
    else: None
