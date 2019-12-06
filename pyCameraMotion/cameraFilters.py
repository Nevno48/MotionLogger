#!/bin/python3
from picamera import PiCamera, Color
from time import sleep
from datetime import datetime

#datetime test
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

mydate = datetime.now()
monthName = mydate.strftime("%B")

hour = datetime.now().hour % 12
minute = datetime.now().minute
second = datetime.now().second

if(datetime.now().hour >= 0 and datetime.now().hour < 12):
    tzinfo = "AM"
else:
    tzinfo = "PM"


#camera test
#camera object to refer to
camera = PiCamera()

#annotation
#text background
camera.annotate_background = Color("blue")
#text foreground
camera.annotate_foreground = Color("yellow")
#text size in px
camera.annotate_text_size = 50
#text at top center
camera.annotate_text = "Date:%s %d %d Time:%d:%d %s" % (monthName, day, year, hour, minute, tzinfo)

#properties
#brightness
camera.brightness = 45
#pixel resolution
camera.resolution = (2560,1920)

#color filters/effects
#camera.image_effect = "colorswap"
#camera.image_effect = "oilpaint"
#camera.image_effect = "cartoon"
#camera.image_effect = "sketch"
#camera.image_effect = "denoise"
#camera.image_effect = "emboss"
#camera.image_effect = "hatch"
#camera.image_effect = "gpen"
#camera.image_effect = "pastel"
#camera.image_effect = "watercolor"
#camera.image_effect = "film"
#camera.image_effect = "blur"
#camera.image_effect = "washedout"
#camera.image_effect = "posterise"
#camera.image_effect = "colorpoint"
#camera.image_effect = "colorbalance"
#camera.image_effect = "deinterlace1"
#camera.image_effect = "deinterlace2"

#taking the picture

camera.start_preview()
sleep(5)
camera.capture("./imageTests/cameraFilterTestDeinterlace2.jpg")
camera.stop_preview()
camera.close()
