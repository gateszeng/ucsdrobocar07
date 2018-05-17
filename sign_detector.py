import cv2
import numpy as np


stop_detect = cv2.CascadeClassifier('./stopsign_classifier.xml')
yield_detect = cv2.CascadeClassifier('./yieldsign12Stages.xml')
speedlimits_detect = cv2.CascadeClassifier('./Speedlimit_24_15Stages.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)

while True:
    ret, img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    yields = yield_detect.detectMultiScale(gray,1.2,4)
    stops = stop_detect.detectMultiScale(gray,1.2,5)
    signs = speedlimits_detect.detectMultiScale(gray,1.1,3)

    for (x,y,h,w) in signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(img,"speed limit", (x,y+h),font, 1,(255,0,0),2)

    for (x,y,h,w) in stops:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(img,"stop", (x,y+h),font, 1,(255,0,0),2)

    for (x,y,h,w) in yields:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)    
        cv2.putText(img,"yield", (x,y+h),font, 1,(255,0,0),2)

    cv2.imshow('im',img)
    if (cv2.waitKey(1) == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()
