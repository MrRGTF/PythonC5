import turtle, sys, random

#========================Variables========================#

coordsx = {1: -225, 2: -175, 3: -125, 4: -75, 5: -25, 6: 25, 7: 75, 8: 125, 9: 175, 10: 225}
coordsy = {1: 225, 2: 175, 3: 125, 4: 75, 5: 25, 6: -25, 7: -75, 8: -125, 9: -175, 10: -225}

tableSize = 10
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
    thisOne.color("green")
    thisOne.goto(coordsx[x], coordsy[y])

def moveP2(x, y, name):
    thisOne = makeTurtle("square", name, 0)
    thisOne.penup()
    thisOne.color("blue")
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

def randBot():
    botmovex = random.randint(1, 10)
    botmovey = random.randint(1, 10)
    return botmovex, botmovey

#------------------Simple Bot------------------#
class SimpleBot:
    def __init__(self, player, tableLength):
        self.reward = []
        initiateTableGrid(self.reward, 10)
        self.player = player
        self.tableLength = tableLength
        
#-------Bot functions------#        
    def botCheckHorizontal(self, tableGrid, player, x, y, tableLength):
        count = 0
        for number in range(x-1, -1, -1):
            if tableGrid[y][number] == player:
                count += 1
            else:
                break
        
        for number in range(x+1, tableLength):
            if tableGrid[y][number] == player:
                count += 1
            else:
                break
                
        return int(count)
                
    def botCheckVertical(self, tableGrid, player, x, y, tableLength):
        count = 0
        for number in range(y-1, -1, -1):
            if tableGrid[number][x] == player:
                count += 1
            else:
                break
        
        for number in range(y+1, tableLength):
            if tableGrid[number][x] == player:
                count += 1
            else:
                break
        
        return int(count)

    def botCheckDiagonal(self, tableGrid, player, x, y, tableLength):
        return int(self.botCheckDiagonal1(tableGrid, player, x, y, tableLength) + self.botCheckDiagonal2(tableGrid, player, x, y, tableLength))

    def botCheckDiagonal1(self, tableGrid, player, x, y, tableLength):
        count = 0
        for number in range(1, tableLength):
            try:
                if tableGrid[y-number][x-number] == player:
                    count += 1
                else:
                    break
            except:
                break
                    
        for number in range(1, tableLength):
            try:
                if tableGrid[y+number][x+number] == player:
                    count += 1
                else:
                    break
            except:
                break
                    
        return int(count)

    def botCheckDiagonal2(self, tableGrid, player, x, y, tableLength):
        count = 0
        for number in range(1, tableLength):
            try:
                if tableGrid[y+number][x-number] == player:
                    count += 1
                else:
                    break
            except:
                break
                    
        for number in range(1, tableLength):
            try:
                if tableGrid[y-number][x+number] == player:
                    count += 1
                else:
                    break
            except:
                break
                    
        return int(count)
        

#-------Reward functions------#
    def calcReward(self, tableGrid, rewardGrid, player, x, y, tableLength):
        botH = self.botCheckHorizontal(tableGrid, player, x, y, tableLength)
        botV = self.botCheckVertical(tableGrid, player, x, y, tableLength)
        botD = self.botCheckDiagonal(tableGrid, player, x, y, tableLength)
        if tableGrid[y][x] != 0:
            rewardGrid[y][x] = -1
        else:
            rewardGrid[y][x] = botH + botV + botD
        
    def findReward(self, tableGrid, rewardGrid, player, tableLength):
        playerReward = []
        initiateTableGrid(playerReward, 10)
        hiXAr = []
        hiYAr = []
        hiXPAr = []
        hiYPAr = []
        for x2 in range (0, tableLength):
            for y2 in range (0, tableLength):
                self.calcReward(tableGrid, rewardGrid, player, x2, y2, tableLength)
        for x3 in range (0, tableLength):
            for y3 in range(0, tableLength):
                self.calcReward(tableGrid, playerReward, 1, x3, y3, tableLength)
        
        valueX = []
        valueY = []
        values = []
        hiX = []
        hiY = []
               
        for row in range(0, tableLength):
            for column in range(0, tableLength):
                enemyReward = playerReward[row][column]
                if enemyReward > 2:
                    enemyReward = enemyReward*2.5
                values.append(rewardGrid[row][column] + enemyReward)
                valueX.append(column)
                valueY.append(row)
                
        highest = max(values)
        for index, value in enumerate(values):
            if value == highest:
                hiX.append(valueX[index])
                hiY.append(valueY[index])
                
        hiIndex = random.randint(0,len(hiX)-1)
        
        return hiX[hiIndex], hiY[hiIndex]
        
#---------Executable functions-----------#
    def core(self, tableGrid):
        x, y = self.findReward(tableGrid, self.reward, self.player, self.tableLength)
        return x, y

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

def humanVSBot(tableGrid, tableLength):
    aBot = SimpleBot(2, tableLength)
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
            botx, boty = aBot.core(tableGrid)
            moveP2(botx + 1, boty + 1, i)
            tableGrid[boty][botx] = 2
            if checkWin(tableGrid, 2, tableSize, botx+1, boty+1) == True:
                print("You're such a failure, gets beaten by a simple bot.")
                finish = input("Press enter to exit")
                sys.exit(1)
        
def botVSBot(tableGrid, tableLength):
    aBot = SimpleBot(1, tableLength)
    bBot = SimpleBot(2, tableLength)
    for i in range (1, 102, 1):
        if i % 2 == 1:
            botx, boty = aBot.core(tableGrid)
            moveP1(botx + 1, boty + 1, i)
            tableGrid[boty][botx] = 1
            if checkWin(tableGrid, 1, tableSize, botx+1, boty+1) == True:
                print("Bot 1 won!")
                finish = input("Press enter to exit")
                sys.exit(1)
        elif i % 2 == 0:
            botx, boty = bBot.core(tableGrid)
            moveP2(botx + 1, boty + 1, i)
            tableGrid[boty][botx] = 2
            if checkWin(tableGrid, 2, tableSize, botx+1, boty+1) == True:
                print("Bot 2 won!")
                finish = input("Press enter to exit")
                sys.exit(1)                

while True:
    menu = ""
    menu = input("Input HH or 1 for human vs human, HB or 2 for human vs bot, BB or 3 for bot vs bot and E or 4 to exit: ")
    if menu == "HH" or menu == "1":
        humanVSHuman()
    elif menu == "HB" or menu == "2":
        humanVSBot(tableGrid, tableSize)
    elif menu == "BB" or menu == "3":
        botVSBot(tableGrid, tableSize)
    elif menu == "E" or menu == "4":
        sys.exit(1)
    else: print("That's not a valid input!")
    
    print("It's a draw!")
