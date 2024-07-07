import cv2
import mediapipe as mp
import pyautogui as pgui

def detect_gesture():
    mh=mp.solutions.hands
    ms=mp.solutions.drawing_styles
    m=mp.solutions.drawing_utils 
    cap=cv2.VideoCapture(0)
    hands=mh.Hands()
    
    while True:
        d,img=cap.read()
        img=cv2.cvtColor(cv2.flip(img,1),cv2.COLOR_BGR2RGB)
        r=hands.process(img)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        if r.multi_hand_landmarks:
            for hand_landmarks in r.multi_hand_landmarks:
                m.draw_landmarks(img,hand_landmarks,mh.HAND_CONNECTIONS)
        cv2.imshow('Handgesture',img)
        cv2.waitKey(1)
detect_gesture()

def gesture_handle(gesture):
    if gesture=="click":
        pgui.click()
    elif gesture=="left-click":
        pgui.click(button="left")
    elif gesture=="right-click":
        pgui.click(button="right")
    elif gesture=="switch-tab":
        pgui.click('ctrl','tab')
while True:
    gesture=detect_gesture()
    gesture_handle(gesture)