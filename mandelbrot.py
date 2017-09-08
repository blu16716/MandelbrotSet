from PIL import Image, ImageDraw
import random
import math
import PIL.Image
# from mpmath import *
RMAX = 2.0
RMIN = -2.0
IMAX = 2.0
IMIN = -2.0
length = 100
width = 100
a = .5
b = .5
changeSize = raw_input("Do you want to change the size of the image, the default is 100 by 100? ")
if (changeSize == "yes" or changeSize == "Yes"):
    length = int(raw_input("What do you want the length to be? "))
    width = int(raw_input("What do you want the width to be? "))
pixel = complex(a, b)
img = Image.new("RGB", (width, length))
draw = ImageDraw.Draw(img)
def c_for_position(row, col):
   rPart = RMIN + ((RMAX - RMIN)/width)*col
   iPart = IMIN + ((IMAX - IMIN)/length)*row
   return complex(rPart,iPart)


def intoAnEquation():
   maxIteration = int(raw_input("How many iterations do you want to execute? "))
   pixelLoad = img.load()
   for row in range(length):
       for col in range(width):
           c = c_for_position(row, col)
           z = complex(0,0)
           for iteration in range(1, maxIteration):
               z = z**2 + c
               if abs(z) > 2:
                   redvalue = 255/iteration
                   greenvalue = 80
                   bluevalue = 100*iteration
                   img.putpixel((col, row), (redvalue, greenvalue, bluevalue))
                   break

   img.show()

intoAnEquation()
