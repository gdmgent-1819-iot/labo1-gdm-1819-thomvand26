from random import randint
from sense_hat import SenseHat
import sys
import time

sense = SenseHat()
rectColour = (150,150,150)
isGrowing = True

currentProperties = [1,1,6,6]

def createRect(originX, originY, width, height):

    for y in range(8):
        if originY <= y <= (originY + y):
            for x in range(8):
                if originX <= x <= (originX + width):
                    if (y == originY) or (y == originY + height - 1):
                        sense.set_pixel(x, y, rectColour)
                    elif (x == originX) or (x == originY + width - 1):
                        sense.set_pixel(x, y, rectColour)

# def grow(properties):
#     if properties[2] < 8:
#         return [(properties[0] - 1), (properties[1] - 1), (properties[2] + 2), (properties[3] + 2)]
#     else:
#         isGrowing = False

createRect(1,1,6,6)

def grow():
    if currentProperties[2] < 8:
        currentProperties[0] - 1
        currentProperties[1] - 1
        currentProperties[2] + 2
        currentProperties[3] + 2
    else:
        isGrowing = False

def shrink():
    if currentProperties[2] < 8:
        currentProperties[0] + 1
        currentProperties[1] + 1
        currentProperties[2] - 2
        currentProperties[3] - 2
    else:
        isGrowing = False

t = 0

while True:
    try:
        t += 1
        if isGrowing:
            grow()
        else:
            shrink()
            
        createRect(t,t,2,2)
        time.sleep(0.5)
        sense.clear()
    except KeyboardInterrupt:
        sense.clear()
        sys.exit()