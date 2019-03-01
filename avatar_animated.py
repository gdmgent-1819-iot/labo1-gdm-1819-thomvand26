from random import randint
from sense_hat import SenseHat
import sys
import time

sense = SenseHat()


while True:
    try:
        colour1 = (randint(0, 255), randint(0, 255), randint(0, 255))
        colour2 = (randint(0, 255), randint(0, 255), randint(0, 255))

        for y in range(8):
            for x in range(4):
                randNum = randint(0,1)
                if randNum == 0:
                    sense.set_pixel(x, y, colour1)
                    sense.set_pixel((7-x), y, colour1)
                else:
                    sense.set_pixel(x, y, colour2)
                    sense.set_pixel((7-x), y, colour2)

        time.sleep(2)
        sense.clear()
    except KeyboardInterrupt:
        sense.clear()
        sys.exit()