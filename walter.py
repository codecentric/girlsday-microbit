import radio
import random
from microbit import *

# The radio won't work unless it's switched on.
radio.reset()
radio.config(queue = 1)
radio.on()

# the images and strings.
figures = ["Schere", "Stein", "Papier", "Brunnen"]
images = [Image.NO, Image.DIAMOND, Image.GHOST, Image.ASLEEP]
result = other_result = figures[3]
sleeptime = 1000

# Event loop.
while True:

    display.show('Hallo')

    if accelerometer.was_gesture('shake') or button_a.was_pressed():
        index = random.randint(0, 2)
        display.clear()
        myhand = figures[index]
        display.show(images[index])
        radio.send(figures[index])
        sleep(sleeptime)
        received = radio.receive()
        print("_s_")
        if (received):
            print("received:" + received)
        if (myhand):
            print("myhand:" + myhand)
        print("-e-")

        if (received == "Schere"):
            if (myhand == "Schere"):
                display.show(Image.SURPRISED)
            elif (myhand == "Stein"):
                display.show(Image.HAPPY)
            elif (myhand == "Papier"):
                display.show(Image.SAD)
        elif (received == "Stein"):
            if (myhand == "Schere"):
                display.show(Image.SAD)
            elif (myhand == "Stein"):
                display.show(Image.SURPRISED)
            elif (myhand == "Papier"):
                display.show(Image.HAPPY)
        elif (received == "Papier"):
            if (myhand == "Schere"):
                display.show(Image.HAPPY)
            elif (myhand == "Stein"):
                display.show(Image.SAD)
            elif (myhand == "Papier"):
                display.show(Image.SURPRISED)
        elif (received):
            display.scroll(received + " kenn ich nicht. Wähle Schere, Stein oder Papier")

        radio.off()
        sleep(sleeptime)
        radio.on()

    if button_b.was_pressed():
        display.scroll("oh.. ein Tip? .. ich Spiele ein Spiel und warte auf " +
            "eins von drei Symbolen als Wort")

        sleep(sleeptime)

    sleep(10)