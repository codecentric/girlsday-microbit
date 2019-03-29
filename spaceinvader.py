from microbit import *
from random import randint


# SETTINGS #
asteroidDensity = 3  # sets the possibility of an asteroid inversely
#                     (random bool has to be True X times)
loopTime = 10  # refresh time of the game logic (<> game speed)
gameSpeed = 600  # defines the start speed of the game 1000 = 1s
nextLvlAt = 20    # game steps per level


# VARIABLES #
bJustStarted = True
grid = []
bYouLose = False
lvl = 1
stpsUntlNxtLvl = nextLvlAt
stpsUntlNxtRfrsh = 0


# FUNCTIONS #
def getStepsUntilNextRefresh():
    global loopTime
    global gameSpeed
    return int((gameSpeed / loopTime))
# END getStepsUntilNextRefresh


def drawGrid():
    global bYouLose
    if (len(grid) > 0):
        # if an asteroid collides with the ship
        # then the game is lost
        if (grid[4][4]):
            bYouLose = True
        # draw the grid with the center 5 cols
        for row in range(0, len(grid)):
            for col in range(2, len(grid[row])-2):
                isOn = 0
                if (grid[row][col] or (row == 4 and col == 4)):
                    isOn = 5
                display.set_pixel(col-2, row, isOn)
# END drawGrid


def is_On():
    ret = True
    # if the randomint is true X times then the pixel is on
    for i in range(0, asteroidDensity):
        rnd = randint(0, 1)
        if (rnd == 0):
            ret = False
            break
    return ret
# END is_On


def createRow():
    cols = []
    # go for all 9 pixels in row
    # (5 for the grid and 2 on every side for memory)
    for i in range(0, 9):
        isOn = is_On()
        cols.append(isOn)
    return cols
# END createRow


def buildGrid():
    global stpsUntlNxtLvl
    global gameSpeed
    global lvl
    # if start of game -> build empty grid
    if (len(grid) == 0):
        for i in range(0, 5):
            grid.append([False for i in range(0, 9)])
    # if grid is already built, delete last row and create new one at the top
    else:
        grid.pop(4)
        grid.insert(0, createRow())
    # draw grid
    drawGrid()
    # count steps and increase difficulty
    stpsUntlNxtLvl -= 1
    if (stpsUntlNxtLvl == 0):
        if ((gameSpeed - 100) > 100):  # until 200
            gameSpeed -= 100
        elif ((gameSpeed - 20) > 20):  # until 20
            gameSpeed -= 20
        if (gameSpeed > 20):
            stpsUntlNxtLvl = nextLvlAt
            lvl += 1
            # flash screen
            display.show(Image("99999:90009:90009:90009:99999"))
            sleep(10)
            drawGrid()
# END buildGrid


def shiftLeft():
    for row in range(0, len(grid)):
        grid[row].pop(8)
        grid[row].insert(0, is_On())
# END shiftLeft


def shiftRight():
    for row in range(0, len(grid)):
        grid[row].pop(0)
        grid[row].append(is_On())
# END shiftRight


# GAME LOOP #
stpsUntlNxtRfrsh = getStepsUntilNextRefresh()
while True:
    if (bJustStarted and button_a.was_pressed()):
        bJustStarted = False
        display.scroll("SpaceCraft", delay=100)
        sleep(500)
        for i in range(3, 0, -1):
            display.show(str(i))
            sleep(500)
    elif (bJustStarted):
        display.show(Image.ARROW_W)
    elif (bYouLose):
        display.show(Image.NO)
        sleep(500)
        display.scroll("You lost at lvl " + str(lvl) + "!")
    else:
        if (len(grid) > 0):
            if (button_a.was_pressed()):
                shiftLeft()
                drawGrid()
            if (button_b.was_pressed()):
                shiftRight()
                drawGrid()
        if (stpsUntlNxtRfrsh == 0):
            buildGrid()
            stpsUntlNxtRfrsh = getStepsUntilNextRefresh()
        stpsUntlNxtRfrsh -= 1
        sleep(loopTime)