import time
from sense_hat import SenseHat

sense = SenseHat()
nmd = 'NMD'
counter = 0

while True:
    for var in nmd:
        sense.show_letter(var)
        time.sleep(1)
    time.sleep(2)