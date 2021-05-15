## demo of running mediapipe in local machine
## taking video feed from mobile and procesing

import cv2
import time
import mediapipe as mp
import numpy as np
import csv

data_file = open('data/datapoints.csv','w',newline='')
writer = csv.writer(data_file)
writer.writerow(["tip_x","tip_y","dip_x","dip_y","pip_x","pip_y",'ispressed'])
def storeData(state):
    writer.writerow(state)
    
##def inregion(coord,lower,upper):
##    if(coord[0])
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
image_width  = cap.get(3)   
image_hight = cap.get(4)
green = (0,255,0)
font=cv2.FONT_HERSHEY_SIMPLEX
x_pos,y_pos = None,None
count = 0
state = ''
#'http://192.168.0.101:8080/video'
print("started getting feed")
with mp_hands.Hands(
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as hands:
    while cap.isOpened():
        success,image = cap.read()
        if not success:
            print("failed to load")
            continue
        image.flags.writeable = True
        image = cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_RGB2BGR)
        results = hands.process(image)
        if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            x_pos_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x 
            y_pos_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            x_pos_dip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x 
            y_pos_dip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
            x_pos_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x 
            y_pos_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y 
            if cv2.waitKey(33) == ord('a'):
                print('pressed')
                state = 'pressed'
                storeData([x_pos_tip,y_pos_tip,x_pos_dip,y_pos_dip,x_pos_pip,y_pos_pip,1])
            if cv2.waitKey(33) == ord('s'):
                print('not pressed')
                state='not pressed'
                storeData([x_pos_tip,y_pos_tip,x_pos_dip,y_pos_dip,x_pos_pip,y_pos_pip,0])
        cv2.putText(image,state,(50,50),font,1,(0,255,0),2,cv2.LINE_4)
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(33)==ord('q'):
            data_file.close()
            break
    cap.release()
    cv2.destroyAllWindows()
    
