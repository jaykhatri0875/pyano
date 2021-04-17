'''
camera feed test module
'''

import cv2
import numpy as np
feed = cv2.VideoCapture('http://192.168.0.105:8080/video')
print("started getting feed")
while True:
    ret,frame=feed.read()
    frame = frame[200:,0:]
    blur = cv2.GaussianBlur(frame,(5,5),0)
    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,120)
    lines = cv2.HoughLines(edges,1,np.pi/180.0,20,30,50)
    cv2.imshow("edges",edges)
    #cv2.imshow('video-test',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        print('turning off ')
        break
feed.release()
cv2.destroyAllWindows()
