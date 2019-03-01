from random import randint
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
nmd = 'NMD'

while True:
    try:
        for var in nmd:
            sense.show_letter(var, text_colour = [randint(0, 255), randint(0, 255), randint(0, 255)])
            sleep(1)
        sleep(2)
    except KeyboardInterrupt:
        sense.clear()
        quit()
