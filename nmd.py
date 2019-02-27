from random import randint
from sense_hat import SenseHat
import sys
import time

sense = SenseHat()
nmd = 'NMD'

while True:
    try:
        for var in nmd:
            sense.show_letter(var, text_colour = [randint(0, 255), randint(0, 255), randint(0, 255)])
            time.sleep(1)
        time.sleep(2)
    except KeyboardInterrupt:
        sense.clear()
        sys.exit()
