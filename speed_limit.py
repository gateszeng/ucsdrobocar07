import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('spd_limit_rgn.yml')

speedlimits_detect = cv2.CascadeClassifier('./Speedlimit_24_15Stages.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)

while True:
    ret, img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    signs = speedlimits_detect.detectMultiScale(gray,1.1,3)

    for (x,y,h,w) in signs:
        Id = recognizer.predict_label(gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(img,str(Id), (x,y+h),font, 1,(255,0,0),2)


    cv2.imshow('im',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
