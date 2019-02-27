from sense_hat import SenseHat
import sys
import time

sense = SenseHat()

white = (250, 250, 250)
zero = (0, 0, 0)
red = (250, 0, 0)
skin = (240, 100, 75)
blue = (0, 0, 255)
brown = (200, 80, 40)

normalPose = [
    zero, zero, red, red, red, zero, zero, zero,
    zero, red, red, red, red, red, red, zero,
    zero, zero, brown, skin, skin, skin, zero, zero,
    zero, zero, skin, skin, brown, brown, zero, zero,
    zero, red, blue, red, red, blue, red, zero,
    zero, skin, blue, blue, blue, blue, skin, zero,
    zero, zero, blue, blue, blue, blue, zero, zero,
    zero, zero, brown, zero, zero, brown, zero, zero
    ]

jumpPose = [
    zero, zero, red, red, red, zero, zero, zero,
    zero, red, red, red, red, red, red, zero,
    zero, zero, brown, skin, skin, skin, zero, skin,
    zero, zero, skin, skin, brown, brown, red, zero,
    zero, red, blue, red, red, blue, zero, zero,
    skin, zero, blue, blue, blue, blue, brown, zero,
    zero, zero, blue, blue, blue, blue, brown, zero,
    zero, brown, zero, zero, zero, zero, zero, zero
    ]

def normal ():
    sense.set_pixels(normalPose)

def jump ():
    sense.set_pixels(jumpPose)

while True:
    try:
        normal()
        sense.stick.direction_up = jump
        time.sleep(1)
    except KeyboardInterrupt:
        sense.clear()
        sys.exit()