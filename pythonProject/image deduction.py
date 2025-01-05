import cv2
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('img.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face.detectMultiScale(gray,1,4,4)
for(x,y,w,h) in face:

    cv2.rectangle(img,(x, y), (x + w, y + h), (0,255,0), 1)
cv2.imshow('r',img)
cv2.waitKey()


