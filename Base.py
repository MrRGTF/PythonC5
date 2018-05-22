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
def checkWin(tableGrid, player, tableLength, x, y):
    if checkHorizontal(tableGrid, player, x, y, tableLength) or checkVertical(tableGrid, player, x, y, tableLength) or checkDiagonal(tableGrid, player, x-1, y-1, tableLength):
        return True

def checkHorizontal(tableGrid, player, x, y, tableLength):
    count = 0
    for number in range(0, tableLength):
        if tableGrid[y-1][number] == player:
            count += 1
        else:
            count = 0
        if count == 5:
            return True
    return False
                
def checkVertical(tableGrid, player, x, y, tableLength):
    count = 0
    for number in range(0, tableLength):
        if tableGrid[number][x-1] == player:
            count += 1
        else:
            count = 0
        if count == 5:
            return True
    return False

def checkDiagonal(tableGrid, player, x, y, tableLength):
    if checkDiagonal1(tableGrid, player, x, y, tableLength) or checkDiagonal2(tableGrid, player, x, y, tableLength):
        return True
    else:
        return False

def checkDiagonal1(tableGrid, player, x, y, tableLength):
    while True:
        if (x == 0) or (y == 9):
            iniX = x
            iniY = y
            break
        else:
            x -= 1
            y += 1

    count = 0
    for number in range(0, tableLength):
        try:
            if tableGrid[iniY-number][iniX+number] == player:
                count += 1
            else:
                count = 0
            if count == 5:
                return True

        except:
            break

    return False

def checkDiagonal2(tableGrid, player, x, y, tableLength):
    while True:
        if (x == 0) or (y == 0):
            iniX = x
            iniY = y
            break
        else:
            x -= 1
            y -= 1

    count = 0
    for number in range(0, tableLength):
        try:
            if tableGrid[iniY+number][iniX+number] == player:
                count += 1
            else:
                count = 0
            if count == 5:
                return True
        except:
            break

    return False

#========================Code========================#

drawField()
initiateTableGrid(tableGrid, 10)
def humanVSHuman():
    for i in range (1, 102, 1):
        if i % 2 == 1:
        
            while True:
                x = int(input("Player 1, input x: "))
                y = int(input("Player 1, input y: "))
                if x < 1 or x > 10 or y < 1 or y > 10:
                    print("Not valid")
                elif tableGrid[y-1][x-1] != 0:
                    print("You can't place a piece here!")
                else:
                    break
                
            moveP1(x, y, i)
            tableGrid[y-1][x-1] = 1
            if checkWin(tableGrid, 1, tableSize, x, y) == True:
                print("Player 1 won")
                finish = input("Press enter to exit")
                sys.exit(1)
        elif i % 2 == 0:
            
            while True:
                x = int(input("Player 2, input x: "))
                y = int(input("Player 2, input y: "))
                if x < 1 or x > 10 or y < 1 or y > 10:
                    print("Not valid")
                elif tableGrid[y-1][x-1] != 0:
                    print("You can't place a piece here!")
                else:
                    break
                
            moveP2(x, y, i)
            tableGrid[y-1][x-1] = 2
            if checkWin(tableGrid, 2, tableSize, x, y) == True:
                print("Player 2 won")
                finish = input("Press enter to exit")
                sys.exit(1)

def humanVSBot():
    None

def botVSBot():
    None

while True:
    menu = input("Input HH or 1 for human vs human, HB or 2 for human vs bot, BB or 3 for bot vs bot: ")
    if menu == "HH" or menu == 1:
        humanVSHuman()
    elif menu == "HB" or menu == 2:
        humanVSBot()
    elif menu == "BB" or menu == 3:
        botVSBot()
    else: print("That's not a valid input!")
    
