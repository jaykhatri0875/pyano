## this is piano made out of python script and you can play air piano at normal distance from computer \
## Accoring to camera width you can increase keys and also in notes you can add diff tones to play

##Script uses Google's opensource handtracking framework - Mediapipe



##importing necessary libraries 
import cv2
import time
import mediapipe as mp
import numpy as np
import notes as n
import math

#distance function which calculates geometric ditance between two points is plane
def dist(p1x,p2x,p1y,p2y):
    return math.sqrt((p2y-p1y)**2+(p2x-p1x)**2)*100

#is-pressed is booleanfunction checks whether user has made gesture which can be considered as key press or not
def isP(arr):
    tx,ty,dx,dy,px,py=arr
    dis1 = dist(tx,dx,ty,dy)
    dis2 = dist(tx,px,ty,py)
    dis3 = dist(dx,px,dy,py)
    if(dis1 < 3.4 and dis2 < 5 and dis3 < 4):
        return True
    return
#drawing lines on user screen for key reference
def draw_lines(image):
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

    
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

image_width  = cap.get(3)   
image_hight = cap.get(4)

green = (0,255,0)

x_pos,y_pos = None,None
count = 0 ## not required
f_vec = [] ## feature vector

print("started getting feed (press q to quit)")

with mp_hands.Hands(
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as hands:
    while cap.isOpened():
        success,image = cap.read()
        if not success:
            print("failed to load")
            continue
        draw_lines(image)
        image.flags.writeable = True
        image=cv2.flip(image,1)
        image1 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        results = hands.process(image1)
        if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            ## getting index fingers coordinates here
            x_pos_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x 
            y_pos_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            x_pos_dip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x 
            y_pos_dip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
            x_pos_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x 
            y_pos_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
            f_vec = [x_pos_tip,y_pos_tip,x_pos_dip,y_pos_dip,x_pos_pip,y_pos_pip]
            x_pos = x_pos_tip * image_width
            y_pos = y_pos_tip * image_hight
            ## to check whether or not index finger is in key region or not and is pressing over the region
            ## if pressed it will play tone according  to the key region 
            if(x_pos>0 and x_pos<40 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_a3()
                count=1
            elif(x_pos>40 and x_pos<80 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_b3()
                count=1
            elif(x_pos>80 and x_pos<120 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_c3()
                count=1

            elif(x_pos>120 and x_pos<160 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_d3()
                count=1

            elif(x_pos>200 and x_pos<240 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_e3()
                count=1

            elif(x_pos>240 and x_pos<280 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_f3()
                
            elif(x_pos>280 and x_pos<320 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_g3()
                count=1

            elif(x_pos>320 and x_pos<360 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_a4()
                count=1

            elif(x_pos>360 and x_pos<400 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_b4()
                count=1

            elif(x_pos>400 and x_pos<440 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_c4()
                count=1

            elif(x_pos>440 and x_pos<480 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_d4()
                count=1

            elif(x_pos>480 and x_pos<520 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_e4()
                count=1
                
            elif(x_pos>520 and x_pos<560 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_f4()
                count=1
                
            elif(x_pos>560 and x_pos<600 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_g4()
                count=1

            elif(x_pos>600 and x_pos<640 and y_pos > 60 and y_pos < 250 and count==0 and isP(f_vec)):
                n.play_a5()
                count=1
            else:
                count = 0

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(33)==ord('q'):
            print('thank you for using pyano !')
            break
    cap.release()
    cv2.destroyAllWindows()
