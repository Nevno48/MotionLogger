#!/bin/python3
from picamera import PiCamera, Color
from time import sleep
from datetime import datetime

def videoRecording(totalTime):
    
    camera = PiCamera()

    currentTime = datetime.now()
    currentTime = currentTime.strftime("%Y:%m:%d:%I:%M:%S")
    print("Start time:" + currentTime)
    
    camera.annotate_background = Color("green")
    camera.annotate_foreground = Color("yellow")
    camera.annotate_text = "start time: " + currentTime
    camera.annotate_text_size = 50
    
    currentTime = datetime.now()
    currentTime = currentTime.strftime("%Y:%m:%d:%I:%M:%S")
    startTime = currentTime
    print("Video start:" + startTime)

    camera.start_preview()
    camera.start_recording("./allVideoRecording/%s.h264" % startTime)
    sleep(totalTime)
    camera.stop_recording()
    camera.stop_preview()
    
    currentTime = datetime.now()
    currentTime = currentTime.strftime("%Y:%m:%d:%I:%M:%S")
    print("Video end:" + currentTime)
    camera.close()
    return startTime
