#capture images when human is present

import cv2
#install cv2 and time if not installed 
import time

#load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#to capture video from webcam
cap = cv2.VideoCapture(0) #0 for default cam

count = 0
while True:
    #Read the frame
    _, img = cap.read()

    #convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    #draw the rectangle around each face
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

        #display
        cv2.imshow('img', img)
        t = time.strftime("%Y-%m-%d_%H-%M-%S")

        print("Image "+t+" saved")
        file = 'F:/ip/'+t+'.jpg'
        cv2.imwrite(file,img)
        count += 1
    #Stop if ESC is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

#Release the VideoCapture object
cap.release()
