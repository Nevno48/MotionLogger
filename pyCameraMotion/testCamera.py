#!/bin/python3
from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
sleep(1)
camera.capture("./imageTests/imageTest.jpg")
camera.stop_preview()
camera.close()
