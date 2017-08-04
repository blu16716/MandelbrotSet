from PIL import Image, ImageDraw
import random
import math
import PIL.Image
from mpmath import *

RMAX = 2.0
RMIN = -2.0
IMAX = 2.0
IMIN = -2.0
LENGTH = 800
WIDTH = 600

z = 0
iteration = 0
newz1 = 0
newz2 = 0j
# a = 0
# b = 0

a = .5
b = .5

pixel = complex(a, b)

img = Image.new("RGB", (WIDTH, LENGTH))
draw = ImageDraw.Draw(img)


def equation(z, pixel):
    f = math.pow(z, 2) + pixel
    return f


# def changinitup(z, pixel):
#     z = math.pow(z, 2) + pixel
#     return z

def loopinitup(z, pixel):
    z = [0]
    for r in range(1000):
        z = math.pow(z, 2) + pixel
        zValue.append(z)

#need to create graph(seperate from num of pixels), divide page and graph by pixels,
#using for loop change which pixel (nested for loop?) go across x direction - add to real part,
# go up and down y direction use imaginary part (a + bj) a = a+ .2 only, don't add to b

def c_for_position(row, col):
    rPart = RMIN + ((RMAX - RMIN)/WIDTH)*col
    iPart = IMIN + ((IMAX - IMIN)/LENGTH)*row

    return complex(rPart,iPart)


def intoAnEquation():
    maxIteration = int(raw_input("How many iterations do you want to execute? "))
    # z = 0
    # iteration = 0
    # newz1 = 0
    # newz2 = 0j
    # a = 0
    # b = 0
    pixelLoad = img.load()
    #in for loops already tried using SIZE, too many numbers, all very large :(
    for row in range(LENGTH):
        for col in range(WIDTH):
            # b = b + .2
            # a = a + .2
            c = c_for_position(row, col)
            z = complex(0,0)
            for iteration in range(1, maxIteration):
                z = z**2 + c

                if abs(z) > 2:
                    redvalue = 255/iteration**2
                    greenvalue = 0 #255/iteration*2
                    bluevalue = 255/iteration
                    img.putpixel((col, row), (redvalue, greenvalue, bluevalue))
                    break
                else:
                    redvalue = 255/iteration
                    greenvalue = 0
                    bluevalue = 0
                    img.putpixel((col, row), (redvalue, greenvalue, bluevalue))
    img.show()
            # print c

    #         f = equation(z, c)
    #
    #
    #
    #         # print pixel
    #         # print loopinitup(z,pixel)
    #
    #         #Nested for looop perhaps???? or while loop
    #         freal = f.real
    #         fimag = f.imag
    #         # print f
    #         # print freal
    #         # print fimag
    #         #if (abs(math.sqrt(math.pow(freal, 2) + math.pow(fimag, 2)) >= 2)):
    #         if(loopinitup(z,pixel) >= 2):
    #             bound = "unbounded"
    #             redvalue = 255
    #             greenvalue = 0
    #             bluevalue = 0
    #         #elif (abs(math.sqrt(math.pow(freal, 2) + math.pow(fimag, 2)) < 2)):
    #         elif (loopinitup(z,pixel) < 2):
    #             bound = "bounded"
    #             redvalue = 0
    #             greenvalue = 0
    #             bluevalue = 255
    #         img.putpixel((row, col), (redvalue, greenvalue, bluevalue))
    # img.show()

# print loopinitup(z, pixel)
intoAnEquation()
