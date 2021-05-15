## demo of running mediapipe in local machine
## taking video feed from mobile and procesing

import cv2
import time
import mediapipe as mp
import numpy as np
import notes as n


cav = tk.Tk()

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
image_width  = cap.get(3)   
image_hight = cap.get(4)
green = (0,255,0)
x_pos,y_pos = None,None
count = 0
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
        
        cv2.rectangle(image,(0,60),(40,250),green,thickness=2)
        cv2.rectangle(image,(40,60),(80,250),green,thickness=2)
        cv2.rectangle(image,(80,60),(120,250),green,thickness=2)
        cv2.rectangle(image,(120,60),(160,250),green,thickness=2)
        cv2.rectangle(image,(160,60),(200,250),green,thickness=2)
        cv2.rectangle(image,(200,60),(240,250),green,thickness=2)
        cv2.rectangle(image,(240,60),(280,250),green,thickness=2)
        cv2.rectangle(image,(280,60),(320,250),green,thickness=2)
        cv2.rectangle(image,(320,60),(360,250),green,thickness=2)
        cv2.rectangle(image,(360,60),(400,250),green,thickness=2)
        cv2.rectangle(image,(400,60),(440,250),green,thickness=2)
        cv2.rectangle(image,(440,60),(480,250),green,thickness=2)
        cv2.rectangle(image,(480,60),(520,250),green,thickness=2)
        cv2.rectangle(image,(520,60),(560,250),green,thickness=2)
        cv2.rectangle(image,(560,60),(600,250),green,thickness=2)
        cv2.rectangle(image,(600,60),(640,250),green,thickness=2)
        
        image.flags.writeable = True
        image = cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_RGB2BGR)
        results = hands.process(image)
        if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            x_pos = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
            y_pos = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_hight
            if(x_pos>0 and x_pos<40 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_a3()
                count=1
            elif(x_pos>40 and x_pos<80 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_b3()
                count=1
            elif(x_pos>80 and x_pos<120 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_c3()
                count=1

            elif(x_pos>120 and x_pos<160 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_d3()
                count=1

            elif(x_pos>200 and x_pos<240 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_e3()
                count=1

            elif(x_pos>240 and x_pos<280 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_f3()
                
            elif(x_pos>280 and x_pos<320 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_g3()
                count=1

            elif(x_pos>320 and x_pos<360 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_a4()
                count=1

            elif(x_pos>360 and x_pos<400 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_b4()
                count=1

            elif(x_pos>400 and x_pos<440 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_c4()
                count=1

            elif(x_pos>440 and x_pos<480 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_d4()
                count=1

            elif(x_pos>480 and x_pos<520 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_e4()
                count=1
                
            elif(x_pos>520 and x_pos<560 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_f4()
                count=1
                
            elif(x_pos>560 and x_pos<600 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_g4()
                count=1

            elif(x_pos>600 and x_pos<640 and y_pos > 60 and y_pos < 250 and count==0):
                n.play_a5()
                count=1
            else:
                count = 0

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
          break
    cap.release()
