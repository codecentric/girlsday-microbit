import radio
from microbit import display, Image, button_a, button_b

code = 'Walter'
flash = 'flash'

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        radio.send(flash)  # a-ha
    if button_b.was_pressed():
        radio.send(code)  # a-ha
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == flash:
        # If there's an incoming correct code message display the flash
        display.show(flash, delay=100, wait=False)
    elif incoming == code:
        display.scroll("... der Walfisch")