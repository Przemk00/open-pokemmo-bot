import pyautogui
import time
import random
import logging

from config import *

# PyAutoGui functions

def pressKey(key, times = 1, interval = DELAY_BETWEEN_COMMANDS):
    for i in range(0, times):
        pyautogui.keyDown(key)
        time.sleep(.08)
        pyautogui.keyUp(key)
        time.sleep(interval + shortTime())

def typeWord(word):
    for i in word:
        pressKey(i)

def moveMouse(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(randomTime())

def moveMouseAndClick(x, y, button):
    pyautogui.click(x=x, y=y, button=button)
    time.sleep(randomTime())

def holdKey(key, seconds=1):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)
    time.sleep(shortTime())

# General

def shortTime():
    return random.randrange(1, 4) / 100

def randomTime():
    return random.randrange(2, 20) / 100

def startCountDown():
    # Countdown timer
    print("Starting", end="")
    for i in range(0, START_DELAY):
        print(".", end="")
        time.sleep(1)
    print("Go")
    
# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)