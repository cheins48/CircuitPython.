import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")

while True:
     dot.fill((255,0,0))
     time.sleep(.5)
     dot.fill((255,0,100))
     time.sleep(.5)
