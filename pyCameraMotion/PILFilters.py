#!/bin/python3
from PIL import Image, ImageFilter

#main function
def pilFilter():
    filename = "./imageTests/PILFilterTest1.jpg"
    image = Image.open(filename)
    image.filter(ImageFilter.CONTOUR)
    image.show()

pilFilter()
