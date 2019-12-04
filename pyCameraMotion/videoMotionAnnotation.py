import cv2
import numpy as np
def videoMotionAnnotation(filename="2019:12:04:12:43:25.h264"):
    cap = cv2.VideoCapture(filename)
    #get current frame
    ret, frame = cap.read()
    #get next frame
    ret, frame2 = cap.read()

    while(cap.isOpened()):
        #difference between frame 1 and 2
        diff = cv2.absdiff(frame1, frame2)

        #greyscale photo
        greyscale = cv2.cvtColor(diff, COLOR_BRG2GRAY)

        #blur image using GaussianBlur effect
        blur = GaussianBlur(greyscale, (5,5), 0)

        #threshold for image difference
        #_, uses previous variable created
        _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dialated = cv2.dialate(threshold, None, iterations=3)

        #find contours(outline) of objects
        contours, _ = cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN.APPROX_SIMPLE)

        #create rectangles
        for contour in contours:
            #assign x, y coordinates, width, height)
            (x,y,w,h) = cv2.boundingRect(contour)

            if(cv2.contourArea(contour) < 700):
                continue
            #draw rectangle based on top left and bottom right corner, color, weight of rectangle line
            cv2.rectangle(frame1, (x, y), ((x+w), (y+h)), (0, 255, 0), 2)
            #have text indicating movement
            cv2.putText(frame1, "Status: ()".format("Movement"), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)


        cv2.imshow("inter",frame)

        if(cv2.waitKey(40) == 27):
            break
        
    cv2.destroyAllWindows()
    cap.release()
