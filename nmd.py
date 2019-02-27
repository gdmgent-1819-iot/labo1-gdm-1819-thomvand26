import atexit
from random import randint
from sense_hat import SenseHat
import time

sense = SenseHat()
nmd = 'NMD'

while True:
    for var in nmd:
        sense.
        sense.show_letter(var, text_colour = [randint(0, 255), randint(0, 255), randint(0, 255)])
        time.sleep(1)
    time.sleep(2)

atexit.register(sense.clear())