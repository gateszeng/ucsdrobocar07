from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import imutils
import cv2
import numpy as np
import time
import serial
import io

stop_detect = cv2.CascadeClassifier('./stopsign_classifier.xml')
yield_detect = cv2.CascadeClassifier('./yieldsign12Stages.xml')
speedlimits_detect = cv2.CascadeClassifier('./Speedlimit_24_15Stages.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
frames = 0

vs = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()

ser = serial.Serial(
port = '/dev/serial0', \
baudrate = 115200, \
bytesize = serial.EIGHTBITS, \
timeout = 0)

print("Sign Recognition Started")
prev = time.time()
start = time.time()
while (time.time() - start) < 10:
    img = vs.read()
    #print(len(img), len(img[0]))
    #img = imutils.resize(img, width=150)
    #print(len(img), len(img[0]))
    #print(len(img[0]), len(img))
    img = img[:, (len(img[0])//2):]
    #print(len(img[0]), len(img))
    #ret, img =cam.read()
    frames = frames + 1
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    yields = yield_detect.detectMultiScale(gray,1.2,4)
    stops = stop_detect.detectMultiScale(gray,1.2,5)
    signs = speedlimits_detect.detectMultiScale(gray,1.1,3)

    '''
    for (x,y,h,w) in signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(img,"speed limit", (x,y+h),font, 1,(255,0,0),2)
        print("speed limit sign")
    '''

    for (x,y,h,w) in stops:
        print("stop sign")
        #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        #cv2.putText(img,"stop", (x,y+h),font, 1,(255,0,0),2)
        '''
        curr = time.time()
        if (curr - prevStop) >= 3:
            print("sending stop")
            prevStop = curr
            ser.write(bytes(b'1'))
        '''

    '''
    for (x,y,h,w) in yields:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)    
        cv2.putText(img,"yield", (x,y+h),font, 1,(255,0,0),2)
        print("yield sign")
    '''

    curr = time.time()

    if len(stops) > 0:
        if (curr - prev) >= 3:
            print("sending stop")
            prev = curr
            ser.write('stop\n'.encode('utf-8'))
    '''
    elif len(signs) > 0:
        ser.write('speed_limit\n'.encode('utf-8'))
    elif len(yields) > 0:
        ser.write('yield\n'.encode('utf-8'))
    '''

    #time.sleep(0.1)

    #cv2.imshow('im',img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        print("q pressed")
        break
end = time.time()

print("Time recorded", end - start)
print("FPS", frames/(end-start))
#cam.release()
ser.close()
cv2.destroyAllWindows()
vs.stop()
