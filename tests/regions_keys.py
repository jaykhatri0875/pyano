## aim to separate image into multiple regions just like piano keys
## this is static way of defining piano but need to take input from user and based on edges drawn on paper to make piano need to assign values and play tones

##module 1: aim to play different tunes in diffrenet software defined piano keys
## trying to draw one line first 

import cv2
import numpy as np
green = (0,255,0)
blue = (255,0,0)
feed = cv2.VideoCapture(0)
print("started getting feed")
width  = feed.get(3)   
height = feed.get(4)
key1 = (0,60)
key2 = ()
print((width,height))
while True:
    ret,frame=feed.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame,(0,60),(40,300),green,thickness=2)
    cv2.rectangle(frame,(40,60),(80,300),green,thickness=2)
    cv2.rectangle(frame,(80,60),(120,300),green,thickness=2)
    cv2.rectangle(frame,(120,60),(160,300),green,thickness=2)
    cv2.rectangle(frame,(160,60),(200,300),green,thickness=2)
    cv2.rectangle(frame,(200,60),(240,300),green,thickness=2)
    cv2.rectangle(frame,(240,60),(280,300),green,thickness=2)
    cv2.rectangle(frame,(280,60),(320,300),green,thickness=2)
    cv2.rectangle(frame,(320,60),(360,300),green,thickness=2)
    cv2.rectangle(frame,(360,60),(400,300),green,thickness=2)
    cv2.rectangle(frame,(400,60),(440,300),green,thickness=2)
    cv2.rectangle(frame,(440,60),(480,300),green,thickness=2)
    cv2.rectangle(frame,(480,60),(520,300),green,thickness=2)
    cv2.rectangle(frame,(520,60),(560,300),green,thickness=2)
    cv2.rectangle(frame,(560,60),(600,300),green,thickness=2)
    cv2.rectangle(frame,(600,60),(640,300),green,thickness=2)
   
    cv2.imshow('video-test',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        print('turning off ')
        break
feed.release()
cv2.destroyAllWindows()


##  
##'''
##import cv2
##import time
##import mediapipe as mp
##import numpy as np
##mp_drawing = mp.solutions.drawing_utils
##mp_hands = mp.solutions.hands
##cap = cv2.VideoCapture(0)
###'http://192.168.0.101:8080/video'
##print("started getting feed")
##with mp_hands.Hands(
##    min_detection_confidence = 0.5,
##    min_tracking_confidence = 0.5) as hands:
##    while cap.isOpened():
##        success,image = cap.read()
##        if not success:
##            print("failed to load")
##            continue
##        image.flags.writeable = True
##        image = cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_RGB2BGR)
##        results = hands.process(image)
##        if results.multi_hand_landmarks:
##          for hand_landmarks in results.multi_hand_landmarks:
##            mp_drawing.draw_landmarks(
##                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
##        cv2.imshow('MediaPipe Hands', image)
##        if cv2.waitKey(5) & 0xFF == 27:
##          break
##    cap.release()
##'''

