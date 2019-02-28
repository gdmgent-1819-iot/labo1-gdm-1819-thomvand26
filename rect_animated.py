from random import randint
from sense_hat import SenseHat
import sys
import time

sense = SenseHat()
rectColour = (150,150,150)

def createRect(originX, originY, width, height):

    for y in range(8):
        if originY <= y <= (originY + y):
            for x in range(8):
                if originX <= x <= (originX + width):
                    if (y == originY) or (y == originY + height):
                        sense.set_pixel(x, y, rectColour)
                    elif (x == originX) or (x == originY + width):
                        sense.set_pixel(x, y, rectColour)

while True:
    try:
        # for y in range(8):
        #     for x in range(8):
        #         sense.set_pixel(x, y, randint(0, 255), randint(0, 255), randint(0, 255))
        #         time.sleep(0.2)
        #         sense.set_pixel(x, y, 0, 0, 0)

        #         if x + y == 18:
        #             x = 0
        #             y = 0
        createRect(0,0,8,8)
    except KeyboardInterrupt:
        sense.clear()
        sys.exit()