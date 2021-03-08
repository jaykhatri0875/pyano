'''
camera feed test module
'''

import cv2
feed = cv2.VideoCapture('http://192.168.0.102:8080/video')
print("started getting feed")
while True:
    ret,frame=feed.read()
    cv2.imshow('video-test',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        print('turning off ')
        break
feed.release()
cv2.destroyAllWindows()
