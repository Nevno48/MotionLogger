#!/bin/python3
from picamera import PiCamera, Color
from time import sleep
from datetime import datetime

def timeLapse(increment, totalAmount):
    
    camera = PiCamera()

    currentTime = datetime.now()
    currentTime = currentTime.strftime("%Y:%m:%d:%I:%M:%S")
    print("Start Time:" + currentTime)
    
    camera.annotate_background = Color("green")
    camera.annotate_foreground = Color("yellow")
    camera.annotate_text = currentTime
    camera.annotate_text_size = 50

    amountOfPictures = 0
    while(amountOfPictures < totalAmount):
        currentTime = datetime.now()
        currentTime = currentTime.strftime("%Y:%m:%d:%I:%M:%S")
        print("Picture taken:" + currentTime)
        camera.capture("./allTimeLapse/%s.jpg" % currentTime)
        sleep(increment)
        amountOfPictures += 1
        #print(amountOfPictures)
    camera.close()

"""
now = "1234"
print(now)
timeLapse(now,1, 3)
"""
