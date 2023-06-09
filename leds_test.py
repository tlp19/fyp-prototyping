import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 60, bpp=3, brightness=0.2)

pixels.fill((255,255,255))