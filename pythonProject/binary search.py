import numpy as np
import cv2
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread('img.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
faces =face.detectMultiScale(gray,1.3,5)
if faces is ():
    print("No faces found")
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,255),2)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    ro