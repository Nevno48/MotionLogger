#!/bin/python3
from videoRecording import *
from cameraLapse import *
from time import sleep
from datetime import datetime
import os

validInput = True

print("Welcome to Motion Logger v0.5")
while(True):
    userInput = input("""
What would you like to make:
Time Lapse: Still images taken in increments based on the total
amount of pictures and determine if there is a difference between the first and last image
Video Recording: A video showing what the camera sees.
Enter "t" for time lapse.
Enter "v" for video recording.
Enter "q" to quit.
""")

    
    if(userInput.lower() == "t"):
        
        #increments per pictures
        timeIncrement = input("What time increment would you like to use in seconds: ")
        timeIncrement = int(timeIncrement)
        #adjust for accurate time increments
        timeIncrement = timeIncrement - .284
        #total amount of pictures
        incrementAmount = input("How many times would you like to take a picture: ")
        incrementAmount = float(incrementAmount)
        
        timeLapse(timeIncrement, incrementAmount)

        break

        
    elif(userInput.lower() == "v"):

        #get current time
        current = datetime.now()
        currentTime = current.strftime("%Y:%m:%d:%I:%M:%S")
        print("Time format: year:month:day:12-hour:minute:second")
        print("Current/Start time from prompt: %s" % currentTime)
        
        videoTime = input("How long do you want the video in seconds: ")
        videoTime = float(videoTime)
        videoTime = videoTime - .284
        
        fileTime = videoRecording(videoTime)
        filename = fileTime + ".h264"
        
        break
    elif(userInput.lower() == "q"):

        break

    else:
        continue



        
