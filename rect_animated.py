from random import randint
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
rectColour = (150,150,150)
isGrowing = True

currentProperties = [3,3,2,2]

def createRect(originX, originY, width, height):

    for y in range(8):
        if originY <= y < (originY + width):
            for x in range(8):
                if originX <= x < (originX + width):
                    if (y == originY) or (y == originY + height - 1):
                        sense.set_pixel(x, y, rectColour)
                    elif (x == originX) or (x == originY + width - 1):
                        sense.set_pixel(x, y, rectColour)

def grow():
    global isGrowing

    if currentProperties[2] < 8:
        currentProperties[0] -= 1
        currentProperties[1] -= 1
        currentProperties[2] += 2
        currentProperties[3] += 2
    else:
        isGrowing = False

def shrink():
    global isGrowing

    if currentProperties[2] > 2:
        currentProperties[0] += 1
        currentProperties[1] += 1
        currentProperties[2] -= 2
        currentProperties[3] -= 2
    else:
        isGrowing = True


createRect(currentProperties[0], currentProperties[1], currentProperties[2], currentProperties[3])
sleep(0.5)
sense.clear()

while True:
    try:
        if isGrowing:
            grow()
        else:
            shrink()
            
        createRect(currentProperties[0], currentProperties[1], currentProperties[2], currentProperties[3])
        sleep(0.5)
        sense.clear()
    except KeyboardInterrupt:
        sense.clear()
        quit()
