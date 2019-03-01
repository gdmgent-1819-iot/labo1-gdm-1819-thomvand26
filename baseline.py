from random import randint
from sense_hat import SenseHat

sense = SenseHat()
text = 'Hello! We are New Media Development :)'

while True:
    try:
        sense.show_message(text, back_colour = [randint(20, 70), randint(20, 70), randint(20, 70)], text_colour = [randint(200, 255), randint(200, 255), randint(200, 255)])
    except KeyboardInterrupt:
        sense.clear()
        quit()
