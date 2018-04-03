# Simple example to test the board


import pycom
import time


# Disable heartbeat LED
pycom.heartbeat(False)

for cycles in range(10): # stop after 10 cycles

    pycom.rgbled(0x007f00) # green
    time.sleep(5)

    pycom.rgbled(0x7f7f00) # yellow
    time.sleep(1.5)

    pycom.rgbled(0x7f0000) # red
    time.sleep(3)

