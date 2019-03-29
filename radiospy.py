import radio
from microbit import *

# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    display.show('-')
    received = radio.receive()
    if (received):
        display.scroll(received)
    sleep(10)