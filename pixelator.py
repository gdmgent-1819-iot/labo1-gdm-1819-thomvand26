from random import randint
from sense_hat import SenseHat
import sys
import time

sense = SenseHat()

while True:
    try:
        for y in range(7):
            for x in range(7):
                sense.set_pixel(y, x, randint(0, 255), randint(0, 255), randint(0, 255))
                time.sleep(0.2)
                sense.set_pixel(y, x, 0, 0, 0)

                if x + y = 14:
                    x = 0
                    y = 0
    except KeyboardInterrupt:
        sense.clear()
        sys.exit()
