import pyautogui
import time

def holdKey(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

time.sleep(5)
holdKey('w', 2.2)

