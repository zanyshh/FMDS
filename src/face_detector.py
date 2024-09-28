# haarcascade_frontalface_default.xml
import sys
import os
import cv2



# video capture and frame variable
frame = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

# Loop to start recognizing faces
while True:
    start_rec,display_image = video_capture.read()
    grayscale = cv2.cvtColor(display_image,cv2.COLOR_BGR2GRAY)
    face = frame.detectMultiScale(grayscale,1.3,6)


# Creates rectangle on detecting face
    for (x1,y1,w1,h1) in face:
        cv2.rectangle(display_image,(x1,y1),(x1+w1, y1+h1), (255,0,0), 5)

# Creates the window on which everything is shown (includes window title)     
    cv2.imshow('FMDS (Face and Motion Detection Software)',display_image)
    h = cv2.waitKey(40) & 0xff
    if h == 40:
        break

# function to quit window and stop video capture
video_capture.release()
cv2.destroyAllWindows()


        



