import pyautogui as pgui
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
    
    