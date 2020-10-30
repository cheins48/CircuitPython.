import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")

while True:
     dot.fill((100,0,0))
     time.sleep(100)
     dot.fill((100,0,0))
     time.sleep(100)
