from random import randint
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    try:
        for y in range(8):
            for x in range(8):
                sense.set_pixel(x, y, randint(0, 255), randint(0, 255), randint(0, 255))
                sleep(0.2)
                sense.set_pixel(x, y, 0, 0, 0)

                if x + y == 18:
                    x = 0
                    y = 0
    except KeyboardInterrupt:
        sense.clear()
        quit()
